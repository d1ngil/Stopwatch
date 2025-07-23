# Python PyQt5 Stopwatch
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QVBoxLayout, QHBoxLayout, QPushButton, QMainWindow)
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QIcon

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00:00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")
        self.setWindowIcon(QIcon("IMG_1143.png"))
        self.setGeometry(600, 300, 700, 500)
        self.time_label.setStyleSheet("font-size: 100px;"
            "background-color: hsl(136, 100%, 61%);"
            "border: 3px solid;"   
            "border-radius: 10px;")

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label, alignment=Qt.AlignHCenter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.start_button.setObjectName("start")
        self.stop_button.setObjectName("stop")
        self.reset_button.setObjectName("reset")

        self.setStyleSheet("""
        QPushButton, QLabel{
            padding: 20px;
            font-weight: bold;
            font-family: calibri;
        }
        QPushButton{
        font-size: 80px;
                font-family: Arial;
                margin: 5px;
                border: 3px solid;
                border-radius: 20px;
        }
        QPushButton#start{
                background-color: hsl(0, 5%, 80%);
        }
        QPushButton#stop{
                background-color: hsl(0, 5%, 80%);
        }
        QPushButton#reset{
                background-color: hsl(0, 5%, 80%);
        }
        QPushButton#start:hover{
                background-color: hsl(0, 5%, 60%);
        }
        QPushButton#stop:hover{
                background-color: hsl(0, 5%, 60%);
        }
        QPushButton#reset:hover{
                background-color: hsl(0, 5%, 60%);
        }
        """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}:{milliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())