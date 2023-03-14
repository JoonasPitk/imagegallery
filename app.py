from pathlib import Path
from sys import argv

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from pyqt_slideshow import SlideShow

from customFileDialog import fileDialog


modulePath = Path(__file__).parent.absolute()
iconPath = modulePath / "icon"


class ToggleableTimer:
    def __init__(self, qtimer):
        self.qtimer = qtimer
        self.disabled = True

# Since we're replacing the library timer, we need to define methods it'd need.
    def start(self):
        # Timer starts, since disabled is set as True.
        if self.disabled:
            self.qtimer.start()
            self.disabled = False
    
    def stop(self):
        self.qtimer.stop()
        self.disabled = True

    def setInterval(self, value):
        self.qtimer.setInterval(value)


# TODO: Stop the timer when manually moving between pictures.
class CustomSettings(SlideShow):
    # For overriding some pyqt_slideshow functionalities.
    def _SlideShow__initUi(self, *args, **kwargs):
        super()._SlideShow__initUi(*args, **kwargs) # Bring initUI from the library.
        self.qtimer = self._SlideShow__timer # Set the library's timer variable to a new one.
        self.timer = ToggleableTimer(self.qtimer) # Set ToggleableTimer class to a variable.
        self._SlideShow__timer = self.timer # When library's timer is called, use ours instead.

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_P:
            self.toggleSlideShowPlayback()
        if event.key() == Qt.Key_Q:
            self.close()
        
    def toggleSlideShowPlayback(self):
        if self.timer.disabled:
            self.timer.start()
        else:
            self.timer.stop()


def main():
    app = QApplication(argv)
    selectedFiles = fileDialog()
    if not selectedFiles:
        return
    slideShow = CustomSettings()
    # TODO: Set the window size to 16:9, not by the first loaded picture.
    slideShow.setWindowTitle("Image Gallery")
    slideShow.setFilenames(selectedFiles)
    # Fit an image to the window, no matter the aspect ratio.
    slideShow._SlideShow__view.setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)
    # slideShow.setNavigationButtonVisible(False) # Do not show left and right navigation buttons.
    # slideShow.setBottomButtonVisible(False) # Do not show bottom navigation buttons.
    slideShow.setInterval(1000) # Milliseconds before moving to the next image.
    slideShow.setTimerEnabled(False) # Disable the slide show timer for the first image.
    slideShow._SlideShow__nextBtn.setIcon(iconPath / "next.svg")
    slideShow._SlideShow__prevBtn.setIcon(iconPath / "prev.svg")
    slideShow.show()
    app.exec_()


if __name__ == "__main__":
    main()
