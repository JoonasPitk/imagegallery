from os import execl
from sys import executable, argv
from pathlib import Path
from configparser import ConfigParser

from PyQt5.QtCore import Qt
from pyqt_slideshow import SlideShow

from ownTimer import ToggleableTimer

config = ConfigParser()
config.read("config.ini")

class CustomSettings(SlideShow):

    def _SlideShow__initUi(self, *args, **kwargs):
        super()._SlideShow__initUi(*args, **kwargs) # Bring __initUI from the library.
    
        # Replace pyqt_slideshow's timer.

        self.qtimer = self._SlideShow__timer # Get the library's original timer to self.qtimer.
        self.timer = ToggleableTimer(self.qtimer) # Create a wrapped timer from the original QTimer.
        self._SlideShow__timer = self.timer # Replace the library's timer with ours.

        # Set our own interval for the timer.
        self.interval = config.getint("Timer", "interval")
        self.setInterval(self.interval)

        # Start with a disabled timer.
        self.setTimerEnabled(config.getboolean("Timer", "state"))
        if config.getboolean("Timer", "state") == True: 
            self.timer.disabled = False

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

        # Close the slide show and reboot the application.
        if event.key() == Qt.Key_N:
            execl(executable, executable, *argv)
        if event.key() == Qt.Key_P:
            self.toggleSlideShowPlayback()
        if event.key() == Qt.Key_K:
            self._SlideShow__next()

            # If the timer is running, reset the countdown.
            if self.timer.disabled == False:
                self.setInterval(self.interval)
        if event.key() == Qt.Key_J:
            self._SlideShow__prev()

            # If the timer is running, reset the countdown.
            if self.timer.disabled == False:
                self.setInterval(self.interval)
        
    def toggleSlideShowPlayback(self):
        if self.timer.disabled:
            self.timer.enable()
        else:
            self.timer.disable()
