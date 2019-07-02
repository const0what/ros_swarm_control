# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'items.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(674, 557)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 70, 676, 103))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.ItemLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.ItemLayout.setContentsMargins(0, 0, 0, 0)
        self.ItemLayout.setObjectName("ItemLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.GpsRadioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.GpsRadioButton.setMaximumSize(QtCore.QSize(52, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        self.GpsRadioButton.setFont(font)
        self.GpsRadioButton.setObjectName("GpsRadioButton")
        self.horizontalLayout_2.addWidget(self.GpsRadioButton)
        self.HomeRadioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.HomeRadioButton.setMinimumSize(QtCore.QSize(0, 0))
        self.HomeRadioButton.setMaximumSize(QtCore.QSize(64, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        self.HomeRadioButton.setFont(font)
        self.HomeRadioButton.setObjectName("HomeRadioButton")
        self.horizontalLayout_2.addWidget(self.HomeRadioButton)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.ItemLayout.addLayout(self.horizontalLayout_4, 0, 3, 1, 1)
        self.SelectCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.SelectCheckBox.setMinimumSize(QtCore.QSize(24, 32))
        self.SelectCheckBox.setMaximumSize(QtCore.QSize(24, 24))
        self.SelectCheckBox.setMouseTracking(True)
        self.SelectCheckBox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.SelectCheckBox.setText("")
        self.SelectCheckBox.setIconSize(QtCore.QSize(32, 32))
        self.SelectCheckBox.setCheckable(True)
        self.SelectCheckBox.setObjectName("SelectCheckBox")
        self.ItemLayout.addWidget(self.SelectCheckBox, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ipEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ipEdit.sizePolicy().hasHeightForWidth())
        self.ipEdit.setSizePolicy(sizePolicy)
        self.ipEdit.setMinimumSize(QtCore.QSize(164, 0))
        self.ipEdit.setMaximumSize(QtCore.QSize(164, 32))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ipEdit.setFont(font)
        self.ipEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.ipEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ipEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ipEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.ipEdit.setObjectName("ipEdit")
        self.horizontalLayout_3.addWidget(self.ipEdit)
        self.portEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portEdit.sizePolicy().hasHeightForWidth())
        self.portEdit.setSizePolicy(sizePolicy)
        self.portEdit.setMaximumSize(QtCore.QSize(56, 32))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.portEdit.setFont(font)
        self.portEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.portEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.portEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.portEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.portEdit.setObjectName("portEdit")
        self.horizontalLayout_3.addWidget(self.portEdit)
        self.ItemLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
        self.ModeComboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.ModeComboBox.setMaximumSize(QtCore.QSize(128, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.ModeComboBox.setFont(font)
        self.ModeComboBox.setObjectName("ModeComboBox")
        self.ItemLayout.addWidget(self.ModeComboBox, 1, 3, 1, 1)
        self.ArmButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ArmButton.setMaximumSize(QtCore.QSize(84, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ArmButton.setFont(font)
        self.ArmButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.ArmButton.setObjectName("ArmButton")
        self.ItemLayout.addWidget(self.ArmButton, 1, 5, 1, 1)
        self.ConnectButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConnectButton_2.sizePolicy().hasHeightForWidth())
        self.ConnectButton_2.setSizePolicy(sizePolicy)
        self.ConnectButton_2.setMaximumSize(QtCore.QSize(96, 32))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.ConnectButton_2.setFont(font)
        self.ConnectButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ConnectButton_2.setObjectName("ConnectButton_2")
        self.ItemLayout.addWidget(self.ConnectButton_2, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ItemLayout.addItem(spacerItem, 1, 4, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.NameLabel_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.NameLabel_2.setMaximumSize(QtCore.QSize(96, 32))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.NameLabel_2.setFont(font)
        self.NameLabel_2.setObjectName("NameLabel_2")
        self.horizontalLayout.addWidget(self.NameLabel_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.BatteryTextLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.BatteryTextLabel.setMaximumSize(QtCore.QSize(34, 32))
        self.BatteryTextLabel.setObjectName("BatteryTextLabel")
        self.horizontalLayout.addWidget(self.BatteryTextLabel)
        self.Batterylabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Batterylabel.setMaximumSize(QtCore.QSize(56, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setBold(True)
        font.setWeight(75)
        self.Batterylabel.setFont(font)
        self.Batterylabel.setObjectName("Batterylabel")
        self.horizontalLayout.addWidget(self.Batterylabel)
        self.ItemLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.LocalRadioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.LocalRadioButton.setMinimumSize(QtCore.QSize(0, 0))
        self.LocalRadioButton.setMaximumSize(QtCore.QSize(64, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        self.LocalRadioButton.setFont(font)
        self.LocalRadioButton.setObjectName("LocalRadioButton")
        self.ItemLayout.addWidget(self.LocalRadioButton, 0, 2, 1, 1)
        self.widget = QtWidgets.QWidget(self.gridLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(140, 242, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 255, 172))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(174, 248, 116))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 121, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(93, 161, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(140, 242, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(197, 248, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(140, 242, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 255, 172))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(174, 248, 116))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 121, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(93, 161, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(140, 242, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(197, 248, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 121, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(140, 242, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 255, 172))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(174, 248, 116))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 121, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(93, 161, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 121, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 121, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(140, 242, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(140, 242, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(140, 242, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.widget.setPalette(palette)
        self.widget.setAutoFillBackground(True)
        self.widget.setObjectName("widget")
        self.ItemLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.GPSStateLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.GPSStateLabel.setObjectName("GPSStateLabel")
        self.ItemLayout.addWidget(self.GPSStateLabel, 0, 5, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 674, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.GpsRadioButton.setText(_translate("MainWindow", "&gps"))
        self.HomeRadioButton.setText(_translate("MainWindow", "ho&me"))
        self.ipEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\'; font-size:11pt; font-weight:400;\">192.168.128.101</span></p></body></html>"))
        self.portEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\'; font-size:11pt;\">9090</span></p></body></html>"))
        self.ArmButton.setText(_translate("MainWindow", "Arm"))
        self.ConnectButton_2.setText(_translate("MainWindow", "Connect"))
        self.NameLabel_2.setText(_translate("MainWindow", "Drone_"))
        self.BatteryTextLabel.setText(_translate("MainWindow", "bat:"))
        self.Batterylabel.setText(_translate("MainWindow", "100%"))
        self.LocalRadioButton.setText(_translate("MainWindow", "&local"))
        self.GPSStateLabel.setText(_translate("MainWindow", "TextLabel"))
