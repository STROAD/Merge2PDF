import sys
import os
from tempfile import gettempdir
import fitz
from re import match

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from merge2pdf import utils


def test_is_valid_path():
    valid_path = os.getenv("USERPROFILE")
    assert utils.is_valid_path(valid_path) is True

    relative_path = "..\\merge2pdf"
    assert utils.is_valid_path(relative_path) is False

    non_existing_path = "/non_existing_directory"
    assert utils.is_valid_path(non_existing_path) is False

    assert utils.is_valid_path("") is False

    assert utils.is_valid_path(None) is False

    assert utils.is_valid_path(0) is False


def test_is_valid_name():
    test_cases = [
        ("myfile", True),
        ("file1234", True),
        ("01234", True),
        ("document_v2", True),
        ("my<file", False),
        ("file|1234", False),
        ("doc?", False),
        ("pdf.pdf", False),
    ]

    for name, expected_result in test_cases:
        assert utils.is_valid_name(name) is expected_result


def test_create_temp_pdf():
    temp_pdf_path = utils.create_temp_pdf()

    assert os.path.exists(temp_pdf_path) is True

    assert temp_pdf_path.endswith(".pdf") is True

    utils.delete_temp_file()
    assert os.path.exists(temp_pdf_path) is False


def test_delete_temp_file(tmpdir):
    existing_file_path = str(tmpdir.join("existing_file.txt"))
    open(existing_file_path, "w").close()

    assert os.path.isfile(existing_file_path) == True
    utils.delete_temp_file(existing_file_path)
    assert os.path.isfile(existing_file_path) == False

    non_existing_file_path = str(tmpdir.join("non_existing_file.txt"))

    assert os.path.isfile(non_existing_file_path) == False
    utils.delete_temp_file(non_existing_file_path)
