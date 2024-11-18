from entities.task import Task
from interface_adapters.database.task_repository import TaskRepository


class AddTaskUseCase:
    """
    Caso de uso para agregar una tarea.
    """
    def __init__(self, task_repository: TaskRepository):
        """
        Constructor
        :param task_repository:
        """
        self.task_repository = task_repository

    def execute(self, title: str, description: str = None)-> Task:
        """
        Ejecutar caso de uso para agregar una tarea
        :param title:
        :param description:
        :return: Tarea agregada
        """
        new_task = Task(title=title, description=description)
        return self.task_repository.add_task(new_task)