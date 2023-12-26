# Merge to PDF

Merge to PDF 개발과 관련된 내용입니다.

Merge to PDF는 Windows 11에서 개발되고 테스트 되었습니다.  
[Python](https://www.python.org/) [3.12.1](https://www.python.org/downloads/release/python-3121) 버전을 사용하며, [PySide6](https://pypi.org/project/PySide6), [PyMuPDF](https://github.com/pymupdf/PyMuPDF) 라이브러리를 사용합니다.  
코드 포맷터로 [Black](https://github.com/psf/black)을 사용합니다.  
테스트에는 [pytest](https://github.com/pytest-dev/pytest)를 사용합니다.


## 설치 및 실행
1. Python 설치  
Python 3.12.1 설치  
(3.12.1 이외의 버전에서는 정상작동 보장 불가)

2. Repository clone  
`git clone https://github.com/STROAD/Merge2PDF.git`

3. 라이브러리 설치  
PySide6, PyMuPDF 설치
```shell
pip install black
pip install PySide6
pip install PyMuPDF
pip install pytest
```

4. Merge to PDF 실행  
Merge2PDF.py 실행


## 프로젝트 구조
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


## PySide6 기본 사용법
Qt Designer 위치: `venv\Lib\site-packages\PySide6\designer.exe`

Python 코드 보기가 안될 경우: `venv\Lib\site-packages\PySide6\`에서 `uic.exe`복사 후 `bin\`에 붙여넣기

### 리소스 파일 추가

리소스 파일(아이콘, 이미지 등)들을 resources_rc.qrc 파일에 경로를 지정해주고 아래 명령어를 통해 resources_rc.py 파일로 변환
```shell
pyside6-rcc resources_rc.qrc -o resources_rc.py
```


## exe 빌드하기
exe 빌드를 위한 라이브러리 설치  
`pip install pyinstaller`

아래 명령어를 통해 exe 빌드(프로젝트 최상위 폴더(Merge2PDF\\)에서 빌드)
```shell
pyinstaller --clean .\merge2pdf\Merge2PDF.spec
```


## 테스트
프로젝트 최상위 폴더(Merge2PDF\\)에서 `pytest` 명령어 실행
