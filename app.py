from os import fspath
from pathlib import Path
from sys import argv

from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog #, QStackedWidget, QListView, QLineEdit
from pyqt_slideshow import SlideShow


module_path = Path(__file__).parent.absolute()
icon_path = module_path / "icon"

def main():
    app = QApplication(argv)
    selectedFiles = getOpenFilesAndDirs()
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

def getOpenFilesAndDirs(parent=None, caption="Select files", directory="",
                        filter="", initialFilter="", options=None):
    # def updateText():
    #     # update the contents of the line edit widget with the selected files
    #     selected = []
    #     for index in view.selectionModel().selectedRows():
    #         selected.append("'{}'".format(index.data()))
    #     lineEdit.setText(" ".join(selected))

    dialog = QFileDialog(parent, windowTitle=caption)
    dialog.setFileMode(dialog.ExistingFiles)
    if options:
        dialog.setOptions(options)
    dialog.setOption(dialog.DontUseNativeDialog, True)
    if directory:
        dialog.setDirectory(directory)
    if filter:
        dialog.setNameFilter(filter)
        if initialFilter:
            dialog.selectNameFilter(initialFilter)

    # by default, if a directory is opened in file listing mode, 
    # QFileDialog.accept() shows the contents of that directory, but we 
    # need to be able to "open" directories as we can do with files, so we 
    # just override accept() with the default QDialog implementation which 
    # will just return exec_()
    dialog.accept = lambda: QDialog.accept(dialog)

    # there are many item views in a non-native dialog, but the selectedRones displaying 
    # the actual contents are created inside a QStackedWidget; they are a 
    # QTreeView and a QListView, and the tree is only used when the 
    # viewMode is set to QFileDialog.Details, which is not this case
    # stackedWidget = dialog.findChild(QStackedWidget)
    # view = stackedWidget.findChild(QListView)
    # view.selectionModel().selectionChanged.connect(updateText)

    # lineEdit = dialog.findChild(QLineEdit)
    # # clear the line edit contents whenever the current directory changes
    # dialog.directoryEntered.connect(lambda: lineEdit.setText(""))

    dialog.exec_()
    return expandDirs(dialog.selectedFiles())

def expandDirs(paths):
    result = []
    for pathString in paths:
        path = Path(pathString)
        if path.is_dir():
            result.extend(fspath(x) for x in path.iterdir())
        else:
            result.append(pathString)
    return result


if __name__ == "__main__":
    main()
