import sys
from PyQt4 import QtCore, QtGui, uic
from skimage import util, io
import qimage2ndarray
import numpy as np
import scipy.misc

qtCreatorFile = "untitled.ui"  # Enter file here.
qimg = QtGui.QImage()
qimg2 = QtGui.QImage()

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.openImg.clicked.connect(self.openFile)
        self.pushButton_3.clicked.connect(self.invert)
        self.pushButton.clicked.connect(self.verticalFlip)
        self.pushButton_5.clicked.connect(self.horiFlip)
        self.pushButton_4.clicked.connect(self.saveImg)

    def openFile(self):
        """path = QtGui.QFileDialog.getOpenFileName(None, "Select Image")"""
        path = '/home/rujeet/Firefox_wallpaper.png'
        image1 = io.imread(path)
        qimg = qimage2ndarray.array2qimage(image1)
        global qimg2
        qimg2 = qimg
        self.pix = QtGui.QPixmap.fromImage(qimg)
        self.pix = self.pix.scaled(
            self.label_2.width(), self.label_2.height(),
            QtCore.Qt.KeepAspectRatio)
        self.label_2.setPixmap(self.pix)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)

    def invert(self):
        print("invert Pressed")
        global qimg2
        imgNdArray = qimage2ndarray.rgb_view(qimg2)
        invertImage = util.invert(imgNdArray)
        qimg2 = qimage2ndarray.array2qimage(invertImage)
        pixmap2 = QtGui.QPixmap.fromImage(
            qimage2ndarray.array2qimage(invertImage))
        pixmap2 = pixmap2.scaled(
            self.label_2.width(), self.label_2.height(),
            QtCore.Qt.KeepAspectRatio)
        self.label_2.setPixmap(pixmap2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)

    def verticalFlip(self):
        global qimg2
        imgNdArray = qimage2ndarray.rgb_view(qimg2)
        imgNdArray = imgNdArray[::-1]
        qimg2 = qimage2ndarray.array2qimage(imgNdArray)
        pixmap2 = QtGui.QPixmap.fromImage(qimg2)
        pixmap2 = pixmap2.scaled(
            self.label_2.width(), self.label_2.height(),
            QtCore.Qt.KeepAspectRatio)
        self.label_2.setPixmap(pixmap2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)

    def horiFlip(self):
        global qimg2
        imgNdArray = qimage2ndarray.rgb_view(qimg2)
        imgNdArray = np.fliplr(imgNdArray)
        qimg2 = qimage2ndarray.array2qimage(imgNdArray)
        pixmap2 = QtGui.QPixmap.fromImage(qimg2)
        pixmap2 = pixmap2.scaled(
            self.label_2.width(), self.label_2.height(),
            QtCore.Qt.KeepAspectRatio)
        self.label_2.setPixmap(pixmap2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)

    def saveImg(self):
        print("save pressed")
        imgArray = qimage2ndarray.rgb_view(qimg2)
        print(imgArray)
        io.imsave('output.jpg', imgArray)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
