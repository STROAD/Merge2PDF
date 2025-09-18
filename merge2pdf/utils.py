import os
from tempfile import gettempdir
import fitz
import comtypes.client
from re import match


# constant
TEMP_PDF_NAME = "temp_pdf_file.pdf"


def is_valid_path(path):
    """경로 유효성 검사
    입력받은 경로가 존재하는 디렉터리인지, 절대경로인지, 접근 가능한지 확인
    Args:
        path (str): 유효성 검사를 할 경로

    Returns:
        bool: True(유효한 경로) or False(유효하지 않은 경로)

    """
    if path is None or not isinstance(path, str):
        return False

    if not os.path.isdir(path):
        return False

    if not os.path.isabs(path):
        return False

    if not os.access(path, os.W_OK) and os.access(path, os.R_OK):
        return False

    return True


def is_valid_name(name):
    """이름 유효성 검사
    입력받은 (파일)이름이 윈도우 상에서 유효한 (파일)이름인지 확인

    Args:
        name (str): 유효성 검사를 할 (파일)이름

    Returns:
        bool: True(유효한 이름) or False(유효하지 않은 이름)

    """
    name_pattern = r'^[^<>:"/\\|?*\x00-\x1F.]+$'

    if match(name_pattern, name):
        return True
    else:
        return False


def is_file_name_duplicate(path, file_name):
    """파일 이름 중복 검사
    입력받은 주소에 입력받은 파일 이름과 동일한 이름의 파일이 있는지 확인

    Args:
        path (str): 파일 이름 중복 검사를 할 파일의 경로
        file_name (str): 파일 이름 중복 검사를 할 파일 이름

    Returns:
        bool: True(중복됨) or False(중복되지 않음)

    """
    file_name += ".pdf"

    if os.path.exists(os.path.join(path, file_name)):
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


def is_office_app_installed(app_name):
    """Office 애플리케이션이 설치되었는지 확인

    Args:
        app_name (str): 확인할 애플리케이션의 COMProgID (예: "PowerPoint.Application").

    Returns:
        bool: 애플리케이션이 설치되었으면 True, 아니면 False
    """
    try:
        # COM 객체 생성을 시도
        comtypes.client.CreateObject(app_name, dynamic=True)
        return True
    except (OSError, comtypes.COMError):
        # COM 객체 생성에 실패시 설치되지 않은 것으로 간주
        return False
    except Exception as e:
        print(f"애플리케이션 설치 여부 확인 중 오류 발생: {e}")
        return False


def get_supported_extensions(type=0):
    """지원 가능한 확장자 확인

    Args:
        type (int): 지원 가능 확장자를 반환해줄 때 어떤 형식으로 반환할지 설졍
            type 0: ('.pdf', '.png'), type 1: ("*.pdf *.png")

    Returns:
        supported_extensions (tuple): 지원 가능한 확장자
    """
    supported_extensions = tuple()

    SUPPORTED_DEFAULT_EXTENSIONS = (".pdf", ".png", ".jpg", ".jpeg")
    SUPPORTED_PPT_EXTENSIONS = (".ppt", ".pptx")
    SUPPORTED_WORD_EXTENSIONS = (".doc", ".docx")

    supported_extensions += SUPPORTED_DEFAULT_EXTENSIONS

    if is_office_app_installed("PowerPoint.Application"):
        supported_extensions += SUPPORTED_PPT_EXTENSIONS
    if is_office_app_installed("Word.Application"):
        supported_extensions += SUPPORTED_WORD_EXTENSIONS

    if type == 1:
        supported_extensions = (" ".join(f"*{_}" for _ in supported_extensions),)

    return supported_extensions


def convert_to_pdf(file_path, save_dir=gettempdir(), save_name=TEMP_PDF_NAME):
    """PDF로 변환
    PowerPoint, Word 파일을 PDF로 변환

    Args:
        file_path (str): 변환할 파일의 경로
        save_dir (str): 변환된 파일을 저장할 경로
        save_name (str): 변환된 파일을 저장할 이름

    Returns:
        pdf_path (str): 변환된 PDF 파일의 경로

    """

    file_path = os.path.abspath(file_path)
    save_path = os.path.abspath(os.path.join(save_dir, save_name))

    app = None
    try:
        file_extension = os.path.splitext(file_path)[1].lower()

        if file_extension in [".ppt", ".pptx"]:
            app = comtypes.client.CreateObject("PowerPoint.Application")
            doc = app.Presentations.Open(file_path, WithWindow=False)
            save_format = 32  # ppSaveAsPDF

        elif file_extension in [".doc", ".docx"]:
            app = comtypes.client.CreateObject("Word.Application")
            doc = app.Documents.Open(file_path, ReadOnly=True)
            save_format = 17  # wdFormatPDF

        # app.Visible = False
        doc.SaveAs(save_path, FileFormat=save_format)

        return save_path

    except Exception as e:
        print(f"변환 중 오류 발생 {e}")
        delete_temp_file(save_path)
        raise e

    finally:
        if doc:
            doc.Close()
        if app:
            app.Quit()


def merge_to_pdf(files_list, save_dir, save_name, pdf_compression, length, progress):
    """PDF로 병합

    Args:
        files_list (List[str]): 병합할 파일들의 경로가 담겨있는 리스트
        save_dir (str): 병합된 파일을 저장할 경로
        save_name (str): 병합된 파일을 저장할 이름
        pdf_compression (str): PDF 압축 저장 여부
        length (str): files_list의 길이
        progress: Progress Dialog

    Returns:
        bool: True(병합 중단) or False(병합 중단 X)

    """
    cancelled = False

    temp_pdf_path = create_temp_pdf()
    temp_pdf = fitz.open(temp_pdf_path)
    progress.setValue(0)

    # 파일 병합
    for i, file in enumerate(files_list):
        try:
            if not os.path.exists(file):
                raise FileNotFoundError
        except FileNotFoundError:
            continue

        if progress.wasCanceled():
            cancelled = True
            break

        doc = fitz.open(file)
        progress.setValue(1 + i)

        if file.endswith(".pdf"):
            temp_pdf.insert_pdf(doc)
        else:
            temp_pdf.insert_file(doc)

        doc.close()

        progress.setValue(2 + i)

    if not cancelled:
        # create_temp_pdf()에서 임의로 생성한 빈 페이지 삭제
        temp_pdf.delete_page(0)

        # 파일 저장
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
        progress.setValue(length + 2)

    temp_pdf.close()
    delete_temp_file(temp_pdf_path)

    return cancelled
