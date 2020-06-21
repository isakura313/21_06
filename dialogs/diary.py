import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QInputDialog, QPushButton, QVBoxLayout

class Diary(QWidget):

    def __init__(self):
        super().__init__()

        self.initUi()
    data = []

    def initUi(self):
        self.todos = QVBoxLayout()
        self.btn = QPushButton("Добавить дело", self)
        self.todos.addWidget(self.btn)
        self.btn.clicked.connect(self.showDialog)
        # self.diary.move(50, 50)
        # self.diary.setFixedHeight(200)
        # self.diary.setFixedWidth(200)

        self.setGeometry(400, 300, 500, 300)
        self.setWindowTitle("Мой дневничок")
        self.show()
    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', "Введите запись")
        if ok:
            self.data.append(str(text))
            self.todos.addWidget(QLabel(str(text)))
            self.setLayout(self.todos)

app = QApplication(sys.argv)
diary = Diary()
sys.exit(app.exec_())

