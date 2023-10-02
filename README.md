# MergeFiles
파일 병합 프로그램

## 빌드하기
### 리소스 파일 추가하기  

리소스 파일(아이콘, 이미지 등)들을 resources_rc.qrc 파일에 경로를 지정해주고 아래 명령어를 통해 resources_rc.py 파일로 변환해준다.
```sh
pyside6-rcc resources_rc.qrc -o resources_rc.py
```
