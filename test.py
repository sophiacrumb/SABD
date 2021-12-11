from FileSlicer import FileSlicer
from ChunkWriter import ChunkWriter

test_path_prefix = "/home/alex"


def get_full_test_filepath(filename):
    return "{prefix}/{filename}".format(prefix=test_path_prefix, filename=filename)


slicer = FileSlicer(get_full_test_filepath("a"), 10)
print(slicer.get_filepath())
b = slicer.get_next_chunk()[0]
print(b)
ChunkWriter.write_chunk(b, get_full_test_filepath("b"))
c = slicer.get_next_chunk()
print(c)
ChunkWriter.write_chunk(c[0], get_full_test_filepath("c"))
d = slicer.get_next_chunk()[0]
print(d)
if d != None:
    ChunkWriter.write_chunk(d, get_full_test_filepath("d"))
e = slicer.get_next_chunk()
print(e)

ChunkWriter.write_chunks([get_full_test_filepath("b"), get_full_test_filepath("c"), get_full_test_filepath("d")],
                         get_full_test_filepath("e"))
