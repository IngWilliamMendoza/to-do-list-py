from interface_adapters.database.task_repository import TaskRepository


class DeleteTaskUseCase:
    """
    Caso de uso para eliminar una tarea.
    """
    def __init__(self, task_repository: TaskRepository):
        """
        Constructor
        :param task_repo: TaskRepository
        """
        self.task_repository = task_repository

    def execute(self, task_id: int) -> bool:
        return self.task_repository.delete_task(task_id)