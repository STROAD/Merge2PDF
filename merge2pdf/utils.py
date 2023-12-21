import os
from tempfile import gettempdir
import fitz
from re import match


# constant
TEMP_PDF_NAME = "temp_pdf_file.pdf"


def is_valid_path(path):
    """경로 유효성 검사
    입력받은 경로가 존재하는 디렉터리인지, 절대경로인지, 접근 가능한지 확인
    Args:
        path (str): 유효성 검사를 할 경로

    Returns:
        bool

    """
    if not os.path.isdir(path):
        return False

    if not os.path.isabs(path):
        return False

    if not os.access(path, os.R_OK) and os.access(path, os.W_OK):
        return False

    return True


def is_valid_file_name(file_name):
    """파일 이름 유효성 검사
    입력받은 파일 이름이 윈도우 상에서 유효한 파일 이름인지 확인

    Args:
        file_name (str): 유효성 검사를 할 파일 이름

    Returns:
        bool

    """
    name_pattern = r'^[^<>:"/\\|?*\x00-\x1F.]+$'

    if match(name_pattern, file_name):
        return True
    else:
        return False


def create_temp_pdf():
    """임시 PDF 파일 생성
    비어있는 새로운 페이지 1개가 있는 임시 PDF 파일 생성

    Returns:
        temp_pdf_path (str): 임시 PDF 파일 경로

    """
    temp_dir = gettempdir()
    temp_pdf_path = os.path.join(temp_dir, TEMP_PDF_NAME)

    delete_temp_file(temp_pdf_path)

    temp_pdf = fitz.open()
    temp_pdf.new_page()

    temp_pdf.save(temp_pdf_path)
    temp_pdf.close()

    return temp_pdf_path


def delete_temp_file(temp_file_path=os.path.join(gettempdir(), TEMP_PDF_NAME)):
    """임시 파일 삭제
    임의로 생성했던 임시 파일 삭제

    Args:
        temp_file_path (str): 삭제할 임시 파일의 경로

    """
    if os.path.isfile(temp_file_path):
        os.remove(temp_file_path)


def merge_to_pdf(files_list, save_dir, save_name, pdf_compression, length, progress):
    """PDF로 병합

    Args:
        files_list (List[str]): 병합할 파일들의 경로가 담겨있는 리스트
        save_dir (str): 병합된 파일을 저장할 경로
        save_name (str): 병합된 파일을 저장할 이름
        pdf_compression (str): PDF 압축 저장 여부
        length (str): files_list의 길이
        progress: Progress Dialog

    """
    temp_pdf_path = create_temp_pdf()
    progress.setValue(0)

    temp_pdf = fitz.open(temp_pdf_path)
    progress.setValue(1)

    for i, file in enumerate(files_list):
        if progress.wasCanceled():
            doc.close()
            break

        doc = fitz.open(file)

        if file.endswith(".pdf"):
            temp_pdf.insert_pdf(doc)
        else:
            temp_pdf.insert_file(doc)

        doc.close()

        progress.setValue(i + 2)

    temp_pdf.delete_page(0)
    progress.setValue(length + 2)

    save_name += ".pdf"
    if pdf_compression:
        temp_pdf.save(
            os.path.join(save_dir, save_name),
            garbage=4,
            deflate=True,
            deflate_images=True,
            deflate_fonts=True,
        )
    else:
        temp_pdf.save(os.path.join(save_dir, save_name))
    progress.setValue(length + 3)

    temp_pdf.close()
    progress.setValue(length + 4)

    delete_temp_file(temp_pdf_path)
