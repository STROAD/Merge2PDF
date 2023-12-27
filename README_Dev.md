# Merge to PDF
Content related to the development of **Merge to PDF**.

**Merge to PDF** was developed and tested using [Python](https://www.python.org) [3.12.1](https://www.python.org/downloads/release/python-3121) on Windows 11.  
It uses the [PySide6](https://pypi.org/project/PySide6), [PyMuPDF](https://github.com/pymupdf/PyMuPDF) libraries.  
It uses [Black](https://github.com/psf/black) as a code formatter.  
It uses [pytest](https://github.com/pytest-dev/pytest) for testing.


## Installation & Usage
1. Installing Python  
Installing Python 3.12.1  
(Not guaranteed to work on versions other than 3.12.1)

2. Repository clone  
`git clone https://github.com/STROAD/Merge2PDF.git`

3. Installing Libraries  
Install PySide6, PyMuPDF
```shell
pip install black
pip install PySide6
pip install PyMuPDF
pip install pytest
```

4. Running Merge to PDF  
Run Merge2PDF.py


## Project Structure
```
📦 Merge2PDF
├─ 📜 README.md
├─ 📜 README_Dev.md
├─ 📜 .gitignore
├─ 📜 LICENSE
├─ 📁 merge2pdf
│   ├─ 📜 __init__.py
│   ├─ 📜 Merge2PDF.py
│   ├─ 📜 Merge2PDF_UI.py
│   ├─ 📜 utils.py
│   ├─ 📜 custom_errors.py
│   ├─ 📜 resources_rc.py
│   └─ 📜 Merge2PDF.spec
├─ 📁 resources
│   ├─ 📜 Merge2PDF_ui.ui
│   ├─ 📜 resources_rc.qrc
│   └─ 📁 icon
│       └─ 📜 Merge2PDF_Icon.ico
└─ 📁 test
    ├─ 📜 test_utils.py
    └─ 📁 resources
        ├─ 📜 0.pdf
        ├─    ...
        └─ 📜 19.pdf
```


## Basic PySide6 Usage
Qt Designer location: `venv\Lib\site-packages\PySide6\designer.exe`

If View Python Code doesn't work: Copy `uic.exe` from `venv\Lib\site-packages\PySide6\` and paste into `bin\`

### Adding resource files
Path your resource files (icons, images, etc.) to the `resources_rc.qrc` file and convert them to the `resources_rc.py` file with the following command
```shell
pyside6-rcc resources_rc.qrc -o resources_rc.py
```


## To Build an EXE
Installing libraries to build EXE  
`pip install pyinstaller`

Build the exe with the command below (build from the project top-level folder (Merge2PDF\\))
```shell
pyinstaller --clean .\merge2pdf\Merge2PDF.spec
```


## Test
Run the `pytest` command in the top-level folder of your project (Merge2PDF\\)
