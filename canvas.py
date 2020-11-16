# -*- coding: utf-8 -*-

import sys
import os
import pickle
import csv
import math
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPainter
import MeasuringObjects.main as analyzer

class Canvas(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.mode = 3   # temp: 0 -> length measure, 1 -> add, 2 -> erase, 3 -> move

        self.points = []
        self.session_points = {}    # store points for all images opened
                                    # format: { "imgname.ext" : [QPoint(x1,y1), ...] }
        self.session_points_actual = {}     # store original resolution session data for exporting

        self.wing_length = 0
        self.length_coords = []
        self.session_lengths = {}   # same idea but we store length/end data
        self.session_lengths_actual = {}

        self.drag_index = -1
        self.length_drag_index = -1

        self.pointer = QtCore.QPoint()
        self.end = QtCore.QPoint()

        self.pen_size = 15

        self.image_name = ""
        self.img_width = 0
        self.img_height = 0
        self.pixmap = QtGui.QPixmap()


    def paintEvent(self, event):
        if self.image_name != "":
            qp = QtGui.QPainter(self)
            # for now, we just keep the size the image was opened at
            qp.drawPixmap(self.pixmap.rect(), self.pixmap)

            if self.mode == 0:
                pen = QtGui.QPen(QtGui.QColor(10, 255, 10, 200), self.pen_size)
                pen.setCapStyle(QtCore.Qt.RoundCap)
                qp.setPen(pen)
                for pt in self.length_coords:
                    qp.drawPoint(pt)
                pen = QtGui.QPen(QtGui.QColor(10, 190, 10, 200), 3)
                pen.setCapStyle(QtCore.Qt.RoundCap)
                qp.setPen(pen)
                qp.drawLine(self.length_coords[0], self.length_coords[1])

            pen = QtGui.QPen(QtGui.QColor(255, 10, 10, 200), self.pen_size)
            pen.setCapStyle(QtCore.Qt.RoundCap)
            qp.setPen(pen)
            for pt in self.points:
                qp.drawPoint(pt)

    def mousePressEvent(self, event):
        self.pointer = event.pos()
        self.end = event.pos()
        if self.mode == 0:
            for i, pt in enumerate(self.length_coords):
                if abs((pt - self.pointer).manhattanLength()) < 20:
                    self.length_drag_index = i
        elif self.mode == 1:
            # only allow adding points within the bounds of the image
            if (self.pointer.x() - self.pixmap.width() < 0 and
                    self.pointer.y() - self.pixmap.height() < 0):
                self.points.append(self.pointer)
        elif self.mode == 2:
            for pt in self.points:
                if abs((pt - self.pointer).manhattanLength()) < 20:
                    self.points.remove(pt)
        elif self.mode == 3:
            # select the index of the point the user is clicking on
            for i, pt in enumerate(self.points):
                if abs((pt - self.pointer).manhattanLength()) < 20:
                    self.drag_index = i

        self.session_points[self.image_name] = self.points  # update session
        if self.points:     # if we actually have points update _actual session
            self.session_points_actual[self.image_name],\
                self.session_lengths_actual[self.image_name] = self.convertRelativePoints()
        self.session_lengths[self.image_name] = self.length_coords
        self.update()

    def setImage(self, image_path):
        # add if we already know about the image load it into current points, else create it
        if image_path in self.session_points:
            self.points = self.session_points[image_path]
        else:
            self.points = []
            self.session_points[image_path] = []
            self.session_points_actual[image_path] = []

        self.image_name = image_path
        unscaled_pix = QtGui.QPixmap(image_path)
        self.img_width = unscaled_pix.width()
        self.img_height = unscaled_pix.height()
        self.pixmap = unscaled_pix.scaled(self.width(), self.height(),
                            QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)

        # add old or new wing length data
        if image_path in self.session_lengths:
            self.length_coords = self.session_lengths[image_path]
            self.wing_length = int(math.hypot(
                self.length_coords[0].x() - self.length_coords[1].x(),
                self.length_coords[0].y() - self.length_coords[1].y()))
        else:
            self.new_length_points(self.pixmap.width(), self.pixmap.height())
            self.session_lengths[image_path] = self.length_coords

        self.update()

    def new_length_points(self, width, height):
        y = int(height / 2)
        x1 = int(width * (1/3))
        x2 = int(width * (2/3))
        self.length_coords = []
        self.length_coords.append(QtCore.QPoint(x1,y))
        self.length_coords.append(QtCore.QPoint(x2,y))
        self.wing_length = int(math.hypot(x2 - x1, y - y))

    def analyzeLength(self):
        self.length_coords = []
        start, end = analyzer.analyze(self.image_name)
        x_factor = self.img_width / self.pixmap.width()
        y_factor = self.img_height / self.pixmap.height()
        self.length_coords.append(QtCore.QPoint(start[0] / x_factor  , start[1] / y_factor))
        self.length_coords.append(QtCore.QPoint(end[0] / x_factor, end[1] / y_factor))
        self.session_lengths[self.image_name] = self.length_coords
        _,self.wing_length = self.convertRelativePoints()
        self.session_lengths_actual[self.image_name] = self.wing_length
        self.update()

    def setLength(self):
        self.mode = 0
        self.update()

    def setNormal(self):
        self.mode = 3
        self.update()

    def setAdd(self):
        self.mode = 1
        self.update()

    def setErase(self):
        self.mode = 2
        self.update()

    def loadSwapFile(self, dirpath):
        try:
            filepath = os.path.join(dirpath, '.session.swp')
            with open(filepath, mode='rb') as swapfile:
                self.session_points = pickle.loads(swapfile.read())
        except FileNotFoundError:
            pass

    def exportSwapFile(self, dirpath):
        filepath = os.path.join(dirpath, '.session.swp')
        with open(filepath, mode='wb+') as swapfile:
            pickle.dump(self.session_points, swapfile)

    def exportLandmarks(self, filepath):
        if filepath is not None and filepath != '':
            with open(filepath, mode='w+') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                points_og,_ = self.convertRelativePoints()
                writer.writerow("wing length: " + str(self.wing_length))

                for point in points_og:
                    writer.writerow([point.x(), point.y()])

    def exportAll(self, dirpath):
        for entry in self.session_points_actual:
            filename = entry + ".csv"
            filepath = os.path.join(dirpath, filename)
            with open(filepath, mode='w+') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                points_og = self.session_points_actual[entry]
                length_og = self.session_lengths_actual[entry]
                csv_file.write("wing length: " + str(length_og) + "\n")
                for point in points_og:
                    writer.writerow([point.x(), point.y()])


    # def saveMarkedImage(self):
    #     """repaints the image with the landmark/length points in its
    #     original resolution and saves as a png image"""
    #     points_og = self.convertRelativePoints()
    #     tmp_painter = QtGui.QPainter()
    #     tmp_painter.drawPixmap(self.pixmap.rect(), self.pixmap)
    #     pen_scale = self.img_width / self.pixmap.width()
    #     pen = QtGui.QPen(QtGui.QColor(255, 10, 10, 200), self.pen_size * pen_scale)
    #     pen.setCapStyle(QtCore.Qt.RoundCap)
    #     tmp_painter.setPen(pen)
    #     for pt in self.points:
    #         tmp_painter.drawPoint(pt)
    #     save_image = QtGui.QImage(self.img_width, self.img_height, QtGui.QImage.Format_RGB32)
    #     src_rect = QtCore.QRect()
    #     tmp_painter.drawImage(rect, save_image, )

    def convertRelativePoints(self):
        points_og = []
        length_og = 0
        x_factor = self.img_width / self.pixmap.width()
        y_factor = self.img_height / self.pixmap.height()
        for point in self.points:
            x_og = point.x() * x_factor
            y_og = point.y() * y_factor
            points_og.append(QtCore.QPoint(x_og, y_og))
        self.wing_length = int(math.hypot(
            (self.length_coords[0].x() - self.length_coords[1].x()) * x_factor,
            (self.length_coords[0].y() - self.length_coords[1].y()) * y_factor))
        length_og = self.wing_length
        return points_og, length_og


    def mouseMoveEvent(self, event):
        if self.mode == 3 and self.drag_index >= 0:
            self.end = event.pos()
            self.points[self.drag_index] = event.pos()
            self.update()
        elif self.mode == 0 and self.length_drag_index >= 0:
            self.end = event.pos()
            self.length_coords[self.length_drag_index] = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if self.mode == 3 and self.drag_index >= 0:
            self.end = event.pos()
            self.points[self.drag_index] = event.pos()
            self.drag_index = -1    # indicate we arent dragging anymore
            self.session_points[self.image_name] = self.points  # update session
            self.session_points_actual[self.image_name],_ = self.convertRelativePoints()
            self.update()
        if self.mode == 0 and self.length_drag_index >= 0:
            self.end = event.pos()
            self.length_coords[self.length_drag_index] = event.pos()
            self.length_drag_index = -1
            self.session_lengths[self.image_name] = self.length_coords
            _,self.wing_length = self.convertRelativePoints()
            self.session_lengths_actual[self.image_name] = self.wing_length
            self.update()
