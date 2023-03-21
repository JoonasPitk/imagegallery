class ToggleableTimer():
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
        
        # Prevent some library methods from starting the timer
        if self.disabled:
            return
        self.qtimer.start()
        print("start")
    
    def stop(self):
        self.qtimer.stop()
        print("stop")

    def setInterval(self, value: int):
        self.qtimer.setInterval(value)
        print("interval set")
