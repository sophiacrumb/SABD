from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, update
from sqlalchemy.orm import declarative_base, sessionmaker
from ChunkRecord import ChunkRecord
from FileRecord import FileRecord
from HashRecord import HashRecord

Base = declarative_base()
DATABASE_URL = 'postgresql://postgres:Password123!@localhost'
db_engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=db_engine)
session = Session()


class Files(Base):
    __tablename__ = 'Files'
    id = Column(Integer, primary_key=True)
    filename = Column(String(255), unique=True)

    def get_record(filepath):
        record = session.query(Files).filter(Files.filename==filepath).first()
        return record
    
    def create_record(fileRecord):
        record = Files(filename = fileRecord.filepath)
        session.add(record)
        session.commit()
        created_record = session.query(Files).filter(Files.filename==fileRecord.filepath).first()
        return created_record.id


class ChunkHashes(Base):
    __tablename__ = 'ChunkHashes'
    id = Column(Integer, primary_key=True)
    hash = Column(String(255), unique=True)
    linksCount = Column(Integer)
    size = Column(Integer)

    def create_record(chHashesRecord):
        record = ChunkHashes(hash = chHashesRecord.hash, linksCount = chHashesRecord.links_count, size = chHashesRecord.size)
        session.add(record)
        session.commit()
        created_record = session.query(ChunkHashes).filter(ChunkHashes.hash==chHashesRecord.hash).first()
        return created_record.id
    
    def get_record(hashed_chunk):
        record = session.query(ChunkHashes).filter(ChunkHashes.hash==hashed_chunk).first()
        return record
    
    def inc_links_count_by_id(hash_id):
        session.query(ChunkHashes).filter(ChunkHashes.id==hash_id).update({'linksCount': (ChunkHashes.linksCount+1)})
        session.commit()



class Chunks(Base):
    __tablename__ = 'Chunks'
    id = Column(Integer, primary_key=True)
    chunkOrder = Column(Integer)
    fileId = Column(Integer, ForeignKey('Files.id'))
    hashId = Column(Integer, ForeignKey('ChunkHashes.id'))


    def create_record(chRecord):
        record = Chunks(chunkOrder = chRecord.chunk_order, fileId = chRecord.file_id, hashId = chRecord.hash_id)
        session.add(record)
        session.commit()
        created_record = session.query(Chunks).filter(Chunks.chunkOrder==chRecord.chunk_order).first()
        return created_record.id


    def get_sorted_hash_ids_by_chunk_order_for_file_id(fileId):
        chunksAndHashesIds = {}
        for chObj in session.query(Chunks).filter(Chunks.fileId==fileId).all():
            chunksAndHashesIds.update({chObj.chunkOrder: chObj.hashId})
        return chunksAndHashesIds.values()


if __name__ == '__main__':
    #Base.metadata.create_all(db_engine)
    print('Hi')
