from sqlalchemy import create_engine 
#criação do banco de dados
from sqlalchemy.orm import sessionmaker, declarative_base


db = create_engine("sqlite:///./arretadoshop.db")
Session = sessionmaker(bind=db)
session = Session()



