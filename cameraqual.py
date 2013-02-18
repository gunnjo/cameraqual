# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cameraqual.ui'
#
# Created: Mon Feb 18 09:58:13 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(640, 500, 102, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 90, 421, 361))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(540, 100, 211, 171))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.PSNR = QtGui.QLabel(self.layoutWidget)
        self.PSNR.setObjectName(_fromUtf8("PSNR"))
        self.horizontalLayout_4.addWidget(self.PSNR)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_5.addWidget(self.label_9)
        self.SSIM = QtGui.QLabel(self.layoutWidget)
        self.SSIM.setObjectName(_fromUtf8("SSIM"))
        self.horizontalLayout_5.addWidget(self.SSIM)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.BLACK = QtGui.QLabel(self.layoutWidget)
        self.BLACK.setObjectName(_fromUtf8("BLACK"))
        self.horizontalLayout_3.addWidget(self.BLACK)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.White = QtGui.QLabel(self.layoutWidget)
        self.White.setObjectName(_fromUtf8("White"))
        self.horizontalLayout_2.addWidget(self.White)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.FrameNum = QtGui.QLabel(self.layoutWidget)
        self.FrameNum.setObjectName(_fromUtf8("FrameNum"))
        self.horizontalLayout.addWidget(self.FrameNum)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionText = QtGui.QAction(MainWindow)
        self.actionText.setObjectName(_fromUtf8("actionText"))

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), QtCore.QCoreApplication.instance().quit)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def closeEvent( self, event):
        event.accept()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Peak Signal-to-Noise Ratio</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "PSNR", None, QtGui.QApplication.UnicodeUTF8))
        self.PSNR.setText(QtGui.QApplication.translate("MainWindow", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Structural SIMularity: </p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "SSIM", None, QtGui.QApplication.UnicodeUTF8))
        self.SSIM.setText(QtGui.QApplication.translate("MainWindow", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Black", None, QtGui.QApplication.UnicodeUTF8))
        self.BLACK.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "White", None, QtGui.QApplication.UnicodeUTF8))
        self.White.setText(QtGui.QApplication.translate("MainWindow", "255", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.FrameNum.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.actionText.setText(QtGui.QApplication.translate("MainWindow", "text", None, QtGui.QApplication.UnicodeUTF8))
        self.actionText.setToolTip(QtGui.QApplication.translate("MainWindow", "tooltip", None, QtGui.QApplication.UnicodeUTF8))
