from pathlib import Path
from sys import argv

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from pyqt_slideshow import SlideShow

from customFileDialog import fileDialog


modulePath = Path(__file__).parent.absolute()
iconPath = modulePath / "icon"

def main():
    app = QApplication(argv)
    selectedFiles = fileDialog()
    if not selectedFiles:
        return
    slideShow = SlideShow()
    slideShow.setWindowTitle("Image Gallery")
    slideShow.setFilenames(selectedFiles)
    slideShow._SlideShow__view.setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)
    # slideshow.setNavigationButtonVisible(False) # Do not show left and right navigation buttons.
    # slideshow.setBottomButtonVisible(False) # Do not show bottom navigation buttons.
    # slideshow.setInterval(2000) # Milliseconds before moving to the next image.
    slideShow.setTimerEnabled(False) # Disable the slideshow timer when booted up.
    slideShow._SlideShow__nextBtn.setIcon(iconPath / "next.svg")
    slideShow._SlideShow__prevBtn.setIcon(iconPath / "prev.svg")
    slideShow.show()
    app.exec_()


if __name__ == "__main__":
    main()
