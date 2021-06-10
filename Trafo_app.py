# #######################################

__author__ = "Yavuz Bektaş & "
__version__ = "0.2"
__email__ = "yavuzbektas@gmail.com"
__linkedin__ = "https://www.linkedin.com/in/yavuz-bekta%C5%9F-28659642/"
__release_date__ = "2021.06.09"
__github__ = "https://github.com/yavuzbektas/transformator_calc"
# #######################################
from PySide2.QtWidgets import QApplication,QMainWindow,QDialog,QMessageBox,QTableWidgetItem
from PySide2.QtGui import QIcon
from QT_file.login import Ui_Dialog as login_dialog
import db_sql
import sys, os,socket
import myConfig


if len(sys.argv)>1:
    serverpath = sys.argv[1]
    print ('Server Adress Arguman olarak verildi:', str(sys.argv[1]))
else :
    
    serverpath = os.getcwd()
    print("Server Adres olarak bulundugu dizin kullanılacak : " ,serverpath )
    
config_file = myConfig.read_config()
ICON_DIR= config_file.get("PATHS", "ICON_DIR")
myConfig.write_config(config_file,config_file.sections(),os.getcwd()) # bulundugu klasore ini dosyasini yarattı
#LOCAL_IPs= list(config_file.get("ALLOWED_IPs", "IPs").split(";"))


def table_update(data, headers, sender):
    sender.clear()
    sender.setColumnCount(len(headers))
    sender.setHorizontalHeaderLabels(headers)
    sender.setRowCount(0)
    if data:
        sender.insertRow(0)
        # self.ui.tableWidget_3.insertColumn(0)

        for row, form in enumerate(data):

            for column, item in enumerate(form):
                sender.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1
            row_pos = sender.rowCount()
            sender.insertRow(row_pos)

    else:
        sender.clear()

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
        self.setWindowTitle("Kullanıcı Girişi Sayfası ")
        self.setWindowIcon(QIcon(ICON_DIR +"\\"+"logo.jpg"))
        self.ui.tabWidget.setCurrentIndex(0)
        self.readConfig()
        #self.db=db_sql.mydb()
        self.ui.tabWidget.tabBar().setEnabled(False)

        self.handle_button()
        self.get_hostname()
        self.get_AllUser()
    def handle_button(self):

        self.ui.pb_cancel.clicked.connect(self.pushbutton_pressed)
        self.ui.pb_cancel2.clicked.connect(self.pushbutton_pressed)
        self.ui.pb_login.clicked.connect(self.pushbutton_pressed)
        self.ui.pb_save.clicked.connect(self.pushbutton_pressed)
        self.ui.pb_login_user.clicked.connect(self.pushbutton_pressed)
        self.ui.pb_sil_user.clicked.connect(self.pushbutton_pressed)
        self.ui.pb_ekle.clicked.connect(self.pushbutton_pressed)
        self.ui.pb_sil.clicked.connect(self.pushbutton_pressed)
    def pushbutton_pressed(self):
        sender = self.sender()
        if sender.objectName()=="pb_cancel" or sender.objectName()=="pb_cancel2":
            self.close()
        elif sender.objectName()=="pb_login":
            data = self.login_check() if self.login_check()!=False else None
            self.goApp(data)
        elif sender.objectName()=="pb_login_user":
            self.login_check()
        elif  sender.objectName()=="pb_save":
            self.add_user()
        elif  sender.objectName()=="pb_sil_user":
            
            self.delete_User()
        elif  sender.objectName()=="pb_ekle":
            
            self.addIP()
        elif  sender.objectName()=="pb_sil":
            
            self.removeIP()
        else:
            print("gecersiz buton adı")
    def login_check(self):
        username = self.ui.lineEdit.text()
        password =self.ui.lineEdit_2.text()
        data = db.check_user((username,password))
        
        
        
        if data==None:
            # error_msjbox(title='Value Error', text='Please fill the blanks')
            self.ui.label_6.setText('Lütfen Girdiğiniz Değerleri Kontrol Edin')
            print("Kullanıcı Hatası")
            return False
        elif data[3]=="Yönetici":
            self.ui.tabWidget.tabBar().setEnabled(True)
            self.ui.label_6.setText('Yönetici girisi Yapıldı')
            return  data
        elif data[3]=="Standart":
            
            self.ui.label_6.setText('Standart Kullanıcı girisi Yapıldı. Trafo Sayfalara gidebilirsiniz.')
            return  data
    def removeIP(self):
       
        item=self.ui.listWidget.currentItem().text()
        if item!=None :
            db.delete_ips(item)
            self.readConfig()
        
    def addIP(self):
        ip = self.ui.lineEdit_ip.text()
        import re
        x = re.findall("^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4}$", ip)
        if x and db.check_ips(ip)==None:
            db.insert_ips((ip))
            self.ui.label_6.setText("IP eklendi.")
            self.ui.listWidget.addItem(ip)
        else:
            self.ui.label_6.setText("Bu IP zaten ekli veya Girdiğiniz IP geçerli değil.")
    def readConfig(self):
        self.ui.listWidget.clear()    
        items = db.showall_ips()
        for ip in items:
                self.ui.listWidget.addItem(str(ip[0]))
    def goApp(self,data): 
        trafo_index= self.ui.comboBox_2.currentIndex()   
        if data!=None:
            if trafo_index==0: 
                import myApp
                self.window = myApp.MyWindow()
                self.window.setWindowIcon(QIcon(ICON_DIR +"\\"+"logo.jpg"))
                # self.window.ui.lineEdit_2.setText(data[3])
                # self.window.user_admin_check()
                self.window.ui.lineEdit_user.setText(data[1])
                self.close()
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0)
            elif trafo_index==1:
                

                import myizole_trifaz
                self.window =myizole_trifaz.MyWindow()
                self.window.setWindowIcon(QIcon(ICON_DIR +"\\"+"logo.jpg"))
                # self.window.ui.lineEdit_2.setText(data[3])
                # self.window.user_admin_check()
                self.window.ui.lineEdit_user.setText(data[1])
                self.close()
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0)
            elif trafo_index==2:
                import mysont_monofaz
                self.window =mysont_monofaz.SontMonofazwindow()
                self.window.setWindowIcon(QIcon(ICON_DIR +"\\"+"logo.jpg"))
                # self.window.ui.lineEdit_2.setText(data[3])
                # self.window.user_admin_check()
                self.window.ui.lineEdit_user.setText(data[1])
                self.close()
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0)
            elif trafo_index==3:
                import mysont_trifaz
                self.window =mysont_trifaz.SontTrifazwindow()
                self.window.setWindowIcon(QIcon(ICON_DIR +"\\"+"logo.jpg"))
                # self.window.ui.lineEdit_2.setText(data[3])
                # self.window.user_admin_check()
                self.window.ui.lineEdit_user.setText(data[1])
                self.close()
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0)   
            elif trafo_index==4:
                import mysok_monofaz
                self.window =mysok_monofaz.SokMonofazwindow()
                self.window.setWindowIcon(QIcon(ICON_DIR +"\\"+"logo.jpg"))
                # self.window.ui.lineEdit_2.setText(data[3])
                # self.window.user_admin_check()
                self.window.ui.lineEdit_user.setText(data[1])
                self.close()
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0)
            elif trafo_index==5:
                import mysok_trifaz
                self.window =mysok_trifaz.SokTrifazwindow()
                self.window.setWindowIcon(QIcon(ICON_DIR +"\\"+"logo.jpg"))
                # self.window.ui.lineEdit_2.setText(data[3])
                # self.window.user_admin_check()
                self.window.ui.lineEdit_user.setText(data[1])
                self.close()
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0) 
            elif trafo_index==6:
                import myoto_monofaz
                self.window =myoto_monofaz.OtoMonofazwindow()
                self.window.setWindowIcon(QIcon(ICON_DIR +"\\"+"logo.jpg"))
                # self.window.ui.lineEdit_2.setText(data[3])
                # self.window.user_admin_check()
                self.window.ui.lineEdit_user.setText(data[1])
                self.close()
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0)
            elif trafo_index==7:
                import myoto_trifaz
                self.window =myoto_trifaz.OtoTrifazwindow()
                self.window.setWindowIcon(QIcon(ICON_DIR +"\\"+"logo.jpg"))
                # self.window.ui.lineEdit_2.setText(data[3])
                # self.window.user_admin_check()
                self.window.ui.lineEdit_user.setText(data[1])
                self.close()
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0) 
            elif trafo_index==8:
                import myharmonik
                self.window =myharmonik.Harmonikwindow()
                self.window.setWindowIcon(QIcon(ICON_DIR +"\\"+"logo.jpg"))
                # self.window.ui.lineEdit_2.setText(data[3])
                # self.window.user_admin_check()
                self.window.ui.lineEdit_user.setText(data[1])
                self.close()
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0)
            elif trafo_index==9:
                import myups
                self.window =myups.UPSwindow()
                self.window.setWindowIcon(QIcon(ICON_DIR +"\\"+"logo.jpg"))
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
            print("Kullanıcı Hatası")
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
                self.get_AllUser()
            else:
                self.ui.label_6.setText("Şifreler eşleşmiyor")
                print("Şifreler eşleşmiyor")
    def get_AllUser(self):
        users = db.showall_user()
        table_update(users, ("ID", "Kullanici","Yetki"), self.ui.tableWidget)
    def delete_User(self):
        userID = int(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 0).text())
       
        try :
            db.delete_user(userID)
            data =db.showall_user()
            table_update(data, ("ID", "Kullanici","Yetki"), self.ui.tableWidget)
            self.ui.label_6.setText('Kullanıcı Silindi')
        except:
            self.ui.label_6.setText('Lütfen Girdiğiniz Değerleri Kontrol Edin')
    
    def get_hostname(self):
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print(hostname,local_ip)
        
        
        #if local_ip in LOCAL_IPs:
        if db.check_ips(str(local_ip))!=None:
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
