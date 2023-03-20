from pathlib import Path

from PyQt5.QtCore import Qt
from pyqt_slideshow import SlideShow


class CustomSettings(SlideShow):

    def _SlideShow__initUi(self, *args, **kwargs):
        super()._SlideShow__initUi(*args, **kwargs) # Bring __initUI from the library.
    
        # Replace pyqt_slideshow's timer.

        self.qtimer = self._SlideShow__timer # Get the library's original timer to self.qtimer.
        self.timer = ToggleableTimer(self.qtimer) # Create a wrapped timer from the original QTimer.
        self._SlideShow__timer = self.timer # Replace the library's timer with ours.

        # Set our own timer interval.
        self.interval = 1000 # In milliseconds.
        self.setInterval(self.interval)

        # Disable the timer at the start.
        self.setTimerEnabled(False)

        # Keep the aspect ratio of images.
        self._SlideShow__view.setAspectRatioMode(Qt.KeepAspectRatio)

        # Set custom icons.

        modulePath = Path(__file__).parent.absolute()
        iconPath = modulePath / "icon"
        self._SlideShow__nextBtn.setIcon(iconPath / "next.svg")
        self._SlideShow__prevBtn.setIcon(iconPath / "prev.svg")

        # self.setNavigationButtonVisible(False) # Do not show left and right navigation buttons.
        # self.setBottomButtonVisible(False) # Do not show bottom navigation buttons.

        # TODO: Set the window aspect ratio to 16:9, not by the first loaded picture?

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            self.close()
        if event.key() == Qt.Key_P:
            self.toggleSlideShowPlayback()
        if event.key() == Qt.Key_K:
            self._SlideShow__next()
            self.setInterval(self.interval)
        if event.key() == Qt.Key_J:
            self._SlideShow__prev()
            self.setInterval(self.interval)
        
    def toggleSlideShowPlayback(self):
        if self.timer.disabled:
            self.timer.enable()
        else:
            self.timer.disable()


class ToggleableTimer:
    def __init__(self, qtimer):
        self.qtimer = qtimer
        self.disabled = True

    def enable(self):
        self.disabled = False
        self.start()

    def disable(self):
        self.stop()
        self.disabled = True

    # Since we're replacing the library timer, we need to define methods it'll need.

    def start(self):
        if self.disabled:
            return
        self.qtimer.start()
    
    def stop(self):
        self.qtimer.stop()

    def setInterval(self, value: int):
        self.qtimer.setInterval(value)
