class PathError(Exception):
    def __init__(self, path):
        self.path = path
        super().__init__(f"유효하지 않은 경로입니다: '{path}'")


class FileNameError(Exception):
    def __init__(self, name, type):
        self.name = name

        if type == "invalid":
            self.message = f"유효하지 않은 이름입니다: '{name}'"
        if type == "duplicate":
            self.message = f"동일한 이름의 파일이 존재합니다: '{name}'"

        super().__init__(self.message)


class NoFileError(Exception):
    def __init__(self, file=None):
        self.file = file

        if file is None:
            self.message = "병합할 파일이 존재하지 않습니다"
        else:
            self.message = f"파일을 찾을 수 없습니다: '{file}'"

        super().__init__(self.message)
