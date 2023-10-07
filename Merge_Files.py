import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from Merge_Files_UI import Ui_MainWindow


file_filter = (".pdf", ".png", ".jpg", ".jpeg", ".pptx", ".ppt")


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def add_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")


def close():
    QMainWindow.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
