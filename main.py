import sys
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow
from visual3d.gl_widget import GLWidget
from visual3d.task_manager import TaskManager
from api.server import create_flask_app


class TaskManager:
    def __init__(self, renderer):
        self.renderer = renderer
        self.tasks = []
        self.stats = {}

    def auto_simulate_loop(self):
        pass

    def add_task(self, sku, zone, priority):
        task = {
            "sku": sku,
            "zone": zone,
            "priority": priority
        }
        self.tasks.append(task)

    def get_stats(self):
        return self.stats


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WCS 仓储仿真平台 v10")
        self.setGeometry(100, 100, 1200, 800)
        self.viewer = GLWidget(self)
        self.setCentralWidget(self.viewer)
        self.manager = TaskManager(self.viewer.renderer)
        threading.Thread(target=self.manager.auto_simulate_loop, daemon=True).start()
        flask_app = create_flask_app(self.manager)
        threading.Thread(target=lambda: flask_app.run(port=8000), daemon=True).start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
