from PyQt5.QtCore import Qt

from pyqt_slideshow import SlideShow


class CustomSettings(SlideShow):
    # For overriding some pyqt_slideshow functionalities.
    def _SlideShow__initUi(self, *args, **kwargs):
        super()._SlideShow__initUi(*args, **kwargs) # Bring initUI from the library.
        self.qtimer = self._SlideShow__timer # Set the library's timer variable to a new one.
        self.timer = ToggleableTimer(self.qtimer) # Set ToggleableTimer class to a variable.
        self._SlideShow__timer = self.timer # When library's timer is called, use ours instead.

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            self.close()
        if event.key() == Qt.Key_P:
            self.toggleSlideShowPlayback()
        if event.key() == Qt.Key_K:
            self._SlideShow__next()
            # If the timer is already running, reset the countdown.
            if self.timer.disabled == False:
                SlideShow.setInterval(self, 1000)
        if event.key() == Qt.Key_J:
            if self.timer.disabled:
                self._SlideShow__prev()
                # Library starts the timer here, so we stop it.
                self.timer.stop()
            else:
                self._SlideShow__prev()
                # Timer is already running, reset the countdown.
                SlideShow.setInterval(self, 1000)

    # TODO: Respect the timer state when UI elements are clicked.
        
    def toggleSlideShowPlayback(self):
        if self.timer.disabled:
            self.timer.start()
        else:
            self.timer.stop()


class ToggleableTimer:
    def __init__(self, qtimer):
        self.qtimer = qtimer
        self.disabled = True

# Since we're replacing the library timer, we need to define methods it'd need.
    def start(self):
        self.qtimer.start()
        self.disabled = False
    
    def stop(self):
        self.qtimer.stop()
        self.disabled = True

    def setInterval(self, value: int):
        self.qtimer.setInterval(value)
