class FileRecord:
    def __init__(self, filepath, primary_key=None):
        self.id = primary_key
        self.filepath = filepath
