import json
import os

class adapter:

    def __init__(self, file_type):
        self.file_type = file_type
        self.instance = {
            "py": pythonFileProcessing(),
            "java": pythonFileProcessing(),
            "ts": pythonFileProcessing(),
            "js": pythonFileProcessing()
        }


    def get(self):
        return self.instance[self.file_type] if self.file_type in self.instance else None


class pythonFileProcessing:

    multi_line_comment_format = ["'''", '"""']

    def __init__(self):
        pass

    def read_file(self, lines):
        resp = responseModel()
        for line in lines:
            line = line.strip()
            resp.lines += 1
            if not line:
                resp.blankLines += 1
            else:
                if line[0] == "#":
                    resp.commentedLines += 1
                else:
                    resp.codeLines += 1
        return resp

    def get_multiline_comment_count(self,lines):
        pass



class jsFileProcessing:
    pass


class tsFileProcessing:
    pass


class javaFileProcessing:
    pass



class responseModel:

    lines: int = 0
    codeLines: int = 0
    commentedLines: int = 0
    blankLines: int = 0


dir_path = "files"
print(f"file in folder: {os.listdir()}")
for root, dirs, files in os.walk(dir_path):
    print(files)
    for file in files:
        file_path = os.path.join(root, file)
        open_file = open(file_path, "r")
        lines = open_file.readlines()
        obj = adapter(file_path.split(".")[1])
        file_obj = obj.get()
        resp = file_obj.read_file(lines)
        print(f"for file:{file} \n {json.dumps(resp.__dict__)}")
