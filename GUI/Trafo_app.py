# #######################################

__author__ = "Yavuz Bektaş & "
__version__ = "1.0"
__email__ = "yavuzbektas@gmail.com"
__linkedin__ = "https://www.linkedin.com/in/yavuz-bekta%C5%9F-28659642/"
__release_date__ = "2020.05.01"
__github__ = ""
# #######################################
from PySide2.QtWidgets import QApplication,QMainWindow,QDialog,QMessageBox
from QT_file.login import Ui_Dialog as login_dialog
import db_sql
import sys, os,socket
import myConfig


config_file = myConfig.read_config()

LOCAL_IPs= list(config_file.get("ALLOWED_IPs", "IPs").split(";"))

def error_msjbox( text, title):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.setText(text)
    msgBox.setWindowTitle(title)
    msgBox.setStandardButtons(QMessageBox.Ok)
    # mylog(text, type="error")
    return msgBox.exec()
db=db_sql.mydb()
class Login(QDialog):
    def __init__(self,parent=None):
        super(Login, self).__init__(parent)
        self.ui=login_dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Kullanıcı Girisi Sayfası")
        #self.db=db_sql.mydb()


        self.handle_button()
        self.get_hostname()
    def handle_button(self):

        self.ui.pb_cancel.clicked.connect(self.pushbutton_pressed)
        self.ui.pb_cancel2.clicked.connect(self.pushbutton_pressed)
        self.ui.pb_login.clicked.connect(self.pushbutton_pressed)
        self.ui.pb_save.clicked.connect(self.pushbutton_pressed)
    def pushbutton_pressed(self):
        sender = self.sender()
        if sender.objectName()=="pb_cancel" or sender.objectName()=="pb_cancel2":
            self.close()
        elif sender.objectName()=="pb_login":
            self.login_check()
        elif  sender.objectName()=="pb_save":
            self.add_user()
        else:
            print("nothing")
    def login_check(self):
        username = self.ui.lineEdit.text()
        password =self.ui.lineEdit_2.text()
        data = db.check_user((username,password))
        trafo_index= self.ui.comboBox_2.currentIndex()
        if data!=None:
            if trafo_index==0: 
                import myApp
                self.window = myApp.MyWindow()
                
                # self.window.ui.lineEdit_2.setText(data[3])
                # self.window.user_admin_check()
                self.window.ui.lineEdit_user.setText(data[1])
                self.close()
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0)
            elif trafo_index==1:
                

                import myizole_trifaz
                self.window =myizole_trifaz.IzoleTrifazwindow()
                
                # self.window.ui.lineEdit_2.setText(data[3])
                # self.window.user_admin_check()
                self.window.ui.lineEdit_user.setText(data[1])
                self.close()
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0)
            elif trafo_index==2:
                import mysont_monofaz
                self.window =mysont_monofaz.SontMonofazwindow()
                
                # self.window.ui.lineEdit_2.setText(data[3])
                # self.window.user_admin_check()
                self.window.ui.lineEdit_user.setText(data[1])
                self.close()
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0)
            elif trafo_index==3:
                import mysont_trifaz
                self.window =mysont_trifaz.SontTrifazwindow()
                
                # self.window.ui.lineEdit_2.setText(data[3])
                # self.window.user_admin_check()
                self.window.ui.lineEdit_user.setText(data[1])
                self.close()
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0)   
            elif trafo_index==4:
                import mysok_monofaz
                self.window =mysok_monofaz.SokMonofazwindow()
                
                # self.window.ui.lineEdit_2.setText(data[3])
                # self.window.user_admin_check()
                self.window.ui.lineEdit_user.setText(data[1])
                self.close()
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0)
            elif trafo_index==5:
                import mysok_trifaz
                self.window =mysok_trifaz.SokTrifazwindow()
                
                # self.window.ui.lineEdit_2.setText(data[3])
                # self.window.user_admin_check()
                self.window.ui.lineEdit_user.setText(data[1])
                self.close()
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0) 
            elif trafo_index==6:
                import myoto_monofaz
                self.window =myoto_monofaz.OtoMonofazwindow()
                
                # self.window.ui.lineEdit_2.setText(data[3])
                # self.window.user_admin_check()
                self.window.ui.lineEdit_user.setText(data[1])
                self.close()
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0)
            elif trafo_index==7:
                import myoto_trifaz
                self.window =myoto_trifaz.OtoTrifazwindow()
                
                # self.window.ui.lineEdit_2.setText(data[3])
                # self.window.user_admin_check()
                self.window.ui.lineEdit_user.setText(data[1])
                self.close()
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0) 
            elif trafo_index==8:
                import myharmonik
                self.window =myharmonik.Harmonikwindow()
                
                # self.window.ui.lineEdit_2.setText(data[3])
                # self.window.user_admin_check()
                self.window.ui.lineEdit_user.setText(data[1])
                self.close()
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0)
            elif trafo_index==9:
                import myups
                self.window =myups.UPSwindow()
                
                # self.window.ui.lineEdit_2.setText(data[3])
                # self.window.user_admin_check()
                self.window.ui.lineEdit_user.setText(data[1])
                self.close()
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0)
            elif trafo_index==10:
                import mymonoUI
                self.window =mymonoUI.MonoUIwindow()
                
                # self.window.ui.lineEdit_2.setText(data[3])
                # self.window.user_admin_check()
                self.window.ui.lineEdit_user.setText(data[1])
                self.close()
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0)
        else:
            # error_msjbox(title='Value Error', text='Please fill the blanks')
            self.ui.label_6.setText('Lütfen Girdiğiniz Değerleri Kontrol Edin')
            print("User error")
    def add_user(self):
        username = self.ui.lineEdit_3.text()
        password = self.ui.lineEdit_4.text()
        re_password = self.ui.lineEdit_5.text()
        usertype = self.ui.comboBox.currentText()

        data = db.check_username((username,))

        if data != None:
            print("Bu kullanıcı Zaten kayıtlı.Baska bir kullanıcı adı deneyiniz. ")
            self.ui.label_6.setText("Bu kullanıcı Zaten kayıtlı.Baska bir kullanıcı adı deneyiniz.")
        else:
            if password==re_password and password!="":
                db.insert_user((username,password,usertype))
                self.ui.label_6.setText("Kullanıcı basarı ile yaratıldı . Lütfen giriş yapınız.")
            else:
                self.ui.label_6.setText("Şifreler eşleşmiyor")
                print("Şifreler eşleşmiyor")
    def get_hostname(self):
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print(hostname,local_ip)
        if local_ip in LOCAL_IPs:
            return True
        else:

            error_msjbox(title='Yetkisiz Kullanıcı ', text='Bu bilgisyar yetkili bi kullanıcı değildir.\nLütfen yöneticinizle görüşün.')
            sys.exit(0)
# ================ SHOW PAGES ================================================
def show_LoginPage():
    app = QApplication(sys.argv)


    # =======================================

    # window = MyWindow() # bu login ile değiştirilecek
    # window.ui.lineEdit_82.setText("Admin")
    # window.user_admin_check()

    window = Login()

    window.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Programdan Cıkılıyor")

if __name__ == "__main__":
    try:


        show_LoginPage()

    except Exception as err:
        print(err)
