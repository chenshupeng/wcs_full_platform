import sys, threading
from PyQt5.QtWidgets import QApplication, QMainWindow
from visual3d.task_manager import TaskManager
from api.server import create_flask_app

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WCS 仓储仿真平台 v8 - 控制面板集成")
        self.setGeometry(100, 100, 800, 600)
        self.manager = TaskManager()

        threading.Thread(target=self.manager.auto_simulate_loop, daemon=True).start()
        flask_app = create_flask_app(self.manager)
        threading.Thread(target=lambda: flask_app.run(port=8000), daemon=True).start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())