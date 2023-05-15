from pathlib import Path
from configparser import ConfigParser

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence
from pyqt_slideshow import SlideShow

from ownTimer import ToggleableTimer
from customFileDialog import fileDialog


class CustomSettings(SlideShow):
        
    # Read a config file.
    config = ConfigParser()
    config.read("config.ini")

    def _SlideShow__initUi(self, *args, **kwargs):
        super()._SlideShow__initUi(*args, **kwargs) # Bring __initUI from the library.
    
        # Keep the aspect ratio of images so they always fit.
        self._SlideShow__view.setAspectRatioMode(Qt.KeepAspectRatio)

        # Replace pyqt_slideshow's timer.

        self.qtimer = self._SlideShow__timer # Get the library's original timer to self.qtimer.
        self.timer = ToggleableTimer(self.qtimer) # Create a wrapped timer from the original QTimer.
        self._SlideShow__timer = self.timer # Replace the library's timer with ours.


        # Set our own interval for the timer, via config.ini.
        self.interval = self.config.getint("Timer", "interval", fallback=6000)
        self.setInterval(self.interval)

        # Start with a disabled timer.
        self.setTimerEnabled(self.config.getboolean("Timer", "enabled", fallback=False))
        if self.config.getboolean("Timer", "enabled") == True: 
            self.timer.disabled = False

        # Set icons so they can be found in a compiled application.

        modulePath = Path(__file__).parent.absolute()
        iconPath = modulePath / "icon"
        self._SlideShow__nextBtn.setIcon(iconPath / "next.svg")
        self._SlideShow__prevBtn.setIcon(iconPath / "prev.svg")

        # Set UI elements via config.ini

        self.setNavigationButtonVisible(
            self.config.getboolean("UI", "navarrows", fallback=True))
        self.setBottomButtonVisible(
            self.config.getboolean("UI", "navbuttons", fallback=False))

        # Set signals for the shortcuts.

        self.quit_shortcut = QShortcut(
            QKeySequence(self.config.get("Keybinds", "quit", fallback="Ctrl+Q")), self)
        self.quit_shortcut.activated.connect(self.close)

        self.open_shortcut = QShortcut(
            QKeySequence(self.config.get("Keybinds", "open", fallback="Ctrl+O")), self)
        self.open_shortcut.activated.connect(self.openFileDialog)

    # Reopen the file dialog and open the selected files.
    def openFileDialog(self):
        selectedFiles = fileDialog()
        if not selectedFiles:
            return
        self.setFilenames(selectedFiles)
        self.show()

    # TODO: Set the window aspect ratio to 16:9, not by the first loaded picture?

    def keyPressEvent(self, event):
        # Events for single key presses.

        if event.key() == QKeySequence(
            self.config.get("Keybinds", "nextimage", fallback="K")):
            self._SlideShow__next()

            # If the timer is running, reset the countdown.
            if self.timer.disabled == False:
                self.setInterval(self.interval)
                
        if event.key() == QKeySequence(
            self.config.get("Keybinds", "previmage", fallback="J")):
            self._SlideShow__prev()

            # If the timer is running, reset the countdown.
            if self.timer.disabled == False:
                self.setInterval(self.interval)

        if event.key() == QKeySequence(
            self.config.get("Keybinds", "toggle", fallback="P")):
            self.toggleSlideShowPlayback()

        
    def toggleSlideShowPlayback(self):
        if self.timer.disabled:
            self.timer.enable()
        else:
            self.timer.disable()
