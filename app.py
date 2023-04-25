from sys import argv

from PyQt5.QtWidgets import QApplication

from customFileDialog import fileDialog
from adjustments import CustomSettings


def main():
    app = QApplication(argv)
    selectedFiles = fileDialog()
    if not selectedFiles:
        return
    slideShow = CustomSettings()
    slideShow.setWindowTitle("Image Gallery")
    slideShow.setFilenames(selectedFiles)
    slideShow.show()
    app.exec_()

if __name__ == "__main__":
    main()
