from PyQt5 import QtCore, QtGui

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
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)

    # (70, 70, 70) theming
    brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)

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
