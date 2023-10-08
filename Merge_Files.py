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
        """선택 폴더 내 (file_filter에 존재하는 확장자를 가진)모든 파일을 files_list widget에 추가"""
        list_widget = self.ui.files_list

        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        files_list = os.listdir(folder)
        files_list = [file for file in files_list if file.endswith(file_filter)]

        list_widget.addItems(files_list)

    def add_files(self):
        """선택 파일을 files_list widget에 추가
        (file_filter에 존재하는 확장자를 가진 파일만 선택 가능)
        """
        list_widget = self.ui.files_list

        files = QFileDialog.getOpenFileNames(
            self,
            "Select Files",
            filter="Images (*.png *.jpg *.jpeg);;PDF (*.pdf);;PowerPoint (*.pptx *.ppt)",
        )[0]
        list_widget.addItems(files)


def close():
    QMainWindow.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
