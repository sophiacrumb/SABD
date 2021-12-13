from ChunkRecord import ChunkRecord
from FileRecord import FileRecord
from FileSlicer import FileSlicer
from HashRecord import HashRecord
from ChunkWriter import ChunkWriter
from DBConnector import Chunks, Files, ChunkHashes

import hashlib


def count_hash(bytes_to_hash):
    return hashlib.md5(bytes_to_hash).hexdigest()


def get_full_filepath_in_workdir(filename):
    import os
    return "{cur_dir}/{filename}".format(cur_dir=os.getcwd(), filename=filename)


class Main:
    result_file_name = "result"

    @staticmethod
    def upload(filepath, chunk_size):
        slicer = FileSlicer(filepath, chunk_size)

        file_id = Main.__get_file_id_even_if_absent(filepath)

        while None not in (chunk_with_order := slicer.get_next_chunk()):
            chunk_data = chunk_with_order[0]
            chunk_order = chunk_with_order[1]

            hash_id = Main.__write_chunk_once_and_return_hash_id(chunk_data, chunk_size)

            chunk_record = ChunkRecord(chunk_order, file_id, hash_id)
            # DONE
            Chunks.create_record(chunk_record)


    @staticmethod
    def __get_file_id_even_if_absent(filepath):
        # DONE
        file_record = Files.get_record(filepath)
        if not file_record:
            file_record = FileRecord(filepath)
            # DONE
            file_id = Files.create_record(file_record)
        else:
            file_id = file_record.id
        return file_id


    @staticmethod
    def __write_chunk_once_and_return_hash_id(chunk_data, chunk_size):
        hashed_chunk = count_hash(chunk_data)

        # TODO ChunkHashes class is the connector to ChunkHashes table
        # get_hash_record() receives hashed_chunk data and returns hash_record from table or None
        hash_record = ChunkHashes.get_record(hashed_chunk)
        if not hash_record:
            links_count = 1
            hash_record = HashRecord(hashed_chunk, links_count, chunk_size)
            # TODO DONE
            hash_id = ChunkHashes.create_record(hash_record)
            ChunkWriter.write_chunk(chunk_data, get_full_filepath_in_workdir(hash_id))
        else:
            # TODO inc_links_count_by_id increments links count of hash on DB side
            hash_id = hash_record.id
            ChunkHashes.inc_links_count_by_id(hash_record.id)

        return hash_id


    @staticmethod
    def download(filepath):
        file_record = Files.get_record(filepath)
        if not file_record:
            raise Exception("file {path} not found in Files table".format(path=filepath))

        # TODO get_sorted_hash_ids_by_chunk_order_for_file_id returns list of hash_ids sorted by chunk order
        #  for particular file. All needed data can be gathered from Chunks table.
        #  Sorting can be performed on DB side (in SQL query) or on our side.
        #  The preferred way is our side but it can require several SQL queries
        hash_ids = Chunks.get_sorted_hash_ids_by_chunk_order_for_file_id(file_record.id)

        chunk_data_filepaths = [get_full_filepath_in_workdir(hash_id) for hash_id in hash_ids]
        ChunkWriter.write_chunks(chunk_data_filepaths, get_full_filepath_in_workdir(Main.result_file_name))
