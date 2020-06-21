""" Пример расположения с помощью сетки"""


import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget #представляет из себя одно окно
from PyQt5.QtWidgets import QLineEdit #кнопочки, на которые можно нажимать
from PyQt5.QtWidgets import QFormLayout #кнопочки, на которые можно нажимать
from PyQt5.QtWidgets import QPushButton #кнопочки, на которые можно нажимать
from PyQt5.QtWidgets import QLabel #кнопочки, на которые можно нажимать


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Первая программа на PyQt5")
# window.setGeometry(400, 400, 600, 600)

layout = QFormLayout()
"""В QGrid у нас первый аргумент это строка, второй у позиция в ней"""
layout.addRow(QLabel("Привет, пора отдать свои данные"))
layout.addRow("имя", QLineEdit())
layout.addRow("фамилия", QLineEdit())
layout.addRow("номер кредитной карты", QLineEdit())
layout.addRow(QPushButton("Отправить данные"))


window.setLayout(layout)
window.show()
sys.exit(app.exec())
