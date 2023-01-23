import sys
import pathlib

from PyQt5.QtWidgets import QApplication
from pyqt_slideshow import SlideShow

module_path = pathlib.Path(__file__).parent.absolute()
icon_path = module_path / "icon"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    slideshow = SlideShow()
    slideshow.setFilenames([
        "./testpictures/AlbumArt1.jpg",
        "./testpictures/AlbumArt2.jpg",
        "./testpictures/AlbumArt3.jpg",
        "./testpictures/AlbumArt4.jpg",
        "./testpictures/AlbumArt5.jpg",])
    # slideshow.setNavigationButtonVisible(False) # Do not show left and right navigation buttons.
    # slideshow.setBottomButtonVisible(False) # Do not show bottom navigation buttons.
    slideshow.setTimerEnabled(False) # Disable the slideshow timer when booted up.
    slideshow._SlideShow__nextBtn.setIcon(icon_path / "next.svg")
    slideshow._SlideShow__prevBtn.setIcon(icon_path / "prev.svg")
    slideshow.show()
    app.exec_()
