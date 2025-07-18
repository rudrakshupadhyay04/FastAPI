# step-1 Create Engine
# step-2 Declare a Mapping i.e. declaritive_base
# step-3 create a session using sessionMaker
from sqlalchemy import create_engine # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore


SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind= engine,  autoflush= False, autocommit= False, )

Base = declarative_base()
