# -*- coding: utf-8 -*-

import sys
import os
import csv
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPainter

class Canvas(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.mode = 0 # temp: 0 -> move, 1 -> add, 2 -> erase

        self.points = []
        self.pointer = QtCore.QPoint()
        self.end = QtCore.QPoint()

        self.image_name = ""
        self.img_width = 0
        self.img_height = 0
        self.pixmap = QtGui.QPixmap()


    def paintEvent(self, event):
        if (self.image_name != ""):
            qp = QtGui.QPainter(self)
            #real_height = pixmap.height()
            #real_width = pixmap.width()

            # for now, we just keep the size the image was opened at
            # scaled_pixmap = self.pixmap.scaled(self.width(), self.height(),
            #                               QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
            qp.drawPixmap(self.pixmap.rect(), self.pixmap)
            for pt in self.points:
                pen = QtGui.QPen(QtGui.QColor(255, 10, 10, 255), 10)
                qp.setPen(pen)
                qp.drawPoint(pt)

    def mousePressEvent(self, event):
        self.pointer = event.pos()
        self.end = event.pos()
        if self.mode == 2:
            for pt in self.points:
                if abs((pt - self.pointer).manhattanLength()) < 20:
                    self.points.remove(pt)
        elif self.mode == 1:
            # only allow adding points within the bounds of the image
            if (self.pointer.x() - self.pixmap.width() < 0 and
                    self.pointer.y() - self.pixmap.height() < 0):
                self.points.append(self.pointer)
        self.update()

    def setImage(self, image_path):
        self.image_name = image_path
        unscaled_pix = QtGui.QPixmap(image_path)
        self.img_width = unscaled_pix.width()
        self.img_height = unscaled_pix.height()
        self.pixmap = unscaled_pix.scaled(self.width(), self.height(),
                            QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.update()

    def setNormal(self):
        self.mode = 0

    def setAdd(self):
        self.mode = 1

    def setErase(self):
        self.mode = 2

    def exportLandmarks(self, filename=None):
        cwd = os.getcwd()
        if filename is None:
            filename,_ = os.path.splitext(self.image_name)
            filename += ".csv"

        print(os.path.join(cwd, filename))
        with open(os.path.join(cwd, filename), mode='w+') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for point in self.convertRelativePoints():
                writer.writerow([point.x(), point.y()])
        print(self.points)

    def convertRelativePoints(self):
        points_og = []
        x_factor = self.img_width / self.pixmap.width()
        y_factor = self.img_height / self.pixmap.height()
        for point in self.points:
            x_og = point.x() * x_factor
            y_og = point.y() * y_factor
            points_og.append(QtCore.QPoint(x_og, y_og))
        return points_og


    def mouseMoveEvent(self, event):
        if self.mode == 3:
            self.end = event.pos()
            self.update()
        elif self.mode == 1:
            pass
        elif self.mode == 2:
            pass
        elif self.mode == 0:
            pass

    def mouseReleaseEvent(self, event):
        if self.mode == 3:
            self.pointer = event.pos()
            self.end = event.pos()
            self.update()
        elif self.mode == 1:
            pass
        elif self.mode == 2:
            pass
        elif self.mode == 0:
            pass

