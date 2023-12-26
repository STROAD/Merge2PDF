import sys
import os
import pytest
from unittest.mock import Mock

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


def test_is_file_name_duplicate():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources")
    test_cases = [
        ("0", True),
        ("1", True),
        ("19", True),
        ("a", False),
        ("abc", False),
        ("abc123", False),
        ("name_0", False),
        ("pdf.pdf", False),
    ]

    for name, expected_result in test_cases:
        assert utils.is_file_name_duplicate(path, name) is expected_result


def test_create_temp_pdf():
    temp_pdf_path = utils.create_temp_pdf()

    assert os.path.exists(temp_pdf_path) is True

    assert temp_pdf_path.endswith(".pdf") is True

    utils.delete_temp_file()
    assert os.path.exists(temp_pdf_path) is False


def test_delete_temp_file(tmpdir):
    existing_file_path = str(tmpdir.join("existing_file.txt"))
    open(existing_file_path, "w").close()

    assert os.path.isfile(existing_file_path) is True
    utils.delete_temp_file(existing_file_path)
    assert os.path.isfile(existing_file_path) is False

    non_existing_file_path = str(tmpdir.join("non_existing_file.txt"))

    assert os.path.isfile(non_existing_file_path) is False
    utils.delete_temp_file(non_existing_file_path)


@pytest.mark.parametrize("pdf_compression", [False, True])
def test_merge_to_pdf(tmpdir, pdf_compression):
    resources_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "resources"
    )
    files_list = [os.path.join(resources_dir, f"{i}.pdf") for i in range(20)]
    save_dir = str(tmpdir.mkdir("output"))
    save_name = "merged"
    length = len(files_list)

    progress = Mock()

    utils.merge_to_pdf(
        files_list, save_dir, save_name, pdf_compression, length, progress
    )

    merged_file = os.path.join(save_dir, save_name + ".pdf")
    assert os.path.isfile(merged_file)
