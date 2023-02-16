from os import fspath
from pathlib import Path
from sys import argv

from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog
from pyqt_slideshow import SlideShow


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

def customFileDialog(parent = None, title = "Select files", directory = "",
                    filter = "Image files (*.jpg *.png *.gif *.svg)", initialFilter = "",
                    options = None):
    dialog = QFileDialog(parent, windowTitle = title)
    dialog.setFileMode(dialog.FileMode.ExistingFiles)
    if options:
        dialog.setOptions(options)
    dialog.setOption(dialog.Option.DontUseNativeDialog, True)
    if directory:
        dialog.setDirectory(directory)
    if filter:
        dialog.setNameFilter(filter)
        if initialFilter:
            dialog.selectNameFilter(initialFilter)

    # By default, if a directory is opened in file listing mode, 
    # QFileDialog.accept() shows the contents of that directory, but we 
    # need to be able to "open" directories as we can do with files, so we 
    # just override accept() with the default QDialog implementation which 
    # will just return exec_()
    dialog.accept = lambda: QDialog.accept(dialog)
    dialogResult = dialog.exec_()
    if dialogResult != QDialog.DialogCode.Accepted:
        return []
    return expandDirs(dialog.selectedFiles())

def expandDirs(paths):
    result = []
    for pathString in paths:
        path = Path(pathString)
        if path.is_dir():
            result.extend(sorted(fspath(x) for x in path.iterdir()))
        else:
            result.append(pathString)
    return result


if __name__ == "__main__":
    main()
