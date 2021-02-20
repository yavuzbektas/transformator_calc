from QT_file.mainsont_trifaz import Ui_MainWindow
from PySide2.QtWidgets import QApplication,QMainWindow
class SontTrifazwindow(QMainWindow):
    def __init__(self, parent=None):
        super(SontTrifazwindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Trafo Hesaplama Programı V0 - Sont Trafosu Trifaz Hesaplama")
        self.handle_button()
    
    def logout_myapp(self):
        import Trafo_app
        self.window = Trafo_app.Login()

        self.close()
        self.window.show()
    def handle_button(self):
        
        self.ui.pushButton_35.clicked.connect(self.logout_myapp)