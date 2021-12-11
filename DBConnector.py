from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, update
from sqlalchemy.orm import declarative_base, sessionmaker

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
    
    def create_record(filepath):
        record = Files(filename = filepath)
        session.add(record)
        session.commit()
        created_record = session.query(Files).filter(Files.filename==filepath).first()
        return created_record.id

class ChunkHashes(Base):
    __tablename__ = 'ChunkHashes'
    id = Column(Integer, primary_key=True)
    hash = Column(String(255), unique=True)
    linksCount = Column(Integer)
    size = Column(Integer)

    def create_record(hash, links_count, size):
        record = Files(hash = hash, linksCount = links_count, size = size)
        session.add(record)
        session.commit()


class Chunks(Base):
    __tablename__ = 'Chunks'
    id = Column(Integer, primary_key=True)
    chunkOrder = Column(Integer)
    fileId = Column(Integer, ForeignKey('Files.id'))
    hashId = Column(Integer, ForeignKey('ChunkHashes.id'))

    def create_record(chunk_order, file_id, hash_id):
        record = Chunks(chunkOrder = chunk_order, fileId = file_id, hashId = hash_id)
        session.add(record)
        session.commit()
        

if __name__ == '__main__':
    #Base.metadata.create_all(db_engine)
    print('Hi')
