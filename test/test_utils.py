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