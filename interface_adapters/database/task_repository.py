from typing import Type

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from entities.task import Task

class TaskRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def _get_task_by_id(self, task_id: int) -> Type[Task] | None:
        """
        Metodo privado que obtiene una tarea de la base de datos.
        :param task_id: Identificador de la tarea que se desea obtener.
        :return: Instancia de la clase Task.
        """
        return self.db_session.query(Task).filter(Task.id == task_id, Task.deleted == False).first()

    def get_all_task(self) -> list[Type[Task]]:
        """
        Obtiene todas las tareas de la base de datos que no han sido eliminadas
        :return:
        """
        return self.db_session.query(Task).filter(Task.deleted == False).all()

    def add_task(self, task: Task) -> Task:
        """
        Agrega una nueva tarea a la base de datos.
        :param task: Instancia de la clase Task que se desea agregar.
        :return: La tarea agregada.
        """
        try:
            self.db_session.add(task)
            self.db_session.commit()
            self.db_session.refresh(task)
            return task
        except SQLAlchemyError as e:
            self.db_session.rollback()
            raise e

    def update_task(self, task_id: int, **kwargs) -> Type[Task]:
        """
        Actualiza una tarea en la base de datos.
        :param task_id: Identificador de la tarea que se desea actualizar.
        :param kwargs: Campos y valores que se desean actualizar.
        :return: La tarea actualizada.
        """
        if not kwargs:
            raise ValueError("No se han especificado campos a actualizar.")
        task = self._get_task_by_id(task_id)
        if not task:
            raise None
        valid_fields = {column.name for column in Task.__tablename__.columns}
        update = False
        for key, value in kwargs.items():
            if key in valid_fields:
                setattr(task, key, value)
                update = True
        if not update:
            raise ValueError("No se han especificado campos validos a actualizar.")

        try:
            self.db_session.commit()
            self.db_session.refresh(task)
            return task
        except SQLAlchemyError as e:
            self.db_session.rollback()
            raise e

    def delete_task(self, task_id: int) -> bool:
        """
        Elimina una tarea de la base de datos.
        :param task_id: La tarea que se desea eliminar.
        :return: True si la tarea fue eliminada, False en caso contrario.
        """
        task = self._get_task_by_id(task_id)
        if task:
            try:
                task.deleted = True
                self.db_session.commit()
                return True
            except SQLAlchemyError as e:
                self.db_session.rollback()
                raise e
        return False