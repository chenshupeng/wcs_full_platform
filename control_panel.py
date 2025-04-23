from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from visual3d.gl_widget import GLWidget

class ControlPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        self.viewer = GLWidget()
        layout.addWidget(self.viewer)

        self.refresh_button = QPushButton("刷新任务")
        self.refresh_button.clicked.connect(lambda: print("触发手动刷新任务"))
        layout.addWidget(self.refresh_button)
        self.setLayout(layout)