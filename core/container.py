from dependency_injector import containers, providers
from frameworks_drivers.db.db_config import setup_database
from interface_adapters.database.task_repository import TaskRepository
from use_cases.add_task import AddTaskUseCase
from use_cases.delete_task import DeleteTaskUseCase
from use_cases.list_tasks import ListTasksUseCase
from use_cases.update_task import UpdateTaskUseCase

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    database = providers.Singleton(setup_database, config=config)
    task_repository = providers.Factory(TaskRepository, db_session=database.provided.session)

    add_task_use_case = providers.Factory(AddTaskUseCase, task_repository=task_repository)
    list_tasks_use_case = providers.Factory(ListTasksUseCase, task_repository=task_repository)
    update_task_use_case = providers.Factory(UpdateTaskUseCase, task_repository=task_repository)
    delete_task_use_case = providers.Factory(DeleteTaskUseCase, task_repository=task_repository)