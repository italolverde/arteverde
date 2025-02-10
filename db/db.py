from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy import create_engine, String, ForeignKey
from typing import List
from flask_login import UserMixin

class Base(DeclarativeBase):
    pass

class TB_User(Base, UserMixin):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome:Mapped[str]
    email:Mapped[str]
    senha:Mapped[str]
    admin:Mapped[bool]

    vendas:Mapped[List["TB_vendas"]] = relationship("TB_vendas", backref='user')
 
    def get_id(self): #sobresrever get id do UserMixin
        return str(self.id)

    @classmethod
    def find(cls, **kwargs):
        if 'email' in kwargs:
            return session.query(cls).filter_by(email=kwargs['email']).first()
        elif 'id' in kwargs:
            return session.query(cls).filter_by(id=kwargs['id']).first() 
        else: 
            raise AttributeError('A busca deve ser feita por email ou id.')


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

class TB_vendas(Base):
    __tablename__ = 'vendas'
    id:Mapped[int] = mapped_column(primary_key=True)
    cli_id:Mapped[int] = mapped_column(ForeignKey('users.id'))

engine = create_engine("sqlite:///banco.db")
# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)

session = Session(bind=engine)