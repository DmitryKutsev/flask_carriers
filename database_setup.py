import sys
# для настройки баз данных
from sqlalchemy import Column, ForeignKey, Integer, String

# для определения таблицы и модели
from sqlalchemy.ext.declarative import declarative_base

# для создания отношений между таблицами
from sqlalchemy.orm import relationship

# для настроек
from sqlalchemy import create_engine

# создание экземпляра declarative_base
Base = declarative_base()

# здесь добавим классы

# создает экземпляр create_engine в конце файла
engine = create_engine('sqlite:///logistic.db')




class Carrier(Base):
    __tablename__ = 'carrier'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Forwarder(Base):
    __tablename__ = 'forwarder'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class FreeOrder(Base):
    __tablename__ = 'free_order'

    id = Column(Integer, primary_key=True)
    forwarder = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    summ = Column(Integer,  nullable=False)

class TakenOrder(Base):
    __tablename__ = 'taken_order'

    id = Column(Integer, primary_key=True)
    carrier = Column(String(250), ForeignKey('carrier.name'), nullable=False)
    forwarder = Column(String(250), ForeignKey('forwarder.name'), nullable=False)
    value = Column(Integer,  nullable=False)

class FinishedOrder(Base):
    __tablename__ = 'finished_order'

    id = Column(Integer, primary_key=True)
    carrier = Column(String(250), ForeignKey('carrier.name'), nullable=False)
    forwarder = Column(String(250), ForeignKey('forwarder.name'), nullable=False)
    value = Column(Integer,  nullable=False)

if __name__ == "__main__":
    Base.metadata.create_all(engine)