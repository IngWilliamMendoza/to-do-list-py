from PyQt6.QtWidgets.QWidget import update

from interface_adapters.database.task_repository import TaskRepository


class UpdateTaskUseCase:
    """
    Caso de uso para actualizar una tarea.
    """
    def __init__(self, task_repository: TaskRepository):
        """
        Constructor
        :param task_repository: TaskRepository
        """
        self.task_repository = task_repository

    def execute(self, task_id: int, **kwargs) -> bool:
        """
        Ejecutar caso de uso para actualizar una tarea
        :param task_id:
        :param kwargs:
        :return:
        """
        update_task = self.task_repository.update_task(task_id, **kwargs)
        return update_task is not None