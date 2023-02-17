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
    # TODO: Set the window size to 16:9, not by the first loaded picture.
    slideShow.setWindowTitle("Image Gallery")
    slideShow.setFilenames(selectedFiles)
    # Fit an image to the window, no matter the aspect ratio.
    slideShow._SlideShow__view.setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)
    # slideShow.setNavigationButtonVisible(False) # Do not show left and right navigation buttons.
    # slideShow.setBottomButtonVisible(False) # Do not show bottom navigation buttons.
    # slideShow.setInterval(2000) # Milliseconds before moving to the next image.
    # TODO: Disable the timer altogether.
    slideShow.setTimerEnabled(False) # Disable the slide show timer for the first image.
    slideShow._SlideShow__nextBtn.setIcon(iconPath / "next.svg")
    slideShow._SlideShow__prevBtn.setIcon(iconPath / "prev.svg")
    slideShow.show()
    app.exec_()


if __name__ == "__main__":
    main()
