from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine 

class Base(DeclarativeBase):
    pass

class TB_User(Base):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome:Mapped[str]
    email:Mapped[str]
    senha:Mapped[str]


engine = create_engine("sqlite:///banco.db")

Base.metadata.create_all(bind=engine)