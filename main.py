from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton
import sys
from datetime import datetime


class AgeCalulater(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculater")
        grid = QGridLayout()

        # create widgets
        name_label = QLabel("Name:")
        self.name_line_edit = QLineEdit()

        date_birth_label = QLabel("Date of Birth MM/DD/YYYY: ")
        self.date_birth_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate Age")
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel("")

        # add widgets to group
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(date_birth_label, 1, 0)
        grid.addWidget(self.date_birth_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_age(self):
        current_year = datetime.now().year
        date_of_birth = self.date_birth_line_edit.text()
        year_birth = datetime.strptime(date_of_birth, "%m/%d/%y").date().year
        age = current_year - year_birth
        self.output_label.setText(f"{self.name_line_edit.text()} is {age} years old.")


app = QApplication(sys.argv)
age_calculater = AgeCalulater()
age_calculater.show()
sys.exit(app.exec())
