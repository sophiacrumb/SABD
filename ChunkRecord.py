class ChunkRecord:
    def __init__(self, chunk_order, file_id, hash_id, primary_key=None):
        self.id = primary_key
        self.chunk_order = chunk_order
        self.file_id = file_id
        self.hash_id = hash_id
