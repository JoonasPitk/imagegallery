from PyQt5.QtWidgets import QApplication
from pyqt_slideshow import SlideShow


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    s = SlideShow()
    s.setFilenames([
        "./testpictures/AlbumArt1.jpg",
        "./testpictures/AlbumArt2.jpg",
        "./testpictures/AlbumArt3.jpg",
        "./testpictures/AlbumArt4.jpg",
        "./testpictures/AlbumArt5.jpg",])
    # s.setNavigationButtonVisible(False) # to not show the navigation button
    # s.setBottomButtonVisible(False) # to not show the bottom button
    s.show()
    app.exec_()
