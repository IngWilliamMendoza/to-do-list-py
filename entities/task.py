from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Task(Base):
    """
    Clase que representa una tarea.
    """
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    deleted = Column(Boolean, default=False)

    def __init__(self, title: str, description: str = None, completed: bool = False):
        """
        Constructor de la clase Task.
        :param title: Titulo de la tarea.
        :param description: Descripcion de la tarea.
        :param completed: Indica si la tarea esta complet
        """
        self.tile = title
        self.description = description
        self.completed = completed

    def __repr__(self):
        """
        Representacion de la tarea.
        :return:
        """
        return f"<Task(id={self.id}, title={self.title}, completed={self.completed})>"