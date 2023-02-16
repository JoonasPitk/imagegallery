from pathlib import Path
from sys import argv

from PyQt5.QtWidgets import QApplication
from pyqt_slideshow import SlideShow

from customFileDialog import customFileDialog


module_path = Path(__file__).parent.absolute()
icon_path = module_path / "icon"

def main():
    app = QApplication(argv)
    selectedFiles = customFileDialog()
    if not selectedFiles:
        return
    slideShow = SlideShow()
    slideShow.setWindowTitle("Image Gallery")
    slideShow.setFilenames(selectedFiles)
    # slideshow.setNavigationButtonVisible(False) # Do not show left and right navigation buttons.
    # slideshow.setBottomButtonVisible(False) # Do not show bottom navigation buttons.
    # slideshow.setInterval(2000) # Milliseconds before moving to the next image.
    slideShow.setTimerEnabled(False) # Disable the slideshow timer when booted up.
    slideShow._SlideShow__nextBtn.setIcon(icon_path / "next.svg")
    slideShow._SlideShow__prevBtn.setIcon(icon_path / "prev.svg")
    slideShow.show()
    app.exec_()


if __name__ == "__main__":
    main()
