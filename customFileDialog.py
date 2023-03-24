from os import fspath
from pathlib import Path

from PyQt5.QtWidgets import QFileDialog, QDialog


def fileDialog(parent = None, title = "Select files", directory = "",
                    filter = "Image files (*.jpg *.jpeg *.png *.gif *.svg *.webp)",
                    initialFilter = "",
                    options = None):
    dialog = QFileDialog(parent, windowTitle = title)
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

    # By default, if a directory is opened in file listing mode, 
    # QFileDialog.accept() shows the contents of that directory, but we 
    # need to be able to "open" directories as we can do with files, so we 
    # just override accept() with the default QDialog implementation which 
    # will just return exec_()
    dialog.accept = lambda: QDialog.accept(dialog)
    dialogResult = dialog.exec_()
    if dialogResult != QDialog.Accepted:
        return []
    return expandDirs(dialog.selectedFiles())

def expandDirs(paths):
    result = []
    types = ("*.jpg", "*.jpeg", "*.png", "*.gif", "*.svg", "*.webp")
    for pathString in paths:
        path = Path(pathString)
        if path.is_dir():
            for files in types:
                result.extend(sorted(fspath(dir) for dir in path.rglob(files)))
        else:
            result.append(pathString)
    return result
