import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import QTimer, QTime

class AlarmClock(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Будильник")
        self.setGeometry(100, 100, 300, 150)

        self.label = QLabel("Установите время будильника (HH:MM):", self)
        self.label.setGeometry(10, 10, 280, 30)

        self.entry = QLineEdit(self)
        self.entry.setGeometry(10, 40, 100, 30)

        self.set_button = QPushButton("Установить", self)
        self.set_button.setGeometry(120, 40, 80, 30)
        self.set_button.clicked.connect(self.set_alarm)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.alarm)

    def set_alarm(self):
        alarm_time = self.entry.text()
        current_time = QTime.currentTime()
        alarm_time_obj = QTime.fromString(alarm_time, "HH:mm")

        if alarm_time_obj <= current_time:
            QMessageBox.critical(self, "Ошибка", "Выберите будущее время!")
        else:
            time_difference = current_time.msecsTo(alarm_time_obj)
            self.timer.start(time_difference)

    def alarm(self):
        self.timer.stop()
        QMessageBox.information(self, "Будильник", "Пора вставать!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AlarmClock()
    window.show()
    sys.exit(app.exec_())
