import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from resources.Merge2PDF_UI import Ui_MainWindow
import re
import utils


class DownloadDirError(Exception):
    pass


class FileNameError(Exception):
    pass


class NoFileError(Exception):
    pass


def close():
    QMainWindow.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def add_folder(self):
        """선택 폴더 내 (file_filter에 존재하는 확장자를 가진)모든 파일을 files_list widget에 추가"""
        file_list_widget = self.ui.files_list

        folder = QFileDialog.getExistingDirectory(self, "Select Folder").replace(
            "/", "\\"
        )

        # folder에 존재하는 모든 파일 중 file_filter의 확장자를 가진 파일들만 파일 경로와 파일명을 같이 저장
        files_list = [
            "".join((folder, "\\", file))
            for file in os.listdir(folder)
            if file.endswith((".pdf", ".png", ".jpg", ".jpeg"))
        ]
        file_list_widget.addItems(files_list)

    def add_files(self):
        """선택 파일을 files_list widget에 추가
        (file_filter에 존재하는 확장자를 가진 파일만 선택 가능)
        """
        file_list_widget = self.ui.files_list

        files = QFileDialog.getOpenFileNames(
            self,
            "Select Files",
            filter="사용자 지정 파일 (*.png *.jpg *.jpeg *.pdf)",
        )[0]

        for i in range(len(files)):
            files[i] = files[i].replace("/", "\\")

        file_list_widget.addItems(files)

    def remove_files(self):
        """iles_list widget에서 선택한 파일을 제거"""
        file_list_widget = self.ui.files_list

        for file in file_list_widget.selectedIndexes():
            file_list_widget.takeItem(file.row())

    def select_folder(self):
        """병합 완료된 파일을 다운로드할 폴더 선택"""

        download_folder = QFileDialog.getExistingDirectory(
            self, "Select Folder"
        ).replace("/", "\\")

        self.ui.lineEdit_dir.setText(download_folder)

    def start_merge(self):
        """파일 병합 시작

        Raises:
            DownloadDirError: 파일 경로가 올바르지 않은 경우 발생
            FileNameError: 파일 이름이 올바르지 않은 경우 발생
            NoFileError: 병합할 파일이 없는 경우 발생
        """
        file_list_widget = self.ui.files_list

        download_dir = self.ui.lineEdit_dir.text()
        file_name = self.ui.lineEdit_name.text()

        dir_pattern = r"^[a-zA-Z]:\\(?:[a-zA-Z0-9\s_@\-^!#$%&+={}\[\]]+\\)*[a-zA-Z0-9\s_@\-^!#$%&+={}]+\\?$"
        name_pattern = r"^[a-zA-Z0-9_-]{1,255}$"
        if not re.match(dir_pattern, download_dir):
            QMessageBox.warning(self, "다운로드 위치 오류", "다운로드 위치가 잘못되었습니다.")
            raise DownloadDirError
        elif not re.match(name_pattern, file_name):
            QMessageBox.warning(self, "파일 이름 오류", "파일 이름이 잘못되었습니다.")
            raise FileNameError

        pdf_compression = self.ui.radioButton_yes.isChecked()
        files_list = [
            file_list_widget.item(i).text() for i in range(file_list_widget.count())
        ]
        if not files_list:
            QMessageBox.warning(self, "파일 없음", "병합할 파일이 없습니다.")
            raise NoFileError

        utils.merge_to_pdf(files_list, download_dir, file_name, pdf_compression)

        QMessageBox.information(self, "파일 병합 완료", "파일 병합이 완료되었습니다.")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())