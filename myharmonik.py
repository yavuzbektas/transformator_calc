from QT_file.mainharmonik import Ui_MainWindow
from PySide2.QtWidgets import QApplication,QMainWindow
class Harmonikwindow(QMainWindow):
    def __init__(self, parent=None):
        super(Harmonikwindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Trafo Hesaplama Programı V0 - Harmonik Trafosu  Hesaplama")
        self.handle_button()
    
    def logout_myapp(self):
        import Trafo_app
        self.window = Trafo_app.Login()

        self.close()
        self.window.show()
    def handle_button(self):
        
        self.ui.pushButton_35.clicked.connect(self.logout_myapp)