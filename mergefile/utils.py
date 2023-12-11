import os
import tempfile
import fitz


# constant
TEMP_PDF_NAME = "temp_pdf_file.pdf"


def create_temp_pdf():
    """임시 PDF 파일 생성
    비어있는 새로운 페이지 1개가 있는 임시 PDF 파일 생성

    Returns:
        temp_pdf_path (str): 임시 PDF 파일 경로

    """
    temp_dir = tempfile.gettempdir()
    temp_pdf_path = os.path.join(temp_dir, TEMP_PDF_NAME)

    temp_pdf = fitz.open()
    temp_pdf.new_page()

    temp_pdf.save(temp_pdf_path)
    temp_pdf.close()

    return temp_pdf_path


def delete_temp_file(temp_file_path=os.path.join(tempfile.gettempdir(), TEMP_PDF_NAME)):
    """임시 파일 삭제
    임의로 생성했던 임시 파일 삭제

    Args:
        temp_file_path (str): 삭제할 임시 파일의 경로

    """
    if os.path.exists(temp_file_path):
        os.remove(temp_file_path)


def merge_to_pdf(files_list, save_dir, save_name, save_format):
    """PDF로 병합

    Args:
        files_list (List[str]): 병합할 파일들의 경로가 담겨있는 리스트
        save_dir (str): 병합된 파일을 저장할 경로
        save_name (str): 병합된 파일을 저장할 이름
        save_format (str): 병합된 파일을 저장할 파일 확장자

    """


def merge_to_img(files_list, save_dir, save_name, save_format):
    """이미지(.png or .jpg)로 병합

    Args:
        files_list (List[str]): 병합할 파일들의 경로가 담겨있는 리스트
        save_dir (str): 병합된 파일을 저장할 경로
        save_name (str): 병합된 파일을 저장할 이름
        save_format (str): 병합된 파일을 저장할 파일 확장자

    """
