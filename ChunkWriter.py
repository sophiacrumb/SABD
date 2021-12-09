from pathlib import Path

class ChunkWriter:

    @staticmethod
    def write_chunks(chunks_file_list, output_file):
        ChunkWriter.delete_existing_output_file(output_file)

        with open(output_file, 'ab') as w_file:
            for chunk_file in chunks_file_list:
                with open(chunk_file, 'rb') as r_file:
                    data_chunk = r_file.read()
                    w_file.write(data_chunk)

    @staticmethod
    def write_chunk(data_chunk, output_file):
        ChunkWriter.delete_existing_output_file(output_file)

        with open(output_file, 'ab') as file:
            file.write(data_chunk)

    @staticmethod        
    # as we use append mode, we don't want collisions with pre-existing files
    def delete_existing_output_file(output_file):
        output_file_path = Path(output_file)
        if output_file_path.is_file():
            output_file_path.unlink()
