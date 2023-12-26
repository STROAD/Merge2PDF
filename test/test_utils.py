import sys
import os
from tempfile import gettempdir
import fitz
from re import match

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from merge2pdf import utils
