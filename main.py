import sys
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide6.QtGui import QPixmap, QIcon
from UI.main_window import Ui_MainWindow
from services.calculations import iteration, bisection, newton

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Чисельне розв'язування нелінійних рівнянь")
        self.setWindowIcon(QIcon("UI/ico.png"))
        self.ui.Calculate.clicked.connect(self.calculate)
        self.ui.Show.clicked.connect(lambda: self.show_chart(None))
        self.prev_method = None 
    
    def convert_func(self, func):
        x = sp.symbols('x')
        expr = sp.sympify(func)
        return expr, x
    
    def show_chart(self, draw_point=None):
        function_str = self.ui.function_input.text()
        x1 = self.ui.X1SpinBox.value()
        x2 = self.ui.X2SpinBox.value()
        accuracy = self.ui.AccuracySpinBox.value()
        
        expr, x = self.convert_func(function_str)
        
        f = sp.lambdify(x, expr, 'numpy')
        
        steps = int(((abs(x1) + abs(x2)) // accuracy) + 1)
        
        x_vals = np.linspace(x1, x2, steps)
        y_vals = f(x_vals)
        if draw_point is not None:
            # Малюємо графік функції
            plt.figure(figsize=(4, 3), dpi=100)
            plt.plot(x_vals, y_vals, label=function_str)
            
            # Вибір точки для малювання
            try:
                point_y = f(draw_point)
            except:
                point_y = 0

            # Додаємо точку
            print(draw_point, point_y)
            plt.plot(draw_point, point_y, 'ro')  # 'ro' - червона точка
            
            # Збереження графіка
            plt.axhline(0, color='black', linewidth=1.5) 
            plt.title(f'Графік функції {function_str} з точкою')
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.legend()
            plt.grid(True)
            plt.savefig("plot.png")  # Зберегти зображення
            plt.close()  # Закриваємо графік, щоб не відобразити його
            
        else:
            plt.plot(x_vals, y_vals, label=function_str)
            plt.axhline(0, color='black', linewidth=1.5) 
            plt.title(f'Графік функції {function_str}')
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.legend()
            plt.grid(True)
            plt.show()  # Відображаємо графік
    
    def clear_table(self):
        self.ui.results_table.clear()
        self.ui.results_table.setHorizontalHeaderLabels(['К-ть ітерацій', 'Корінь', 'Значення'])
        self.ui.results_table.setRowCount(0)
    
    def calculate(self):
        if self.ui.radioButton.isChecked():
            method = iteration
            if self.prev_method != "iteration" and self.prev_method is not None:
                self.clear_table()
            self.prev_method = "iteration"
        elif self.ui.radioButton_2.isChecked():
            method = bisection
            if self.prev_method != "bisection" and self.prev_method is not None:
                self.clear_table()
            self.prev_method = "bisection"
        else:
            method = newton
            if self.prev_method != "newton" and self.prev_method is not None:
                self.clear_table()
            self.prev_method = "newton"
            
        
        x1 = self.ui.X1SpinBox.value()
        x2 = self.ui.X2SpinBox.value()
        accuracy = self.ui.AccuracySpinBox.value()
        expr, x = self.convert_func(self.ui.function_input.text())
        res = method(x1, x2, accuracy, expr, x)
            
        if res:
            row = self.ui.results_table.rowCount()
            self.ui.results_table.insertRow(row)
            self.ui.results_table.setItem(row, 0, QTableWidgetItem(str(res[0])))
            self.ui.results_table.setItem(row, 1, QTableWidgetItem(str(res[1])))
            self.ui.results_table.setItem(row, 2, QTableWidgetItem(str(res[2])))
            self.show_chart(draw_point=res[1])
            self.ui.img_place.setPixmap(QPixmap("plot.png"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())