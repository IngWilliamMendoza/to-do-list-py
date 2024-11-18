from typing import List

from entities.task import Task
from interface_adapters.database.task_repository import TaskRepository


class ListTasksUseCase:
    """
    Caso de uso para listar tareas.
    """
    def __init__(self, task_repository: TaskRepository):
        """
        Constructor de la clase ListTasksUseCase.
        :param task_repository:
        """
        self.task_repository = task_repository

    def execute(self) -> List[Task]:
        """
        Ejecuta la logica para obtener todas las tareas.
        :return:
        """
        return self.task_repository.get_all_task()