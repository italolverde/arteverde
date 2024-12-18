from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine, String, ForeignKey
from typing import List

class Base(DeclarativeBase):
    pass

class TB_User(Base):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome:Mapped[str]
    email:Mapped[str]
    senha:Mapped[str]
    admin:Mapped[bool]

class TB_categoria(Base):
    __tablename__ = 'categoria'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome:Mapped[str]
    produtos:Mapped[List["TB_produto"]] = relationship("TB_produto", backref='categoria')

class TB_produto(Base):
    __tablename__ = 'produto'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome:Mapped[str]
    preco:Mapped[float]
    categoria_id:Mapped[int] = mapped_column(ForeignKey('categoria.id'))
    #Dar um jeito de enfiar foto aqui dentro !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

engine = create_engine("sqlite:///banco.db")
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)