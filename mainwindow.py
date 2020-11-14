# -*- coding: utf-8 -*-
#
# main window of the application
#
#

from PyQt5 import QtCore, QtGui, QtWidgets
from enum import Enum
from pathlib import Path
import os

import palette
from canvas import Canvas

# import imagelist


class Ui_MainWindow():

    class edit_state(Enum):
        STATE_NORMAL = 1
        STATE_ADD = 2
        STATE_ERASE = 3
    STATE_NORMAL = edit_state.STATE_NORMAL
    STATE_ADD = edit_state.STATE_ADD
    STATE_ERASE = edit_state.STATE_ERASE

    edit_state = STATE_NORMAL

    state_dict = {
        STATE_NORMAL : "normal",
        STATE_ADD    : "add",
        STATE_ERASE  : "erase"
    }

    show_length_ctrl = False

    current_dir = Path.home()
    current_file = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 640)
        self.setupPalette(MainWindow)
        self.setupWidgets(MainWindow)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    setupPalette = palette.setupPalette


    def setupWidgets(self, MainWindow):
        # main and size policy
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.main_layout = QtWidgets.QHBoxLayout()
        self.main_layout.setObjectName("main_layout")
        self.action_bar = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.action_bar.sizePolicy().hasHeightForWidth())

        # action bar (toolbar on the left)
        self.action_bar.setSizePolicy(sizePolicy)
        self.action_bar.setMinimumSize(QtCore.QSize(50, 440))
        self.action_bar.setStyleSheet("background-color:rgb(53, 53, 55)")
        self.action_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.action_bar.setFrameShadow(QtWidgets.QFrame.Plain)
        self.action_bar.setLineWidth(0)
        self.action_bar.setObjectName("action_bar")

        # setup open button
        self.open_button = QtWidgets.QToolButton(self.action_bar)
        self.open_button.setGeometry(QtCore.QRect(1, 10, 48, 60))
        self.open_button.setAutoFillBackground(False)
        self.open_button.setStyleSheet("color:rgb(255, 255, 255)")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_button.setIcon(icon)
        self.open_button.setIconSize(QtCore.QSize(32, 32))
        self.open_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.open_button.setAutoRaise(True)
        self.open_button.setObjectName("open_button")

        # setup export button
        self.export_button = QtWidgets.QToolButton(self.action_bar)
        self.export_button.setGeometry(QtCore.QRect(1, 70, 48, 60))
        self.export_button.setAutoFillBackground(False)
        self.export_button.setStyleSheet("color:rgb(255, 255, 255)")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.export_button.setIcon(icon1)
        self.export_button.setIconSize(QtCore.QSize(32, 32))
        self.export_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.export_button.setAutoRaise(True)
        self.export_button.setObjectName("export_button")

        # setup detect button
        self.detect_button = QtWidgets.QToolButton(self.action_bar)
        self.detect_button.setGeometry(QtCore.QRect(1, 130, 48, 60))
        self.detect_button.setAutoFillBackground(False)
        self.detect_button.setStyleSheet("color:rgb(255, 255, 255)")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/detect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.detect_button.setIcon(icon2)
        self.detect_button.setIconSize(QtCore.QSize(32, 32))
        self.detect_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.detect_button.setAutoRaise(True)
        self.detect_button.setObjectName("detect_button")

        # setup move/normal mode button
        self.move_button = QtWidgets.QToolButton(self.action_bar)
        self.move_button.setGeometry(QtCore.QRect(1, 200, 48, 60))
        self.move_button.setAutoFillBackground(False)
        self.move_button.setStyleSheet("color:white")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/pointer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.move_button.setIcon(icon3)
        self.move_button.setIconSize(QtCore.QSize(32, 32))
        self.move_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.move_button.setAutoRaise(True)
        self.move_button.setObjectName("move_button")

        # setup add button
        self.add_button = QtWidgets.QToolButton(self.action_bar)
        self.add_button.setGeometry(QtCore.QRect(1, 260, 48, 60))
        self.add_button.setAutoFillBackground(False)
        self.add_button.setStyleSheet("color:white")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resources/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_button.setIcon(icon4)
        self.add_button.setIconSize(QtCore.QSize(32, 32))
        self.add_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.add_button.setAutoRaise(True)
        self.add_button.setObjectName("add_button")

        # setup erase button
        self.erase_button = QtWidgets.QToolButton(self.action_bar)
        self.erase_button.setGeometry(QtCore.QRect(1, 320, 48, 60))
        self.erase_button.setAutoFillBackground(False)
        self.erase_button.setStyleSheet("color:white")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("resources/erase.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.erase_button.setIcon(icon5)
        self.erase_button.setIconSize(QtCore.QSize(32, 32))
        self.erase_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.erase_button.setAutoRaise(True)
        self.erase_button.setObjectName("erase_button")

        # setup length button
        self.length_button = QtWidgets.QToolButton(self.action_bar)
        self.length_button.setGeometry(QtCore.QRect(1,380, 48, 60))
        self.length_button.setAutoFillBackground(False)
        self.length_button.setStyleSheet("color:white")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("resources/length.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.length_button.setIcon(icon6)
        self.length_button.setIconSize(QtCore.QSize(32, 32))
        self.length_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.length_button.setAutoRaise(True)
        self.length_button.setObjectName("length_button")
        self.length_button.setToolTip("Show/hide wing length control points")

        self.main_layout.addWidget(self.action_bar)
        self.center_frame = QtWidgets.QFrame(self.centralwidget)
        self.center_frame.setMinimumSize(QtCore.QSize(25, 120))
        self.center_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.center_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.center_frame.setObjectName("center_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.center_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.canvas_frame = QtWidgets.QFrame(self.center_frame)
        self.canvas_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.canvas_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.canvas_frame.setObjectName("canvas_frame")

        # image view setup
        self.canvas_layout = QtWidgets.QHBoxLayout(self.canvas_frame)
        self.canvas_layout.setObjectName("canvas_layout")
        self.image_view = Canvas(self.canvas_frame)
        #self.image_view = QtWidgets.QLabel(self.canvas_frame)
        #self.image_view.setText("")
        # self.image_view.setScaledContents(True)
        self.image_view.setObjectName("image_view")
        self.canvas_layout.addWidget(self.image_view)

        self.verticalLayout.addWidget(self.canvas_frame)

        # file list view setup
        self.file_list_view = QtWidgets.QListWidget(self.center_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_list_view.sizePolicy().hasHeightForWidth())
        self.file_list_view.setSizePolicy(sizePolicy)
        self.file_list_view.setMinimumSize(QtCore.QSize(0, 120))
        self.file_list_view.setMaximumSize(QtCore.QSize(16777215, 120))
        self.file_list_view.setBaseSize(QtCore.QSize(0, 0))
        self.file_list_view.setObjectName("file_list_view")
        self.verticalLayout.addWidget(self.file_list_view)

        self.main_layout.addWidget(self.center_frame)
        self.horizontalLayout.addLayout(self.main_layout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 19))
        self.menubar.setStyleSheet("background-color:rgb(70, 70, 70);\n"
                                   "color:rgb(211, 215, 207);")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuAnalyze = QtWidgets.QMenu(self.menubar)
        self.menuAnalyze.setObjectName("menuAnalyze")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("background-color:rgb(70, 70, 70);\n"
                                     "color:rgb(255, 255, 255)")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionExport_As = QtWidgets.QAction(MainWindow)
        self.actionExport_As.setObjectName("actionExport_As")
        self.actionExport_All = QtWidgets.QAction(MainWindow)
        self.actionExport_All.setObjectName("actionExport_All")
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionExport_As)
        self.menuFile.addAction(self.actionExport_All)
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAnalyze.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())


    # further required setup stuff
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open_button.setText(_translate("MainWindow", "open"))
        self.export_button.setText(_translate("MainWindow", "export"))
        self.detect_button.setText(_translate("MainWindow", "detect"))
        self.move_button.setText(_translate("MainWindow", "move"))
        self.add_button.setText(_translate("MainWindow", "add"))
        self.erase_button.setText(_translate("MainWindow", "erase"))
        self.length_button.setText(_translate("MainWindow", "length"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuAnalyze.setTitle(_translate("MainWindow", "Analyze"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File..."))
        self.actionExport_As.setText(_translate("MainWindow", "Export As..."))
        self.actionExport_All.setText(_translate("MainWindow", "Export All"))

        # connect event handlers to menu bar buttons
        self.actionOpen_File.triggered.connect(self.open_clicked)
        self.actionExport_As.triggered.connect(self.export_clicked)
        self.actionExport_All.triggered.connect(self.export_clicked)

        # connect event handlers to action bar buttons
        self.open_button.clicked.connect(self.open_clicked)
        self.export_button.clicked.connect(self.export_clicked)
        self.detect_button.clicked.connect(self.detect_clicked)
        self.move_button.clicked.connect(self.move_clicked)
        self.add_button.clicked.connect(self.add_clicked)
        self.erase_button.clicked.connect(self.erase_clicked)
        self.length_button.clicked.connect(self.length_clicked)

        self.file_list_view.itemDoubleClicked.connect(self.file_list_clicked)



    # ACTIONS

    # on open button click
    def open_clicked(self):
        self.statusbar.showMessage("opening...")
        self.current_file = self.open_file_picker()
        self.current_dir = str(Path(self.current_file).parent)

        imagefilter = [".png", ".jpg", ".bmp", ".gif"]

        dir_contents = os.listdir(self.current_dir)
        dir_contents.sort()
        for imagefile in dir_contents:
            _, ext = os.path.splitext(imagefile)
            if ext.lower() in imagefilter:
                self.file_list_view.addItem(imagefile)

        self.update_image()
        self.update_statusbar()

    # on export button click
    def export_clicked(self):
        if self.current_file != "":
            self.statusbar.showMessage("exporting...")
            filename = self.save_file_picker()
            print(filename)
            self.image_view.exportLandmarks(filename)
            self.update_statusbar()

    def export_all_clicked(self):
        if self.current_file != "":
            self.statusbar.showMessage("exporting...")
            self.image_view.exportAll(self.current_dir)
            self.update_statusbar()

    def change_button_state(self):
        checked_style = "color:white;background-color:#5e3b63"
        unchecked_style = "color:white;background-color:#5e3b63"
        if self.edit_state == self.STATE_NORMAL:
            self.move_button.setStyleSheet("color:white;background-color:#5e3b63")
            self.add_button.setStyleSheet("color:white;background-color:#353537")
            self.erase_button.setStyleSheet("color:white;background-color:#353537")
        elif self.edit_state == self.STATE_ADD:
            self.move_button.setStyleSheet("color:white;background-color:#353537")
            self.add_button.setStyleSheet("color:white;background-color:#5e3b63")
            self.erase_button.setStyleSheet("color:white;background-color:#353537")
        elif self.edit_state == self.STATE_ERASE:
            self.move_button.setStyleSheet("color:white;background-color:#353537")
            self.add_button.setStyleSheet("color:white;background-color:#353537")
            self.erase_button.setStyleSheet("color:white;background-color:#5e3b63")

    # on detect button click
    def detect_clicked(self):
        self.statusbar.showMessage("detect")
        self.update_statusbar()

    # on move button click
    def move_clicked(self):
        self.edit_state = self.STATE_NORMAL
        self.change_button_state()
        self.image_view.setNormal()
        self.update_statusbar()

    # on add button click
    def add_clicked(self):
        self.edit_state = self.STATE_ADD
        self.change_button_state()
        self.image_view.setAdd()
        self.update_statusbar()

    # on erase button click
    def erase_clicked(self):
        self.edit_state = self.STATE_ERASE
        self.change_button_state()
        self.image_view.setErase()
        self.update_statusbar()

    # on length ctrl toggle clicked
    def length_clicked(self):
        if self.show_length_ctrl == False:
            self.show_length_ctrl = True
            self.image_view.setLength()
            self.length_button.setStyleSheet("color:white;background-color:#5e3b63")
            self.move_button.setStyleSheet("color:white;background-color:#353537")
            self.add_button.setStyleSheet("color:white;background-color:#353537")
            self.erase_button.setStyleSheet("color:white;background-color:#353537")
        else:
            self.show_length_ctrl = False
            self.image_view.setNormal()
            self.edit_state = self.STATE_NORMAL
            self.change_button_state()
            self.length_button.setStyleSheet("color:white;background-color:#353537")
        self.update_statusbar()

    def file_list_clicked(self, item):
        self.current_file = os.path.join(self.current_dir, item.text())
        self.update_image()
        self.update_statusbar()

    def update_image(self):
        #width = self.image_view.width()
        #height = self.image_view.height()
        self.image_view.setImage(self.current_file)

    def update_statusbar(self):
        if self.show_length_ctrl == True:
            lenstr = "Drag points to measure length, click length button again to save"
        elif len(self.current_file) > 1:
            lenstr = "wing length: " + str(self.image_view.wing_length) + "px"
        else:
            lenstr = ""
        _, filename = os.path.split(self.current_file)
        msgstr = " [" + self.state_dict[self.edit_state] + "]    " + filename + "    " + lenstr
        self.statusbar.showMessage(msgstr)

    def open_file_picker(self):
        imagefilter = "Image Files (*.png *.jpg *.bmp *.PNG *.JPG *.BMP *.GIF *.gif)"
        caption = "Import image file"
        filename = QtWidgets.QFileDialog.getOpenFileName(caption=caption,
                                                         filter=imagefilter)
        return filename[0]

    def save_file_picker(self):
        imagefilter = "CSV Files (*.csv *.txt)"
        caption = "Export data to CSV"
        imgname,_ = os.path.splitext(self.current_file)
        prefname = os.path.join(os.getcwd(), imgname + ".csv")
        filename = QtWidgets.QFileDialog.getSaveFileName(caption=caption,
                                                         directory=prefname,
                                                         filter=imagefilter)
        return filename[0]


