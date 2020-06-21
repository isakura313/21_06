import sys
import random
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QPushButton

def greeting():
    """ Слот функция, которая нам предлагает поиграть в казино"""
    rand = random.randint(0, 1)
    print(rand)
    if rand > 0.5:
        msg.setText("Вы выйграли!")
    else:
        msg.setText("Вы проиграли(")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Маленькое казино")
layout = QVBoxLayout()
btn = QPushButton("Привет")
btn.clicked.connect(greeting) # вот тут у нас прикрепляется функция

layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
