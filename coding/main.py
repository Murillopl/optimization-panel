from qt_core import *
import sys
from Window import MyFirstWindow
import win32com.client


if __name__ == "__main__":
    QApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    
    first_window = MyFirstWindow()

    first_window.show()

    sys.exit(app.exec())