import os
import tempfile
import fitz


def create_temp_pdf():
    """임시 PDF 파일 생성
    비어있는 새로운 페이지 1개가 있는 임시 PDF 파일 생성

    Returns:
        temp_pdf_path (str): 임시 PDF 파일 경로

    """


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
