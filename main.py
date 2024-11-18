from frameworks_drivers.gui.main_window import MainWindow
from PyQt6.QtWidgets import QApplication
import sys

from core.container import Container

def main():
    app = QApplication(sys.argv)

    container = Container()
    container.config.from_dict({
        "database": {
            "url": "sqlite:///database.db"
        }
    })

    main_window = MainWindow(
        add_task_use_case = container.add_task_use_case(),
        delete_task_use_case = container.delete_task_use_case(),
        list_tasks_use_case = container.list_tasks_use_case(),
        update_task_use_case = container.update_task_use_case()
    )

    main_window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()