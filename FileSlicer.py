class FileSlicer:
    def __init__(self, filepath, chunk_size):
        self._filepath = filepath
        self._chunk_size = chunk_size
        self._chunk_order = -1
        self._file_handler = self.get_file_handler(filepath)

    # when accessing a new file we null the amount of read chunks
    def set_filepath(self, filepath):
        self._filepath = filepath
        self._chunk_order = -1

    def set_chunk_size(self, filepath):
        self._chunk_size = chunk_size

    def get_filepath(self):
        return self._filepath

    def get_chunk_size(self, filepath):
        return self._chunk_size

    def get_chunk_order(self):
        return self._chunk_order

    def get_file_handler(self, filepath):
        try:
            my_file_handler = open(filepath, "rb")
        except IOError:
            print("File not found or path is incorrect. Try another path")
            return None
        return my_file_handler

    # (None, ...) is returned when eof or file not found
    def get_next_chunk(self):
        # file handler is None if eof or filepath is invalid
        if self._file_handler == None:
            return (None, self._chunk_order)
        
        chunk = self._file_handler.read(self._chunk_size)
        self._chunk_order += 1
        if len(chunk) == 0:
            self._file_handler.close()
            self._file_handler = None
            chunk = None
        
        return (chunk, self._chunk_order)