import sys
import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QMessageBox,
    QProgressDialog,
)
from Merge2PDF_UI import Ui_MainWindow
import utils
from custom_errors import *
from __init__ import __version__


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def open_help(self):
        os.startfile("https://stroad.github.io/Merge2PDF-help")

    def open_info(self):
        text = f"""<h3>Merge to PDF 정보</h3>
<p>Merge to PDF</p>
<p><a href="https://github.com/STROAD/Merge2PDF">Merge to PDF GitHub</a></p>
<p>버전: {__version__}</p>"""

        QMessageBox.about(self, "Merge to PDF", text)

    def add_folder(self):
        """선택 폴더 내 특정 확장자를 가진 파일들의 [경로\파일명]을 files_list widget에 추가"""
        file_list_widget = self.ui.files_list

        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder != "":
            folder = folder.replace("/", "\\")

            files_list = [
                "".join((folder, "\\", file))
                for file in os.listdir(folder)
                if file.endswith((".pdf", ".png", ".jpg", ".jpeg"))
            ]
            file_list_widget.addItems(files_list)

    def add_files(self):
        """선택 파일을 files_list widget에 추가
        (특정 확장자를 가진 파일만 선택 가능)
        """
        file_list_widget = self.ui.files_list

        files = QFileDialog.getOpenFileNames(
            self,
            "Select Files",
            filter="사용자 지정 파일 (*.png *.jpg *.jpeg *.pdf)",
        )[0]

        if files:
            for i in range(len(files)):
                files[i] = files[i].replace("/", "\\")

            file_list_widget.addItems(files)

    def remove_files(self):
        """iles_list widget에서 선택한 파일 제거"""
        file_list_widget = self.ui.files_list

        selected_indexes = file_list_widget.selectedIndexes()

        if selected_indexes:
            selected_indexes.sort(reverse=True)

            for file in selected_indexes:
                file_list_widget.takeItem(file.row())

    def select_folder(self):
        """병합 완료된 파일을 다운로드할 폴더 선택"""

        download_folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if download_folder != "":
            download_folder = download_folder.replace("/", "\\")

            self.ui.lineEdit_path.setText(download_folder)

    def start_merge(self):
        """파일 병합 시작

        Raises:
            PathError: 경로가 올바르지 않은 경우 발생
            FileNameError: 파일 이름이 올바르지 않은 경우 발생
            NoFileError: 병합할 파일이 없는 경우 발생
        """
        file_list_widget = self.ui.files_list

        download_path = self.ui.lineEdit_path.text()
        file_name = self.ui.lineEdit_name.text()

        if not utils.is_valid_path(download_path):
            QMessageBox.warning(self, "다운로드 위치 오류", "다운로드 위치가 잘못되었습니다.")
            raise PathError(download_path)
        elif not utils.is_valid_name(file_name):
            QMessageBox.warning(self, "파일 이름 오류", "파일 이름이 잘못되었습니다.")
            raise FileNameError(file_name, "invalid")
        elif utils.is_file_name_duplicate(download_path, file_name):
            reply = QMessageBox.question(
                self, "파일 이름 중복", "동일한 이름의 파일이 존재합니다. 덮어 씌우겠습니까?"
            )

            if reply == QMessageBox.StandardButton.No:
                file_name += ".pdf"
                raise FileNameError(file_name, "duplicate")

        # pdf_compression: True -> 압축 O, False -> 압축 X
        pdf_compression = self.ui.radioButton_yes.isChecked()
        files_list = [
            file_list_widget.item(i).text() for i in range(file_list_widget.count())
        ]
        if not files_list:
            QMessageBox.warning(self, "파일 없음", "병합할 파일이 없습니다.")
            raise NoFileError

        progress = QProgressDialog("파일 병합중...", "중단", 0, len(files_list) + 2, self)
        progress.setWindowTitle("Merge to PDF")
        progress.setWindowModality(Qt.WindowModal)
        progress.setMinimumDuration(0)

        cancelled = utils.merge_to_pdf(
            files_list,
            download_path,
            file_name,
            pdf_compression,
            len(files_list),
            progress,
        )

        if cancelled:
            QMessageBox.information(self, "파일 병합 취소", "파일 병합이 취소되었습니다.")
        else:
            QMessageBox.information(self, "파일 병합 완료", "파일 병합이 완료되었습니다.")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        utils.delete_temp_file()
