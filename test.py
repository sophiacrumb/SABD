from FileSlicer import FileSlicer
from ChunkWriter import ChunkWriter

slicer = FileSlicer("/home/alex/a", 10)
print(slicer.get_filepath())
b = slicer.get_next_chunk()[0]
print(b)
ChunkWriter.write_chunk(b, "/home/alex/b")
c = slicer.get_next_chunk()
print(c)
ChunkWriter.write_chunk(c[0], "/home/alex/c")
d = slicer.get_next_chunk()[0]
print(d)
if d != None:
	ChunkWriter.write_chunk(d, "/home/alex/d")
e = slicer.get_next_chunk()
print(e)

ChunkWriter.write_chunks(["/home/alex/b","/home/alex/c","/home/alex/d"],"/home/alex/e")