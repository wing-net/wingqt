# -*- coding: utf-8 -*-
#
# main window of the application
#
#

from PyQt5 import QtCore, QtGui, QtWidgets
from enum import Enum


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

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 640)
        self.setupPalette(MainWindow)
        self.setupWidgets(MainWindow)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def setupPalette(self, MainWindow):
        palette = QtGui.QPalette()

        # white color theming
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)

        # black color theming
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)

        # (84, 83, 81) theming
        brush = QtGui.QBrush(QtGui.QColor(84, 83, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)

        # (42, 42, 41) theming
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)

        # (42, 41, 40) theming
        brush = QtGui.QBrush(QtGui.QColor(42, 41, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)

        # (255, 255, 220) theming
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)

        # white semi-transparent theming
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)

        # (126, 125, 122) theming
        brush = QtGui.QBrush(QtGui.QColor(126, 125, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)

        # (105, 104, 101) theming
        brush = QtGui.QBrush(QtGui.QColor(105, 104, 101))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)

        # (56, 56, 54) theming
        brush = QtGui.QBrush(QtGui.QColor(56, 56, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)

        # (94, 59, 99) theming
        brush = QtGui.QBrush(QtGui.QColor(94, 59, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)

        # misc theming
        brush = QtGui.QBrush(QtGui.QColor(84, 83, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)

        brush = QtGui.QBrush(QtGui.QColor(145, 145, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)

        MainWindow.setPalette(palette)


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
        self.open_button = QtWidgets.QToolButton(self.action_bar, clicked = self.open_clicked)
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
        self.export_button = QtWidgets.QToolButton(self.action_bar, clicked = self.export_clicked)
        self.export_button.setGeometry(QtCore.QRect(1, 80, 48, 60))
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
        self.detect_button = QtWidgets.QToolButton(self.action_bar, clicked = self.detect_clicked)
        self.detect_button.setGeometry(QtCore.QRect(1, 150, 48, 60))
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
        self.move_button = QtWidgets.QToolButton(self.action_bar, clicked = self.move_clicked)
        self.move_button.setGeometry(QtCore.QRect(1, 230, 48, 60))
        self.move_button.setAutoFillBackground(False)
        self.move_button.setStyleSheet("color:rgb(255, 255, 255)")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/pointer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.move_button.setIcon(icon3)
        self.move_button.setIconSize(QtCore.QSize(32, 32))
        self.move_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.move_button.setAutoRaise(True)
        self.move_button.setObjectName("move_button")

        # setup add button
        self.add_button = QtWidgets.QToolButton(self.action_bar, clicked = self.add_clicked)
        self.add_button.setGeometry(QtCore.QRect(1, 300, 48, 60))
        self.add_button.setAutoFillBackground(False)
        self.add_button.setStyleSheet("color:rgb(255, 255, 255)")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resources/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_button.setIcon(icon4)
        self.add_button.setIconSize(QtCore.QSize(32, 32))
        self.add_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.add_button.setAutoRaise(True)
        self.add_button.setObjectName("add_button")

        # setup erase button
        self.erase_button = QtWidgets.QToolButton(self.action_bar, clicked = self.erase_clicked)
        self.erase_button.setGeometry(QtCore.QRect(1, 370, 48, 60))
        self.erase_button.setAutoFillBackground(False)
        self.erase_button.setStyleSheet("color:rgb(255, 255, 255)")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("resources/erase.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.erase_button.setIcon(icon5)
        self.erase_button.setIconSize(QtCore.QSize(32, 32))
        self.erase_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.erase_button.setAutoRaise(True)
        self.erase_button.setObjectName("erase_button")

        self.line = QtWidgets.QFrame(self.action_bar)
        self.line.setGeometry(QtCore.QRect(0, 217, 50, 10))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
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
        self.verticalLayout.addWidget(self.canvas_frame)
        self.file_scrollarea = QtWidgets.QScrollArea(self.center_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_scrollarea.sizePolicy().hasHeightForWidth())
        self.file_scrollarea.setSizePolicy(sizePolicy)
        self.file_scrollarea.setMinimumSize(QtCore.QSize(0, 120))
        self.file_scrollarea.setWidgetResizable(True)
        self.file_scrollarea.setObjectName("file_scrollarea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 880, 118))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.file_scrollarea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.file_scrollarea)
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
        self.actionOpen_Folder = QtWidgets.QAction(MainWindow)
        self.actionOpen_Folder.setObjectName("actionOpen_Folder")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionExport_As = QtWidgets.QAction(MainWindow)
        self.actionExport_As.setObjectName("actionExport_As")
        self.actionExport_All = QtWidgets.QAction(MainWindow)
        self.actionExport_All.setObjectName("actionExport_All")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionClose_All = QtWidgets.QAction(MainWindow)
        self.actionClose_All.setObjectName("actionClose_All")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionOpen_Folder)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.actionExport_As)
        self.menuFile.addAction(self.actionExport_All)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionClose_All)
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAnalyze.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())


    # further setup stuff, do not edit
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open_button.setText(_translate("MainWindow", "open"))
        self.export_button.setText(_translate("MainWindow", "export"))
        self.detect_button.setText(_translate("MainWindow", "detect"))
        self.move_button.setText(_translate("MainWindow", "move"))
        self.add_button.setText(_translate("MainWindow", "add"))
        self.erase_button.setText(_translate("MainWindow", "erase"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuAnalyze.setTitle(_translate("MainWindow", "Analyze"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File..."))
        self.actionOpen_Folder.setText(_translate("MainWindow", "Open Folder..."))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionExport_As.setText(_translate("MainWindow", "Export As..."))
        self.actionExport_All.setText(_translate("MainWindow", "Export All"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose_All.setText(_translate("MainWindow", "Close All"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


    # ACTIONS

    # on open button click
    def open_clicked(self):
        self.statusbar.showMessage("open")
        self.statusbar.showMessage(self.state_dict[self.edit_state])

    # on export button click
    def export_clicked(self):
        self.statusbar.showMessage("export")
        self.statusbar.showMessage(self.state_dict[self.edit_state])

    # on detect button click
    def detect_clicked(self):
        self.statusbar.showMessage("detect")
        self.statusbar.showMessage(self.state_dict[self.edit_state])

    # on move button click
    def move_clicked(self):
        self.edit_state = self.STATE_NORMAL
        self.statusbar.showMessage(self.state_dict[self.edit_state])

    # on add button click
    def add_clicked(self):
        self.edit_state = self.STATE_ADD
        self.statusbar.showMessage(self.state_dict[self.edit_state])

    # on erase button click
    def erase_clicked(self):
        self.edit_state = self.STATE_ERASE
        self.statusbar.showMessage(self.state_dict[self.edit_state])




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
