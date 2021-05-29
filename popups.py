
from QT_file.klemens import Ui_Dialog as Klemens_dialog
from QT_file.izolasyon import Ui_Dialog as Izolasyon_dialog
from QT_file.tel_select import Ui_Dialog as Telselect_dialog
from QT_file.genel_param import Ui_Dialog as GenelParam_dialog
from QT_file.reciepe import Ui_Dialog as Reciepe_dialog
from QT_file.karkas import Ui_Dialog as Karkas_dialog
from QT_file.about import Ui_Form as About_window
from QT_file.kesit_param import Ui_Dialog as KesitParam_dialog
import hesaplamalar  as hp
from PySide2.QtWidgets import QMainWindow,QDialog,QTableWidgetItem,QPushButton,QLineEdit,QLabel,QMessageBox
from PySide2.QtCore import SIGNAL, QObject,QTimer,Qt,QRect,QDateTime
import db_sql,math,time
import veri_tipi as vt
import json

headers_recete= ("id","kullanıcı","musteri_adi","siparis_kodu","guc","primer", \
                "sekonder","VA","trafo_tipi","Tarih" )
headers_klemens= ("ID", "klemens_Adı","en","boy","yukseklik", "akim", "Kayıt Tarihi")
headers_ayak= ("ID", "AYAK_Adı","en","boy","yukseklik", "Kayıt Tarihi")
headers_kapton= ("ID", "Kapton_Adı","Yukseklik", "Ozzellik-1", "Kayıt Tarihi")
headers_folyotel_tel= ("ID", "Tel_Adı","En", "Yukseklik", "Ozzellik-1","Ozzellik-2", "Kayıt Tarihi")
headers_kare_tel= ("ID", "Tel_Adı","En","Yukseklik", "Ozzellik-1", "Ozzellik-2","Kayıt Tarihi")
headers_karkas= ("ID", "Karkas_Adı","En", "Boy","Ozellik-1" ,"Ozellik-2" ,"Kayıt Tarihi")
headers_teller= ("ID", "Tel_Adı","Cap", "Ozellik-1","Ozellik-2", "Kayıt Tarihi")
headers_logs = ("ID", "Code","Unit","UserID", "Record Date")

# ======================  tablolar =========================
db=db_sql.mydb()
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
def update_msjbox(text,title):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText(text)
    msgBox.setWindowTitle(title)
    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Discard |QMessageBox.Cancel)
    buttonOk = msgBox.button(QMessageBox.Ok)
    buttonOk.setText('Guncelle')
    buttonKaydet = msgBox.button(QMessageBox.Discard)
    buttonKaydet.setText('Yeni Kayıt')
    buttonIptal = msgBox.button(QMessageBox.Cancel)
    buttonIptal.setText('Iptal')
    return msgBox.exec()
def delete_msjbox(text,title):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.setText(text)
    msgBox.setWindowTitle(title)
    msgBox.setStandardButtons(QMessageBox.Discard | QMessageBox.Cancel)
    buttonY = msgBox.button(QMessageBox.Discard)
    buttonY.setText('Sil')
    return msgBox.exec()
def clear_msjbox(text,title):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.setText(text)
    msgBox.setWindowTitle(title)
    msgBox.setStandardButtons(QMessageBox.Discard | QMessageBox.Cancel)
    buttonY = msgBox.button(QMessageBox.Discard)
    buttonY.setText('Temizle')
    return msgBox.exec()
def warning_msjbox(text,title):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.setText(text)
    msgBox.setWindowTitle(title)
    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    buttonY = msgBox.button(QMessageBox.Ok)
    buttonY.setText('Devam Et')
    return msgBox.exec()
def info_msjbox(text,title):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText(text)
    msgBox.setWindowTitle(title)
    msgBox.setStandardButtons(QMessageBox.Ok )
    buttonOk = msgBox.button(QMessageBox.Ok)
    buttonOk.setText('Tamam')

    return msgBox.exec()
class Aboutwindow(QMainWindow):
    def __init__(self, parent=None):
        super(Aboutwindow, self).__init__(parent)
        self.ui = About_window()
        self.ui.setupUi(self)
class Karkasdialog(QDialog):
    def __init__(self, parent=None):
        super(Karkasdialog, self).__init__(parent)
        self.ui = Karkas_dialog()

        self.ui.setupUi(self)
        self.handle_button()

        data = db.showall_karkas()
        table_update(data, headers_karkas, self.ui.tableWidget)

    def handle_button(self):
        self.ui.pushButton_ara.clicked.connect(self.filter_karkas_table)
        self.ui.pushButton_sec.clicked.connect(self.karkas_select)
        self.ui.tableWidget.itemClicked.connect(self.callback_from_karkas_table)
        self.ui.pushButton_sil.clicked.connect(self.karkas_delete)
        self.ui.pushButton_kaydet.clicked.connect(self.karkas_kaydet)
    def filter_karkas_table(self):
        self.ui.lineEdit_3.text()
        self.ui.comboBox.currentIndex()

        data = db.showfilter_karkas(index=self.ui.comboBox.currentIndex(), filter_value=self.ui.lineEdit_3.text())

        table_update(data, headers_karkas, self.ui.tableWidget)
    def callback_from_karkas_table(self):
        self.karkas_ID = int(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 0).text())

        data = db.calldata_with_id_karkas(self.karkas_ID)
        if data != None:
            self.ui.lineEdit_ID.setText(str(data[0]))
            self.ui.lineEdit_karkas_name.setText(str(data[1]))
            self.ui.doubleSpinBox_karkas_en.setValue(data[2])
            self.ui.doubleSpinBox_karkas_boy.setValue(data[3])
            self.ui.lineEdit_karkas_ozellik_1.setText(data[4])
            self.ui.lineEdit_karkas_ozellik_2.setText(data[5])
            return True
        else:
            return False
    def karkas_select(self):

        self.close()
        return self.ui.doubleSpinBox_karkas_en.value(), self.ui.doubleSpinBox_karkas_boy.value()
    def karkas_delete(self):
        self.karkas_ID = int(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 0).text())
        warning_msjbox(text=f"{self.karkas_ID} Nolu Seçmiş Olduğunuz Kayıt Silinecektir.",title=" Uyarı - Kayıt Silinecektir.")
        try :
            db.delete_karkas(self.karkas_ID)
            data =db.showall_karkas()
            table_update(data, headers_karkas, self.ui.tableWidget)
        except:
            error_msjbox(title='Kayıt Bulunamadı', text='Lütfen Tablodan Bir Kayıt Seçiniz.')
    def karkas_kaydet(self):

        if self.ui.lineEdit_ID.text()!="":
            button_name=update_msjbox(text="Kaydı Güncelemek için -Güncelle- Butonuna, \n Yeni Kayıt Yaratmak için ise -Yeni Kayıt- Butonuna Basınız",title="Kayıt Ekleme/Yenileme")
            if button_name == QMessageBox.Ok:
                try :
                    db.update_karkas((self.ui.lineEdit_karkas_name.text(),
                                     self.ui.doubleSpinBox_karkas_en.value(),self.ui.doubleSpinBox_karkas_boy.value(),
                                     self.ui.lineEdit_karkas_ozellik_1.text(),self.ui.lineEdit_karkas_ozellik_2.text(),int(self.ui.lineEdit_ID.text())))
                    info_msjbox(text="Mevcut Kayıt Başaıryla Güncellendi", title="İşlem Başarılı")
                except Exception as err:
                    error_msjbox(title='Kayıt Bulunamadı', text='Lütfen Tablodan Bir Kayıt Seçiniz.')
                    print(err)

            if button_name == QMessageBox.Discard:
                try :
                    data = db.check_karkas((self.ui.lineEdit_karkas_name.text()))

                    if data!="" and data!=None:
                        error_msjbox(text='Bu isimle bir Karkas ismi var Lütfen İsmi Değiştirin', title='Karkas isim Hatası')
                        return False
                    db.insert_karkas((self.ui.lineEdit_karkas_name.text(),
                                     self.ui.doubleSpinBox_karkas_en.value(),self.ui.doubleSpinBox_karkas_boy.value(),
                                     self.ui.lineEdit_karkas_ozellik_1.text(),self.ui.lineEdit_karkas_ozellik_2.text()))
                    info_msjbox(text="Kayıt Başaıryla Kaydedildi",title="İşlem Başarılı")
                except Exception as err:
                    error_msjbox(title='Kayıt Bulunamadı', text='Lütfen Tablodan Bir Kayıt Seçiniz.')
        else:
            try:
                db.insert_karkas((self.ui.lineEdit_karkas_name.text(),
                                 self.ui.doubleSpinBox_karkas_en.value(), self.ui.doubleSpinBox_karkas_boy.value(),
                                 self.ui.lineEdit_karkas_ozellik_1.text(), self.ui.lineEdit_karkas_ozellik_2.text()))
                info_msjbox(text="Kayıt Başaıryla Kaydedildi", title="İşlem Başarılı")
            except:
                error_msjbox(title='Kayıt Bulunamadı', text='Lütfen Tablodan Bir Kayıt Seçiniz.')
        data = db.showall_karkas()
        table_update(data, headers_karkas, self.ui.tableWidget)
class GenelParamdialog(QDialog):
    def __init__(self, parent=None):
        super(GenelParamdialog, self).__init__(parent)
        self.ui = GenelParam_dialog()
        self.ui.setupUi(self)
        self.handle_button()

    def handle_button(self):
        self.ui.pushButton_sec.clicked.connect(self.param_select)
        self.ui.doubleSpinBox_sac.valueChanged.connect(self.onerilen_hesapla)

    def param_select(self):
        self.close()
    def onerilen_hesapla(self):
        import hesaplamalar  as hp
        gauss,c_deg= hp.gauss_onerilen_hesapla(sac=self.ui.doubleSpinBox_sac.value())
        self.ui.doubleSpinBox_gauss2.setValue(gauss)
        self.ui.doubleSpinBox_c2.setValue(c_deg)
class Telselectdialog(QDialog):
    """Tel Seçim Sınıfı

    Args:
        QDialog ([type]): [description]
    """    
    def __init__(self, parent=None):
        super(Telselectdialog, self).__init__(parent)
        self.ui = Telselect_dialog()
        self.ui.setupUi(self)
        self.handle_button()
        self.teltipi=""
        # self.db=db_sql.mydb()
        #data = db.showall_teller()
        #table_update(data, headers_teller, self.ui.tableWidget)
        
    def update_all_table(self):
        data = db.showfilter_teller(index=2, filter_value=self.teltipi)
        table_update(data, headers_teller, self.ui.tableWidget)
        data = db.showfilter_karetel(index=3, filter_value=self.teltipi)
        table_update(data, headers_kare_tel, self.ui.tableWidget_2)
        data = db.showall_folyotel()
        table_update(data, headers_folyotel_tel, self.ui.tableWidget_3)
        data = db.showall_kapton()
        table_update(data, headers_kapton, self.ui.tableWidget_4)
    def handle_button(self):
        self.ui.pushButton_ara_tel.clicked.connect(self.filter_telsecim_table)
        self.ui.pushButton_sec_tel.clicked.connect(self.telsecim_select)
        self.ui.pushButton_kaydet_tel.clicked.connect(self.telsecim_kaydet)
        self.ui.pushButton_sil_tel.clicked.connect(self.telsecim_delete)
        self.ui.tableWidget.itemClicked.connect(self.callback_from_telsecim_table)

        self.ui.pushButton_ara_karetel.clicked.connect(self.filter_karetelsecim_table)
        self.ui.pushButton_sec_karetel.clicked.connect(self.karetelsecim_select)
        self.ui.pushButton_Kaydet_karetel.clicked.connect(self.karetelsecim_kaydet)
        self.ui.pushButton_sil_karetel.clicked.connect(self.karetelsecim_delete)
        self.ui.tableWidget_2.itemClicked.connect(self.callback_from_karetelsecim_table)

        self.ui.pushButton_ara_folyo.clicked.connect(self.filter_folyotelsecim_table)
        self.ui.pushButton_sec_folyo.clicked.connect(self.folyotelsecim_select)
        self.ui.pushButton_kaydet_folyo.clicked.connect(self.folyotelsecim_kaydet)
        self.ui.pushButton_sil_folyo.clicked.connect(self.folyotelsecim_delete)
        self.ui.tableWidget_3.itemClicked.connect(self.callback_from_folyotelsecim_table)

        self.ui.pushButton_ara_kapton.clicked.connect(self.filter_kaptonsecim_table)
        self.ui.pushButton_sec_kapton.clicked.connect(self.kaptonsecim_select)
        self.ui.pushButton_kaydet_kapton.clicked.connect(self.kaptonsecim_kaydet)
        self.ui.pushButton_sil_kapton.clicked.connect(self.kaptonsecim_delete)
        self.ui.tableWidget_4.itemClicked.connect(self.callback_from_kaptonsecim_table)

    def filter_telsecim_table(self):
        self.ui.lineEdit_3.text()
        self.ui.comboBox.currentIndex()
        data = db.showfilter_teller(index=self.ui.comboBox.currentIndex(), filter_value=self.ui.lineEdit_3.text())
        table_update(data, headers_teller, self.ui.tableWidget)

    def callback_from_telsecim_table(self):
        self.teller_ID = int(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 0).text())

        data = db.calldata_with_id_teller(self.teller_ID)
        if data != None:
            self.ui.lineEdit_ID.setText(str(data[0]))
            self.ui.lineEdit_tel_name.setText(str(data[1]))
            self.ui.doubleSpinBox_tel_cap.setValue(data[2])
            self.ui.lineEdit_tel_ozellik_1.setText(str(data[3]))
            self.ui.lineEdit_tel_ozellik_2.setText(str(data[4]))
            return True
        else:
            return False
        pass

    def telsecim_select(self):

        self.close()
        return self.ui.doubleSpinBox_tel_cap.value()
    def telsecim_delete(self):
        self.teller_ID = int(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 0).text())
        warning_msjbox(text=f"{self.teller_ID} Nolu Seçmiş Olduğunuz Kayıt Silinecektir.",title=" Uyarı - Kayıt Silinecektir.")
        try :
            db.delete_teller(self.teller_ID)
            data =db.showall_teller()
            table_update(data, headers_teller, self.ui.tableWidget)
        except:
            error_msjbox(title='Kayıt Bulunamadı', text='Lütfen Tablodan Bir Kayıt Seçiniz.')
    def telsecim_kaydet(self):

        if self.ui.lineEdit_ID.text()!="":
            button_name=update_msjbox(text="Kaydı Güncelemek için -Güncelle- Butonuna, \nYeni Kayıt Yaratmak için ise -Yeni Kayıt- Butonuna Basınız",title="Kayıt Ekleme/Yenileme")
            if button_name == QMessageBox.Ok:
                try :
                    db.update_teller((self.ui.lineEdit_tel_name.text(),
                                     self.ui.doubleSpinBox_tel_cap.value(),
                                     self.ui.lineEdit_tel_ozellik_1.text(),self.ui.lineEdit_tel_ozellik_2.text(),int(self.ui.lineEdit_ID.text())))
                    info_msjbox(text="Mevcut Kayıt Başaıryla Güncellendi", title="İşlem Başarılı")
                except Exception as err:
                    error_msjbox(title='Kayıt Bulunamadı', text='Lütfen Tablodan Bir Kayıt Seçiniz.')
                    print(err)

            if button_name == QMessageBox.Discard:
                try :
                    data = db.check_teller((self.ui.lineEdit_tel_name.text()))

                    if data!="" and data!=None:
                        error_msjbox(text='Bu isimle bir Yuvarlak TEl  ismi var Lütfen İsmi Değiştirin', title='Yuvarlak TEl isim Hatası')
                        return False
                    db.insert_teller((self.ui.lineEdit_tel_name.text(),
                                     self.ui.doubleSpinBox_tel_cap.value(),
                                     self.ui.lineEdit_tel_ozellik_1.text(),self.ui.lineEdit_tel_ozellik_2.text()))
                    info_msjbox(text="Kayıt Başaıryla Kaydedildi",title="İşlem Başarılı")
                except Exception as err:
                    error_msjbox(title='Kayıt Bulunamadı', text='Lütfen Tablodan Bir Kayıt Seçiniz.')
        else:
            try:
                db.insert_teller((self.ui.lineEdit_tel_name.text(),
                                 self.ui.doubleSpinBox_tel_cap.value(),
                                 self.ui.lineEdit_tel_ozellik_1.text(), self.ui.lineEdit_tel_ozellik_2.text()))
                info_msjbox(text="Kayıt Başaıryla Kaydedildi", title="İşlem Başarılı")
            except:
                error_msjbox(title='Kayıt Bulunamadı', text='Lütfen Tablodan Bir Kayıt Seçiniz.')
        data = db.showall_teller()
        table_update(data, headers_teller, self.ui.tableWidget)


    def filter_karetelsecim_table(self):#  KareTel Secim ----------------------
        self.ui.lineEdit_4.text()
        self.ui.comboBox_2.currentIndex()

        data = db.showfilter_karetel(index=self.ui.comboBox_2.currentIndex(), filter_value=self.ui.lineEdit_4.text())

        table_update(data, headers_kare_tel, self.ui.tableWidget_2)

    def callback_from_karetelsecim_table(self):
        self.kare_tel_ID = int(self.ui.tableWidget_2.item(self.ui.tableWidget_2.currentRow(), 0).text())

        data = db.calldata_with_id_karetel(self.kare_tel_ID)
        if data != None:
            self.ui.lineEdit_ID_2.setText(str(data[0]))
            self.ui.lineEdit_tel_name_2.setText(str(data[1]))
            self.ui.doubleSpinBox_tel_cap_2.setValue(data[2])
            self.ui.doubleSpinBox_tel_cap_3.setValue(data[3])
            self.ui.lineEdit_karetel_ozellik_1.setText(str(data[4]))
            self.ui.lineEdit_karetel_ozellik_2.setText(str(data[5]))
            return True
        else:
            return False
        pass

    def karetelsecim_select(self):

        self.close()
        return self.ui.doubleSpinBox_tel_cap_2.value(), self.ui.doubleSpinBox_tel_cap_3.value()

        pass
    def karetelsecim_delete(self):
        self.kareteller_ID = int(self.ui.tableWidget_2.item(self.ui.tableWidget_2.currentRow(), 0).text())
        warning_msjbox(text=f"{self.kareteller_ID} Nolu Seçmiş Olduğunuz Kayıt Silinecektir.",title=" Uyarı - Kayıt Silinecektir.")
        try :
            db.delete_karetel(self.kareteller_ID)
            data =db.showall_karetel()
            table_update(data, headers_kare_tel, self.ui.tableWidget_2)
        except:
            error_msjbox(title='Kayıt Bulunamadı', text='Lütfen Tablodan Bir Kayıt Seçiniz.')
    def karetelsecim_kaydet(self):

        if self.ui.lineEdit_ID_2.text()!="":
            button_name=update_msjbox(text="Kaydı Güncelemek için -Güncelle- Butonuna, \n Yeni Kayıt Yaratmak için ise -Yeni Kayıt- Butonuna Basınız",title="Kayıt Ekleme/Yenileme")
            if button_name == QMessageBox.Ok:
                try :
                    db.update_karetel((self.ui.lineEdit_tel_name_2.text(),
                                     self.ui.doubleSpinBox_tel_cap_2.value(),self.ui.doubleSpinBox_tel_cap_3.value(),
                                     self.ui.lineEdit_karetel_ozellik_1.text(),self.ui.lineEdit_karetel_ozellik_2.text(),int(self.ui.lineEdit_ID_2.text())))
                    info_msjbox(text="Mevcut Kayıt Başaıryla Güncellendi", title="İşlem Başarılı")
                except Exception as err:
                    error_msjbox(title='Kayıt Bulunamadı', text='Lütfen Tablodan Bir Kayıt Seçiniz.')
                    print(err)

            if button_name == QMessageBox.Discard:
                try :
                    data = db.check_karetel((self.ui.lineEdit_tel_name_2.text()))

                    if data!="" and data!=None:
                        error_msjbox(text='Bu isimle bir KareTel tel ismi var. Lütfen İsmi Değiştirin', title='KareTel isim Hatası')
                        return False
                    db.insert_karetel((self.ui.lineEdit_tel_name_2.text(),
                                     self.ui.doubleSpinBox_tel_cap_2.value(),self.ui.doubleSpinBox_tel_cap_3.value(),
                                     self.ui.lineEdit_karetel_ozellik_1.text(),self.ui.lineEdit_karetel_ozellik_2.text()))
                    info_msjbox(text="Kayıt Başaıryla Kaydedildi",title="İşlem Başarılı")
                except Exception as err:
                    error_msjbox(title='Kayıt Bulunamadı', text='Lütfen Tablodan Bir Kayıt Seçiniz.')
        else:
            try:
                db.insert_karetel((self.ui.lineEdit_tel_name_2.text(),
                                 self.ui.doubleSpinBox_tel_cap_2.value(),self.ui.doubleSpinBox_tel_cap_3.value(),
                                 self.ui.lineEdit_karetel_ozellik_1.text(), self.ui.lineEdit_karetel_ozellik_2.text()))
                info_msjbox(text="Kayıt Başaıryla Kaydedildi", title="İşlem Başarılı")
            except:
                error_msjbox(title='Kayıt Bulunamadı', text='Lütfen Tablodan Bir Kayıt Seçiniz.')
        data = db.showall_karetel()
        table_update(data, headers_kare_tel, self.ui.tableWidget_2)
    #  FolyoTel Secim ----------------------
    def filter_folyotelsecim_table(self):
        self.ui.lineEdit_5.text()
        self.ui.comboBox_3.currentIndex()

        data = db.showfilter_folyotel(index=self.ui.comboBox_3.currentIndex(), filter_value=self.ui.lineEdit_5.text())

        table_update(data, headers_folyotel_tel, self.ui.tableWidget_3)

    def callback_from_folyotelsecim_table(self):
        self.folyo_tel_ID = int(self.ui.tableWidget_3.item(self.ui.tableWidget_3.currentRow(), 0).text())

        data = db.calldata_with_id_folyotel(self.folyo_tel_ID)
        if data != None:
            self.ui.lineEdit_ID_3.setText(str(data[0]))
            self.ui.lineEdit_tel_name_3.setText(str(data[1]))
            self.ui.doubleSpinBox_tel_cap_4.setValue(data[2])
            self.ui.doubleSpinBox_tel_cap_5.setValue(data[3])
            self.ui.lineEdit_folyotel_ozellik_1.setText(str(data[4]))
            self.ui.lineEdit_folyotel_ozellik_2.setText(str(data[5]))
            return True
        else:
            return False
        pass

    def folyotelsecim_select(self):

        self.close()
        return self.ui.doubleSpinBox_tel_cap_4.value(), self.ui.doubleSpinBox_tel_cap_5.value()
    def folyotelsecim_delete(self):
        self.folyo_tel_ID = int(self.ui.tableWidget_3.item(self.ui.tableWidget_3.currentRow(), 0).text())
        warning_msjbox(text=f"{self.folyo_tel_ID} Nolu Seçmiş Olduğunuz Kayıt Silinecektir.",title=" Uyarı - Kayıt Silinecektir.")
        try :
            db.delete_folyotel(self.folyo_tel_ID)
            data =db.showall_folyotel()
            table_update(data, headers_folyotel_tel, self.ui.tableWidget_3)
        except:
            error_msjbox(title='Kayıt Bulunamadı', text='Lütfen Tablodan Bir Kayıt Seçiniz.')
    def folyotelsecim_kaydet(self):

        if self.ui.lineEdit_ID_3.text()!="":
            button_name=update_msjbox(text="Kaydı Güncelemek için -Güncelle- Butonuna, \n Yeni Kayıt Yaratmak için ise -Yeni Kayıt- Butonuna Basınız",title="Kayıt Ekleme/Yenileme")
            if button_name == QMessageBox.Ok:
                try :
                    db.update_folyotel((self.ui.lineEdit_tel_name_3.text(),
                                     self.ui.doubleSpinBox_tel_cap_4.value(),self.ui.doubleSpinBox_tel_cap_5.value(),
                                     self.ui.lineEdit_folyotel_ozellik_1.text(),self.ui.lineEdit_folyotel_ozellik_2.text(),int(self.ui.lineEdit_ID_3.text())))
                    info_msjbox(text="Mevcut Kayıt Başaıryla Güncellendi", title="İşlem Başarılı")
                except Exception as err:
                    error_msjbox(title='Kayıt Bulunamadı', text='Lütfen Tablodan Bir Kayıt Seçiniz.')
                    print(err)

            if button_name == QMessageBox.Discard:
                try :
                    data = db.check_folyotel((self.ui.lineEdit_tel_name_3.text()))

                    if data!="" and data!=None:
                        error_msjbox(text='Bu isimle bir folyo ismi var Lütfen İsmi Değiştirin', title='Folyo isim Hatası')
                        return False
                    db.insert_folyotel((self.ui.lineEdit_tel_name_3.text(),
                                     self.ui.doubleSpinBox_tel_cap_4.value(),self.ui.doubleSpinBox_tel_cap_5.value(),
                                     self.ui.lineEdit_folyotel_ozellik_1.text(),self.ui.lineEdit_folyotel_ozellik_2.text()))
                    info_msjbox(text="Kayıt Başaıryla Kaydedildi",title="İşlem Başarılı")
                except Exception as err:
                    error_msjbox(title='Kayıt Bulunamadı', text='Lütfen Tablodan Bir Kayıt Seçiniz.')
        else:
            try:
                db.insert_folyotel((self.ui.lineEdit_tel_name_3.text(),
                                 self.ui.doubleSpinBox_tel_cap_4.value(),self.ui.doubleSpinBox_tel_cap_5.value(),
                                 self.ui.lineEdit_folyotel_ozellik_1.text(), self.ui.lineEdit_folyotel_ozellik_2.text()))
                info_msjbox(text="Kayıt Başaıryla Kaydedildi", title="İşlem Başarılı")
            except:
                error_msjbox(title='Kayıt Bulunamadı', text='Lütfen Tablodan Bir Kayıt Seçiniz.')
        data = db.showall_folyotel()
        table_update(data, headers_folyotel_tel, self.ui.tableWidget_3)
    #  Kapton Secim ----------------------
    def filter_kaptonsecim_table(self):
        self.ui.lineEdit_6.text()
        self.ui.comboBox_4.currentIndex()

        data = db.showfilter_kapton(index=self.ui.comboBox_4.currentIndex(), filter_value=self.ui.lineEdit_6.text())

        table_update(data, headers_kapton, self.ui.tableWidget_4)

    def callback_from_kaptonsecim_table(self):
        self.kapton_ID = int(self.ui.tableWidget_4.item(self.ui.tableWidget_4.currentRow(), 0).text())

        data = db.calldata_with_id_kapton(self.kapton_ID)
        if data != None:
            self.ui.lineEdit_ID_4.setText(str(data[0]))
            self.ui.lineEdit_tel_name_4.setText(str(data[1]))
            self.ui.doubleSpinBox_tel_cap_6.setValue(data[2])

            self.ui.lineEdit_kapton_ozellik_1.setText(str(data[3]))
            return True
        else:
            return False
        pass

    def kaptonsecim_select(self):

        self.close()
        return self.ui.doubleSpinBox_tel_cap_6.value()

        pass
    def kaptonsecim_delete(self):
        self.kapton_ID = int(self.ui.tableWidget_4.item(self.ui.tableWidget_4.currentRow(), 0).text())
        warning_msjbox(text=f"{self.kapton_ID} Nolu Seçmiş Olduğunuz Kayıt Silinecektir.",title=" Uyarı - Kayıt Silinecektir.")
        try :
            db.delete_kapton(self.kapton_ID)
            data =db.showall_kapton()
            table_update(data, headers_kapton, self.ui.tableWidget_4)
        except:
            error_msjbox(title='Kayıt Bulunamadı', text='Lütfen Tablodan Bir Kayıt Seçiniz.')
    def kaptonsecim_kaydet(self):

        if self.ui.lineEdit_ID_4.text()!="":
            button_name=update_msjbox(text="Kaydı Güncelemek için -Güncelle- Butonuna, \n Yeni Kayıt Yaratmak için ise -Yeni Kayıt- Butonuna Basınız",title="Kayıt Ekleme/Yenileme")
            if button_name == QMessageBox.Ok:
                try :
                    db.update_kapton((self.ui.lineEdit_tel_name_4.text(),
                                     self.ui.doubleSpinBox_tel_cap_6.value(),
                                     self.ui.lineEdit_kapton_ozellik_1.text(),int(self.ui.lineEdit_ID_4.text())))
                    info_msjbox(text="Mevcut Kayıt Başaıryla Güncellendi", title="İşlem Başarılı")
                except Exception as err:
                    error_msjbox(title='Kayıt Bulunamadı', text='Lütfen Tablodan Bir Kayıt Seçiniz.')
                    print(err)

            if button_name == QMessageBox.Discard:
                try :
                    data = db.check_kapton((self.ui.lineEdit_tel_name_4.text()))

                    if data!="" and data!=None:
                        error_msjbox(text='Bu isimle bir Kapton ismi var Lütfen İsmi Değiştirin', title='Kapton isim Hatası')
                        return False
                    db.insert_kapton((self.ui.lineEdit_tel_name_4.text(),
                                     self.ui.doubleSpinBox_tel_cap_6.value(),
                                     self.ui.lineEdit_kapton_ozellik_1.text()))
                    info_msjbox(text="Kayıt Başaıryla Kaydedildi",title="İşlem Başarılı")
                except Exception as err:
                    error_msjbox(title='Kayıt Bulunamadı', text='Lütfen Tablodan Bir Kayıt Seçiniz.')
        else:
            try:
                db.insert_kapton((self.ui.lineEdit_tel_name_4.text(),
                                 self.ui.doubleSpinBox_tel_cap_4.value(),
                                 self.ui.lineEdit_kapton_ozellik_1.text()))
                info_msjbox(text="Kayıt Başaıryla Kaydedildi", title="İşlem Başarılı")
            except:
                error_msjbox(title='Kayıt Bulunamadı', text='Lütfen Tablodan Bir Kayıt Seçiniz.')
        data = db.showall_kapton()
        table_update(data, headers_kapton, self.ui.tableWidget_4)
class Izolasyondialog(QDialog):
    def __init__(self, parent=None):
        super(Izolasyondialog, self).__init__(parent)
        self.ui = Izolasyon_dialog()
        self.ui.setupUi(self)
        self.handle_button()
        self.ekran_select()
        self.ekstra_select()

    def handle_button(self):
        self.ui.pushButton_sec.clicked.connect(self.param_select)
        self.ui.checkBox.stateChanged.connect(self.ekran_select)
        self.ui.checkBox_2.stateChanged.connect(self.ekstra_select)

    def ekran_select(self):
        if self.ui.checkBox.isChecked():
            self.ui.doubleSpinBox_4.setEnabled(True)
            self.ui.doubleSpinBox_4.setValue(0.19)
        else:
            self.ui.doubleSpinBox_4.setEnabled(False)
            self.ui.doubleSpinBox_4.setValue(0)

    def ekstra_select(self):
        if self.ui.checkBox_2.isChecked():
            self.ui.doubleSpinBox_5.setEnabled(True)
            self.ui.doubleSpinBox_5.setValue(0.19)
        else:
            self.ui.doubleSpinBox_5.setEnabled(False)
            self.ui.doubleSpinBox_5.setValue(0)

    def param_select(self):

        self.close()
class Klemensdialog(QDialog):
    def __init__(self, parent=None):
        super(Klemensdialog, self).__init__(parent)
        self.ui = Klemens_dialog()
        self.ui.setupUi(self)
        self.handle_button()
        # self.db=db_sql.mydb()
        data = db.showall_klemens()

        table_update(data, headers_klemens, self.ui.tableWidget_klemens)
        data = db.showall_ayak()
        table_update(data, headers_ayak, self.ui.tableWidget_ayak)

    def handle_button(self):
        self.ui.pushButton_ara_klemens.clicked.connect(self.filter_klemens_table)
        
        self.ui.tableWidget_klemens.itemClicked.connect(self.callback_from_klemens_table)
        self.ui.pushButton_ara_ayak.clicked.connect(self.filter_ayak_table)
       
        self.ui.tableWidget_ayak.itemClicked.connect(self.callback_from_ayak_table)
        self.ui.pushButton_sec.clicked.connect(self.select_button_pressed)
        self.ui.pushButton_kaydet_klemens.clicked.connect(self.klemens_kaydet)
        self.ui.pushButton_sil_klemens.clicked.connect(self.klemens_delete)
        self.ui.pushButton_kaydet_ayak.clicked.connect(self.ayak_kaydet)
        self.ui.pushButton_sil_ayak.clicked.connect(self.ayak_delete)
    def filter_klemens_table(self):
        self.ui.lineEdit_klemens.text()
        self.ui.comboBox_klemens.currentIndex()

        data = db.showfilter_klemens(index=self.ui.comboBox_klemens.currentIndex(),
                                     filter_value=self.ui.lineEdit_klemens.text())

        table_update(data, headers_klemens, self.ui.tableWidget_klemens)

    def filter_ayak_table(self):
        self.ui.lineEdit_ayak.text()
        self.ui.comboBox_ayak.currentIndex()

        data = db.showfilter_ayak(index=self.ui.comboBox_ayak.currentIndex(), filter_value=self.ui.lineEdit_ayak.text())

        table_update(data, headers_ayak, self.ui.tableWidget_ayak)

    def callback_from_klemens_table(self):
        self.klemens_ID = int(self.ui.tableWidget_klemens.item(self.ui.tableWidget_klemens.currentRow(), 0).text())

        data = db.calldata_with_id_klemens(self.klemens_ID)
        if data != None:
            self.ui.lineEdit_ID_klemens.setText(str(data[0]))
            self.ui.lineEdit_klemens_name.setText(str(data[1]))
            self.ui.doubleSpinBox_klemens_a.setValue(data[2])
            self.ui.doubleSpinBox_klemens_b.setValue(data[3])
            self.ui.doubleSpinBox_klemens_c.setValue(data[4])
            self.ui.doubleSpinBox_klemens_akim.setValue(data[5])
            return True
        else:
            return False

    def callback_from_ayak_table(self):
        self.ayak_ID = int(self.ui.tableWidget_ayak.item(self.ui.tableWidget_ayak.currentRow(), 0).text())

        data = db.calldata_with_id_ayak(self.ayak_ID)
        if data != None:
            self.ui.lineEdit_ID_ayak.setText(str(data[0]))
            self.ui.lineEdit_ayak_name.setText(str(data[1]))
            self.ui.doubleSpinBox_ayak_a.setValue(data[2])

            return True
        else:
            return False

    def select_button_pressed(self):
        self.close()
    

    def klemens_delete(self):
        self.klemens_ID = int(self.ui.tableWidget_klemens.item(self.ui.tableWidget_klemens.currentRow(), 0).text())
        warning_msjbox(text=f"{self.klemens_ID} Nolu Seçmiş Olduğunuz Kayıt Silinecektir.",title=" Uyarı - Kayıt Silinecektir.")
        try :
            db.delete_klemens(self.klemens_ID)
            data =db.showall_klemens()
            table_update(data, headers_klemens, self.ui.tableWidget_klemens)
        except:
            error_msjbox(title='Kayıt Bulunamadı', text='Lütfen Tablodan Bir Kayıt Seçiniz.')
    def klemens_kaydet(self):

        if self.ui.lineEdit_ID_klemens.text()!="":
            button_name=update_msjbox(text="Kaydı Güncelemek için -Güncelle- Butonuna, \n Yeni Kayıt Yaratmak için ise -Yeni Kayıt- Butonuna Basınız",title="Kayıt Ekleme/Yenileme")
            if button_name == QMessageBox.Ok:
                try :
                    db.update_klemens((self.ui.lineEdit_klemens_name.text(),
                                     self.ui.doubleSpinBox_klemens_a.value(),self.ui.doubleSpinBox_klemens_b.value(),self.ui.doubleSpinBox_klemens_c.value(),
                                     self.ui.doubleSpinBox_klemens_akim.value(),int(self.ui.lineEdit_ID_klemens.text())))
                    info_msjbox(text="Mevcut Kayıt Başaıryla Güncellendi", title="İşlem Başarılı")
                except Exception as err:
                    error_msjbox(title='Kayıt Bulunamadı', text='Lütfen Tablodan Bir Kayıt Seçiniz.')
                    print(err)

            if button_name == QMessageBox.Discard:
                try :
                    data = db.check_klemens((self.ui.lineEdit_klemens_name.text()))

                    if data!="" and data!=None:
                        error_msjbox(text='Bu isimle bir  klemens ismi var Lütfen İsmi Değiştirin', title='klemens isim Hatası')
                        return False
                    db.insert_klemens((self.ui.lineEdit_klemens_name.text(),
                                     self.ui.doubleSpinBox_klemens_a.value(),self.ui.doubleSpinBox_klemens_b.value(),self.ui.doubleSpinBox_klemens_c.value(),
                                     self.ui.doubleSpinBox_klemens_akim.value()))
                    info_msjbox(text="Kayıt Başaıryla Kaydedildi",title="İşlem Başarılı")
                except Exception as err:
                    error_msjbox(title='Kayıt Bulunamadı', text='Lütfen Tablodan Bir Kayıt Seçiniz.')
                    print(err)
        else:
            try:
                db.insert_klemens((self.ui.lineEdit_klemens_name.text(),
                                     self.ui.doubleSpinBox_klemens_a.value(),self.ui.doubleSpinBox_klemens_b.value(),self.ui.doubleSpinBox_klemens_c.value(),
                                     self.ui.doubleSpinBox_klemens_akim.value()))
                info_msjbox(text="Kayıt Başaıryla Kaydedildi", title="İşlem Başarılı")
            except Exception as err:
                error_msjbox(title='Kayıt Bulunamadı', text='Lütfen Tablodan Bir Kayıt Seçiniz.')
                print(err)
        data = db.showall_klemens()
        table_update(data, headers_klemens, self.ui.tableWidget_klemens)
    def ayak_delete(self):
        self.ayak_ID = int(self.ui.tableWidget_ayak.item(self.ui.tableWidget_ayak.currentRow(), 0).text())
        warning_msjbox(text=f"{self.ayak_ID} Nolu Seçmiş Olduğunuz Kayıt Silinecektir.",title=" Uyarı - Kayıt Silinecektir.")
        try :
            db.delete_ayak(self.ayak_ID)
            data =db.showall_ayak()
            table_update(data, headers_ayak, self.ui.tableWidget_ayak)
        except:
            error_msjbox(title='Kayıt Bulunamadı', text='Lütfen Tablodan Bir Kayıt Seçiniz.')
    def ayak_kaydet(self):

        if self.ui.lineEdit_ID_ayak.text()!="":
            button_name=update_msjbox(text="Kaydı Güncelemek için -Güncelle- Butonuna, \n Yeni Kayıt Yaratmak için ise -Yeni Kayıt- Butonuna Basınız",title="Kayıt Ekleme/Yenileme")
            if button_name == QMessageBox.Ok:
                try :
                    db.update_ayak((self.ui.lineEdit_ayak_name.text(),
                                     self.ui.doubleSpinBox_ayak_a.value(),self.ui.doubleSpinBox_ayak_b.value(),self.ui.doubleSpinBox_ayak_c.value(),
                                     int(self.ui.lineEdit_ID_ayak.text())))
                    info_msjbox(text="Mevcut Kayıt Başaıryla Güncellendi", title="İşlem Başarılı")
                except Exception as err:
                    error_msjbox(title='Kayıt Bulunamadı', text='Lütfen Tablodan Bir Kayıt Seçiniz.')
                    print(err)

            if button_name == QMessageBox.Discard:
                try :
                    data = db.check_ayak((self.ui.lineEdit_ayak_name.text()))

                    if data!="" and data!=None:
                        error_msjbox(text='Bu isimle bir  ayak ismi var Lütfen İsmi Değiştirin', title='ayak isim Hatası')
                        return False
                    db.insert_ayak((self.ui.lineEdit_ayak_name.text(),
                                     self.ui.doubleSpinBox_ayak_a.value(),self.ui.doubleSpinBox_ayak_b.value(),self.ui.doubleSpinBox_ayak_c.value(),
                                     ))
                    info_msjbox(text="Kayıt Başaıryla Kaydedildi",title="İşlem Başarılı")
                except Exception as err:
                    error_msjbox(title='Kayıt Bulunamadı', text='Lütfen Tablodan Bir Kayıt Seçiniz.')
                    print(err)
        else:
            try:
                db.insert_ayak((self.ui.lineEdit_ayak_name.text(),
                                     self.ui.doubleSpinBox_ayak_a.value(),self.ui.doubleSpinBox_ayak_b.value(),self.ui.doubleSpinBox_ayak_c.value(),
                                     ))
                info_msjbox(text="Kayıt Başaıryla Kaydedildi", title="İşlem Başarılı")
            except Exception as err:
                error_msjbox(title='Kayıt Bulunamadı', text='Lütfen Tablodan Bir Kayıt Seçiniz.')
                print(err)
        data = db.showall_ayak()
        table_update(data, headers_ayak, self.ui.tableWidget_ayak)
class KesitParamdialog(QDialog):
    def __init__(self, parent=None):
        super(KesitParamdialog, self).__init__(parent)
        self.ui = KesitParam_dialog()
        self.ui.setupUi(self)
        self.guc = 1000.0
        self.frekans = 50.0
        self.karkas_en = 54.0
        self.karkas_boy = 44.0
        self.karkas_yukseklik = 120.0
        self.c = 7.0
        self.karkas_verim = 100.0
        self.gauss =15000.0
        self.cu_yog = 3
        self.al_yog = 1.6
        self.dig_yog = 1.6
        self.cu_par=8700
        self.al_par=2700 
        self.dig_par=2700
        
        self.gn1 = []
        self.gn2 = []
        self.gl = []
        self.gl2 = []
        self.kademe = 0
        self.max_kademe = 3
        self.sarim = ""
        self.primer_sarim_yukseklik_toplam = 22.0
        self.sekonder_sarim_yukseklik_toplam = 44.0
        self.sva1_sarim_yukseklik_toplam = 33.0
        self.sva2_sarim_yukseklik_toplam = 44.0
        self.sva3_sarim_yukseklik_toplam = 44.0
        self.sva4_sarim_yukseklik_toplam = 0.0
        self.sva5_sarim_yukseklik_toplam = 0.0
        self.sva6_sarim_yukseklik_toplam = 0.0
        self.sva7_sarim_yukseklik_toplam = 0.0
        self.sva8_sarim_yukseklik_toplam = 0.0
        self.sva9_sarim_yukseklik_toplam = 0.0
        self.sva10_sarim_yukseklik_toplam = 0.0
        self.primer_izolasyon = 0.0
        self.sva1_izolasyon = 0.0
        self.sva2_izolasyon = 0.0
        self.sva3_izolasyon = 0.0
        self.sva4_izolasyon = 0.0
        self.sva5_izolasyon = 0.0
        self.sva6_izolasyon = 0.0
        self.sva7_izolasyon = 0.0
        self.sva8_izolasyon = 0.0
        self.sva9_izolasyon = 0.0
        self.sva10_izolasyon = 0.0
        self.veri_kumesi()
        self.object_signals()
        self.kademe_button_show(self.max_kademe)
        self.trafoTipi=""
        self.baglanti=""
        self.Kf=0
        self.Ku=0
        self.Um  =0 
        self.Lg_man=0
        self.klemens_a=0
        self.klemens_b=0
        self.ayak_a=0
        self.akim_m = 0.0
        self.enduktans_m = 0.0
        self.sacTipi=0
        self.nuveBosluk = 0
        self.sacYogunluk=0.0
    def veri_kumesi(self):
        self.group_list_items = [self.ui.doubleSpinBox_akim1, self.ui.doubleSpinBox_akim2,
                                      self.ui.doubleSpinBox_cap1,
                                      self.ui.doubleSpinBox_cap2, self.ui.doubleSpinBox_sipir1,
                                      self.ui.doubleSpinBox_kesit1,
                                      self.ui.doubleSpinBox_sipir2, self.ui.doubleSpinBox_voltaj,
                                      "self.ui.comboBox_folyotel",
                                      "self.ui.comboBox_folyotel", "self.ui.comboBox_karetel",  # 10
                                      self.ui.comboBox_teltipi,
                                      self.ui.doubleSpinBox_folyotel11, self.ui.doubleSpinBox_folyotel12,
                                      self.ui.doubleSpinBox_folyotel21, self.ui.doubleSpinBox_folyotel22,
                                      self.ui.doubleSpinBox_folyotel31, self.ui.doubleSpinBox_folyotel32,
                                      self.ui.doubleSpinBox_folyotel41, self.ui.doubleSpinBox_folyotel42,
                                      self.ui.doubleSpinBox_kapton1, self.ui.doubleSpinBox_kapton2,
                                      self.ui.doubleSpinBox_kapton3, self.ui.doubleSpinBox_kapton4,
                                      self.ui.doubleSpinBox_karetel11, self.ui.doubleSpinBox_karetel12,
                                      self.ui.doubleSpinBox_karetel21, self.ui.doubleSpinBox_karetel22,
                                      self.ui.doubleSpinBox_karetel31, self.ui.doubleSpinBox_karetel32,
                                      self.ui.doubleSpinBox_karetel41, self.ui.doubleSpinBox_karetel42,
                                      # 31
                                      "self.ui.comboBox_telkademe", self.ui.lineEdit_kademeadi,
                                      self.ui.doubleSpinBox_kesit2,
                                      self.ui.doubleSpinBox_tel_en, self.ui.doubleSpinBox_tel_yuk,
                                      self.ui.doubleSpinBox_spirkat,  # 37
                                      self.ui.doubleSpinBox_kat, self.ui.doubleSpinBox_katbosluk,
                                      self.ui.doubleSpinBox_tel_uzunluk,
                                      self.ui.doubleSpinBox_tel_agirlik,
                                      self.ui.doubleSpinBox_sarim_yukseklik,
                                      self.ui.doubleSpinBox_sonkat_spir, self.ui.checkBox_check_spir_man,
                                      "self.ui.pushButton_h1_p_buton_21", "self.ui.pushButton_karetel",
                                      "self.ui.pushButton_folyotel", "self.ui.pushButton_kapton",
                                      self.ui.checkBox_check_spir_man,
                                      self.ui.label_kesit_ok, self.ui.label_kesit_error,
                                      self.ui.label_akim_ok, self.ui.label_akim_error,
                                      self.ui.doubleSpinBox_mancap_1,  # 54
                                      self.ui.doubleSpinBox_mancap_2, self.ui.doubleSpinBox_mancap_3,
                                      self.ui.doubleSpinBox_mancap_4,
                                      self.ui.lineEdit_mlz_tel_1, self.ui.lineEdit_mlz_tel_2,
                                      self.ui.lineEdit_mlz_tel_3, self.ui.lineEdit_mlz_tel_4,
                                      self.ui.lineEdit_mlz_karetel_1, self.ui.lineEdit_mlz_karetel_2,  # 63
                                      self.ui.lineEdit_mlz_karetel_3, self.ui.lineEdit_mlz_karetel_4,
                                      self.ui.lineEdit_mlz_folyotel_1, self.ui.lineEdit_mlz_folyotel_2,
                                      self.ui.lineEdit_mlz_folyotel_3, self.ui.lineEdit_mlz_folyotel_4,
                                      self.ui.lineEdit_mlz_kapton_1, self.ui.lineEdit_mlz_kapton_2,
                                      self.ui.lineEdit_mlz_kapton_3, self.ui.lineEdit_mlz_kapton_4,  # 73
                                     self.ui.groupBox_gb_check_tel_1,
                                     self.ui.groupBox_gb_check_tel_2,
                                     self.ui.groupBox_gb_check_tel_3,
                                     self.ui.groupBox_gb_check_tel_4,
                                     self.ui.groupBox_gb_check_karetel_1,
                                     self.ui.groupBox_gb_check_karetel_2,
                                     self.ui.groupBox_gb_check_karetel_3,
                                     self.ui.groupBox_gb_check_karetel_4,
                                     self.ui.groupBox_gb_check_folyotel_1,
                                     self.ui.groupBox_gb_check_folyotel_2,
                                     self.ui.groupBox_gb_check_folyotel_3,
                                     self.ui.groupBox_gb_check_folyotel_4,
                                     self.ui.groupBox_gb_check_kapton_1,
                                     self.ui.groupBox_gb_check_kapton_2,
                                     self.ui.groupBox_gb_check_kapton_3,
                                     self.ui.groupBox_gb_check_kapton_4,
                                     self.ui.doubleSpinBox_tel_agirlik_1,
                                     self.ui.doubleSpinBox_tel_agirlik_2,
                                     self.ui.doubleSpinBox_tel_agirlik_3,
                                     self.ui.doubleSpinBox_tel_agirlik_4,
                                     self.ui.doubleSpinBox_karetel_agirlik_1,
                                     self.ui.doubleSpinBox_karetel_agirlik_2,
                                     self.ui.doubleSpinBox_karetel_agirlik_3,
                                     self.ui.doubleSpinBox_karetel_agirlik_4,
                                     self.ui.doubleSpinBox_folyo_agirlik_1,
                                     self.ui.doubleSpinBox_folyo_agirlik_2,
                                     self.ui.doubleSpinBox_folyo_agirlik_3,
                                     self.ui.doubleSpinBox_folyo_agirlik_4,
                                     self.ui.doubleSpinBox_kapton_agirlik_1,
                                     self.ui.doubleSpinBox_kapton_agirlik_2,
                                     self.ui.doubleSpinBox_kapton_agirlik_3,
                                     self.ui.doubleSpinBox_kapton_agirlik_4,
                                      ]
        
        self.group_list_kademe_1 = vt.kademe.copy()
        self.group_list_kademe_2 = vt.kademe.copy()
        self.group_list_kademe_3 = vt.kademe.copy()
        self.group_list_kademe_4 = vt.kademe.copy()
        self.group_list_kademe_5 = vt.kademe.copy()
        self.group_list_kademe_6 = vt.kademe.copy()
        self.group_list_kademe_7 = vt.kademe.copy()
        self.group_list_kademe_8 = vt.kademe.copy()
        self.group_list_kademe_9 = vt.kademe.copy()
        self.group_list_kademe_10 = vt.kademe.copy()
        self.group_name_list_kademe = [self.group_list_kademe_1, self.group_list_kademe_2,
                                         self.group_list_kademe_3,
                                         self.group_list_kademe_4, self.group_list_kademe_5,
                                         self.group_list_kademe_6, self.group_list_kademe_7,
                                         self.group_list_kademe_8, self.group_list_kademe_9,
                                         self.group_list_kademe_10]

    def test(self):
        self.save_selected_kademe(kademe=int(self.ui.doubleSpinBox_kademe_no.value()))
    def object_signals(self):
        self.ui.doubleSpinBox_gauss.valueChanged.connect(self.update_gauss )
        self.ui.pushButton_kad_1.clicked.connect(self.kademe_data_show)
        self.ui.pushButton_kad_2.clicked.connect(self.kademe_data_show)
        self.ui.pushButton_kad_3.clicked.connect(self.kademe_data_show)
        self.ui.pushButton_kad_4.clicked.connect(self.kademe_data_show)
        self.ui.pushButton_kad_5.clicked.connect(self.kademe_data_show)
        self.ui.pushButton_kad_6.clicked.connect(self.kademe_data_show)
        self.ui.pushButton_kad_7.clicked.connect(self.kademe_data_show)
        self.ui.pushButton_kad_8.clicked.connect(self.kademe_data_show)
        self.ui.pushButton_kad_9.clicked.connect(self.kademe_data_show)
        self.ui.pushButton_kad_10.clicked.connect(self.kademe_data_show)
        for item in self.group_list_items:

            if type(item) == str:
                continue
            elif  item.metaObject().className() == "QGroupBox":
                item.clicked.connect(self.select_tel_gb)
        #self.ui.doubleSpinBox_v_sk_1.valueChanged.connect(lambda x:self.save_selected_kademe(kademe=int(self.ui.doubleSpinBox_kademe_no.value())))
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.test)
        self.timer.start(1000)
        self.ui.pushButton_kaydet.clicked.connect(lambda x:self.save_selected_kademe(kademe=int(self.ui.doubleSpinBox_kademe_no.value())))
        self.ui.pushButton_kaydet.clicked.connect(lambda x:self.timer.stop())
        self.ui.pushButton_kaydet_2.clicked.connect(lambda x:self.timer.stop())
        self.ui.pushButton_kaydet_2.clicked.connect(self.close)
    def update_gauss(self):
        self.gauss=self.ui.doubleSpinBox_gauss.value()
    def object_multi_connect(self, object, arg):
        if type(object) == str:
            return False
        elif object.metaObject().className() == "QDoubleSpinBox":
            return object.valueChanged.connect(arg)
        elif object.metaObject().className() == "QComboBox":
            return object.currentTextChanged.connect(arg)
        elif object.metaObject().className() == "QLineEdit":
            return object.textChanged.connect(arg)
        elif object.metaObject().className() == "QPushButton":
            return object.clicked.connect(arg)
        elif object.metaObject().className() == "QCheckBox":
            return object.stateChanged.connect(arg)
        elif object.metaObject().className() == "QLabel":
            return False
        elif object.metaObject().className() == "QGroupBox":
            return object.clicked.connect(self.select_tel_gb)
    def kademe_button_show(self,max_kademe):
        for i in range(0,10):
            object = self.findChild(QPushButton, f"pushButton_kad_{i + 1}")
            if i<max_kademe:
                 object.setEnabled(True)
            else:
                object.setEnabled(False)
    def kademe_data_show(self):
        sender = self.sender()
        old_kademe = int(self.ui.doubleSpinBox_kademe_no.value())
        self.ui.doubleSpinBox_kademe_no.setValue(
            int(sender.objectName().split("_")[len(sender.objectName().split("_")) - 1]) - 1)
        self.save_selected_kademe(old_kademe)
        #self.clear_window_items()
        self.load_selected_kademe(int(sender.objectName().split("_")[len(sender.objectName().split("_")) - 1]) - 1)

    def load_allkademe_values(self,gl):
        try:
            for i in range (0,len(gl)):

                for key in vt.kademe.keys():
                    if key in self.group_name_list_kademe[i].keys():
                        self.group_name_list_kademe[i][key]=gl[i][key]
        except Exception as err:
            print("kademe yukleme hatası :",err)
        return True
    def save_kademe_values(self,gl):
        for i in range (0,10):

            for key in vt.kademe.keys():
                gl[i][key]=self.group_name_list_kademe[i][key]
    def load_selected_kademe(self,kademe):
        self.ui.doubleSpinBox_gauss.setValue(self.gauss)
        self.ui.doubleSpinBox_voltaj.setValue(self.group_name_list_kademe[kademe]["voltaj"])
        self.ui.doubleSpinBox_akim1.setValue(self.group_name_list_kademe[kademe]["akim1"])
        self.ui.doubleSpinBox_akim2.setValue( self.group_name_list_kademe[kademe]["akim2"])
        self.ui.doubleSpinBox_cap1.setValue( self.group_name_list_kademe[kademe]["cap1"])
        self.ui.doubleSpinBox_cap2.setValue( self.group_name_list_kademe[kademe]["cap2"])
        self.ui.doubleSpinBox_sipir1.setValue( self.group_name_list_kademe[kademe]["spir1"])
        self.ui.doubleSpinBox_kesit1.setValue( self.group_name_list_kademe[kademe]["kesit1"])
        self.ui.doubleSpinBox_sipir2.setValue( self.group_name_list_kademe[kademe]["spir2"])

        self.ui.comboBox_teltipi.setCurrentText(self.group_name_list_kademe[kademe]["teltipi"])
        self.ui.doubleSpinBox_folyotel11.setValue( self.group_name_list_kademe[kademe]["folyotel11"])
        self.ui.doubleSpinBox_folyotel12.setValue( self.group_name_list_kademe[kademe]["folyotel12"])
        self.ui.doubleSpinBox_folyotel21.setValue( self.group_name_list_kademe[kademe]["folyotel21"])
        self.ui.doubleSpinBox_folyotel22.setValue( self.group_name_list_kademe[kademe]["folyotel22"])
        self.ui.doubleSpinBox_folyotel31.setValue( self.group_name_list_kademe[kademe]["folyotel31"])
        self.ui.doubleSpinBox_folyotel32.setValue( self.group_name_list_kademe[kademe]["folyotel32"])
        self.ui.doubleSpinBox_folyotel41.setValue( self.group_name_list_kademe[kademe]["folyotel41"])
        self.ui.doubleSpinBox_folyotel42.setValue( self.group_name_list_kademe[kademe]["folyotel42"])
        self.ui.doubleSpinBox_kapton1.setValue( self.group_name_list_kademe[kademe]["kapton1"])
        self.ui.doubleSpinBox_kapton2.setValue( self.group_name_list_kademe[kademe]["kapton2"])
        self.ui.doubleSpinBox_kapton3.setValue( self.group_name_list_kademe[kademe]["kapton3"])
        self.ui.doubleSpinBox_kapton4.setValue( self.group_name_list_kademe[kademe]["kapton4"])
        self.ui.doubleSpinBox_karetel11.setValue( self.group_name_list_kademe[kademe]["karetel11"])
        self.ui.doubleSpinBox_karetel12.setValue( self.group_name_list_kademe[kademe]["karetel12"])
        self.ui.doubleSpinBox_karetel21.setValue( self.group_name_list_kademe[kademe]["karetel21"] )
        self.ui.doubleSpinBox_karetel22.setValue( self.group_name_list_kademe[kademe]["karetel22"])
        self.ui.doubleSpinBox_karetel31.setValue( self.group_name_list_kademe[kademe]["karetel31"] )
        self.ui.doubleSpinBox_karetel32.setValue( self.group_name_list_kademe[kademe]["karetel32"])
        self.ui.doubleSpinBox_karetel41.setValue( self.group_name_list_kademe[kademe]["karetel41"])
        self.ui.doubleSpinBox_karetel42.setValue( self.group_name_list_kademe[kademe]["karetel42"])
        self.ui.lineEdit_kademeadi.setText(self.group_name_list_kademe[kademe]["kademeadi"])
        self.ui.doubleSpinBox_kesit2.setValue( self.group_name_list_kademe[kademe]["kesit2"])
        self.ui.doubleSpinBox_tel_en.setValue( self.group_name_list_kademe[kademe]["tel_en"])
        self.ui.doubleSpinBox_tel_yuk.setValue( self.group_name_list_kademe[kademe]["tel_yuk"])
        self.ui.doubleSpinBox_spirkat.setValue( self.group_name_list_kademe[kademe]["spirkat"])
        self.ui.doubleSpinBox_kat.setValue( self.group_name_list_kademe[kademe]["kat"])
        self.ui.doubleSpinBox_katbosluk.setValue( self.group_name_list_kademe[kademe]["katbosluk"])
        self.ui.doubleSpinBox_tel_uzunluk.setValue( self.group_name_list_kademe[kademe]["tel_uzunluk"])
        self.ui.doubleSpinBox_tel_agirlik.setValue( self.group_name_list_kademe[kademe]["tel_agirlik"])
        self.ui.doubleSpinBox_sarim_yukseklik.setValue( self.group_name_list_kademe[kademe]["sarim_yukseklik"])
        self.ui.doubleSpinBox_sonkat_spir.setValue( self.group_name_list_kademe[kademe]["sonkat_spir"])
        self.ui.checkBox_check_spir_man.setChecked(self.group_name_list_kademe[kademe]["check_spir_man"])
        self.ui.doubleSpinBox_sipir2.setEnabled(self.group_name_list_kademe[kademe]["check_spir_man"])
        self.ui.label_kesit_ok.setVisible(self.group_name_list_kademe[kademe]["kesit_ok"])
        self.ui.label_kesit_error.setVisible( self.group_name_list_kademe[kademe]["kesit_error"])
        self.ui.label_akim_ok.setVisible( self.group_name_list_kademe[kademe]["akim_ok"])
        self.ui.label_akim_error.setVisible( self.group_name_list_kademe[kademe]["akim_error"])
        self.ui.doubleSpinBox_mancap_1.setValue( self.group_name_list_kademe[kademe]["mancap_1"] ) # 54
        self.ui.doubleSpinBox_mancap_2.setValue( self.group_name_list_kademe[kademe]["mancap_2"])
        self.ui.doubleSpinBox_mancap_3.setValue( self.group_name_list_kademe[kademe]["mancap_3"])
        self.ui.doubleSpinBox_mancap_4.setValue( self.group_name_list_kademe[kademe]["mancap_4"])
        self.ui.lineEdit_mlz_tel_1.setText(  self.group_name_list_kademe[kademe]["mlz_tel_1"])
        self.ui.lineEdit_mlz_tel_2.setText(  self.group_name_list_kademe[kademe]["mlz_tel_2"])
        self.ui.lineEdit_mlz_tel_3.setText(  self.group_name_list_kademe[kademe]["mlz_tel_3"])
        self.ui.lineEdit_mlz_tel_4.setText( self.group_name_list_kademe[kademe]["mlz_tel_4"])
        self.ui.lineEdit_mlz_karetel_1.setText(  self.group_name_list_kademe[kademe]["mlz_karetel_1"])
        self.ui.lineEdit_mlz_karetel_2.setText(  self.group_name_list_kademe[kademe]["mlz_karetel_2"] ) # 63
        self.ui.lineEdit_mlz_karetel_3.setText(  self.group_name_list_kademe[kademe]["mlz_karetel_3"])
        self.ui.lineEdit_mlz_karetel_4.setText(  self.group_name_list_kademe[kademe]["mlz_karetel_4"])
        self.ui.lineEdit_mlz_folyotel_1.setText(  self.group_name_list_kademe[kademe]["mlz_folyotel_1"])
        self.ui.lineEdit_mlz_folyotel_2.setText(  self.group_name_list_kademe[kademe]["mlz_folyotel_2"])
        self.ui.lineEdit_mlz_folyotel_3.setText(  self.group_name_list_kademe[kademe]["mlz_folyotel_3"])
        self.ui.lineEdit_mlz_folyotel_4.setText(  self.group_name_list_kademe[kademe]["mlz_folyotel_4"])
        self.ui.lineEdit_mlz_kapton_1.setText(  self.group_name_list_kademe[kademe]["mlz_kapton_1"])
        self.ui.lineEdit_mlz_kapton_2.setText(  self.group_name_list_kademe[kademe]["mlz_kapton_2"])
        self.ui.lineEdit_mlz_kapton_3.setText(  self.group_name_list_kademe[kademe]["mlz_kapton_3"])
        self.ui.lineEdit_mlz_kapton_4.setText(  self.group_name_list_kademe[kademe]["mlz_kapton_4"])
        self.ui.groupBox_gb_check_tel_1.setChecked(self.group_name_list_kademe[kademe]["gb_check_tel_1"])
        self.ui.groupBox_gb_check_tel_2.setChecked(self.group_name_list_kademe[kademe]["gb_check_tel_2"])
        self.ui.groupBox_gb_check_tel_3.setChecked(self.group_name_list_kademe[kademe]["gb_check_tel_3"])
        self.ui.groupBox_gb_check_tel_4.setChecked(self.group_name_list_kademe[kademe]["gb_check_tel_4"])
        self.ui.groupBox_gb_check_karetel_1.setChecked(self.group_name_list_kademe[kademe]["gb_check_karetel_1"])
        self.ui.groupBox_gb_check_karetel_2.setChecked(self.group_name_list_kademe[kademe]["gb_check_karetel_2"])
        self.ui.groupBox_gb_check_karetel_3.setChecked(self.group_name_list_kademe[kademe]["gb_check_karetel_3"])
        self.ui.groupBox_gb_check_karetel_4.setChecked(self.group_name_list_kademe[kademe]["gb_check_karetel_4"])
        self.ui.groupBox_gb_check_folyotel_1.setChecked(self.group_name_list_kademe[kademe]["gb_check_folyotel_1"])
        self.ui.groupBox_gb_check_folyotel_2.setChecked(self.group_name_list_kademe[kademe]["gb_check_folyotel_2"])
        self.ui.groupBox_gb_check_folyotel_3.setChecked(self.group_name_list_kademe[kademe]["gb_check_folyotel_3"])
        self.ui.groupBox_gb_check_folyotel_4.setChecked(self.group_name_list_kademe[kademe]["gb_check_folyotel_4"])
        self.ui.groupBox_gb_check_kapton_1.setChecked(self.group_name_list_kademe[kademe]["gb_check_kapton_1"])
        self.ui.groupBox_gb_check_kapton_2.setChecked(self.group_name_list_kademe[kademe]["gb_check_kapton_2"])
        self.ui.groupBox_gb_check_kapton_3.setChecked(self.group_name_list_kademe[kademe]["gb_check_kapton_3"])
        self.ui.groupBox_gb_check_kapton_4.setChecked(self.group_name_list_kademe[kademe]["gb_check_kapton_4"])
        self.ui.doubleSpinBox_tel_agirlik_1.setValue(self.group_name_list_kademe[kademe]["agr_tel_1"])
        self.ui.doubleSpinBox_tel_agirlik_2.setValue(self.group_name_list_kademe[kademe]["agr_tel_2"])
        self.ui.doubleSpinBox_tel_agirlik_3.setValue(self.group_name_list_kademe[kademe]["agr_tel_3"])
        self.ui.doubleSpinBox_tel_agirlik_4.setValue(self.group_name_list_kademe[kademe]["agr_tel_4"])
        self.ui.doubleSpinBox_karetel_agirlik_1.setValue(self.group_name_list_kademe[kademe]["agr_karetel_1"])
        self.ui.doubleSpinBox_karetel_agirlik_2.setValue(self.group_name_list_kademe[kademe]["agr_karetel_2"])
        self.ui.doubleSpinBox_karetel_agirlik_3.setValue(self.group_name_list_kademe[kademe]["agr_karetel_3"])
        self.ui.doubleSpinBox_karetel_agirlik_4.setValue(self.group_name_list_kademe[kademe]["agr_karetel_4"])
        self.ui.doubleSpinBox_folyo_agirlik_1.setValue(self.group_name_list_kademe[kademe]["agr_folyo_1"])
        self.ui.doubleSpinBox_folyo_agirlik_2.setValue(self.group_name_list_kademe[kademe]["agr_folyo_2"])
        self.ui.doubleSpinBox_folyo_agirlik_3.setValue(self.group_name_list_kademe[kademe]["agr_folyo_3"])
        self.ui.doubleSpinBox_folyo_agirlik_4.setValue(self.group_name_list_kademe[kademe]["agr_folyo_4"])
        self.ui.doubleSpinBox_kapton_agirlik_1.setValue(self.group_name_list_kademe[kademe]["agr_kapton_1"])
        self.ui.doubleSpinBox_kapton_agirlik_2.setValue(self.group_name_list_kademe[kademe]["agr_kapton_2"])
        self.ui.doubleSpinBox_kapton_agirlik_3.setValue(self.group_name_list_kademe[kademe]["agr_kapton_3"])
        self.ui.doubleSpinBox_kapton_agirlik_4.setValue(self.group_name_list_kademe[kademe]["agr_kapton_4"])
        self.ui.doubleSpinBox_kademe_no.setValue(kademe)
    def save_selected_kademe(self,kademe):
        
        self.group_name_list_kademe[kademe]["voltaj"] = self.ui.doubleSpinBox_voltaj.value()
        self.group_name_list_kademe[kademe]["akim1"] = self.ui.doubleSpinBox_akim1.value()
        self.group_name_list_kademe[kademe]["akim2"] =self.ui.doubleSpinBox_akim2.value()
        self.group_name_list_kademe[kademe]["cap1"] =self.ui.doubleSpinBox_cap1 .value()
        self.group_name_list_kademe[kademe]["cap2"] =self.ui.doubleSpinBox_cap2.value()
        self.group_name_list_kademe[kademe]["spir1"] = self.ui.doubleSpinBox_sipir1.value()
        self.group_name_list_kademe[kademe]["kesit1"] =self.ui.doubleSpinBox_kesit1.value()
        self.group_name_list_kademe[kademe]["spir2"] =self.ui.doubleSpinBox_sipir2.value()

        self.group_name_list_kademe[kademe]["teltipi"] =self.ui.comboBox_teltipi.currentText()
        self.group_name_list_kademe[kademe]["folyotel11"] =self.ui.doubleSpinBox_folyotel11.value()
        self.group_name_list_kademe[kademe]["folyotel12"] =self.ui.doubleSpinBox_folyotel12.value()
        self.group_name_list_kademe[kademe]["folyotel21"] =self.ui.doubleSpinBox_folyotel21.value()
        self.group_name_list_kademe[kademe]["folyotel22"] =self.ui.doubleSpinBox_folyotel22.value()
        self.group_name_list_kademe[kademe]["folyotel31"] =self.ui.doubleSpinBox_folyotel31.value()
        self.group_name_list_kademe[kademe]["folyotel32"] =self.ui.doubleSpinBox_folyotel32.value()
        self.group_name_list_kademe[kademe]["folyotel41"] =self.ui.doubleSpinBox_folyotel41.value()
        self.group_name_list_kademe[kademe]["folyotel42"] =self.ui.doubleSpinBox_folyotel42.value()
        self.group_name_list_kademe[kademe]["kapton1"] = self.ui.doubleSpinBox_kapton1.value()
        self.group_name_list_kademe[kademe]["kapton2"] =self.ui.doubleSpinBox_kapton2.value()
        self.group_name_list_kademe[kademe]["kapton3"] =self.ui.doubleSpinBox_kapton3.value()
        self.group_name_list_kademe[kademe]["kapton4"] = self.ui.doubleSpinBox_kapton4.value()
        self.group_name_list_kademe[kademe]["karetel11"] =self.ui.doubleSpinBox_karetel11.value()
        self.group_name_list_kademe[kademe]["karetel12"] =self.ui.doubleSpinBox_karetel12.value()
        self.group_name_list_kademe[kademe]["karetel21"] =self.ui.doubleSpinBox_karetel21.value()
        self.group_name_list_kademe[kademe]["karetel22"] =self.ui.doubleSpinBox_karetel22.value()
        self.group_name_list_kademe[kademe]["karetel31"] =self.ui.doubleSpinBox_karetel31.value()
        self.group_name_list_kademe[kademe]["karetel32"] =self.ui.doubleSpinBox_karetel32.value()
        self.group_name_list_kademe[kademe]["karetel41"] =self.ui.doubleSpinBox_karetel41.value()
        self.group_name_list_kademe[kademe]["karetel42"] =self.ui.doubleSpinBox_karetel42.value()
        self.group_name_list_kademe[kademe]["kademeadi"] =self.ui.lineEdit_kademeadi.text()
        self.group_name_list_kademe[kademe]["kesit2"] = self.ui.doubleSpinBox_kesit2.value()
        self.group_name_list_kademe[kademe]["tel_en"] =self.ui.doubleSpinBox_tel_en.value()
        self.group_name_list_kademe[kademe]["tel_yuk"] =self.ui.doubleSpinBox_tel_yuk.value()
        self.group_name_list_kademe[kademe]["spirkat"] =self.ui.doubleSpinBox_spirkat.value()
        self.group_name_list_kademe[kademe]["kat"] =self.ui.doubleSpinBox_kat.value()
        self.group_name_list_kademe[kademe]["katbosluk"] =self.ui.doubleSpinBox_katbosluk.value()
        self.group_name_list_kademe[kademe]["tel_uzunluk"] =self.ui.doubleSpinBox_tel_uzunluk.value()
        self.group_name_list_kademe[kademe]["tel_agirlik"] =self.ui.doubleSpinBox_tel_agirlik.value()
        self.group_name_list_kademe[kademe]["sarim_yukseklik"] =self.ui.doubleSpinBox_sarim_yukseklik.value()
        self.group_name_list_kademe[kademe]["sonkat_spir"] =self.ui.doubleSpinBox_sonkat_spir.value()
        self.group_name_list_kademe[kademe]["check_spir_man"] =self.ui.checkBox_check_spir_man.isChecked()

        self.group_name_list_kademe[kademe]["kesit_ok"] =self.ui.label_kesit_ok.isVisible()
        self.group_name_list_kademe[kademe]["kesit_error"] =self.ui.label_kesit_error.isVisible()
        self.group_name_list_kademe[kademe]["akim_ok"] =self.ui.label_akim_ok.isVisible()
        self.group_name_list_kademe[kademe]["akim_error"] =self.ui.label_akim_error.isVisible()
        self.group_name_list_kademe[kademe]["mancap_1"] =self.ui.doubleSpinBox_mancap_1.value()
        self.group_name_list_kademe[kademe]["mancap_2"] = self.ui.doubleSpinBox_mancap_2.value()
        self.group_name_list_kademe[kademe]["mancap_3"] = self.ui.doubleSpinBox_mancap_3.value()
        self.group_name_list_kademe[kademe]["mancap_4"] =self.ui.doubleSpinBox_mancap_4.value()
        self.group_name_list_kademe[kademe]["mlz_tel_1"] =self.ui.lineEdit_mlz_tel_1.text()
        self.group_name_list_kademe[kademe]["mlz_tel_2"] =self.ui.lineEdit_mlz_tel_2.text()
        self.group_name_list_kademe[kademe]["mlz_tel_3"] = self.ui.lineEdit_mlz_tel_3.text()
        self.group_name_list_kademe[kademe]["mlz_tel_4"] =self.ui.lineEdit_mlz_tel_4.text()
        self.group_name_list_kademe[kademe]["mlz_karetel_1"] =self.ui.lineEdit_mlz_karetel_1.text()
        self.group_name_list_kademe[kademe]["mlz_karetel_2"] =self.ui.lineEdit_mlz_karetel_2.text()
        self.group_name_list_kademe[kademe]["mlz_karetel_3"] =self.ui.lineEdit_mlz_karetel_3.text()
        self.group_name_list_kademe[kademe]["mlz_karetel_4"] =self.ui.lineEdit_mlz_karetel_4.text()
        self.group_name_list_kademe[kademe]["mlz_folyotel_1"] =self.ui.lineEdit_mlz_folyotel_1.text()
        self.group_name_list_kademe[kademe]["mlz_folyotel_2"] =self.ui.lineEdit_mlz_folyotel_2.text()
        self.group_name_list_kademe[kademe]["mlz_folyotel_3"] =self.ui.lineEdit_mlz_folyotel_3.text()
        self.group_name_list_kademe[kademe]["mlz_folyotel_4"] =self.ui.lineEdit_mlz_folyotel_4.text()
        self.group_name_list_kademe[kademe]["mlz_kapton_1"] =self.ui.lineEdit_mlz_kapton_1.text()
        self.group_name_list_kademe[kademe]["mlz_kapton_2"] =self.ui.lineEdit_mlz_kapton_2.text()
        self.group_name_list_kademe[kademe]["mlz_kapton_3"] =self.ui.lineEdit_mlz_kapton_3.text()
        self.group_name_list_kademe[kademe]["mlz_kapton_4"] =self.ui.lineEdit_mlz_kapton_4.text()
        self.group_name_list_kademe[kademe]["gb_check_tel_1"]=self.ui.groupBox_gb_check_tel_1.isChecked()
        self.group_name_list_kademe[kademe]["gb_check_tel_2"] = self.ui.groupBox_gb_check_tel_2.isChecked()
        self.group_name_list_kademe[kademe]["gb_check_tel_3"] = self.ui.groupBox_gb_check_tel_3.isChecked()
        self.group_name_list_kademe[kademe]["gb_check_tel_4"] = self.ui.groupBox_gb_check_tel_4.isChecked()


        self.group_name_list_kademe[kademe]["gb_check_karetel_1"]=self.ui.groupBox_gb_check_karetel_1.isChecked()
        self.group_name_list_kademe[kademe]["gb_check_karetel_2"]=self.ui.groupBox_gb_check_karetel_2.isChecked()
        self.group_name_list_kademe[kademe]["gb_check_karetel_3"] = self.ui.groupBox_gb_check_karetel_3.isChecked()
        self.group_name_list_kademe[kademe]["gb_check_karetel_4"] = self.ui.groupBox_gb_check_karetel_4.isChecked()
        self.group_name_list_kademe[kademe]["gb_check_folyotel_1"]=self.ui.groupBox_gb_check_folyotel_1.isChecked()
        self.group_name_list_kademe[kademe]["gb_check_folyotel_2"]=self.ui.groupBox_gb_check_folyotel_2.isChecked()
        self.group_name_list_kademe[kademe]["gb_check_folyotel_3"] = self.ui.groupBox_gb_check_folyotel_3.isChecked()
        self.group_name_list_kademe[kademe]["gb_check_folyotel_4"] = self.ui.groupBox_gb_check_folyotel_4.isChecked()

        self.group_name_list_kademe[kademe]["gb_check_kapton_1"]=self.ui.groupBox_gb_check_kapton_1.isChecked()
        self.group_name_list_kademe[kademe]["gb_check_kapton_2"]=self.ui.groupBox_gb_check_kapton_2.isChecked()
        self.group_name_list_kademe[kademe]["gb_check_kapton_3"] = self.ui.groupBox_gb_check_kapton_3.isChecked()
        self.group_name_list_kademe[kademe]["gb_check_kapton_4"] = self.ui.groupBox_gb_check_kapton_4.isChecked()

        self.group_name_list_kademe[kademe]["agr_tel_1"] = self.ui.doubleSpinBox_tel_agirlik_1.value()
        self.group_name_list_kademe[kademe]["agr_tel_2"] = self.ui.doubleSpinBox_tel_agirlik_2.value()
        self.group_name_list_kademe[kademe]["agr_tel_3"] = self.ui.doubleSpinBox_tel_agirlik_3.value()
        self.group_name_list_kademe[kademe]["agr_tel_4"] = self.ui.doubleSpinBox_tel_agirlik_4.value()
        self.group_name_list_kademe[kademe]["agr_karetel_1"] = self.ui.doubleSpinBox_karetel_agirlik_1.value()
        self.group_name_list_kademe[kademe]["agr_karetel_2"] = self.ui.doubleSpinBox_karetel_agirlik_2.value()
        self.group_name_list_kademe[kademe]["agr_karetel_3"] = self.ui.doubleSpinBox_karetel_agirlik_3.value()
        self.group_name_list_kademe[kademe]["agr_karetel_4"] = self.ui.doubleSpinBox_karetel_agirlik_4.value()
        self.group_name_list_kademe[kademe]["agr_folyo_1"] = self.ui.doubleSpinBox_folyo_agirlik_1.value()
        self.group_name_list_kademe[kademe]["agr_folyo_2"] = self.ui.doubleSpinBox_folyo_agirlik_2.value()
        self.group_name_list_kademe[kademe]["agr_folyo_3"] = self.ui.doubleSpinBox_folyo_agirlik_3.value()
        self.group_name_list_kademe[kademe]["agr_folyo_4"] = self.ui.doubleSpinBox_folyo_agirlik_4.value()
        self.group_name_list_kademe[kademe]["agr_kapton_1"] = self.ui.doubleSpinBox_kapton_agirlik_1.value()
        self.group_name_list_kademe[kademe]["agr_kapton_2"] = self.ui.doubleSpinBox_kapton_agirlik_2.value()
        self.group_name_list_kademe[kademe]["agr_kapton_3"] = self.ui.doubleSpinBox_kapton_agirlik_3.value()
        self.group_name_list_kademe[kademe]["agr_kapton_4"] = self.ui.doubleSpinBox_kapton_agirlik_4.value()
        self.hesap_1_gnl(gl=self.group_name_list_kademe, guc=self.guc, frekans=self.frekans, gauss=self.gauss,
                         karkas_en=self.karkas_en, karkas_boy=self.karkas_boy, karkas_yuk=self.karkas_yukseklik,
                         verim=self.karkas_verim, sarim=self.sarim, kademe=int(self.ui.doubleSpinBox_kademe_no.value()))

    def clear_window_items(self):

        self.ui.doubleSpinBox_voltaj.setValue(0)
        self.ui.doubleSpinBox_akim1.setValue(0)
        self.ui.doubleSpinBox_akim2.setValue( 0)
        self.ui.doubleSpinBox_cap1.setValue( 0)
        self.ui.doubleSpinBox_cap2.setValue( 0)
        self.ui.doubleSpinBox_sipir1.setValue( 0)
        self.ui.doubleSpinBox_kesit1.setValue( 0)
        self.ui.doubleSpinBox_sipir2.setValue( 0)

        self.ui.comboBox_teltipi.setCurrentText("AI")
        self.ui.doubleSpinBox_folyotel11.setValue( 0)
        self.ui.doubleSpinBox_folyotel12.setValue( 0)
        self.ui.doubleSpinBox_folyotel21.setValue( 0)
        self.ui.doubleSpinBox_folyotel22.setValue( 0)
        self.ui.doubleSpinBox_folyotel31.setValue( 0)
        self.ui.doubleSpinBox_folyotel32.setValue( 0)
        self.ui.doubleSpinBox_folyotel41.setValue( 0)
        self.ui.doubleSpinBox_folyotel42.setValue( 0)
        self.ui.doubleSpinBox_kapton1.setValue( 0)
        self.ui.doubleSpinBox_kapton2.setValue(0)
        self.ui.doubleSpinBox_kapton3.setValue( 0)
        self.ui.doubleSpinBox_kapton4.setValue( 0)
        self.ui.doubleSpinBox_karetel11.setValue( 0)
        self.ui.doubleSpinBox_karetel12.setValue( 0)
        self.ui.doubleSpinBox_karetel21.setValue(0 )
        self.ui.doubleSpinBox_karetel22.setValue( 0)
        self.ui.doubleSpinBox_karetel31.setValue(0 )
        self.ui.doubleSpinBox_karetel32.setValue(0)
        self.ui.doubleSpinBox_karetel41.setValue( 0)
        self.ui.doubleSpinBox_karetel42.setValue( 0)
        self.ui.lineEdit_kademeadi.setText("")
        self.ui.doubleSpinBox_kesit2.setValue( 0)
        self.ui.doubleSpinBox_tel_en.setValue(0)
        self.ui.doubleSpinBox_tel_yuk.setValue(0)
        self.ui.doubleSpinBox_spirkat.setValue(0)
        self.ui.doubleSpinBox_kat.setValue( 0)
        self.ui.doubleSpinBox_katbosluk.setValue(0)
        self.ui.doubleSpinBox_tel_uzunluk.setValue( 0)
        self.ui.doubleSpinBox_tel_agirlik.setValue( 0)
        self.ui.doubleSpinBox_sarim_yukseklik.setValue( 0)
        self.ui.doubleSpinBox_sonkat_spir.setValue(0)
        self.ui.checkBox_ckeck_sipir_man.setChecked(False)
        self.ui.label_kesit_ok.setVisible(False)
        self.ui.label_kesit_error.setVisible(True)
        self.ui.label_akim_ok.setVisible( False)
        self.ui.label_akim_error.setVisible( True)
        self.ui.doubleSpinBox_mancap_1.setValue( 0 ) # 54
        self.ui.doubleSpinBox_mancap_2.setValue(0)
        self.ui.doubleSpinBox_mancap_3.setValue( 0)
        self.ui.doubleSpinBox_mancap_4.setValue( 0)
        self.ui.lineEdit_mlz_tel_1.setText(   "")
        self.ui.lineEdit_mlz_tel_2.setText(  "")
        self.ui.lineEdit_mlz_tel_3.setText(  "")
        self.ui.lineEdit_mlz_tel_4.setText(  "")
        self.ui.lineEdit_mlz_karetel_1.setText(  "")
        self.ui.lineEdit_mlz_karetel_2.setText(   "" ) # 63
        self.ui.lineEdit_mlz_karetel_3.setText(   "")
        self.ui.lineEdit_mlz_karetel_4.setText(  "")
        self.ui.lineEdit_mlz_folyotel_1.setText(  "")
        self.ui.lineEdit_mlz_folyotel_2.setText(  "")
        self.ui.lineEdit_mlz_folyotel_3.setText(   "")
        self.ui.lineEdit_mlz_folyotel_4.setText(  "")
        self.ui.lineEdit_mlz_kapton_1.setText( "")
        self.ui.lineEdit_mlz_kapton_2.setText( "")
        self.ui.lineEdit_mlz_kapton_3.setText( "")
        self.ui.lineEdit_mlz_kapton_4.setText( "")
        self.ui.groupBox_gb_check_tel_1.setChecked(False)
        self.ui.groupBox_gb_check_tel_2.setChecked(False)
        self.ui.groupBox_gb_check_tel_3.setChecked(False)
        self.ui.groupBox_gb_check_tel_4.setChecked(False)
        self.ui.groupBox_gb_check_karetel_1.setChecked(False)
        self.ui.groupBox_gb_check_karetel_2.setChecked(False)
        self.ui.groupBox_gb_check_karetel_3.setChecked(False)
        self.ui.groupBox_gb_check_karetel_4.setChecked(False)
        self.ui.groupBox_gb_check_folyotel_1.setChecked(False)
        self.ui.groupBox_gb_check_folyotel_2.setChecked(False)
        self.ui.groupBox_gb_check_folyotel_3.setChecked(False)
        self.ui.groupBox_gb_check_folyotel_4.setChecked(False)
        self.ui.groupBox_gb_check_kapton_1.setChecked(False)
        self.ui.groupBox_gb_check_kapton_2.setChecked(False)
        self.ui.groupBox_gb_check_kapton_3.setChecked(False)
        self.ui.groupBox_gb_check_kapton_4.setChecked(False)
        self.ui.doubleSpinBox_tel_agirlik_1.setValue()
        self.ui.doubleSpinBox_tel_agirlik_2.setValue( 0)
        self.ui.doubleSpinBox_tel_agirlik_3.setValue( 0)
        self.ui.doubleSpinBox_tel_agirlik_4.vsetValue( 0)
        self.ui.doubleSpinBox_karetel_agirlik_1.setValue( 0)
        self.ui.doubleSpinBox_karetel_agirlik_2.setValue( 0)
        self.ui.doubleSpinBox_karetel_agirlik_3.setValue( 0)
        self.ui.doubleSpinBox_karetel_agirlik_4.setValue( 0)
        self.ui.doubleSpinBox_folyo_agirlik_1.setValue( 0)
        self.ui.doubleSpinBox_folyo_agirlik_2.setValue( 0)
        self.ui.doubleSpinBox_folyo_agirlik_3.setValue( 0)
        self.ui.doubleSpinBox_folyo_agirlik_4.setValue( 0)
        self.ui.doubleSpinBox_kapton_agirlik_1.setValue( 0)
        self.ui.doubleSpinBox_kapton_agirlik_2.setValue( 0)
        self.ui.doubleSpinBox_kapton_agirlik_3.setValue( 0)
        self.ui.doubleSpinBox_kapton_agirlik_4.setValue( 0)
    def select_tel_gb(self):
        sender = self.sender()
        kademe = int(self.ui.doubleSpinBox_kademe_no.value())
        gb_kademe = int(sender.objectName().split("_")[len(sender.objectName().split("_")) - 1])
        tel_type = sender.objectName().split("_")[len(sender.objectName().split("_")) - 2]
        if sender.isChecked():
            self.open_telsecim(gl=self.group_name_list_kademe, type=tel_type, index=kademe, kademe=gb_kademe)
        else:
            self.tel_deger_sil(gl=self.group_name_list_kademe, type=tel_type, index=kademe, kademe=gb_kademe)
    def tel_deger_al(self, gl, object, type, index=1, kademe=1):
        if type == "tel":

            if kademe == 1:
                self.ui.doubleSpinBox_mancap_1.setValue(object.ui.doubleSpinBox_tel_cap.value())
                self.ui.lineEdit_mlz_tel_1.setText(object.ui.lineEdit_tel_name.text())
            elif kademe == 2:
                self.ui.doubleSpinBox_mancap_2.setValue(object.ui.doubleSpinBox_tel_cap.value())
                self.ui.lineEdit_mlz_tel_2.setText(object.ui.lineEdit_tel_name.text())
            elif kademe == 3:
                self.ui.doubleSpinBox_mancap_3.setValue(object.ui.doubleSpinBox_tel_cap.value())
                self.ui.lineEdit_mlz_tel_3.setText(object.ui.lineEdit_tel_name.text())
            elif kademe == 4:
                self.ui.doubleSpinBox_mancap_4.setValue( object.ui.doubleSpinBox_tel_cap.value())
                self.ui.lineEdit_mlz_tel_4.setText(object.ui.lineEdit_tel_name.text())
        elif type == "karetel":
            if kademe == 1:
                self.ui.doubleSpinBox_karetel12.setValue(object.ui.doubleSpinBox_tel_cap_3.value())
                self.ui.doubleSpinBox_karetel11.setValue(object.ui.doubleSpinBox_tel_cap_2.value())
                self.ui.lineEdit_mlz_karetel_1.setText(object.ui.lineEdit_tel_name_2.text())
            elif kademe == 2:
                self.ui.doubleSpinBox_karetel22.setValue(object.ui.doubleSpinBox_tel_cap_3.value())
                self.ui.doubleSpinBox_karetel21.setValue(object.ui.doubleSpinBox_tel_cap_2.value())
                self.ui.lineEdit_mlz_karetel_2.setText(object.ui.lineEdit_tel_name_2.text())
            elif kademe == 3:

                self.ui.doubleSpinBox_karetel32.setValue(object.ui.doubleSpinBox_tel_cap_3.value())
                self.ui.doubleSpinBox_karetel31.setValue(object.ui.doubleSpinBox_tel_cap_2.value())
                self.ui.lineEdit_mlz_karetel_3.setText(object.ui.lineEdit_tel_name_2.text())
            elif kademe == 4:

                self.ui.doubleSpinBox_karetel42.setValue(object.ui.doubleSpinBox_tel_cap_3.value())
                self.ui.doubleSpinBox_karetel41.setValue(object.ui.doubleSpinBox_tel_cap_2.value())
                self.ui.lineEdit_mlz_karetel_4.setText(object.ui.lineEdit_tel_name_2.text())
        elif type == "folyotel":
            if kademe == 1:
                self.ui.doubleSpinBox_folyotel12.setValue(object.ui.doubleSpinBox_tel_cap_5.value())
                self.ui.doubleSpinBox_folyotel11.setValue(object.ui.doubleSpinBox_tel_cap_4.value())
                self.ui.lineEdit_mlz_folyotel_1.setText(object.ui.lineEdit_tel_name_3.text())
            elif kademe == 2:
                self.ui.doubleSpinBox_folyotel22.setValue(object.ui.doubleSpinBox_tel_cap_5.value())
                self.ui.doubleSpinBox_folyotel21.setValue(object.ui.doubleSpinBox_tel_cap_4.value())
                self.ui.lineEdit_mlz_folyotel_2.setText(object.ui.lineEdit_tel_name_3.text())
            elif kademe == 3:

                self.ui.doubleSpinBox_folyotel32.setValue(object.ui.doubleSpinBox_tel_cap_5.value())
                self.ui.doubleSpinBox_folyotel31.setValue(object.ui.doubleSpinBox_tel_cap_4.value())
                self.ui.lineEdit_mlz_folyotel_3.setText(object.ui.lineEdit_tel_name_3.text())
            elif kademe == 4:

                self.ui.doubleSpinBox_folyotel42.setValue(object.ui.doubleSpinBox_tel_cap_5.value())
                self.ui.doubleSpinBox_folyotel41.setValue(object.ui.doubleSpinBox_tel_cap_4.value())
                self.ui.lineEdit_mlz_folyotel_4.setText(object.ui.lineEdit_tel_name_3.text())
        elif type == "kapton":
            if kademe == 1:
                self.ui.doubleSpinBox_kapton1.setValue(object.ui.doubleSpinBox_tel_cap_6.value())
                self.ui.lineEdit_mlz_kapton_1.setText(object.ui.lineEdit_tel_name_4.text())
            elif kademe == 2:
                self.ui.doubleSpinBox_kapton2.setValue(object.ui.doubleSpinBox_tel_cap_6.value())
                self.ui.lineEdit_mlz_kapton_2.setText(object.ui.lineEdit_tel_name_4.text())
            elif kademe == 3:

                self.ui.doubleSpinBox_kapton3.setValue(object.ui.doubleSpinBox_tel_cap_6.value())
                self.ui.lineEdit_mlz_kapton_3.setText(object.ui.lineEdit_tel_name_4.text())
            elif kademe == 4:

                self.ui.doubleSpinBox_kapton4.setValue(object.ui.doubleSpinBox_tel_cap_6.value())
                self.ui.lineEdit_mlz_kapton_4.setText(object.ui.lineEdit_tel_name_4.text())
        else:
            pass
    def tel_deger_sil(self, gl, type, index=1, kademe=1):
        if type == "tel":

            if kademe == 1:
                self.ui.doubleSpinBox_mancap_1.setValue(0)
                self.ui.lineEdit_mlz_tel_1.setText( "")
            elif kademe == 2:
                self.ui.doubleSpinBox_mancap_2.setValue(0)
                self.ui.lineEdit_mlz_tel_2.setText( "")
            elif kademe == 3:
                self.ui.doubleSpinBox_mancap_3.setValue(0)
                self.ui.lineEdit_mlz_tel_3.setText( "")
            elif kademe == 4:
                self.ui.doubleSpinBox_mancap_4.setValue(0)
                self.ui.lineEdit_mlz_tel_4.setText( "")
        elif type == "karetel":
            if kademe == 1:
                self.ui.doubleSpinBox_karetel12.setValue(0)
                self.ui.doubleSpinBox_karetel11.setValue(0)
                self.ui.lineEdit_mlz_karetel_1.setText( "")
            elif kademe == 2:
                self.ui.doubleSpinBox_karetel22.setValue(0)
                self.ui.doubleSpinBox_karetel21.setValue(0)
                self.ui.lineEdit_mlz_karetel_2.setText( "")
            elif kademe == 3:

                self.ui.doubleSpinBox_karetel32.setValue(0)
                self.ui.doubleSpinBox_karetel31.setValue(0)
                self.ui.lineEdit_mlz_karetel_3.setText( "")
            elif kademe == 4:

                self.ui.doubleSpinBox_karetel42.setValue(0)
                self.ui.doubleSpinBox_karetel41.setValue(0)
                self.ui.lineEdit_mlz_karetel_4.setText( "")
        elif type == "folyotel":
            if kademe == 1:
                self.ui.doubleSpinBox_folyotel12.setValue(0)
                self.ui.doubleSpinBox_folyotel11.setValue(0)
                self.ui.lineEdit_mlz_folyotel_1.setText( "")
            elif kademe == 2:
                self.ui.doubleSpinBox_folyotel22.setValue(0)
                self.ui.doubleSpinBox_folyotel21.setValue(0)
                self.ui.lineEdit_mlz_folyotel_2.setText( "")
            elif kademe == 3:

                self.ui.doubleSpinBox_folyotel32.setValue(0)
                self.ui.doubleSpinBox_folyotel31.setValue(0)
                self.ui.lineEdit_mlz_folyotel_3.setText( "")
            elif kademe == 4:

                self.ui.doubleSpinBox_folyotel42.setValue(0)
                self.ui.doubleSpinBox_folyotel41.setValue(0)
                self.ui.lineEdit_mlz_folyotel_4.setText( "")
        elif type == "kapton":
            if kademe == 1:
                self.ui.doubleSpinBox_kapton1.setValue(0)
                self.ui.lineEdit_mlz_kapton_1.setText( "")
            elif kademe == 2:
                self.ui.doubleSpinBox_kapton2.setValue(0)
                self.ui.lineEdit_mlz_kapton_2.setText( "")
            elif kademe == 3:

                self.ui.doubleSpinBox_kapton3.setValue(0)
                self.ui.lineEdit_mlz_kapton_3.setText( "")
            elif kademe == 4:

                self.ui.doubleSpinBox_kapton4.setValue(0)
                self.ui.lineEdit_mlz_kapton_4.setText( "")
        else:
            pass
    def open_telsecim(self, gl, type="tel", index=1, kademe=1):
        self.window2 = Telselectdialog()
        print(gl[index]["teltipi"])
        if gl[index]["teltipi"]=="Al":
           self.window2.teltipi="ALUMINYUM"
        else:
            self.window2.teltipi="BAKIR"
        self.window2.update_all_table()
        if type == "tel":
            
            self.window2.setWindowTitle("Yuvarlak Tel Seçim Sayfası")
            self.window2.ui.tabWidget.setCurrentIndex(0)
            self.window2.show()
            self.window2.ui.pushButton_sec_tel.clicked.connect(
                lambda x: self.tel_deger_al(gl=gl, object=self.window2, type=type, index=index, kademe=kademe))
        elif type == "karetel":
            self.window2.setWindowTitle("Kare Tel Seçim Sayfası")
            self.window2.ui.tabWidget.setCurrentIndex(1)
            self.window2.show()
            self.window2.ui.pushButton_sec_karetel.clicked.connect(
                lambda x: self.tel_deger_al(gl=gl, object=self.window2, type=type, index=index, kademe=kademe))
        elif type == "folyotel":
            self.window2.setWindowTitle("Folyo Seçim Sayfası")
            self.window2.ui.tabWidget.setCurrentIndex(2)
            self.window2.show()
            self.window2.ui.pushButton_sec_folyo.clicked.connect(
                lambda x: self.tel_deger_al(gl=gl, object=self.window2, type=type, index=index, kademe=kademe))
        elif type == "kapton":
            self.window2.setWindowTitle("Kapton Seçim Sayfası")
            self.window2.ui.tabWidget.setCurrentIndex(3)
            self.window2.show()
            self.window2.ui.pushButton_sec_kapton.clicked.connect(
                lambda x: self.tel_deger_al(gl=gl, object=self.window2, type=type, index=index, kademe=kademe))
        else:
            pass
    def hesap_1_gnl(self, gl, guc, frekans, gauss, karkas_en, karkas_boy, karkas_yuk, verim, sarim, kademe=1):
        if self.trafoTipi=="mono_izole":
            hp.trafo_hesap_1(gl, guc, frekans,
                        gauss, karkas_en, karkas_boy,
                        karkas_yuk, verim, sarim,
                        primer_sarim_yukseklik_toplam=self.primer_sarim_yukseklik_toplam,
                        primer_izolasyon=self.primer_izolasyon,
                        sva1_sarim_yukseklik_toplam=self.sva1_sarim_yukseklik_toplam,
                        sva1_izolasyon=self.sva1_izolasyon,
                        sva2_sarim_yukseklik_toplam=self.sva2_sarim_yukseklik_toplam,
                        sva2_izolasyon=self.sva2_izolasyon,
                        sva3_sarim_yukseklik_toplam=self.sva3_sarim_yukseklik_toplam,
                        sva3_izolasyon=self.sva3_izolasyon,
                        sva4_sarim_yukseklik_toplam=self.sva4_sarim_yukseklik_toplam,
                        sva4_izolasyon=self.sva4_izolasyon,
                        sva5_sarim_yukseklik_toplam=self.sva5_sarim_yukseklik_toplam,
                        sva5_izolasyon=self.sva5_izolasyon,
                        sva6_sarim_yukseklik_toplam=self.sva6_sarim_yukseklik_toplam,
                        sva6_izolasyon=self.sva6_izolasyon,
                        sva7_sarim_yukseklik_toplam=self.sva7_sarim_yukseklik_toplam,
                        sva7_izolasyon=self.sva7_izolasyon,
                        sva8_sarim_yukseklik_toplam=self.sva8_sarim_yukseklik_toplam,
                        sva8_izolasyon=self.sva8_izolasyon,
                        sva9_sarim_yukseklik_toplam=self.sva9_sarim_yukseklik_toplam,
                        sva9_izolasyon=self.sva9_izolasyon,
                        kademe=kademe,
                        cu_par= self.cu_par,
                        cu_yog=self.cu_yog,
                        al_par=self.al_par ,
                        al_yog=self.al_yog,
                        dig_par=self.dig_par,
                        dig_yog=self.dig_yog)
        elif self.trafoTipi=="trifaz_izole":
            hp.trafo_hesap_trifaz_izole(gl, guc, frekans,
                        gauss, karkas_en, karkas_boy,
                        karkas_yuk, verim, sarim,
                        primer_sarim_yukseklik_toplam=self.primer_sarim_yukseklik_toplam,
                        primer_izolasyon=self.primer_izolasyon,
                        baglanti=self.baglanti,
                        kademe=kademe,
                        cu_par= self.cu_par,
                         cu_yog=self.cu_yog,
                        al_par=self.al_par ,
                        al_yog=self.al_yog,
                        dig_par=self.dig_par,
                        dig_yog=self.dig_yog)
        elif self.trafoTipi=="trifaz_oto":
            hp.trafo_hesap_trifaz_oto(gl, guc, frekans,
                        gauss, karkas_en, karkas_boy,
                        karkas_yuk, verim, sarim,
                        primer_sarim_yukseklik_toplam=self.primer_sarim_yukseklik_toplam,
                        primer_izolasyon=self.primer_izolasyon,
                        baglanti=self.baglanti,
                        kademe=kademe,
                        cu_par= self.cu_par,
                         cu_yog=self.cu_yog,
                        al_par=self.al_par ,
                        al_yog=self.al_yog,
                        dig_par=self.dig_par,
                        dig_yog=self.dig_yog)
        elif self.trafoTipi=="monofaz_oto":
            hp.trafo_hesap_monofaz_oto(gl, guc, frekans,
                        gauss, karkas_en, karkas_boy,
                        karkas_yuk, verim, sarim,
                        primer_sarim_yukseklik_toplam=self.primer_sarim_yukseklik_toplam,
                        primer_izolasyon=self.primer_izolasyon,
                        baglanti=self.baglanti,
                        kademe=kademe,
                        cu_par= self.cu_par,
                         cu_yog=self.cu_yog,
                        al_par=self.al_par ,
                        al_yog=self.al_yog,
                        dig_par=self.dig_par,
                        dig_yog=self.dig_yog)
        elif self.trafoTipi=="monofazUI_izole":
            hp.trafo_hesap_monoFazUI_izole(gl, guc, frekans,
                        gauss, karkas_en, karkas_boy,
                        karkas_yuk, verim, sarim,
                        primer_sarim_yukseklik_toplam=self.primer_sarim_yukseklik_toplam,
                        primer_izolasyon=self.primer_izolasyon,
                        baglanti=self.baglanti,
                        kademe=kademe,
                        cu_par= self.cu_par,
                         cu_yog=self.cu_yog,
                        al_par=self.al_par ,
                        al_yog=self.al_yog,
                        dig_par=self.dig_par,
                        dig_yog=self.dig_yog)
        elif self.trafoTipi=="monofaz_sont":    
            degerler=hp.trafo_hesap_monofaz_sont(gl, guc, frekans,
                        gauss, karkas_en, karkas_boy,
                        karkas_yuk, verim, sarim,
                        primer_sarim_yukseklik_toplam=self.primer_sarim_yukseklik_toplam,
                        cu_par= self.cu_par,
                        cu_yog=self.cu_yog,
                        al_par=self.al_par ,
                        al_yog=self.al_yog,
                        dig_par=self.dig_par,
                        dig_yog=self.dig_yog,
                        Lg_man=self.Lg_man, 
                        c=self.c, 
                        Kf=self.Kf, 
                        Ku=self.Ku, 
                        Um=self.Um,
                        klemens_a=self.klemens_a,
                        klemens_b=self.klemens_b,
                        ayak_a=self.ayak_a)
        elif self.trafoTipi=="trifaz_sont":    
            degerler=hp.trafo_hesap_trifaz_sont(gl, guc, frekans,
                        gauss, karkas_en, karkas_boy,
                        karkas_yuk, verim, sarim,
                        primer_sarim_yukseklik_toplam=self.primer_sarim_yukseklik_toplam,
                        cu_par= self.cu_par,
                        cu_yog=self.cu_yog,
                        al_par=self.al_par ,
                        al_yog=self.al_yog,
                        dig_par=self.dig_par,
                        dig_yog=self.dig_yog,
                        Lg_man=self.Lg_man, 
                        c=self.c, 
                        Kf=self.Kf, 
                        Ku=self.Ku, 
                        Um=self.Um,
                        klemens_a=self.klemens_a,
                        klemens_b=self.klemens_b,
                        ayak_a=self.ayak_a)
        elif self.trafoTipi=="monofaz_sok":    
            degerler=hp.trafo_hesap_monofaz_sok(gl, guc, frekans,
                        gauss, karkas_en, karkas_boy,
                        karkas_yuk, verim, sarim,
                        primer_sarim_yukseklik_toplam=self.primer_sarim_yukseklik_toplam,
                        cu_par= self.cu_par,
                        cu_yog=self.cu_yog,
                        al_par=self.al_par ,
                        al_yog=self.al_yog,
                        dig_par=self.dig_par,
                        dig_yog=self.dig_yog,
                        Lg_man=self.Lg_man, 
                        c=self.c, 
                        Kf=self.Kf, 
                        Ku=self.Ku, 
                        Um=self.Um,
                        klemens_a=self.klemens_a,
                        klemens_b=self.klemens_b,
                        ayak_a=self.ayak_a,
                        akim_m=self.akim_m,
                        enduktans_m=self.enduktans_m)
        elif self.trafoTipi=="trifaz_sok":    
            degerler=hp.trafo_hesap_trifaz_sok(gl, guc, frekans,
                        gauss, karkas_en, karkas_boy,
                        karkas_yuk, verim, sarim,
                        primer_sarim_yukseklik_toplam=self.primer_sarim_yukseklik_toplam,
                        cu_par= self.cu_par,
                        cu_yog=self.cu_yog,
                        al_par=self.al_par ,
                        al_yog=self.al_yog,
                        dig_par=self.dig_par,
                        dig_yog=self.dig_yog,
                        Lg_man=self.Lg_man, 
                        c=self.c, 
                        Kf=self.Kf, 
                        Ku=self.Ku, 
                        Um=self.Um,
                        klemens_a=self.klemens_a,
                        klemens_b=self.klemens_b,
                        ayak_a=self.ayak_a,
                        akim_m=self.akim_m,
                        enduktans_m=self.enduktans_m)
        elif self.trafoTipi=="trifaz_Harmonik":    
            degerler=hp.trafo_hesap_trifaz_Harmonik(gl, guc, frekans,
                        gauss, karkas_en, karkas_boy,
                        karkas_yuk, verim, sarim,
                        primer_sarim_yukseklik_toplam=self.primer_sarim_yukseklik_toplam,
                        cu_par= self.cu_par,
                        cu_yog=self.cu_yog,
                        al_par=self.al_par ,
                        al_yog=self.al_yog,
                        dig_par=self.dig_par,
                        dig_yog=self.dig_yog,
                        Lg_man=self.Lg_man, 
                        c=self.c, 
                        Kf=self.Kf, 
                        Ku=self.Ku, 
                        Um=self.Um,
                        klemens_a=self.klemens_a,
                        klemens_b=self.klemens_b,
                        ayak_a=self.ayak_a,
                        akim_m=self.akim_m,
                        enduktans_m=self.enduktans_m,
                        sacTipi=self.sacTipi,
                        nuveBosluk=self.nuveBosluk,
                        sacYogunluk=self.sacYogunluk)
        elif self.trafoTipi=="UPS":
            hp.trafo_hesap_UPS(gl, guc, frekans,
                        gauss, karkas_en, karkas_boy,
                        karkas_yuk, verim, sarim,
                        primer_sarim_yukseklik_toplam=self.primer_sarim_yukseklik_toplam,
                        primer_izolasyon=self.primer_izolasyon,
                        baglanti=self.baglanti,
                        kademe=kademe,
                        cu_par= self.cu_par,
                         cu_yog=self.cu_yog,
                        al_par=self.al_par ,
                        al_yog=self.al_yog,
                        dig_par=self.dig_par,
                        dig_yog=self.dig_yog)
        
        self.load_selected_kademe(kademe=kademe)
        # for i in range (0,self.max_kademe):
        #
        #     print(f" Kademe {i} : " ,self.group_name_list_kademe[i]["akim2"],"\n")

    
class Reciepedialog(QDialog):
    def __init__(self, parent=None):
        super(Reciepedialog, self).__init__(parent)
        self.ui = Reciepe_dialog()
        self.ui.setupUi(self)
        self.handle_button()
        self.recete_veri_kumesi()
        self.visible_item()
        self.tum_kademeleri_guncelle()
        #data = db.showall_recete()
        #table_update(data, headers_recete, self.ui.tableWidget)
        self.filter_recete_table()
    def handle_button(self):
        self.ui.pushButton_ara.clicked.connect(self.filter_recete_table)
        self.ui.pushButton_sec.clicked.connect(self.recete_select)
        self.ui.pushButton_kaydet.clicked.connect(self.insert_recete_table)
        self.ui.pushButton_temizle.clicked.connect(self.clear_recete_fields)
        self.ui.pushButton_sil.clicked.connect(self.delete_recete_table)
        self.ui.tableWidget.itemClicked.connect(self.callback_from_recete_table)
        self.ui.comboBox_filter1.currentIndexChanged.connect(self.date_visible_event)
        self.ui.lineEdit_musteri_adi.textChanged.connect(self.siparis_kodu_olustur)
        self.ui.dateEdit.dateChanged.connect(lambda x:self.ui.lineEdit_ara_text1.setText(self.ui.dateEdit.date().toString("yyyy-MM-dd")))
    def siparis_kodu_olustur(self):
        self.ui.lineEdit_siparis_kodu.setText(self.ui.lineEdit_musteri_adi.text() + "_" +self.ui.lineEdit_kullanici.text() + "_" +str(QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")))
    def recete_veri_kumesi(self):
        self.rec_veriler = vt.recete_veri.copy()

        self.primer_group_elementlist=[self.ui.lineEdit_primer]
        self.sekonder_group_elementlist = [self.ui.lineEdit_sekonder]
        self.va_group_elementlist = [self.ui.lineEdit_sva1,self.ui.lineEdit_sva2,self.ui.lineEdit_sva3,self.ui.lineEdit_sva4,
                                     self.ui.lineEdit_sva5,self.ui.lineEdit_sva6,self.ui.lineEdit_sva7,self.ui.lineEdit_sva8,
                                     self.ui.lineEdit_sva9,self.ui.lineEdit_sva10]
    def date_visible_event(self):
        if self.ui.comboBox_filter1.currentIndex()==5:
            self.ui.dateEdit.setVisible(True)

        else:
            self.ui.dateEdit.setVisible(False)
    def check_requirement_fields(self):
        if self.ui.lineEdit_musteri_adi.text()==""  or self.ui.lineEdit_siparis_kodu.text()=="" :
            return False
        else:
            return True
    def visible_item(self):
        self.ui.dateEdit.setVisible(False)
    def va_kademe_guncelle(self):
        if self.rec_veriler["va_enabled"] == True:
            self.ui.tabWidget_2.setVisible(True)
            self.ui.lineEdit_sekonder.setVisible(False)
            self.ui.label_8.setVisible(True)
            self.ui.label_4.setVisible(False)
        else:
            self.ui.tabWidget_2.setVisible(False)
            self.ui.lineEdit_sekonder.setVisible(True)
            self.ui.label_8.setVisible(False)
            self.ui.label_4.setVisible(True)
        for i in range(0,10):
            if  self.rec_veriler["va_enabled"]==True:

                for y in range(0,10):
                    if self.rec_veriler["va_group_list"][i][y]["voltaj"] > 0:
                        text = self.va_group_elementlist[i].text()
                        self.va_group_elementlist[i].setText(
                            text +  str(self.rec_veriler["va_group_list"][i][y]["voltaj"])+"-" )
                if i < self.rec_veriler["va_kademe"]:
                    self.ui.tabWidget_2.setTabEnabled(i, True)
                    self.ui.tabWidget_2.setTabVisible(i, True)
                else:
                    self.ui.tabWidget_2.setTabEnabled(i,False)
                    self.ui.tabWidget_2.setTabVisible(i, False)
        self.ui.tabWidget_2.setCurrentIndex(0)
    def primer_kademe_guncelle(self):
        for i in range(0, len(self.rec_veriler["primer_group_list"])):
            if self.rec_veriler["primer_group_list"][i]["voltaj"] > 0:

                text = self.ui.lineEdit_primer.text()
                self.ui.lineEdit_primer.setText(text +  str(self.rec_veriler["primer_group_list"][i]["voltaj"]) + "-" )
    def sekonder_kademe_guncelle(self):
        for i in range(0, len(self.rec_veriler["sekonder_group_list"])):
            if self.rec_veriler["va_enabled"]==False:
                if self.rec_veriler["sekonder_group_list"][i]["voltaj"] > 0:
                    text = self.ui.lineEdit_sekonder.text()
                    self.ui.lineEdit_sekonder.setText(
                        text + str(self.rec_veriler["sekonder_group_list"][i]["voltaj"])+ "-" )
    def tum_kademeleri_guncelle(self):
        self.primer_kademe_guncelle()
        self.va_kademe_guncelle()
        self.sekonder_kademe_guncelle()

    def tum_kademeleri_temizle(self):
        self.rec_veriler = vt.recete_veri.copy()
        self.ui.lineEdit_primer.setText("")
        self.ui.lineEdit_sekonder.setText("")
        self.ui.lineEdit_sva1.setText("")
        self.ui.lineEdit_sva2.setText("")
        self.ui.lineEdit_sva3.setText("")
        self.ui.lineEdit_sva4.setText("")
        self.ui.lineEdit_sva5.setText("")
        self.ui.lineEdit_sva6.setText("")
        self.ui.lineEdit_sva7.setText("")
        self.ui.lineEdit_sva8.setText("")
        self.ui.lineEdit_sva9.setText("")
        self.ui.lineEdit_sva10.setText("")
        self.ui.lineEdit_musteri_adi.setText("")
        self.ui.lineEdit_siparis_kodu.setText("")
        self.ui.lineEdit_trafo_tipi.setText("")
    def filter_recete_table(self):
        self.ui.lineEdit_ara_text1.text()
        self.ui.comboBox_filter1.currentIndex()
        self.ui.lineEdit_trafo_tipi.text()
        data = db.showfilter_recete(
            index=(self.ui.comboBox_filter1.currentIndex(),self.ui.comboBox_filter2.currentIndex()),
            filter_value=(self.ui.lineEdit_ara_text1.text(),self.ui.lineEdit_ara_text2.text(),self.ui.lineEdit_trafo_tipi.text()))

        table_update(data, headers_recete, self.ui.tableWidget)
    def delete_recete_table(self):

        if self.ui.doubleSpinBox_ID.value() >= 1:
            returnValue = delete_msjbox(
                text='{} Nolu kayıt silinecektir.\nDevam Etmek için Sil  tuşuna basın'.format(self.ui.doubleSpinBox_ID.value() ),
                title="DİKKAT - Veriler silinecektir")

            if returnValue == QMessageBox.Discard:
                db.delete_recete(int(self.ui.doubleSpinBox_ID.value() ))

                data = db.showfilter_recete(
            index=(self.ui.comboBox_filter1.currentIndex(),self.ui.comboBox_filter2.currentIndex()),
            filter_value=(self.ui.lineEdit_ara_text1.text(),self.ui.lineEdit_ara_text2.text(),self.ui.lineEdit_trafo_tipi.text()))

                table_update(data, headers_recete, self.ui.tableWidget)
                self.clear_recete_fields()
    def clear_recete_fields(self):
        returnValue = clear_msjbox(
            text="Tüm veri girisleri temizlenecektir..\nDevam Etmek için Temizle tuşuna basın",
            title="DİKKAT - Veriler silinecektir")

        if returnValue == QMessageBox.Cancel:
            return False


        self.ui.doubleSpinBox_ID.setValue(0)
        self.ui.doubleSpinBox_guc.setValue(0)
        self.rec_veriler = vt.recete_veri.copy()
        self.ui.lineEdit_primer.setText("")
        self.ui.lineEdit_sekonder.setText("")
        self.ui.lineEdit_sva1.setText("")
        self.ui.lineEdit_sva2.setText("")
        self.ui.lineEdit_sva3.setText("")
        self.ui.lineEdit_sva4.setText("")
        self.ui.lineEdit_sva5.setText("")
        self.ui.lineEdit_sva6.setText("")
        self.ui.lineEdit_sva7.setText("")
        self.ui.lineEdit_sva8.setText("")
        self.ui.lineEdit_sva9.setText("")
        self.ui.lineEdit_sva10.setText("")
        self.ui.lineEdit_musteri_adi.setText("")
        self.ui.lineEdit_siparis_kodu.setText("")
        self.ui.lineEdit_trafo_tipi.setText("")
        self.ui.lineEdit_tarih.setText("")

    def read_data_from_mainwindow(self):
        self.ui.doubleSpinBox_guc.setValue(self.rec_veriler["guc"])
        self.ui.doubleSpinBox_ID.setValue(self.rec_veriler["recete_ID"])
        self.ui.lineEdit_musteri_adi.setText(self.rec_veriler["musteri_adi"])
        self.ui.lineEdit_siparis_kodu.setText(self.rec_veriler["siparis_kodu"])
        self.ui.lineEdit_kullanici.setText(self.rec_veriler["kullanici"])
        self.ui.lineEdit_trafo_tipi.setText(self.rec_veriler["trafo_tipi"])
        self.tum_kademeleri_guncelle()
    def read_data_fromsql_write_fields(self,data):
        self.tum_kademeleri_temizle()
        self.ui.doubleSpinBox_ID.setValue(data[0])
        self.ui.lineEdit_kullanici.setText(data[1])
        self.ui.lineEdit_musteri_adi.setText(data[2])
        self.ui.lineEdit_siparis_kodu.setText(data[3])
        self.ui.doubleSpinBox_guc.setValue(data[4])
        #self.ui.lineEdit_primer.setText(data[5])
        #self.ui.lineEdit_sekonder.setText(data[6])
        #self.ui.lineEdit_sva1.setText(data[7])
        #self.ui.lineEdit_karkas_name.setText(json.loads(data[9])["adi"])
        #self.ui.doubleSpinBox_karkas_en.setValue(float(json.loads(data[9])["en"]))
        #self.ui.doubleSpinBox_karkas_boy.setValue(float(json.loads(data[9])["boy"]))
        #self.ui.doubleSpinBox_karkas_yukseklik.setValue(float(json.loads(data[9])["yukseklik"]))
        #self.ui.doubleSpinBox_karkas_verim.setValue(float(json.loads(data[9])["verim"]))
        self.ui.lineEdit_tarih.setText(data[8])
        self.rec_veriler = json.loads(data[9])
        self.ui.lineEdit_trafo_tipi.setText(data[10])
        self.tum_kademeleri_guncelle()

    def insert_recete_table(self):
        if self.check_requirement_fields()==False:
            error_msjbox(title='Eksik Bilgi', text='Lütfen Musteri Bilgilerini Giriniz.')
            return False
        data = db.check_recete((self.ui.lineEdit_siparis_kodu.text()))
        if data != None:
            error_msjbox(title='Mevcut Kayıt Hatası', text='Eklemek istediğiniz Bu kayıt zaten mevcuttur.')
            #self.ui.statusbar.showMessage('Please change your data')
            return False
        else:

            db.insert_recete((self.ui.lineEdit_kullanici.text(),self.ui.lineEdit_musteri_adi.text(),
                              self.ui.lineEdit_siparis_kodu.text(),
                              self.ui.doubleSpinBox_guc.value(),
                              self.ui.lineEdit_primer.text(),
                              self.ui.lineEdit_sekonder.text(),json.dumps([self.ui.lineEdit_sva1.text(),
                                                                self.ui.lineEdit_sva2.text(),
                                                                self.ui.lineEdit_sva3.text(),
                                                                self.ui.lineEdit_sva4.text(),
                                                                self.ui.lineEdit_sva5.text(),
                                                                self.ui.lineEdit_sva6.text(),
                                                                self.ui.lineEdit_sva7.text(),
                                                                self.ui.lineEdit_sva8.text(),
                                                                self.ui.lineEdit_sva9.text(),
                                                                self.ui.lineEdit_sva10.text()]),
                                                                json.dumps(self.rec_veriler),
                                                                self.ui.lineEdit_trafo_tipi.text())
                              )
            info_msjbox(
                text='Sip. Kod: {} \nKayıt olusturulmustur.\nDevam Etmek için Ok tuşuna basın'.format(
                    self.ui.lineEdit_siparis_kodu.text()),
                title="Bilgi - Yeni Kayıt ")
            #self.ui.statusbar.showMessage('The record added successfully ')

        self.filter_recete_table()

        return True
    def callback_from_recete_table(self):
        self.rec_veriler["recete_ID"]  = int(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 0).text())

        data = db.calldata_with_id_recete(self.rec_veriler["recete_ID"] )
        if data != None:

            self.read_data_fromsql_write_fields(data)

            return True
        else:
            return False
    def recete_select(self):

        self.close()
        return self.rec_veriler["recete_ID"]

