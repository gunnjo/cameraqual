#!/usr/bin/evn python

import cv2.cv as cv
from cameraqual import Ui_MainWindow
from PyQt4 import QtCore, QtGui



class ticktock(QtCore.QTimer):
    def __init__(self, parent=None):
        QtCore.QTimer.__init__(self, parent)

    def startTimer(self, t):
        self.capture = cv.CaptureFromCAM(0)
        self.start(t)
        
    def update(self):
        global ui
        img = cv.QueryFrame(self.capture)
        qimg = QtGui.QImage( img.width, img.height, QtGui.QImage.Format_RGB32)
        for n in range( 0,img.height):
            for m in range( 0,img.width):
                pval = cv.Get2D( img, n,m)
                qimg.setPixel( m, n, QtGui.qRgb( pval[2], pval[1], pval[0]))
        ui.graphicsView.addItem(qimg)

if __name__ == "__main__":
    import sys
    ticker = ticktock()
    
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()


    QtCore.QObject.connect( ticker, QtCore.SIGNAL('timeout()'), ticker.update)

    ticker.startTimer(500)

    sys.exit(app.exec_())


