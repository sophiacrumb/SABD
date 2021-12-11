class HashRecord:
    def __init__(self, hash_value, links_count, size, primary_key=None):
        self.id = primary_key
        self.hash = hash_value
        self.links_count = links_count
        self.size = size
