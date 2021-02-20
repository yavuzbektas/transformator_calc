from QT_file.mainoto_monofaz import Ui_MainWindow

from PySide2.QtWidgets import QMainWindow,QMessageBox,QTableWidgetItem,QDoubleSpinBox,QComboBox,QLineEdit,QLabel,QPushButton,QCheckBox,QDialog
from QT_file.tel_select import Ui_Dialog as Telselect_dialog
from QT_file.kesit_param import Ui_Dialog as KesitParam_dialog
import db_sql,math
import hesaplamalar  as hp
import popups as popup
import printout as printout
db=db_sql.mydb()

headers_sac_tekfaz= ("id","sac_olcu","a_deg","b_deg","c_deg","d_deg","e_deg","f_deg","h_deg","i_deg","k1_deg","k2_deg","ag1_deg","ag2_deg","Ac_deg","Wa_deg","Ap_deg","Kg_deg","At_deg","MPL_deg","MLT_deg")
headers_klemens= ("ID", "klemens_Adı","a degeri", "b_degeri","akim", "Kayıt Tarihi")
headers_ayak= ("ID", "AYAK_Adı","a degeri", "Kayıt Tarihi")
headers_kapton= ("ID", "Kapton_Adı","Yukseklik", "Ozzellik-1", "Kayıt Tarihi")
headers_folyotel_tel= ("ID", "Tel_Adı","Yukseklik","En", "Ozzellik-1","Ozzellik-2", "Kayıt Tarihi")
headers_kare_tel= ("ID", "Tel_Adı","Yukseklik","En", "Ozzellik-1", "Ozzellik-2","Kayıt Tarihi")
headers_karkas= ("ID", "Karkas_Adı","En", "Boy","Ozellik-1" ,"Kayıt Tarihi")
headers_teller= ("ID", "Tel_Adı","Cap", "Cu_yog","Al_yog", "Kayıt Tarihi")
headers_logs = ("ID", "Code","Unit","UserID", "Record Date")
headers_user =  ("ID", "User Name","UserType", "Record Date")
# ======================  mesajlar =========================
def error_msjbox(text, title):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.setText(text)
    msgBox.setWindowTitle(title)
    msgBox.setStandardButtons(QMessageBox.Ok)
    # mylog(text, type="error")
    return msgBox.exec()
def update_msjbox(text, title):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText(text)
    msgBox.setWindowTitle(title)
    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    return msgBox.exec()
def delete_msjbox(text, title):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.setText(text)
    msgBox.setWindowTitle(title)
    msgBox.setStandardButtons(QMessageBox.Discard | QMessageBox.Cancel)
    buttonY = msgBox.button(QMessageBox.Discard)
    buttonY.setText('Delete')
    return msgBox.exec()
def clear_msjbox(text, title):
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
# ======================  Object tipi bulma =========================
def object_type_find(object_name):
    object_type = object_name.split("_")[0]
    if object_type == "doubleSpinBox":
        return QDoubleSpinBox
    elif object_type == "comboBox":
        return QComboBox
    elif object_type == "lineEdit":
        return QLineEdit
    elif object_type == "label":
        return QLabel
    elif object_type == "pushButton":
        return QPushButton
    elif object_type == "checkBox":
        return QCheckBox
    else:
        pass
# ======================  tablolar =========================
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
class OtoMonofazwindow(QMainWindow):
    def __init__(self, parent=None):
        super(OtoMonofazwindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Trafo Hesaplama Programı V0 - Oto Trafosu Monofaz Hesaplama")
        self.veri_kumeleri()

        self.handle_button()
        self.kademeleri_guncelle()
        self.hesaplamalari_guncelle()
    
    def logout_myapp(self):
        import Trafo_app as Trafo_app
        self.window = Trafo_app.Login()

        self.close()
        self.window.show()
    def handle_button(self):
        self.ui.pushButton_35.clicked.connect(self.logout_myapp)
        self.ui.pushButton_parametre.clicked.connect(self.open_genel_parametre)
        self.ui.pushButton_recete.clicked.connect(self.open_recete)
        self.ui.pushButton_karkas.clicked.connect(self.open_karkas)
        self.ui.pushButton_izolasyon.clicked.connect(self.open_izolasyon)
        self.ui.pushButton_yazdir.clicked.connect(self.printout_report)
        self.ui.pushButton_temizle.clicked.connect(self.tum_degerleri_temizle)
        self.ui.pushButton_klemens.clicked.connect(self.open_klemens)

        self.ui.pushButton_hesaplar.clicked.connect(lambda x:self.ekran_degistir(1))
        self.ui.pushButton_geri.clicked.connect(lambda x: self.ekran_degistir(0))
        self.ui.doubleSpinBox_guc.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_sac.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_gauss.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_frekans.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_c.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_karkas_en.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_karkas_boy.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_karkas_verim.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_karkas_yukseklik.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.comboBox_sactipi.currentTextChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_58.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_59.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_62.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_63.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_64.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_65.valueChanged.connect(self.hesaplamalari_guncelle)
        # diğer trafo hesapları
        self.ui.actionHakk_mda.triggered.connect(self.open_about)
        self.ui.actionTri_Faz.triggered.connect(lambda x:self.open_other_trafo(1))
        self.ui.actionMono_Faz.triggered.connect(lambda x: self.open_other_trafo(0))
        self.ui.action_sont_Mono_Faz.triggered.connect(lambda x: self.open_other_trafo(2))
        self.ui.action_sont_Tri_Faz.triggered.connect(lambda x: self.open_other_trafo(3))
        self.ui.action_sok_Mono_Faz.triggered.connect(lambda x: self.open_other_trafo(4))
        self.ui.action_sok_Tri_Faz.triggered.connect(lambda x: self.open_other_trafo(5))
        self.ui.action_oto_Mono_Faz.triggered.connect(lambda x: self.open_other_trafo(6))
        self.ui.action_oto_Tri_Faz.triggered.connect(lambda x: self.open_other_trafo(7))
        self.ui.actionHarmonik_Trafosu.triggered.connect(lambda x: self.open_other_trafo(8))
        self.ui.actionUPS_Trafosu.triggered.connect(lambda x: self.open_other_trafo(9))
        self.ui.action_nt.triggered.connect(lambda x: self.open_other_trafo(10))

        self.primer_object_signals()

        self.izolasyon_object_signals()
        self.karkas_object_signals()
    def hide_list(self,list_name):
        for i in list_name:
            i.setVisible(False)
    def ekran_degistir(self,index):
        self.old_index = self.ui.stackedWidget.currentIndex()
        self.ui.stackedWidget.setCurrentIndex(index)
    def veri_kumeleri(self):
        self.primer_veri_kumesi()
        self.deger=0
        self.primer_izolasyon = 0
        self.toplam_izolasyon= 0
    def kademeleri_guncelle(self):
        self.primer_kademe_goster()
    def hesaplamalari_guncelle(self):
        self.karkas_hesaplama()
        self.hesap_yap(gl=self.group_name_list_1,
                       gl2=self.group_name_list_2,
                       guc=self.ui.doubleSpinBox_guc.value(),
                       frekans=self.ui.doubleSpinBox_frekans.value(),
                       gauss=self.ui.doubleSpinBox_gauss.value(),
                       karkas_en=self.ui.doubleSpinBox_karkas_en.value(),
                       karkas_boy=self.ui.doubleSpinBox_karkas_boy.value(),
                       karkas_yuk=self.ui.doubleSpinBox_karkas_yukseklik.value(),
                       verim=self.ui.doubleSpinBox_karkas_verim.value(),
                       baglanti="mono",
                       sarim="primer",
                       cu_par = self.ui.doubleSpinBox_58.value(),
                       cu_yog = self.ui.doubleSpinBox_59.value(),
                       al_par = self.ui.doubleSpinBox_62.value(),
                       al_yog = self.ui.doubleSpinBox_63.value(),
                       dig_par = self.ui.doubleSpinBox_64.value(),
                       dig_yog = self.ui.doubleSpinBox_65.value(),
                       kademe=int(self.ui.comboBox_primer.currentText()))

    # ======================  open popups =========================
    def open_genel_parametre(self):
        self.window3 = popup.GenelParamdialog()

        self.window3.setWindowTitle("Genel Parametreler Sayfası")
        self.window3.show()
        self.window3.ui.pushButton_sec.clicked.connect(lambda x:self.genel_parametrelere_deger_al(object=self.window3))
        self.window3.ui.doubleSpinBox_sac.setValue(self.ui.doubleSpinBox_sac.value())
        self.window3.ui.doubleSpinBox_gauss.setValue(self.ui.doubleSpinBox_gauss.value())
        self.window3.ui.doubleSpinBox_frekans.setValue(self.ui.doubleSpinBox_frekans.value())
        self.window3.ui.doubleSpinBox_c.setValue(self.ui.doubleSpinBox_c.value())
    def genel_parametrelere_deger_al(self, object):

        self.ui.doubleSpinBox_sac.setValue(object.ui.doubleSpinBox_sac.value())
        self.ui.doubleSpinBox_gauss.setValue(object.ui.doubleSpinBox_gauss.value())
        self.ui.doubleSpinBox_frekans.setValue(object.ui.doubleSpinBox_frekans.value())
        self.ui.doubleSpinBox_c.setValue(object.ui.doubleSpinBox_c.value())
        self.ui.doubleSpinBox_gauss2.setValue(object.ui.doubleSpinBox_gauss2.value())
        self.ui.doubleSpinBox_c2.setValue(object.ui.doubleSpinBox_c2.value())
    def open_recete(self):
        pass
    def open_izolasyon(self):
        self.window3 = popup.Izolasyondialog()

        self.window3.setWindowTitle("Izolasyon Parametreleri Sayfası")

        self.window3.show()
        self.window3.ui.pushButton_sec.clicked.connect(lambda x: self.izolasyon_verileri_guncelle(object=self.window3))
        self.izolasyon_deger_al(object=self.window3)
    def open_karkas(self):
        self.window3 = popup.Karkasdialog()

        self.window3.setWindowTitle("Karkas Seçim Sayfası")
        self.window3.show()
        self.window3.ui.pushButton_sec.clicked.connect(lambda x: self.karkas_deger_al(object=self.window3))
    def open_klemens(self):

        self.window3 = popup.Klemensdialog()

        self.window3.setWindowTitle("Klemens Seçim Sayfası")
        self.window3.show()
        self.window3.ui.pushButton_sec_klemens.clicked.connect(
            lambda x: self.klemens_deger_al(klemens_name=self.window3.ui.lineEdit_klemens_name.text(),
                                            a=self.window3.ui.doubleSpinBox_klemens_a.value(),
                                            b=self.window3.ui.doubleSpinBox_klemens_b.value(),
                                            akim=self.window3.ui.doubleSpinBox_klemens_akim.value()))
        self.window3.ui.pushButton_sec_ayak.clicked.connect(
            lambda x: self.ayak_deger_al(ayak_name=self.window3.ui.lineEdit_ayak_name.text(),
                                         a=self.window3.ui.doubleSpinBox_ayak_a.value()))
    def open_about(self):
        self.window3 = popup.Aboutwindow()

        self.window3.setWindowTitle("Hakkımda Sayfası")
        self.window3.show()
    def open_other_trafo(self,trafo_index):
        if trafo_index == 0:
            import myApp
            self.window = myApp.MyWindow()

            # self.window.ui.lineEdit_2.setText(data[3])
            # self.window.user_admin_check()
            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            self.close()
            self.window.show()
            self.window.ui.stackedWidget.setCurrentIndex(0)
        elif trafo_index == 1:

            import myizole_trifaz
            self.window = myizole_trifaz.IzoleTrifazwindow()

            # self.window.ui.lineEdit_2.setText(data[3])
            # self.window.user_admin_check()
            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            self.close()
            self.window.show()
            self.window.ui.stackedWidget.setCurrentIndex(0)
        elif trafo_index == 2:
            import mysont_monofaz
            self.window = mysont_monofaz.SontMonofazwindow()
            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            self.close()
            self.window.show()
            self.window.ui.stackedWidget.setCurrentIndex(0)
        elif trafo_index == 3:
            import mysont_trifaz
            self.window = mysont_trifaz.SontTrifazwindow()
            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            self.close()
            self.window.show()
            self.window.ui.stackedWidget.setCurrentIndex(0)
        elif trafo_index == 4:
            import mysok_monofaz
            self.window = mysok_monofaz.SokMonofazwindow()

            # self.window.ui.lineEdit_2.setText(data[3])
            # self.window.user_admin_check()
            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            self.close()
            self.window.show()
            self.window.ui.stackedWidget.setCurrentIndex(0)
        elif trafo_index == 5:
            import mysok_trifaz
            self.window = mysok_trifaz.SokTrifazwindow()

            # self.window.ui.lineEdit_2.setText(data[3])
            # self.window.user_admin_check()
            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            self.close()
            self.window.show()
            self.window.ui.stackedWidget.setCurrentIndex(0)
        elif trafo_index == 6:
            import myoto_monofaz
            self.window = myoto_monofaz.OtoMonofazwindow()

            # self.window.ui.lineEdit_2.setText(data[3])
            # self.window.user_admin_check()
            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            self.close()
            self.window.show()
            self.window.ui.stackedWidget.setCurrentIndex(0)
        elif trafo_index == 7:
            import myoto_trifaz
            self.window = myoto_trifaz.OtoTrifazwindow()

            # self.window.ui.lineEdit_2.setText(data[3])
            # self.window.user_admin_check()
            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            self.close()
            self.window.show()
            self.window.ui.stackedWidget.setCurrentIndex(0)
        elif trafo_index == 8:
            import myharmonik
            self.window = myharmonik.Harmonikwindow()

            # self.window.ui.lineEdit_2.setText(data[3])
            # self.window.user_admin_check()
            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            self.close()
            self.window.show()
            self.window.ui.stackedWidget.setCurrentIndex(0)
        elif trafo_index == 9:
            import myups
            self.window = myups.UPSwindow()

            # self.window.ui.lineEdit_2.setText(data[3])
            # self.window.user_admin_check()
            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            self.close()
            self.window.show()
            self.window.ui.stackedWidget.setCurrentIndex(0)
        elif trafo_index == 10:
            import mymonoUI
            self.window = mymonoUI.MonoUIwindow()

            # self.window.ui.lineEdit_2.setText(data[3])
            # self.window.user_admin_check()
            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            self.close()
            self.window.show()
            self.window.ui.stackedWidget.setCurrentIndex(0)
    def open_kesit_hesaplama(self):


        self.window3 = KesitParamdialog()
        sender = self.sender()
        baglanti_turu = sender.objectName().split("_")[2]
        index = 0
        if baglanti_turu == "p":
            self.window3.kademe = int(sender.objectName().split("_")[len(sender.objectName().split("_")) - 1])
            self.window3.guc = self.ui.doubleSpinBox_guc.value()
            self.window3.gn1 = self.group_name_list_1
            self.window3.gn2 = self.group_name_list_2
            self.window3.sarim = "primer"
            self.window3.baglanti_turu = "mono"
        elif baglanti_turu == "sek":
            pass
        else:
            pass

        if self.window3.guc == 0:
            error_msjbox(title='Hesap Hatası', text='Lütfen Önce gücü giriniz.')
            return False
        else:

            self.window3.setWindowTitle("Kesit Parametreleri Sayfası")

        self.window3.karkas_yukseklik = self.ui.doubleSpinBox_karkas_yukseklik.value()
        self.window3.frekans = self.ui.doubleSpinBox_frekans.value()
        self.window3.karkas_en = self.ui.doubleSpinBox_karkas_en.value()
        self.window3.karkas_boy = self.ui.doubleSpinBox_karkas_boy.value()
        self.window3.c = self.ui.doubleSpinBox_c.value()
        self.window3.karkas_verim = self.ui.doubleSpinBox_karkas_verim.value()
        self.window3.gauss = self.ui.doubleSpinBox_gauss.value()
        self.window3.cu_yog = self.ui.doubleSpinBox_58.value()
        self.window3.al_yog = self.ui.doubleSpinBox_62.value()
        self.window3.di_yog = self.ui.doubleSpinBox_64.value()
        self.window3.ui.tabWidget_2.setCurrentIndex(self.window3.kademe - 1)
        self.window3.primer_sarim_yukseklik_toplam = self.primer_sarim_yukseklik_toplam
        global cu_par,cu_yog,al_par,al_yog,dig_par,dig_yog
        self.window3.cu_par = self.ui.doubleSpinBox_58.value()
        self.window3.cu_yog = self.ui.doubleSpinBox_59.value()
        self.window3.al_par = self.ui.doubleSpinBox_62.value()
        self.window3.al_yog = self.ui.doubleSpinBox_63.value()
        self.window3.dig_par = self.ui.doubleSpinBox_64.value()
        self.window3.dig_yog= self.ui.doubleSpinBox_65.value()

        self.window3.primer_izolasyon = self.primer_izolasyon
        self.window3.deger = self.deger
        for y in range(0, 10):
            for i in range(0, 58):
                self.object_multi_value_set(object=self.window3.group_name_list_sekonder[y][i],
                                            object2=self.window3.gn1[y][i])
            self.window3.group_name_list_sekonder[y][6].setValue(self.window3.gn1[y][6].value())

        self.window3.gl = self.window3.gn1[self.window3.kademe - 1]
        self.window3.gl2 = self.window3.gn2[self.window3.kademe - 1]
        self.window3.ui.tabWidget_2.tabBar().hide()
        self.window3.show()
        self.window3.ui.pushButton_kaydet.clicked.connect(self.kesit_man_spir_update)
        self.window3.ui.pushButton_kaydet.clicked.connect(
            lambda x: self.kesit_parametrelerini_yaz(window=self.window3, object=self.window3.gl,
                                                     object2=self.window3.group_name_list_sekonder[
                                                         self.window3.kademe - 1]))
        self.window3.ui.pushButton_kaydet_2.clicked.connect(self.window3.close)
# ======================  IZOLASYONLAR =========================
    def izolasyon_verileri_guncelle(self, object):
        self.ui.doubleSpinBox_primer_izo_deg.setValue(object.ui.doubleSpinBox.value())

        self.ui.doubleSpinBox_pri_sek_izo_deg.setValue(object.ui.doubleSpinBox_3.value())
        self.ui.doubleSpinBox_ekran_izo_deg.setValue(object.ui.doubleSpinBox_4.value())
        self.ui.doubleSpinBox_ekstra_izo_deg.setValue(object.ui.doubleSpinBox_5.value())
        self.ui.doubleSpinBox_primer_izo_tur.setValue(object.ui.doubleSpinBox_6.value())

        self.ui.doubleSpinBox_pri_sek_izo_tur.setValue(object.ui.doubleSpinBox_8.value())
        self.ui.checkBox_ekran_sec.setChecked(object.ui.checkBox.isChecked())
        self.ui.checkBox_ekstra.setChecked(object.ui.checkBox_2.isChecked())
    def izolasyon_deger_al(self, object):
        object.ui.doubleSpinBox.setValue(self.ui.doubleSpinBox_primer_izo_deg.value())

        object.ui.doubleSpinBox_3.setValue(self.ui.doubleSpinBox_pri_sek_izo_deg.value())
        object.ui.doubleSpinBox_4.setValue(self.ui.doubleSpinBox_ekran_izo_deg.value())
        object.ui.doubleSpinBox_5.setValue(self.ui.doubleSpinBox_ekstra_izo_deg.value())
        object.ui.doubleSpinBox_6.setValue(self.ui.doubleSpinBox_primer_izo_tur.value())

        object.ui.doubleSpinBox_8.setValue(self.ui.doubleSpinBox_pri_sek_izo_tur.value())
        object.ui.checkBox.setChecked(self.ui.checkBox_ekran_sec.isChecked())
        object.ui.checkBox_2.setChecked(self.ui.checkBox_ekstra.isChecked())
    def izolasyon_hesapla(self):
        self.primer_izolasyon = hp.primer_izolasyon_hesap(
            izo_deg=self.ui.doubleSpinBox_primer_izo_deg.value(),
            tur=self.ui.doubleSpinBox_primer_izo_tur.value(),
            kademe=int(self.ui.comboBox_primer.currentText()))


        self.toplam_izolasyon = self.primer_izolasyon

        return self.toplam_izolasyon
    def izolasyon_object_signals(self):
        self.ui.doubleSpinBox_primer_izo_deg.valueChanged.connect(self.hesaplamalari_guncelle)

        self.ui.doubleSpinBox_pri_sek_izo_deg.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_ekran_izo_deg.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_ekstra_izo_deg.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_primer_izo_tur.valueChanged.connect(self.hesaplamalari_guncelle)

        self.ui.doubleSpinBox_pri_sek_izo_tur.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.checkBox_ekran_sec.stateChanged.connect(self.hesaplamalari_guncelle)
        self.ui.checkBox_ekstra.stateChanged.connect(self.hesaplamalari_guncelle)
        self.ui.comboBox_primer.currentTextChanged.connect(self.hesaplamalari_guncelle)
 # ================= karkas =====================================
    def karkas_deger_al(self,object):

        self.ui.doubleSpinBox_karkas_en.setValue(object.ui.doubleSpinBox_karkas_en.value())
        self.ui.doubleSpinBox_karkas_boy.setValue(object.ui.doubleSpinBox_karkas_boy.value())
        self.karkas_hesaplama()
    def karkas_hesaplama(self):
        if self.ui.comboBox_sactipi.currentText()=="EI Sac":

            self.ui.doubleSpinBox_karkas_yuk_oto.setValue(hp.karkas_yuk(karkas_en=self.ui.doubleSpinBox_karkas_en.value()))
        elif self.ui.comboBox_sactipi.currentText()=="UI Sac":

            self.ui.doubleSpinBox_karkas_yuk_oto.setValue(hp.karkas_yuk_2(karkas_en=self.ui.doubleSpinBox_karkas_en.value()))

        self.ui.doubleSpinBox_karkas_cm_oto.setValue(hp.karkas_Ac_oto_2(c=self.ui.doubleSpinBox_c.value(),
                                                                   guc=self.ui.doubleSpinBox_guc.value(),
                                                                   frekans=self.ui.doubleSpinBox_frekans.value()))
        self.ui.doubleSpinBox_karkas_cm.setValue(hp.karkas_Ac(karkas_en=self.ui.doubleSpinBox_karkas_en.value(),
                                                           karkas_boy=self.ui.doubleSpinBox_karkas_boy.value()))
        if self.ui.doubleSpinBox_karkas_cm.value() >= self.ui.doubleSpinBox_karkas_cm_oto.value():
            self.ui.label_Ac_ok.setVisible(True)
            self.ui.label_Ac_error.setVisible(False)
        else:
            self.ui.label_Ac_ok.setVisible(False)
            self.ui.label_Ac_error.setVisible(True)
        if self.ui.doubleSpinBox_karkas_yukseklik.value() >= self.ui.doubleSpinBox_karkas_yuk_oto.value():
            self.ui.label_yuk_ok.setVisible(True)
            self.ui.label_yuk_error.setVisible(False)
        else:
            self.ui.label_yuk_ok.setVisible(False)
            self.ui.label_yuk_error.setVisible(True)
    def karkas_object_signals(self):
        self.ui.doubleSpinBox_karkas_en.valueChanged.connect(self.karkas_hesaplama)
        self.ui.doubleSpinBox_karkas_boy.valueChanged.connect(self.karkas_hesaplama)
        self.ui.doubleSpinBox_karkas_verim.valueChanged.connect(self.karkas_hesaplama)
        self.ui.doubleSpinBox_karkas_yukseklik.valueChanged.connect(self.karkas_hesaplama)
    # ======================  bosluk hesabı =========================
    def bosluk_hesapla(self):
        self.izolasyon_hesapla()
        gl = self.group_name_list_1
        primer_top_yuk = gl[0][42].value() + gl[1][42].value() + gl[2][42].value() + gl[3][42].value() + gl[4][
            42].value() + gl[5][42].value() + gl[6][42].value() + gl[7][42].value() + gl[8][42].value() + gl[9][
                             42].value()


        if self.ui.comboBox_sactipi.currentIndex() == 0 :
            bosluk = hp.bosluk_hesap_1(karkas_en=self.ui.doubleSpinBox_karkas_en.value(),
                                    primer_top_yuk=primer_top_yuk, sekonder_top_yuk=0,
                                    primer_izolasyon=self.primer_izolasyon)

        elif self.ui.comboBox_sactipi.currentIndex() == 1:
            bosluk = 0
            # bosluk = hp.bosluk_hesap_3(karkas_en=self.ui.doubleSpinBox_karkas_en.value(),
            #                         primer_top_yuk=primer_top_yuk, sekonder_top_yuk=0,
            #                         primer_izolasyon=self.primer_izolasyon,
            #                         kesme_sac_bosluk=self.ui.doubleSpinBox_nuvebosluk.value())
        else:
            bosluk = hp.bosluk_hesap_1(karkas_en=self.ui.doubleSpinBox_karkas_en.value(),
                                       primer_top_yuk=primer_top_yuk, sekonder_top_yuk=0,
                                       primer_izolasyon=self.primer_izolasyon)
        self.ui.doubleSpinBox_8.setValue(bosluk)
        if bosluk > 0 and self.ui.comboBox_sactipi.currentIndex() == 0:
            self.ui.comboBox_2.setCurrentIndex(0)
            self.ui.label_Ac_error_2.setVisible(False)
            self.ui.label_Ac_ok_2.setVisible(True)
        elif bosluk < 0 and self.ui.comboBox_sactipi.currentIndex() == 0:
            self.ui.comboBox_2.setCurrentIndex(1)
            self.ui.label_Ac_error_2.setVisible(True)
            self.ui.label_Ac_ok_2.setVisible(False)
        elif self.ui.comboBox_sactipi.currentIndex() == 1:
            self.ui.comboBox_2.setCurrentIndex(2)
            self.ui.label_Ac_error_2.setVisible(False)
            self.ui.label_Ac_ok_2.setVisible(False)
        else:
            pass
    # ======================  agırlık  hesabı =========================
    def agirlik_hesapla(self):
        gl = self.group_name_list_1
        primer_toplam_agirlik = gl[0][41].value() + gl[1][41].value() + gl[2][41].value() + gl[3][41].value() + \
                                gl[4][41].value() + gl[5][41].value() + gl[6][41].value() + gl[7][41].value() + \
                                gl[8][41].value() + gl[9][41].value()
        primer_cu_agirlik = gl[0][41].value() * gl[0][11].currentIndex() + gl[1][41].value() * gl[1][
            11].currentIndex() + gl[2][41].value() * gl[2][11].currentIndex() + gl[3][41].value() * gl[3][
                                11].currentIndex() + gl[4][41].value() * gl[4][11].currentIndex() + gl[5][
                                41].value() * gl[5][11].currentIndex() + gl[6][41].value() * gl[6][
                                11].currentIndex() + gl[7][41].value() * gl[7][11].currentIndex() + gl[8][
                                41].value() * gl[8][11].currentIndex() + gl[9][41].value() * gl[9][
                                11].currentIndex()
        primer_al_agirlik = primer_toplam_agirlik - primer_cu_agirlik





        self.ui.doubleSpinBox_toplamagirlik_al.setValue(primer_al_agirlik  )

        self.ui.doubleSpinBox_toplamagirlik_cu.setValue(primer_cu_agirlik )

        self.ui.doubleSpinBox_primeragirlik_al.setValue(primer_al_agirlik)

        self.ui.doubleSpinBox_primeragirlik_cu.setValue(primer_cu_agirlik)


    # ======================  olcu hesabı  =========================
    def olcu_hesapla(self):
        self.ui.doubleSpinBox_olcu_a.setValue(self.ui.doubleSpinBox_karkas_en.value() * 3)
        self.ui.doubleSpinBox_olcu_b.setValue(
            self.ui.doubleSpinBox_karkas_boy.value() + self.ui.doubleSpinBox_klemens_a_deg.value() + self.ui.doubleSpinBox_ayak_a_deg.value())
        self.ui.doubleSpinBox_olcu_c.setValue(
            self.ui.doubleSpinBox_karkas_en.value() * 2.5 + self.ui.doubleSpinBox_klemens_b_deg.value())

        if self.ui.lineEdit_klemens_adi.text() != "":
            self.ui.label_klemens_error.setVisible(False)
            self.ui.lineEdit_klemens.setText(self.ui.lineEdit_klemens_adi.text() + " / " + str(
                int(self.ui.doubleSpinBox_klemens_a_deg.value())) + " / " + str(
                int(self.ui.doubleSpinBox_klemens_b_deg.value())))

        else:
            self.ui.label_klemens_error.setVisible(True)
            self.ui.lineEdit_klemens.setText("")
        if self.ui.lineEdit_ayak_adi.text() != "":
            self.ui.label_ayak_error.setVisible(False)
            self.ui.lineEdit_ayak.setText(
                self.ui.lineEdit_ayak_adi.text() + " / " + str(int(self.ui.doubleSpinBox_ayak_a_deg.value())))

        else:
            self.ui.label_ayak_error.setVisible(True)
            self.ui.lineEdit_ayak.setText("")
        self.trafoolcu_hesapla()
    def trafoolcu_hesapla(self):
        if self.ui.comboBox_sactipi.currentIndex() == 1:

            self.ui.doubleSpinBox_trafoolcu_a.setValue(math.ceil(self.ui.doubleSpinBox_karkas_en.value() * 2 + 2 * (
                        self.ui.doubleSpinBox_karkas_en.value() / 2 + self.ui.doubleSpinBox_nuvebosluk.value())))
            self.ui.doubleSpinBox_trafoolcu_c.setValue(math.ceil(
                self.ui.doubleSpinBox_karkas_yukseklik.value() + self.ui.doubleSpinBox_karkas_en.value() * 0.15 + self.ui.doubleSpinBox_karkas_en.value()))
            self.ui.doubleSpinBox_sacagirlik.setValue(0)
        else:
            self.ui.doubleSpinBox_trafoolcu_a.setValue(math.ceil(self.ui.doubleSpinBox_karkas_en.value() * 3))
            self.ui.doubleSpinBox_trafoolcu_c.setValue(math.ceil(self.ui.doubleSpinBox_karkas_en.value() * 2.5))
            self.ui.doubleSpinBox_sacagirlik.setValue(hp.sac_agirlik(karkas_en=self.ui.doubleSpinBox_karkas_en.value(),
                                                                  sac=self.ui.doubleSpinBox_sac.value()))

        self.ui.doubleSpinBox_trafoolcu_b.setValue(
            self.ui.doubleSpinBox_karkas_boy.value() + self.ui.doubleSpinBox_karkas_en.value())

        self.ui.doubleSpinBox_trafoolcu_d.setValue(
            self.ui.doubleSpinBox_trafoolcu_a.value() - self.ui.doubleSpinBox_karkas_en.value() / 2 )
        self.ui.doubleSpinBox_trafoolcu_e.setValue(
            self.ui.doubleSpinBox_karkas_boy.value() + self.ui.doubleSpinBox_karkas_en.value() / 2 )
        self.ui.doubleSpinBox_trafoolcu_f.setValue(0)
    def klemens_deger_al(self, klemens_name, a, b, akim):
        self.ui.lineEdit_klemens_adi.setText(klemens_name)
        self.ui.doubleSpinBox_klemens_a_deg.setValue(a)
        self.ui.doubleSpinBox_klemens_b_deg.setValue(b)
        self.ui.doubleSpinBox_klemens_akim.setValue(akim)
        self.olcu_hesapla()
    def ayak_deger_al(self, ayak_name, a):
        self.ui.lineEdit_ayak_adi.setText(ayak_name)
        self.ui.doubleSpinBox_ayak_a_deg.setValue(a)

        self.olcu_hesapla()
# ================= PRIMER ===============================
    def primer_veri_kumesi(self):
        self.group_list_primer_1 = [self.ui.doubleSpinBox_akim_p_1, self.ui.doubleSpinBox_akim_2_p_1,
                                    self.ui.doubleSpinBox_cap_p_1,
                                    self.ui.doubleSpinBox_cap_2_p_1, self.ui.doubleSpinBox_sipir_p_1,
                                    self.ui.doubleSpinBox_kesit_p_1,
                                    self.ui.doubleSpinBox_sipir_2_p_1, self.ui.doubleSpinBox_v_p_1,
                                    self.ui.comboBox_folyotel_p_1,
                                    self.ui.comboBox_folyotel_p_1, self.ui.comboBox_karetel_p_1,
                                    self.ui.comboBox_tel_p_1,
                                    self.ui.doubleSpinBox_folyotel_11_p_1, self.ui.doubleSpinBox_folyotel_12_p_1,
                                    self.ui.doubleSpinBox_folyotel_21_p_1, self.ui.doubleSpinBox_folyotel_22_p_1,
                                    self.ui.doubleSpinBox_folyotel_31_p_1, self.ui.doubleSpinBox_folyotel_32_p_1,
                                    self.ui.doubleSpinBox_folyotel_41_p_1, self.ui.doubleSpinBox_folyotel_42_p_1,
                                    self.ui.doubleSpinBox_kapton_1_p_1, self.ui.doubleSpinBox_kapton_2_p_1,
                                    self.ui.doubleSpinBox_kapton_3_p_1, self.ui.doubleSpinBox_kapton_4_p_1,
                                    self.ui.doubleSpinBox_kare_tel_11_p_1, self.ui.doubleSpinBox_kare_tel_12_p_1,
                                    self.ui.doubleSpinBox_kare_tel_21_p_1, self.ui.doubleSpinBox_kare_tel_22_p_1,
                                    self.ui.doubleSpinBox_kare_tel_31_p_1, self.ui.doubleSpinBox_kare_tel_32_p_1,
                                    self.ui.doubleSpinBox_kare_tel_41_p_1, self.ui.doubleSpinBox_kare_tel_42_p_1,
                                    self.ui.comboBox_telkademe_p_1, self.ui.lineEdit_no_p_1,
                                    self.ui.doubleSpinBox_kesit_2_p_1,
                                    self.ui.doubleSpinBox_tel_en_1, self.ui.doubleSpinBox_tel_yuk_1,
                                    self.ui.doubleSpinBox_spirkat_1,  # 37
                                    self.ui.doubleSpinBox_kat_1, self.ui.doubleSpinBox_katbosluk_1,
                                    self.ui.doubleSpinBox_tel_uzunluk_1,
                                    self.ui.doubleSpinBox_tel_agirlik_1, self.ui.doubleSpinBox_sarim_yukseklik_1,
                                    self.ui.doubleSpinBox_sonkat_spir_1, self.ui.checkBox_sipir_man_p_10,
                                    self.ui.pushButton_h1_p_buton_21_p_1, self.ui.pushButton_karetel_p_1,
                                    self.ui.pushButton_folyotel_p_1, self.ui.pushButton_kapton_p_1,
                                    self.ui.checkBox_sipir_man_p_1,
                                    self.ui.label_kesit_ok_p_1, self.ui.label_kesit_error_p_1,
                                    self.ui.label_akim_ok_p_1, self.ui.label_akim_error_p_1,
                                    self.ui.doubleSpinBox_mancap_p_11,  # 54
                                    self.ui.doubleSpinBox_mancap_p_12, self.ui.doubleSpinBox_mancap_p_13,
                                    self.ui.doubleSpinBox_mancap_p_14]  # 57
        self.group_list_primer_2 = [self.ui.doubleSpinBox_akim_p_2, self.ui.doubleSpinBox_akim_2_p_2,
                                    self.ui.doubleSpinBox_cap_p_2,
                                    self.ui.doubleSpinBox_cap_2_p_2, self.ui.doubleSpinBox_sipir_p_2,
                                    self.ui.doubleSpinBox_kesit_p_2,
                                    self.ui.doubleSpinBox_sipir_2_p_2, self.ui.doubleSpinBox_v_p_2,
                                    self.ui.comboBox_folyotel_p_2,
                                    self.ui.comboBox_folyotel_p_2, self.ui.comboBox_karetel_p_2,
                                    self.ui.comboBox_tel_p_2,
                                    self.ui.doubleSpinBox_folyotel_11_p_2, self.ui.doubleSpinBox_folyotel_12_p_2,
                                    self.ui.doubleSpinBox_folyotel_21_p_2, self.ui.doubleSpinBox_folyotel_22_p_2,
                                    self.ui.doubleSpinBox_folyotel_31_p_2, self.ui.doubleSpinBox_folyotel_32_p_2,
                                    self.ui.doubleSpinBox_folyotel_41_p_2, self.ui.doubleSpinBox_folyotel_42_p_2,
                                    self.ui.doubleSpinBox_kapton_1_p_2, self.ui.doubleSpinBox_kapton_2_p_2,
                                    self.ui.doubleSpinBox_kapton_3_p_2, self.ui.doubleSpinBox_kapton_4_p_2,
                                    self.ui.doubleSpinBox_kare_tel_11_p_2, self.ui.doubleSpinBox_kare_tel_12_p_2,
                                    self.ui.doubleSpinBox_kare_tel_21_p_2, self.ui.doubleSpinBox_kare_tel_22_p_2,
                                    self.ui.doubleSpinBox_kare_tel_31_p_2, self.ui.doubleSpinBox_kare_tel_32_p_2,
                                    self.ui.doubleSpinBox_kare_tel_41_p_2, self.ui.doubleSpinBox_kare_tel_42_p_2,
                                    self.ui.comboBox_telkademe_p_2, self.ui.lineEdit_no_p_2,
                                    self.ui.doubleSpinBox_kesit_2_p_2,
                                    self.ui.doubleSpinBox_tel_en_2, self.ui.doubleSpinBox_tel_yuk_2,
                                    self.ui.doubleSpinBox_spirkat_2,
                                    self.ui.doubleSpinBox_kat_2, self.ui.doubleSpinBox_katbosluk_2,
                                    self.ui.doubleSpinBox_tel_uzunluk_2,
                                    self.ui.doubleSpinBox_tel_agirlik_2, self.ui.doubleSpinBox_sarim_yukseklik_2,
                                    self.ui.doubleSpinBox_sonkat_spir_2, self.ui.checkBox_sipir_man_p_2,
                                    self.ui.pushButton_h1_p_buton_21_p_2, self.ui.pushButton_karetel_p_2,
                                    self.ui.pushButton_folyotel_p_2, self.ui.pushButton_kapton_p_2,
                                    self.ui.checkBox_sipir_man_p_2,
                                    self.ui.label_kesit_ok_p_2, self.ui.label_kesit_error_p_2,
                                    self.ui.label_akim_ok_p_2, self.ui.label_akim_error_p_2,
                                    self.ui.doubleSpinBox_mancap_p_21,  # 54
                                    self.ui.doubleSpinBox_mancap_p_22, self.ui.doubleSpinBox_mancap_p_23,
                                    self.ui.doubleSpinBox_mancap_p_24]  # 57
        self.group_list_primer_3 = [self.ui.doubleSpinBox_akim_p_3, self.ui.doubleSpinBox_akim_2_p_3,
                                    self.ui.doubleSpinBox_cap_p_3,
                                    self.ui.doubleSpinBox_cap_2_p_3, self.ui.doubleSpinBox_sipir_p_3,
                                    self.ui.doubleSpinBox_kesit_p_3,
                                    self.ui.doubleSpinBox_sipir_2_p_3, self.ui.doubleSpinBox_v_p_3,
                                    self.ui.comboBox_folyotel_p_3,
                                    self.ui.comboBox_folyotel_p_3, self.ui.comboBox_karetel_p_3,
                                    self.ui.comboBox_tel_p_3,
                                    self.ui.doubleSpinBox_folyotel_11_p_3, self.ui.doubleSpinBox_folyotel_12_p_3,
                                    self.ui.doubleSpinBox_folyotel_21_p_3, self.ui.doubleSpinBox_folyotel_22_p_3,
                                    self.ui.doubleSpinBox_folyotel_31_p_3, self.ui.doubleSpinBox_folyotel_32_p_3,
                                    self.ui.doubleSpinBox_folyotel_41_p_3, self.ui.doubleSpinBox_folyotel_42_p_3,
                                    self.ui.doubleSpinBox_kapton_1_p_3, self.ui.doubleSpinBox_kapton_3_p_3,
                                    self.ui.doubleSpinBox_kapton_3_p_3, self.ui.doubleSpinBox_kapton_4_p_3,
                                    self.ui.doubleSpinBox_kare_tel_11_p_3, self.ui.doubleSpinBox_kare_tel_12_p_3,
                                    self.ui.doubleSpinBox_kare_tel_31_p_3, self.ui.doubleSpinBox_kare_tel_32_p_3,
                                    self.ui.doubleSpinBox_kare_tel_31_p_3, self.ui.doubleSpinBox_kare_tel_32_p_3,
                                    self.ui.doubleSpinBox_kare_tel_41_p_3, self.ui.doubleSpinBox_kare_tel_42_p_3,
                                    self.ui.comboBox_telkademe_p_3, self.ui.lineEdit_no_p_3,
                                    self.ui.doubleSpinBox_kesit_2_p_3,
                                    self.ui.doubleSpinBox_tel_en_3, self.ui.doubleSpinBox_tel_yuk_3,
                                    self.ui.doubleSpinBox_spirkat_3,
                                    self.ui.doubleSpinBox_kat_3, self.ui.doubleSpinBox_katbosluk_3,
                                    self.ui.doubleSpinBox_tel_uzunluk_3,
                                    self.ui.doubleSpinBox_tel_agirlik_3, self.ui.doubleSpinBox_sarim_yukseklik_3,
                                    self.ui.doubleSpinBox_sonkat_spir_3, self.ui.checkBox_sipir_man_p_3,
                                    self.ui.pushButton_h1_p_buton_21_p_3, self.ui.pushButton_karetel_p_3,
                                    self.ui.pushButton_folyotel_p_3, self.ui.pushButton_kapton_p_3,
                                    self.ui.checkBox_sipir_man_p_3,
                                    self.ui.label_kesit_ok_p_3, self.ui.label_kesit_error_p_3,
                                    self.ui.label_akim_ok_p_3, self.ui.label_akim_error_p_3,
                                    self.ui.doubleSpinBox_mancap_p_31,  # 54
                                    self.ui.doubleSpinBox_mancap_p_32, self.ui.doubleSpinBox_mancap_p_33,
                                    self.ui.doubleSpinBox_mancap_p_34]  # 57
        self.group_list_primer_4 = [self.ui.doubleSpinBox_akim_p_4, self.ui.doubleSpinBox_akim_2_p_4,
                                    self.ui.doubleSpinBox_cap_p_4,
                                    self.ui.doubleSpinBox_cap_2_p_4, self.ui.doubleSpinBox_sipir_p_4,
                                    self.ui.doubleSpinBox_kesit_p_4,
                                    self.ui.doubleSpinBox_sipir_2_p_4, self.ui.doubleSpinBox_v_p_4,
                                    self.ui.comboBox_folyotel_p_4,
                                    self.ui.comboBox_folyotel_p_4, self.ui.comboBox_karetel_p_4,
                                    self.ui.comboBox_tel_p_4,
                                    self.ui.doubleSpinBox_folyotel_11_p_4, self.ui.doubleSpinBox_folyotel_12_p_4,
                                    self.ui.doubleSpinBox_folyotel_21_p_4, self.ui.doubleSpinBox_folyotel_22_p_4,
                                    self.ui.doubleSpinBox_folyotel_31_p_4, self.ui.doubleSpinBox_folyotel_32_p_4,
                                    self.ui.doubleSpinBox_folyotel_41_p_4, self.ui.doubleSpinBox_folyotel_42_p_4,
                                    self.ui.doubleSpinBox_kapton_1_p_4, self.ui.doubleSpinBox_kapton_4_p_4,
                                    self.ui.doubleSpinBox_kapton_4_p_4, self.ui.doubleSpinBox_kapton_4_p_4,
                                    self.ui.doubleSpinBox_kare_tel_11_p_4, self.ui.doubleSpinBox_kare_tel_12_p_4,
                                    self.ui.doubleSpinBox_kare_tel_21_p_4, self.ui.doubleSpinBox_kare_tel_22_p_4,
                                    self.ui.doubleSpinBox_kare_tel_31_p_4, self.ui.doubleSpinBox_kare_tel_32_p_4,
                                    self.ui.doubleSpinBox_kare_tel_41_p_4, self.ui.doubleSpinBox_kare_tel_42_p_4,
                                    self.ui.comboBox_telkademe_p_4, self.ui.lineEdit_no_p_4,
                                    self.ui.doubleSpinBox_kesit_2_p_4,
                                    self.ui.doubleSpinBox_tel_en_4, self.ui.doubleSpinBox_tel_yuk_4,
                                    self.ui.doubleSpinBox_spirkat_4,
                                    self.ui.doubleSpinBox_kat_4, self.ui.doubleSpinBox_katbosluk_4,
                                    self.ui.doubleSpinBox_tel_uzunluk_4,
                                    self.ui.doubleSpinBox_tel_agirlik_4, self.ui.doubleSpinBox_sarim_yukseklik_4,
                                    self.ui.doubleSpinBox_sonkat_spir_4, self.ui.checkBox_sipir_man_p_4,
                                    self.ui.pushButton_h1_p_buton_21_p_4, self.ui.pushButton_karetel_p_4,
                                    self.ui.pushButton_folyotel_p_4, self.ui.pushButton_kapton_p_4,
                                    self.ui.checkBox_sipir_man_p_4,
                                    self.ui.label_kesit_ok_p_4, self.ui.label_kesit_error_p_4,
                                    self.ui.label_akim_ok_p_4, self.ui.label_akim_error_p_4,
                                    self.ui.doubleSpinBox_mancap_p_41,  # 54
                                    self.ui.doubleSpinBox_mancap_p_42, self.ui.doubleSpinBox_mancap_p_43,
                                    self.ui.doubleSpinBox_mancap_p_44]  # 57
        self.group_list_primer_5 = [self.ui.doubleSpinBox_akim_p_5, self.ui.doubleSpinBox_akim_2_p_5,
                                    self.ui.doubleSpinBox_cap_p_5,
                                    self.ui.doubleSpinBox_cap_2_p_5, self.ui.doubleSpinBox_sipir_p_5,
                                    self.ui.doubleSpinBox_kesit_p_5,
                                    self.ui.doubleSpinBox_sipir_2_p_5, self.ui.doubleSpinBox_v_p_5,
                                    self.ui.comboBox_folyotel_p_5,
                                    self.ui.comboBox_folyotel_p_5, self.ui.comboBox_karetel_p_5,
                                    self.ui.comboBox_tel_p_5,
                                    self.ui.doubleSpinBox_folyotel_11_p_5, self.ui.doubleSpinBox_folyotel_12_p_5,
                                    self.ui.doubleSpinBox_folyotel_21_p_5, self.ui.doubleSpinBox_folyotel_22_p_5,
                                    self.ui.doubleSpinBox_folyotel_31_p_5, self.ui.doubleSpinBox_folyotel_32_p_5,
                                    self.ui.doubleSpinBox_folyotel_41_p_5, self.ui.doubleSpinBox_folyotel_42_p_5,
                                    self.ui.doubleSpinBox_kapton_1_p_5, self.ui.doubleSpinBox_kapton_2_p_5,
                                    self.ui.doubleSpinBox_kapton_3_p_5, self.ui.doubleSpinBox_kapton_4_p_5,
                                    self.ui.doubleSpinBox_kare_tel_11_p_5, self.ui.doubleSpinBox_kare_tel_12_p_5,
                                    self.ui.doubleSpinBox_kare_tel_21_p_5, self.ui.doubleSpinBox_kare_tel_22_p_5,
                                    self.ui.doubleSpinBox_kare_tel_31_p_5, self.ui.doubleSpinBox_kare_tel_32_p_5,
                                    self.ui.doubleSpinBox_kare_tel_41_p_5, self.ui.doubleSpinBox_kare_tel_42_p_5,
                                    self.ui.comboBox_telkademe_p_5, self.ui.lineEdit_no_p_5,
                                    self.ui.doubleSpinBox_kesit_2_p_5,
                                    self.ui.doubleSpinBox_tel_en_5, self.ui.doubleSpinBox_tel_yuk_5,
                                    self.ui.doubleSpinBox_spirkat_5,
                                    self.ui.doubleSpinBox_kat_5, self.ui.doubleSpinBox_katbosluk_5,
                                    self.ui.doubleSpinBox_tel_uzunluk_5,
                                    self.ui.doubleSpinBox_tel_agirlik_5, self.ui.doubleSpinBox_sarim_yukseklik_5,
                                    self.ui.doubleSpinBox_sonkat_spir_5, self.ui.checkBox_sipir_man_p_5,
                                    self.ui.pushButton_h1_p_buton_21_p_5, self.ui.pushButton_karetel_p_5,
                                    self.ui.pushButton_folyotel_p_5, self.ui.pushButton_kapton_p_5,
                                    self.ui.checkBox_sipir_man_p_5,
                                    self.ui.label_kesit_ok_p_5, self.ui.label_kesit_error_p_5,
                                    self.ui.label_akim_ok_p_5, self.ui.label_akim_error_p_5,
                                    self.ui.doubleSpinBox_mancap_p_51,  # 54
                                    self.ui.doubleSpinBox_mancap_p_52, self.ui.doubleSpinBox_mancap_p_53,
                                    self.ui.doubleSpinBox_mancap_p_54]  # 57
        self.group_list_primer_6 = [self.ui.doubleSpinBox_akim_p_6, self.ui.doubleSpinBox_akim_2_p_6,
                                    self.ui.doubleSpinBox_cap_p_6,
                                    self.ui.doubleSpinBox_cap_2_p_6, self.ui.doubleSpinBox_sipir_p_6,
                                    self.ui.doubleSpinBox_kesit_p_6,
                                    self.ui.doubleSpinBox_sipir_2_p_6, self.ui.doubleSpinBox_v_p_6,
                                    self.ui.comboBox_folyotel_p_6,
                                    self.ui.comboBox_folyotel_p_6, self.ui.comboBox_karetel_p_6,
                                    self.ui.comboBox_tel_p_6,
                                    self.ui.doubleSpinBox_folyotel_11_p_6, self.ui.doubleSpinBox_folyotel_12_p_6,
                                    self.ui.doubleSpinBox_folyotel_21_p_6, self.ui.doubleSpinBox_folyotel_22_p_6,
                                    self.ui.doubleSpinBox_folyotel_31_p_6, self.ui.doubleSpinBox_folyotel_32_p_6,
                                    self.ui.doubleSpinBox_folyotel_41_p_6, self.ui.doubleSpinBox_folyotel_42_p_6,
                                    self.ui.doubleSpinBox_kapton_1_p_6, self.ui.doubleSpinBox_kapton_2_p_6,
                                    self.ui.doubleSpinBox_kapton_3_p_6, self.ui.doubleSpinBox_kapton_4_p_6,
                                    self.ui.doubleSpinBox_kare_tel_11_p_6, self.ui.doubleSpinBox_kare_tel_12_p_6,
                                    self.ui.doubleSpinBox_kare_tel_21_p_6, self.ui.doubleSpinBox_kare_tel_22_p_6,
                                    self.ui.doubleSpinBox_kare_tel_31_p_6, self.ui.doubleSpinBox_kare_tel_32_p_6,
                                    self.ui.doubleSpinBox_kare_tel_41_p_6, self.ui.doubleSpinBox_kare_tel_42_p_6,
                                    self.ui.comboBox_telkademe_p_6, self.ui.lineEdit_no_p_6,
                                    self.ui.doubleSpinBox_kesit_2_p_6,
                                    self.ui.doubleSpinBox_tel_en_6, self.ui.doubleSpinBox_tel_yuk_6,
                                    self.ui.doubleSpinBox_spirkat_6,
                                    self.ui.doubleSpinBox_kat_6, self.ui.doubleSpinBox_katbosluk_6,
                                    self.ui.doubleSpinBox_tel_uzunluk_6,
                                    self.ui.doubleSpinBox_tel_agirlik_6, self.ui.doubleSpinBox_sarim_yukseklik_6,
                                    self.ui.doubleSpinBox_sonkat_spir_6, self.ui.checkBox_sipir_man_p_6,
                                    self.ui.pushButton_h1_p_buton_21_p_6, self.ui.pushButton_karetel_p_6,
                                    self.ui.pushButton_folyotel_p_6, self.ui.pushButton_kapton_p_6,
                                    self.ui.checkBox_sipir_man_p_6,
                                    self.ui.label_kesit_ok_p_6, self.ui.label_kesit_error_p_6,
                                    self.ui.label_akim_ok_p_6, self.ui.label_akim_error_p_6,
                                    self.ui.doubleSpinBox_mancap_p_61,  # 54
                                    self.ui.doubleSpinBox_mancap_p_62, self.ui.doubleSpinBox_mancap_p_63,
                                    self.ui.doubleSpinBox_mancap_p_64]  # 57
        self.group_list_primer_7 = [self.ui.doubleSpinBox_akim_p_7, self.ui.doubleSpinBox_akim_2_p_7,
                                    self.ui.doubleSpinBox_cap_p_7,
                                    self.ui.doubleSpinBox_cap_2_p_7, self.ui.doubleSpinBox_sipir_p_7,
                                    self.ui.doubleSpinBox_kesit_p_7,
                                    self.ui.doubleSpinBox_sipir_2_p_7, self.ui.doubleSpinBox_v_p_7,
                                    self.ui.comboBox_folyotel_p_7,
                                    self.ui.comboBox_folyotel_p_7, self.ui.comboBox_karetel_p_7,
                                    self.ui.comboBox_tel_p_7,
                                    self.ui.doubleSpinBox_folyotel_11_p_7, self.ui.doubleSpinBox_folyotel_12_p_7,
                                    self.ui.doubleSpinBox_folyotel_21_p_7, self.ui.doubleSpinBox_folyotel_22_p_7,
                                    self.ui.doubleSpinBox_folyotel_31_p_7, self.ui.doubleSpinBox_folyotel_32_p_7,
                                    self.ui.doubleSpinBox_folyotel_41_p_7, self.ui.doubleSpinBox_folyotel_42_p_7,
                                    self.ui.doubleSpinBox_kapton_1_p_7, self.ui.doubleSpinBox_kapton_2_p_7,
                                    self.ui.doubleSpinBox_kapton_3_p_7, self.ui.doubleSpinBox_kapton_4_p_7,
                                    self.ui.doubleSpinBox_kare_tel_11_p_7, self.ui.doubleSpinBox_kare_tel_12_p_7,
                                    self.ui.doubleSpinBox_kare_tel_21_p_7, self.ui.doubleSpinBox_kare_tel_22_p_7,
                                    self.ui.doubleSpinBox_kare_tel_31_p_7, self.ui.doubleSpinBox_kare_tel_32_p_7,
                                    self.ui.doubleSpinBox_kare_tel_41_p_7, self.ui.doubleSpinBox_kare_tel_42_p_7,
                                    self.ui.comboBox_telkademe_p_7, self.ui.lineEdit_no_p_7,
                                    self.ui.doubleSpinBox_kesit_2_p_7,
                                    self.ui.doubleSpinBox_tel_en_7, self.ui.doubleSpinBox_tel_yuk_7,
                                    self.ui.doubleSpinBox_spirkat_7,
                                    self.ui.doubleSpinBox_kat_7, self.ui.doubleSpinBox_katbosluk_7,
                                    self.ui.doubleSpinBox_tel_uzunluk_7,
                                    self.ui.doubleSpinBox_tel_agirlik_7, self.ui.doubleSpinBox_sarim_yukseklik_7,
                                    self.ui.doubleSpinBox_sonkat_spir_7, self.ui.checkBox_sipir_man_p_7,
                                    self.ui.pushButton_h1_p_buton_21_p_7, self.ui.pushButton_karetel_p_7,
                                    self.ui.pushButton_folyotel_p_7, self.ui.pushButton_kapton_p_7,
                                    self.ui.checkBox_sipir_man_p_7,
                                    self.ui.label_kesit_ok_p_7, self.ui.label_kesit_error_p_7,
                                    self.ui.label_akim_ok_p_7, self.ui.label_akim_error_p_7,
                                    self.ui.doubleSpinBox_mancap_p_71,  # 54
                                    self.ui.doubleSpinBox_mancap_p_72, self.ui.doubleSpinBox_mancap_p_73,
                                    self.ui.doubleSpinBox_mancap_p_74]  # 57
        self.group_list_primer_8 = [self.ui.doubleSpinBox_akim_p_8, self.ui.doubleSpinBox_akim_2_p_8,
                                    self.ui.doubleSpinBox_cap_p_8,
                                    self.ui.doubleSpinBox_cap_2_p_8, self.ui.doubleSpinBox_sipir_p_8,
                                    self.ui.doubleSpinBox_kesit_p_8,
                                    self.ui.doubleSpinBox_sipir_2_p_8, self.ui.doubleSpinBox_v_p_8,
                                    self.ui.comboBox_folyotel_p_8,
                                    self.ui.comboBox_folyotel_p_8, self.ui.comboBox_karetel_p_8,
                                    self.ui.comboBox_tel_p_8,
                                    self.ui.doubleSpinBox_folyotel_11_p_8, self.ui.doubleSpinBox_folyotel_12_p_8,
                                    self.ui.doubleSpinBox_folyotel_21_p_8, self.ui.doubleSpinBox_folyotel_22_p_8,
                                    self.ui.doubleSpinBox_folyotel_31_p_8, self.ui.doubleSpinBox_folyotel_32_p_8,
                                    self.ui.doubleSpinBox_folyotel_41_p_8, self.ui.doubleSpinBox_folyotel_42_p_8,
                                    self.ui.doubleSpinBox_kapton_1_p_8, self.ui.doubleSpinBox_kapton_2_p_8,
                                    self.ui.doubleSpinBox_kapton_3_p_8, self.ui.doubleSpinBox_kapton_4_p_8,
                                    self.ui.doubleSpinBox_kare_tel_11_p_8, self.ui.doubleSpinBox_kare_tel_12_p_8,
                                    self.ui.doubleSpinBox_kare_tel_21_p_8, self.ui.doubleSpinBox_kare_tel_22_p_8,
                                    self.ui.doubleSpinBox_kare_tel_31_p_8, self.ui.doubleSpinBox_kare_tel_32_p_8,
                                    self.ui.doubleSpinBox_kare_tel_41_p_8, self.ui.doubleSpinBox_kare_tel_42_p_8,
                                    self.ui.comboBox_telkademe_p_8, self.ui.lineEdit_no_p_8,
                                    self.ui.doubleSpinBox_kesit_2_p_8,
                                    self.ui.doubleSpinBox_tel_en_8, self.ui.doubleSpinBox_tel_yuk_8,
                                    self.ui.doubleSpinBox_spirkat_8,
                                    self.ui.doubleSpinBox_kat_8, self.ui.doubleSpinBox_katbosluk_8,
                                    self.ui.doubleSpinBox_tel_uzunluk_8,
                                    self.ui.doubleSpinBox_tel_agirlik_8, self.ui.doubleSpinBox_sarim_yukseklik_8,
                                    self.ui.doubleSpinBox_sonkat_spir_8, self.ui.checkBox_sipir_man_p_8,
                                    self.ui.pushButton_h1_p_buton_21_p_8, self.ui.pushButton_karetel_p_8,
                                    self.ui.pushButton_folyotel_p_8, self.ui.pushButton_kapton_p_8,
                                    self.ui.checkBox_sipir_man_p_8,
                                    self.ui.label_kesit_ok_p_8, self.ui.label_kesit_error_p_8,
                                    self.ui.label_akim_ok_p_8, self.ui.label_akim_error_p_8,
                                    self.ui.doubleSpinBox_mancap_p_81,  # 54
                                    self.ui.doubleSpinBox_mancap_p_82, self.ui.doubleSpinBox_mancap_p_83,
                                    self.ui.doubleSpinBox_mancap_p_84]  # 57
        self.group_list_primer_9 = [self.ui.doubleSpinBox_akim_p_9, self.ui.doubleSpinBox_akim_2_p_9,
                                    self.ui.doubleSpinBox_cap_p_9,
                                    self.ui.doubleSpinBox_cap_2_p_9, self.ui.doubleSpinBox_sipir_p_9,
                                    self.ui.doubleSpinBox_kesit_p_9,
                                    self.ui.doubleSpinBox_sipir_2_p_9, self.ui.doubleSpinBox_v_p_9,
                                    self.ui.comboBox_folyotel_p_9,
                                    self.ui.comboBox_folyotel_p_9, self.ui.comboBox_karetel_p_9,
                                    self.ui.comboBox_tel_p_9,
                                    self.ui.doubleSpinBox_folyotel_11_p_9, self.ui.doubleSpinBox_folyotel_12_p_9,
                                    self.ui.doubleSpinBox_folyotel_21_p_9, self.ui.doubleSpinBox_folyotel_22_p_9,
                                    self.ui.doubleSpinBox_folyotel_31_p_9, self.ui.doubleSpinBox_folyotel_32_p_9,
                                    self.ui.doubleSpinBox_folyotel_41_p_9, self.ui.doubleSpinBox_folyotel_42_p_9,
                                    self.ui.doubleSpinBox_kapton_1_p_9, self.ui.doubleSpinBox_kapton_2_p_9,
                                    self.ui.doubleSpinBox_kapton_3_p_9, self.ui.doubleSpinBox_kapton_4_p_9,
                                    self.ui.doubleSpinBox_kare_tel_11_p_9, self.ui.doubleSpinBox_kare_tel_12_p_9,
                                    self.ui.doubleSpinBox_kare_tel_21_p_9, self.ui.doubleSpinBox_kare_tel_22_p_9,
                                    self.ui.doubleSpinBox_kare_tel_31_p_9, self.ui.doubleSpinBox_kare_tel_32_p_9,
                                    self.ui.doubleSpinBox_kare_tel_41_p_9, self.ui.doubleSpinBox_kare_tel_42_p_9,
                                    self.ui.comboBox_telkademe_p_9, self.ui.lineEdit_no_p_9,
                                    self.ui.doubleSpinBox_kesit_2_p_9,
                                    self.ui.doubleSpinBox_tel_en_9, self.ui.doubleSpinBox_tel_yuk_9,
                                    self.ui.doubleSpinBox_spirkat_9,
                                    self.ui.doubleSpinBox_kat_9, self.ui.doubleSpinBox_katbosluk_9,
                                    self.ui.doubleSpinBox_tel_uzunluk_9,
                                    self.ui.doubleSpinBox_tel_agirlik_9, self.ui.doubleSpinBox_sarim_yukseklik_9,
                                    self.ui.doubleSpinBox_sonkat_spir_9, self.ui.checkBox_sipir_man_p_9,
                                    self.ui.pushButton_h1_p_buton_21_p_9, self.ui.pushButton_karetel_p_9,
                                    self.ui.pushButton_folyotel_p_9, self.ui.pushButton_kapton_p_9,
                                    self.ui.checkBox_sipir_man_p_9,
                                    self.ui.label_kesit_ok_p_9, self.ui.label_kesit_error_p_9,
                                    self.ui.label_akim_ok_p_9, self.ui.label_akim_error_p_9,
                                    self.ui.doubleSpinBox_mancap_p_91,  # 54
                                    self.ui.doubleSpinBox_mancap_p_92, self.ui.doubleSpinBox_mancap_p_93,
                                    self.ui.doubleSpinBox_mancap_p_94]  # 57
        self.group_list_primer_10 = [self.ui.doubleSpinBox_akim_p_10, self.ui.doubleSpinBox_akim_2_p_10,
                                     self.ui.doubleSpinBox_cap_p_10,
                                     self.ui.doubleSpinBox_cap_2_p_10, self.ui.doubleSpinBox_sipir_p_10,
                                     self.ui.doubleSpinBox_kesit_p_10,
                                     self.ui.doubleSpinBox_sipir_2_p_10, self.ui.doubleSpinBox_v_p_10,
                                     self.ui.comboBox_folyotel_p_10,
                                     self.ui.comboBox_folyotel_p_10, self.ui.comboBox_karetel_p_10,# 10
                                     self.ui.comboBox_tel_p_10,
                                     self.ui.doubleSpinBox_folyotel_11_p_10, self.ui.doubleSpinBox_folyotel_12_p_10,
                                     self.ui.doubleSpinBox_folyotel_21_p_10, self.ui.doubleSpinBox_folyotel_22_p_10,
                                     self.ui.doubleSpinBox_folyotel_31_p_10, self.ui.doubleSpinBox_folyotel_32_p_10,
                                     self.ui.doubleSpinBox_folyotel_41_p_10, self.ui.doubleSpinBox_folyotel_42_p_10,
                                     self.ui.doubleSpinBox_kapton_1_p_10, self.ui.doubleSpinBox_kapton_2_p_10,
                                     self.ui.doubleSpinBox_kapton_3_p_10, self.ui.doubleSpinBox_kapton_4_p_10,
                                     self.ui.doubleSpinBox_kare_tel_11_p_10, self.ui.doubleSpinBox_kare_tel_12_p_10,
                                     # 25
                                     self.ui.doubleSpinBox_kare_tel_21_p_10, self.ui.doubleSpinBox_kare_tel_22_p_10,
                                     self.ui.doubleSpinBox_kare_tel_31_p_10, self.ui.doubleSpinBox_kare_tel_32_p_10,
                                     self.ui.doubleSpinBox_kare_tel_41_p_10, self.ui.doubleSpinBox_kare_tel_42_p_10,
                                     self.ui.comboBox_telkademe_p_10, self.ui.lineEdit_no_p_10,
                                     self.ui.doubleSpinBox_kesit_2_p_10,
                                     self.ui.doubleSpinBox_tel_en_10, self.ui.doubleSpinBox_tel_yuk_10,
                                     self.ui.doubleSpinBox_spirkat_10,  # 37
                                     self.ui.doubleSpinBox_kat_10, self.ui.doubleSpinBox_katbosluk_10,
                                     self.ui.doubleSpinBox_tel_uzunluk_10,
                                     self.ui.doubleSpinBox_tel_agirlik_10, self.ui.doubleSpinBox_sarim_yukseklik_10,
                                     self.ui.doubleSpinBox_sonkat_spir_10, self.ui.checkBox_sipir_man_p_10,
                                     self.ui.pushButton_h1_p_buton_21_p_10, self.ui.pushButton_karetel_p_10,
                                     self.ui.pushButton_folyotel_p_10, self.ui.pushButton_kapton_p_10,
                                     self.ui.checkBox_sipir_man_p_10,
                                     self.ui.label_kesit_ok_p_10, self.ui.label_kesit_error_p_10,
                                     self.ui.label_akim_ok_p_10, self.ui.label_akim_error_p_10,
                                     self.ui.doubleSpinBox_mancap_p_101,  # 54
                                     self.ui.doubleSpinBox_mancap_p_102, self.ui.doubleSpinBox_mancap_p_103,
                                     self.ui.doubleSpinBox_mancap_p_104]  # 57 #53
        self.group_name_list_1 = [self.group_list_primer_1, self.group_list_primer_2, self.group_list_primer_3,
                                  self.group_list_primer_4, self.group_list_primer_5, self.group_list_primer_6,
                                  self.group_list_primer_7, self.group_list_primer_8, self.group_list_primer_9,
                                  self.group_list_primer_10]

        self.group_list_primer_11 = [self.ui.doubleSpinBox_v_p1, self.ui.doubleSpinBox_h1_p_sipir_1,
                                     self.ui.doubleSpinBox_h1_p_kesit_1, self.ui.doubleSpinBox_h1_p_cap_1,
                                     self.ui.doubleSpinBox_h1_p_akim_1, self.ui.doubleSpinBox_h1_p_sipir_21,
                                     self.ui.doubleSpinBox_h1_p_kesit_21, self.ui.doubleSpinBox_h1_p_cap_21,
                                     self.ui.doubleSpinBox_h1_p_akim_21, self.ui.comboBox_tel_p1,
                                     self.ui.label_kesit_ok_1, self.ui.label_kesit_error_1]
        self.group_list_primer_12 = [self.ui.doubleSpinBox_v_p2, self.ui.doubleSpinBox_h1_p_sipir_2,
                                     self.ui.doubleSpinBox_h1_p_kesit_2, self.ui.doubleSpinBox_h1_p_cap_2,
                                     self.ui.doubleSpinBox_h1_p_akim_2, self.ui.doubleSpinBox_h1_p_sipir_22,
                                     self.ui.doubleSpinBox_h1_p_kesit_22, self.ui.doubleSpinBox_h1_p_cap_22,
                                     self.ui.doubleSpinBox_h1_p_akim_22, self.ui.comboBox_tel_p2,
                                     self.ui.label_kesit_ok_2, self.ui.label_kesit_error_2]
        self.group_list_primer_13 = [self.ui.doubleSpinBox_v_p3, self.ui.doubleSpinBox_h1_p_sipir_3,
                                     self.ui.doubleSpinBox_h1_p_kesit_3, self.ui.doubleSpinBox_h1_p_cap_3,
                                     self.ui.doubleSpinBox_h1_p_akim_3, self.ui.doubleSpinBox_h1_p_sipir_23,
                                     self.ui.doubleSpinBox_h1_p_kesit_23, self.ui.doubleSpinBox_h1_p_cap_23,
                                     self.ui.doubleSpinBox_h1_p_akim_23, self.ui.comboBox_tel_p3,
                                     self.ui.label_kesit_ok_3, self.ui.label_kesit_error_3]
        self.group_list_primer_14 = [self.ui.doubleSpinBox_v_p4, self.ui.doubleSpinBox_h1_p_sipir_4,
                                     self.ui.doubleSpinBox_h1_p_kesit_4, self.ui.doubleSpinBox_h1_p_cap_4,
                                     self.ui.doubleSpinBox_h1_p_akim_4, self.ui.doubleSpinBox_h1_p_sipir_24,
                                     self.ui.doubleSpinBox_h1_p_kesit_24, self.ui.doubleSpinBox_h1_p_cap_24,
                                     self.ui.doubleSpinBox_h1_p_akim_24, self.ui.comboBox_tel_p4,
                                     self.ui.label_kesit_ok_4, self.ui.label_kesit_error_4]
        self.group_list_primer_15 = [self.ui.doubleSpinBox_v_p5, self.ui.doubleSpinBox_h1_p_sipir_5,
                                     self.ui.doubleSpinBox_h1_p_kesit_5, self.ui.doubleSpinBox_h1_p_cap_5,
                                     self.ui.doubleSpinBox_h1_p_akim_5, self.ui.doubleSpinBox_h1_p_sipir_25,
                                     self.ui.doubleSpinBox_h1_p_kesit_25, self.ui.doubleSpinBox_h1_p_cap_25,
                                     self.ui.doubleSpinBox_h1_p_akim_25, self.ui.comboBox_tel_p5,
                                     self.ui.label_kesit_ok_5, self.ui.label_kesit_error_5]
        self.group_list_primer_16 = [self.ui.doubleSpinBox_v_p6, self.ui.doubleSpinBox_h1_p_sipir_6,
                                     self.ui.doubleSpinBox_h1_p_kesit_6, self.ui.doubleSpinBox_h1_p_cap_6,
                                     self.ui.doubleSpinBox_h1_p_akim_6, self.ui.doubleSpinBox_h1_p_sipir_26,
                                     self.ui.doubleSpinBox_h1_p_kesit_26, self.ui.doubleSpinBox_h1_p_cap_26,
                                     self.ui.doubleSpinBox_h1_p_akim_26, self.ui.comboBox_tel_p6,
                                     self.ui.label_kesit_ok_6, self.ui.label_kesit_error_6]
        self.group_list_primer_17 = [self.ui.doubleSpinBox_v_p7, self.ui.doubleSpinBox_h1_p_sipir_7,
                                     self.ui.doubleSpinBox_h1_p_kesit_7, self.ui.doubleSpinBox_h1_p_cap_7,
                                     self.ui.doubleSpinBox_h1_p_akim_7, self.ui.doubleSpinBox_h1_p_sipir_27,
                                     self.ui.doubleSpinBox_h1_p_kesit_27, self.ui.doubleSpinBox_h1_p_cap_27,
                                     self.ui.doubleSpinBox_h1_p_akim_27, self.ui.comboBox_tel_p7,
                                     self.ui.label_kesit_ok_7, self.ui.label_kesit_error_7]
        self.group_list_primer_18 = [self.ui.doubleSpinBox_v_p8, self.ui.doubleSpinBox_h1_p_sipir_8,
                                     self.ui.doubleSpinBox_h1_p_kesit_8, self.ui.doubleSpinBox_h1_p_cap_8,
                                     self.ui.doubleSpinBox_h1_p_akim_8, self.ui.doubleSpinBox_h1_p_sipir_28,
                                     self.ui.doubleSpinBox_h1_p_kesit_28, self.ui.doubleSpinBox_h1_p_cap_28,
                                     self.ui.doubleSpinBox_h1_p_akim_28, self.ui.comboBox_tel_p8,
                                     self.ui.label_kesit_ok_8, self.ui.label_kesit_error_8]
        self.group_list_primer_19 = [self.ui.doubleSpinBox_v_p9, self.ui.doubleSpinBox_h1_p_sipir_9,
                                     self.ui.doubleSpinBox_h1_p_kesit_9, self.ui.doubleSpinBox_h1_p_cap_9,
                                     self.ui.doubleSpinBox_h1_p_akim_9, self.ui.doubleSpinBox_h1_p_sipir_29,
                                     self.ui.doubleSpinBox_h1_p_kesit_29, self.ui.doubleSpinBox_h1_p_cap_29,
                                     self.ui.doubleSpinBox_h1_p_akim_29, self.ui.comboBox_tel_p9,
                                     self.ui.label_kesit_ok_9, self.ui.label_kesit_error_9]
        self.group_list_primer_20 = [self.ui.doubleSpinBox_v_p10, self.ui.doubleSpinBox_h1_p_sipir_10,
                                     self.ui.doubleSpinBox_h1_p_kesit_10, self.ui.doubleSpinBox_h1_p_cap_10,
                                     self.ui.doubleSpinBox_h1_p_akim_10, self.ui.doubleSpinBox_h1_p_sipir_30,
                                     self.ui.doubleSpinBox_h1_p_kesit_30, self.ui.doubleSpinBox_h1_p_cap_30,
                                     self.ui.doubleSpinBox_h1_p_akim_30, self.ui.comboBox_tel_p10,
                                     self.ui.label_kesit_ok_10, self.ui.label_kesit_error_10]
        self.group_name_list_2 = [self.group_list_primer_11, self.group_list_primer_12, self.group_list_primer_13,
                                  self.group_list_primer_14, self.group_list_primer_15, self.group_list_primer_16,
                                  self.group_list_primer_17, self.group_list_primer_18, self.group_list_primer_19,
                                  self.group_list_primer_20]
        self.button_list_1 = [self.ui.pushButton_h1_p_buton_1, self.ui.pushButton_h1_p_buton_2,
                                 self.ui.pushButton_h1_p_buton_3, self.ui.pushButton_h1_p_buton_4,
                                 self.ui.pushButton_h1_p_buton_5, self.ui.pushButton_h1_p_buton_6,
                                 self.ui.pushButton_h1_p_buton_7, self.ui.pushButton_h1_p_buton_8,
                                 self.ui.pushButton_h1_p_buton_9, self.ui.pushButton_h1_p_buton_10]
        self.kademe_list_primer = [[self.ui.groupBox_karetel_1_p_1, self.ui.groupBox_karetel_2_p_1,
                                    self.ui.groupBox_karetel_3_p_1, self.ui.groupBox_karetel_4_p_1],
                                   [self.ui.groupBox_karetel_1_p_2, self.ui.groupBox_karetel_2_p_2,
                                    self.ui.groupBox_karetel_3_p_2, self.ui.groupBox_karetel_4_p_2],
                                   [self.ui.groupBox_karetel_1_p_3, self.ui.groupBox_karetel_2_p_3,
                                    self.ui.groupBox_karetel_3_p_3, self.ui.groupBox_karetel_4_p_3],
                                   [self.ui.groupBox_karetel_1_p_4, self.ui.groupBox_karetel_2_p_4,
                                    self.ui.groupBox_karetel_3_p_4, self.ui.groupBox_karetel_4_p_4],
                                   [self.ui.groupBox_karetel_1_p_5, self.ui.groupBox_karetel_2_p_5,
                                    self.ui.groupBox_karetel_3_p_5, self.ui.groupBox_karetel_4_p_5],
                                   [self.ui.groupBox_karetel_1_p_6, self.ui.groupBox_karetel_2_p_6,
                                    self.ui.groupBox_karetel_3_p_6, self.ui.groupBox_karetel_4_p_6],
                                   [self.ui.groupBox_karetel_1_p_7, self.ui.groupBox_karetel_2_p_7,
                                    self.ui.groupBox_karetel_3_p_7, self.ui.groupBox_karetel_4_p_7],
                                   [self.ui.groupBox_karetel_1_p_8, self.ui.groupBox_karetel_2_p_8,
                                    self.ui.groupBox_karetel_3_p_8, self.ui.groupBox_karetel_4_p_8],
                                   [self.ui.groupBox_karetel_1_p_9, self.ui.groupBox_karetel_2_p_9,
                                    self.ui.groupBox_karetel_3_p_9, self.ui.groupBox_karetel_4_p_9],
                                   [self.ui.groupBox_karetel_1_p_10, self.ui.groupBox_karetel_2_p_10,
                                    self.ui.groupBox_karetel_3_p_10, self.ui.groupBox_karetel_4_p_10],
                                   [self.ui.groupBox_folyotel_1_p_1, self.ui.groupBox_folyotel_2_p_1,
                                    self.ui.groupBox_folyotel_3_p_1, self.ui.groupBox_folyotel_4_p_1],
                                   [self.ui.groupBox_folyotel_1_p_2, self.ui.groupBox_folyotel_2_p_2,
                                    self.ui.groupBox_folyotel_3_p_2, self.ui.groupBox_folyotel_4_p_2],
                                   [self.ui.groupBox_folyotel_1_p_3, self.ui.groupBox_folyotel_2_p_3,
                                    self.ui.groupBox_folyotel_3_p_3, self.ui.groupBox_folyotel_4_p_3],
                                   [self.ui.groupBox_folyotel_1_p_4, self.ui.groupBox_folyotel_2_p_4,
                                    self.ui.groupBox_folyotel_3_p_4, self.ui.groupBox_folyotel_4_p_4],
                                   [self.ui.groupBox_folyotel_1_p_5, self.ui.groupBox_folyotel_2_p_5,
                                    self.ui.groupBox_folyotel_3_p_5, self.ui.groupBox_folyotel_4_p_5],
                                   [self.ui.groupBox_folyotel_1_p_6, self.ui.groupBox_folyotel_2_p_6,
                                    self.ui.groupBox_folyotel_3_p_6, self.ui.groupBox_folyotel_4_p_6],
                                   [self.ui.groupBox_folyotel_1_p_7, self.ui.groupBox_folyotel_2_p_7,
                                    self.ui.groupBox_folyotel_3_p_7, self.ui.groupBox_folyotel_4_p_7],
                                   [self.ui.groupBox_folyotel_1_p_8, self.ui.groupBox_folyotel_2_p_8,
                                    self.ui.groupBox_folyotel_3_p_8, self.ui.groupBox_folyotel_4_p_8],
                                   [self.ui.groupBox_folyotel_1_p_9, self.ui.groupBox_folyotel_2_p_9,
                                    self.ui.groupBox_folyotel_3_p_9, self.ui.groupBox_folyotel_4_p_9],
                                   [self.ui.groupBox_folyotel_1_p_10, self.ui.groupBox_folyotel_2_p_10,
                                    self.ui.groupBox_folyotel_3_p_10, self.ui.groupBox_folyotel_4_p_10],
                                   [self.ui.doubleSpinBox_kapton_1_p_1, self.ui.doubleSpinBox_kapton_2_p_1,
                                    self.ui.doubleSpinBox_kapton_3_p_1, self.ui.doubleSpinBox_kapton_4_p_1],
                                   [self.ui.doubleSpinBox_kapton_1_p_2, self.ui.doubleSpinBox_kapton_2_p_2,
                                    self.ui.doubleSpinBox_kapton_3_p_2, self.ui.doubleSpinBox_kapton_4_p_2],
                                   [self.ui.doubleSpinBox_kapton_1_p_3, self.ui.doubleSpinBox_kapton_2_p_3,
                                    self.ui.doubleSpinBox_kapton_3_p_3, self.ui.doubleSpinBox_kapton_4_p_3],
                                   [self.ui.doubleSpinBox_kapton_1_p_4, self.ui.doubleSpinBox_kapton_2_p_4,
                                    self.ui.doubleSpinBox_kapton_3_p_4, self.ui.doubleSpinBox_kapton_4_p_4],
                                   [self.ui.doubleSpinBox_kapton_1_p_5, self.ui.doubleSpinBox_kapton_2_p_5,
                                    self.ui.doubleSpinBox_kapton_3_p_5, self.ui.doubleSpinBox_kapton_4_p_5],
                                   [self.ui.doubleSpinBox_kapton_1_p_6, self.ui.doubleSpinBox_kapton_2_p_6,
                                    self.ui.doubleSpinBox_kapton_3_p_6, self.ui.doubleSpinBox_kapton_4_p_6],
                                   [self.ui.doubleSpinBox_kapton_1_p_7, self.ui.doubleSpinBox_kapton_2_p_7,
                                    self.ui.doubleSpinBox_kapton_3_p_7, self.ui.doubleSpinBox_kapton_4_p_7],
                                   [self.ui.doubleSpinBox_kapton_1_p_8, self.ui.doubleSpinBox_kapton_2_p_8,
                                    self.ui.doubleSpinBox_kapton_3_p_8, self.ui.doubleSpinBox_kapton_4_p_8],
                                   [self.ui.doubleSpinBox_kapton_1_p_9, self.ui.doubleSpinBox_kapton_2_p_9,
                                    self.ui.doubleSpinBox_kapton_3_p_9, self.ui.doubleSpinBox_kapton_4_p_9],
                                   [self.ui.doubleSpinBox_kapton_1_p_10, self.ui.doubleSpinBox_kapton_2_p_10,
                                    self.ui.doubleSpinBox_kapton_3_p_10, self.ui.doubleSpinBox_kapton_4_p_10],
                                   [self.ui.doubleSpinBox_mancap_p_11, self.ui.doubleSpinBox_mancap_p_12,
                                    self.ui.doubleSpinBox_mancap_p_13, self.ui.doubleSpinBox_mancap_p_14],
                                   [self.ui.doubleSpinBox_mancap_p_21, self.ui.doubleSpinBox_mancap_p_22,
                                    self.ui.doubleSpinBox_mancap_p_23, self.ui.doubleSpinBox_mancap_p_24],
                                   [self.ui.doubleSpinBox_mancap_p_31, self.ui.doubleSpinBox_mancap_p_32,
                                    self.ui.doubleSpinBox_mancap_p_33, self.ui.doubleSpinBox_mancap_p_34],
                                   [self.ui.doubleSpinBox_mancap_p_41, self.ui.doubleSpinBox_mancap_p_42,
                                    self.ui.doubleSpinBox_mancap_p_43, self.ui.doubleSpinBox_mancap_p_44],
                                   [self.ui.doubleSpinBox_mancap_p_51, self.ui.doubleSpinBox_mancap_p_52,
                                    self.ui.doubleSpinBox_mancap_p_53, self.ui.doubleSpinBox_mancap_p_54],
                                   [self.ui.doubleSpinBox_mancap_p_61, self.ui.doubleSpinBox_mancap_p_62,
                                    self.ui.doubleSpinBox_mancap_p_63, self.ui.doubleSpinBox_mancap_p_64],
                                   [self.ui.doubleSpinBox_mancap_p_71, self.ui.doubleSpinBox_mancap_p_72,
                                    self.ui.doubleSpinBox_mancap_p_73, self.ui.doubleSpinBox_mancap_p_74],
                                   [self.ui.doubleSpinBox_mancap_p_81, self.ui.doubleSpinBox_mancap_p_82,
                                    self.ui.doubleSpinBox_mancap_p_83, self.ui.doubleSpinBox_mancap_p_84],
                                   [self.ui.doubleSpinBox_mancap_p_91, self.ui.doubleSpinBox_mancap_p_92,
                                    self.ui.doubleSpinBox_mancap_p_93, self.ui.doubleSpinBox_mancap_p_94],
                                   [self.ui.doubleSpinBox_mancap_p_101, self.ui.doubleSpinBox_mancap_p_102,
                                    self.ui.doubleSpinBox_mancap_p_103, self.ui.doubleSpinBox_mancap_p_104],
                                   ]
        self.kademe_grouplist_primer = [self.ui.groupBox_5, self.ui.groupBox_6, self.ui.groupBox_7, self.ui.groupBox_8,
                              self.ui.groupBox_9,
                              self.ui.groupBox_10, self.ui.groupBox_11, self.ui.groupBox_12, self.ui.groupBox_13,
                              self.ui.groupBox_14]
    def primer_object_signals(self):
        self.ui.comboBox_primer.currentTextChanged.connect(self.primer_kademe_goster)

        for i in range(0, 10):
            #self.group_name_list_sva1[i][49].stateChanged.connect(self.va_man_spir)

            self.button_list_1[i].clicked.connect(self.open_kesit_hesaplama)
            # self.group_name_list_1[i][45].clicked.connect(self.va_open_tel_secim_gnl)
            # self.group_name_list_1[i][46].clicked.connect(self.va_open_tel_secim_gnl)
            # self.group_name_list_1[i][47].clicked.connect(self.va_open_tel_secim_gnl)
            # self.group_name_list_1[i][48].clicked.connect(self.va_open_tel_secim_gnl)
            self.group_name_list_1[i][32].currentTextChanged.connect(self.primer_kademe_goster)
            self.group_name_list_1[i][10].currentTextChanged.connect(self.primer_kademe_goster)
            self.group_name_list_1[i][8].currentTextChanged.connect(self.primer_kademe_goster)
            self.group_name_list_1[i][9].currentTextChanged.connect(self.primer_kademe_goster)
            self.group_name_list_1[i][7].valueChanged.connect(self.hesaplamalari_guncelle)
            self.group_name_list_1[i][49].stateChanged.connect(self.hesaplamalari_guncelle)
            self.group_name_list_1[i][41].valueChanged.connect(self.hesaplamalari_guncelle)
            self.group_name_list_1[i][6].valueChanged.connect(self.hesaplamalari_guncelle)
            for y in range(11, 33):
                self.object_multi_connect(object=self.group_name_list_1[i][y], arg=(self.hesaplamalari_guncelle))
            for y in range(54, 58):
                self.object_multi_connect(object=self.group_name_list_1[i][y], arg=(self.hesaplamalari_guncelle))
    def primer_tel_kademe_resetle(self):
        for index in range(0,10):
            self.kademe_goster(object=self.group_name_list_1[index][10], group_list=self.kademe_list_primer[index])
            self.kademe_goster(object=self.group_name_list_1[index][8], group_list=self.kademe_list_primer[index+10])
            self.kademe_goster(object=self.group_name_list_1[index][9], group_list=self.kademe_list_primer[index+20])
            self.kademe_goster(object=self.group_name_list_1[index][32],
                               group_list=self.kademe_list_primer[index + 30])
    def primer_kademe_goster(self):
        self.kademe_goster(object=self.ui.comboBox_primer, group_list=self.kademe_grouplist_primer)

        self.hesaplamalari_guncelle()
        self.primer_tel_kademe_resetle()

# ========================================================
    def hesap_yap(self,gl,gl2,guc,frekans,gauss,karkas_en,karkas_boy,verim,karkas_yuk,baglanti,sarim,cu_par, cu_yog, al_par, al_yog, dig_par, dig_yog,kademe=1):
        self.hesap_sarim_uzunlugu()
        akim_deger=self.hesap_kademe_akimi(gl,guc)
        for i in range(0,10):
            if gl[i][7].value() > 0 and kademe > i:

                if baglanti=="Yıldız":
                    pass

                elif baglanti=="Üçgen":
                    pass
                elif baglanti=="mono":
                    # spir 1 Hesabı -------------------------
                    gl[i][4].setValue(hp.spir_hesap_1(
                        gerilim=gl[i][7].value(),
                        frekans=frekans,
                        gauss=gauss,
                        karkas_en=karkas_en,
                        karkas_boy=karkas_boy,
                        verim=verim))
                    # spir 2 Hesabı -------------------------
                    if gl[i][49].isChecked():
                        pass
                    else:
                        gl[i][6].setValue(hp.spir_hesap_6(
                            gerilim=gl[i][7].value(),
                            frekans=frekans,
                            gauss=gauss,
                            karkas_en=karkas_en,
                            karkas_boy=karkas_boy,
                            verim=verim))

                    # Akım 1 Hesabı -------------------------
                    if i==0:



                        gl[i][0].setValue(
                            hp.akim_hesap_1(
                                guc=guc,
                                gerilim=gl[i][7].value())-akim_deger)
                    elif i>=1:
                        gl[i][0].setValue(
                            hp.akim_hesap_1(
                                guc=guc,
                                gerilim=gl[i][7].value()))

                # Kesit 1 Hesabı -------------------------
                gl[i][5].setValue(hp.kesit_hesap_1(
                    akim=gl[i][0].value(),
                    akim_yogunlugu=hp.akim_yogunlugu_1(
                        tel_turu=gl[i][11].currentText(),cu_par=cu_par, cu_yog=cu_yog, al_par=al_par, al_yog=al_yog, dig_par=dig_par, dig_yog=dig_yog)))
                # cap 1 Hesabı -------------------------
                gl[i][2].setValue(hp.cap_hesap_1(
                    kesit=gl[i][5].value()))
                # Kesit 2 Hesabı -------------------------
                gl[i][34].setValue(hp.kesit_hesap_2(
                    cap=gl[i][54].value()) + hp.kesit_hesap_2(
                    cap=gl[i][55].value()) + hp.kesit_hesap_2(
                    cap=gl[i][56].value()) + hp.kesit_hesap_2(
                    cap=gl[i][57].value()) +
                                   (gl[i][12].value() * gl[i][13].value()) +
                                   (gl[i][14].value() * gl[i][15].value()) +
                                   (gl[i][16].value() * gl[i][
                                       17].value()) +
                                   (gl[i][18].value() * gl[i][
                                       19].value()) +
                                   gl[i][20].value() +
                                   gl[i][21].value() +
                                   gl[i][22].value() +
                                   gl[i][23].value() +
                                   (gl[i][24].value() * gl[i][
                                       25].value()) +
                                   (gl[i][26].value() * gl[i][
                                       27].value()) +
                                   (gl[i][28].value() * gl[i][
                                       29].value()) +
                                   (gl[i][30].value() * gl[i][
                                       31].value())
                                   )
                # Akım 2 Hesabı -------------------------
                gl[i][1].setValue(hp.akim_hesap_2(

                    kesit=gl[i][34].value(),
                    akim_yogunlugu=hp.akim_yogunlugu_1(
                        tel_turu=gl[i][11].currentText(),cu_par=cu_par, cu_yog=cu_yog, al_par=al_par, al_yog=al_yog, dig_par=dig_par, dig_yog=dig_yog)))
                # cap 2 Hesabı -------------------------
                gl[i][3].setValue(gl[i][54].value()+gl[i][55].value()+gl[i][56].value()+gl[i][57].value())
                # akım 2 ve kesit 2 kontrol -------------------------
                if gl[i][5].value() <= gl[i][34].value():
                    gl[i][50].setVisible(True)
                    gl[i][51].setVisible(False)
                else:
                    gl[i][50].setVisible(False)
                    gl[i][51].setVisible(True)
                if gl[i][0].value() <= gl[i][1].value():
                    gl[i][52].setVisible(True)
                    gl[i][53].setVisible(False)
                else:
                    gl[i][52].setVisible(False)
                    gl[i][53].setVisible(True)
                # -------------------------
                data = db.showfilter_tel_spir(
                    filter_value=gl[i][54].value(),
                    index=0)
                if gl[i][54].value() == 0:
                    tel_cap = 0
                elif data == [] and gl[i][54].value() > 0:
                    tel_cap = (gl[i][54].value() + gl[i][55].value() + gl[i][56].value() + gl[i][57].value())*1.02
                elif data != [] and gl[i][54].value() > 0:
                    tel_cap = data[0][4]
                    # tel yüksekliği Hesabı -------------------------
                gl[i][36].setValue(hp.tel_yukseklik_hesap_1(
                    tel_cap=tel_cap, karetel_yuk1=gl[i][24].value(),
                    karetel_yuk2=gl[i][26].value(),
                    karetel_yuk3=gl[i][28].value(), karetel_yuk4=gl[i][30].value(),
                    folyo_yuk1=gl[i][20].value(), folyo_yuk2=gl[i][21].value(),
                    folyo_yuk3=gl[i][22].value(), folyo_yuk4=gl[i][23].value(),
                    kapton1=gl[i][12].value(), kapton2=gl[i][14].value(),
                    kapton3=gl[i][16].value(), kapton4=gl[i][18].value()))
                # tel en Hesabı -------------------------
                gl[i][35].setValue(hp.tel_en_hesap_1(
                    tel_cap=tel_cap,
                    karetel_en1=gl[i][25].value(),
                    karetel_en2=gl[i][22].value(),
                    karetel_en3=gl[i][29].value(), karetel_en4=gl[i][31].value(),
                    folyo_en1=gl[i][20].value(), folyo_en2=gl[i][21].value(),
                    folyo_en3=gl[i][22].value(), folyo_en4=gl[i][23].value(),
                    kapton1=gl[i][13].value(), kapton2=gl[i][15].value(),
                    kapton3=gl[i][17].value(), kapton4=gl[i][19].value()))
                if gl[i][35].value() > 0:
                    # spir kat Hesabı -------------------------
                    gl[i][37].setValue(hp.spir_kat_hesap_1(
                        karkas_yuk=karkas_yuk,
                        tel_en=gl[i][35].value()))
                    #  kat sayısı -------------------------------
                    if i == 0:
                        if gl[i][37].value() != 0:
                            gl[i][38].setValue(hp.kat_sayisi_hesap_1(
                                spir=gl[i][6].value(),
                                spir_kat=gl[i][37].value()))
                        else :
                            gl[i][38].setValue(0)

                    elif i > 0:
                        gl[i][38].setValue(hp.kat_sayisi_hesap_2(
                            tel_spir_n=gl[i][6].value(),
                            tel_spri_n_1=gl[i - 1][6].value(),
                            kat_bosluk_n_1=gl[i - 1][39].value(),
                            tel_en=gl[i][35].value(),
                            spir_kat=gl[i][37].value()
                        ))
                    # sarım yuksekliği  -------------------------
                    gl[i][42].setValue(hp.sarim_yüksekligi_hesap_1(
                        tel_yuk=gl[i][36].value(),
                        kat_sayisi=gl[i][38].value()))

                    # son kat
                    if i == 0:
                        if math.fmod(gl[i][6].value(), gl[i][37].value()) == 0:
                            gl[i][43].setValue(gl[i][37].value())
                        else:
                            gl[i][43].setValue(hp.son_kat_hesap_1(
                                spir_2=gl[i][6].value(),
                                spir_kat=gl[i][37].value()))

                    elif i > 0:
                        if gl[i][38].value() == 0:
                            gl[i][43].setValue(hp.son_kat_hesap_2(
                                spir_2=gl[i][6].value(),
                                spir_2_n_1=gl[i - 1][6].value()))
                        else:
                            gl[i][43].setValue(hp.son_kat_hesap_3(
                                spir_2=gl[i][6].value(),
                                spir_2_n_1=gl[i - 1][6].value(),
                                kat_bosluk_n_1=gl[i - 1][39].value(),
                                tel_en=gl[i][35].value(),
                                spir_kat=gl[i][37].value()))

                    # kattaki bosluk ---------------------------
                    if i == 0:
                        gl[i][39].setValue(hp.kattaki_bosluk_hesap_1(
                            karkas_yuk=karkas_yuk,
                            tel_en=gl[i][35].value(),
                            son_kat=gl[i][43].value()
                        ))

                    elif i > 0:
                        if gl[i][38].value() == 0:
                            gl[i][39].setValue(hp.kattaki_bosluk_hesap_2(

                                kat_bosluk_n_1=gl[i - 1][39].value(),
                                tel_en=gl[i][35].value(),
                                spir_2=gl[i][6].value(),
                                spir_2_n_1=gl[i - 1][6].value()
                            ))
                        else:
                            gl[i][39].setValue(hp.kattaki_bosluk_hesap_3(
                                karkas_yuk=karkas_yuk,
                                spir_2=gl[i][6].value(),
                                spir_2_n_1=gl[i - 1][6].value(),
                                kat_bosluk_n_1=gl[i - 1][39].value(),
                                tel_en=gl[i][35].value(),
                                spir_kat=gl[i][37].value()

                            ))

                    else:
                        pass

                    # tel uzunluk  ---------------------------
                    a0 = 2 * (karkas_en + karkas_boy) + 8 * 0.05 * karkas_en
                    a1 = a0 + 4 * gl[1][36].value()
                    a2 = a0 + 4 * gl[2][36].value() + 8 * gl[0][36].value() * gl[0][38].value()
                    a3 = a0 + 4 * gl[3][36].value() + 8 * gl[0][36].value() * gl[0][38].value() + 8 * gl[1][
                        36].value() * gl[1][38].value()
                    a4 = a0 + 4 * gl[4][36].value() + 8 * gl[0][36].value() * gl[0][38].value() + 8 * gl[1][
                        36].value() * gl[1][38].value() + 8 * gl[2][36].value() * gl[2][38].value()
                    a5 = a0 + 4 * gl[5][36].value() + 8 * gl[0][36].value() * gl[0][38].value() + 8 * gl[1][
                        36].value() * gl[1][38].value() + 8 * gl[2][36].value() * gl[2][38].value() + 8 * gl[3][
                             36].value() * gl[3][38].value()
                    a6 = a0 + 4 * gl[6][36].value() + 8 * gl[0][36].value() * gl[0][38].value() + 8 * gl[1][
                        36].value() * gl[1][38].value() + 8 * gl[2][36].value() * gl[2][38].value() + 8 * gl[3][
                             36].value() * gl[3][38].value() + 8 * gl[4][36].value() * gl[4][38].value()
                    a7 = a0 + 4 * gl[7][36].value() + 8 * gl[0][36].value() * gl[0][38].value() + 8 * gl[1][
                        36].value() * gl[1][38].value() + 8 * gl[2][36].value() * gl[2][38].value() + 8 * gl[3][
                             36].value() * gl[3][38].value() + 8 * gl[4][36].value() * gl[4][38].value() + 8 * \
                         gl[5][36].value() * gl[5][38].value()
                    a8 = a0 + 4 * gl[8][36].value() + 8 * gl[0][36].value() * gl[0][38].value() + 8 * gl[1][
                        36].value() * gl[1][38].value() + 8 * gl[2][36].value() * gl[2][38].value() + 8 * gl[3][
                             36].value() * gl[3][38].value() + 8 * gl[4][36].value() * gl[4][38].value() + 8 * \
                         gl[5][36].value() * gl[5][38].value() + 8 * gl[6][36].value() * gl[6][38].value()
                    a9 = a0 + 4 * gl[9][36].value() + 8 * gl[0][36].value() * gl[0][38].value() + 8 * gl[1][
                        36].value() * gl[1][38].value() + 8 * gl[2][36].value() * gl[2][38].value() + 8 * gl[3][
                             36].value() * gl[3][38].value() + 8 * gl[4][36].value() * gl[4][38].value() + 8 * \
                         gl[5][36].value() * gl[5][38].value() + 8 * gl[6][36].value() * gl[6][38].value() + 8 * \
                         gl[7][36].value() * gl[7][38].value()
                    all_a = [0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
                    if i == 0:
                        gl[i][40].setValue(
                            ((gl[i][38].value() - 1) * ((2 * (karkas_en + karkas_boy)) +
                                                        8 * karkas_en * 0.05 + 4 * gl[i][36].value()) + \
                             (8 * gl[i][36].value() * (gl[i][38].value() - 1) * (
                                         gl[i][38].value() - 2) / 2)) / 1000 * gl[i][37].value() + \
                            ((2 * (karkas_en + karkas_boy)) + \
                             8 * karkas_en * 0.05 + 4 * gl[i][36].value() + \
                             (8 * gl[i][36].value() * (gl[i][38].value() - 1))) / 1000 * gl[i][43].value())
                    elif i > 0:
                        if gl[i][38].value() == 0:
                            gl[i][40].setValue(
                                (all_a[i] + 8 * (gl[i - 1][38].value() - 1) * gl[i - 1][36].value()) * gl[i][
                                    43].value() / 1000)
                        elif gl[i][38].value() == 1:
                            gl[i][40].setValue(
                                (all_a[i] + 8 * (gl[i - 1][38].value() - 1) * gl[i - 1][36].value()) *
                                math.floor(gl[i - 1][39].value() / gl[i][35].value()) / 1000 + (
                                            all_a[i] + 8 * (gl[i - 1][38].value())
                                            * gl[i - 1][36].value()) * gl[i][43].value() / 1000)

                        else:
                            gl[i][40].setValue(
                                (all_a[i] + 8 * (gl[i - 1][38].value() - 1) * gl[i - 1][36].value())
                                * math.floor(gl[i - 1][39].value() / gl[i][35].value()) / 1000 +
                                ((gl[i][38].value() - 1) * (
                                            all_a[i] + 8 * (gl[i - 1][38].value()) * gl[i - 1][36].value()) +
                                 4 * (gl[i][38].value() - 1) * (gl[i][38].value() - 2) * gl[i][36].value()) * gl[i][
                                    37].value() / 1000
                                + (all_a[i] + 8 * (gl[i - 1][38].value()) * gl[i - 1][36].value() + 8 * (
                                            gl[i][38].value() - 1) *
                                   gl[i][36].value()) * gl[i][43].value() / 1000
                            )

                    if sarim == "sekonder":

                        sek_a1 = a0 + 8 * self.primer_sarim_yukseklik_toplam + 8 * self.primer_izolasyon + 4 * \
                                 gl[1][36].value()
                        sek_a2 = a0 + 8 * self.primer_sarim_yukseklik_toplam + 4 * gl[2][36].value() + 8 * gl[0][
                            36].value() * gl[0][38].value()
                        sek_a3 = a0 + 8 * self.primer_sarim_yukseklik_toplam + 4 * gl[3][36].value() + 8 * gl[0][
                            36].value() * gl[0][38].value() + 8 * gl[1][
                                     36].value() * gl[1][38].value()
                        sek_a4 = a0 + 8 * self.primer_sarim_yukseklik_toplam + 4 * gl[4][36].value() + 8 * gl[0][
                            36].value() * gl[0][38].value() + 8 * gl[1][
                                     36].value() * gl[1][38].value() + 8 * gl[2][36].value() * gl[2][38].value()
                        sek_a5 = a0 + 8 * self.primer_sarim_yukseklik_toplam + 4 * gl[5][36].value() + 8 * gl[0][
                            36].value() * gl[0][38].value() + 8 * gl[1][
                                     36].value() * gl[1][38].value() + 8 * gl[2][36].value() * gl[2][
                                     38].value() + 8 * gl[3][
                                     36].value() * gl[3][38].value()
                        sek_a6 = a0 + 8 * self.primer_sarim_yukseklik_toplam + 4 * gl[6][36].value() + 8 * gl[0][
                            36].value() * gl[0][38].value() + 8 * gl[1][
                                     36].value() * gl[1][38].value() + 8 * gl[2][36].value() * gl[2][
                                     38].value() + 8 * gl[3][
                                     36].value() * gl[3][38].value() + 8 * gl[4][36].value() * gl[4][38].value()
                        sek_a7 = a0 + 8 * self.primer_sarim_yukseklik_toplam + 4 * gl[7][36].value() + 8 * gl[0][
                            36].value() * gl[0][38].value() + 8 * gl[1][
                                     36].value() * gl[1][38].value() + 8 * gl[2][36].value() * gl[2][
                                     38].value() + 8 * gl[3][
                                     36].value() * gl[3][38].value() + 8 * gl[4][36].value() * gl[4][
                                     38].value() + 8 * \
                                 gl[5][36].value() * gl[5][38].value()
                        sek_a8 = a0 + 8 * self.primer_sarim_yukseklik_toplam + 4 * gl[8][36].value() + 8 * gl[0][
                            36].value() * gl[0][38].value() + 8 * gl[1][
                                     36].value() * gl[1][38].value() + 8 * gl[2][36].value() * gl[2][
                                     38].value() + 8 * gl[3][
                                     36].value() * gl[3][38].value() + 8 * gl[4][36].value() * gl[4][
                                     38].value() + 8 * \
                                 gl[5][36].value() * gl[5][38].value() + 8 * gl[6][36].value() * gl[6][38].value()
                        sek_a9 = a0 + 8 * self.primer_sarim_yukseklik_toplam + 4 * gl[9][36].value() + 8 * gl[0][
                            36].value() * gl[0][38].value() + 8 * gl[1][
                                     36].value() * gl[1][38].value() + 8 * gl[2][36].value() * gl[2][
                                     38].value() + 8 * gl[3][
                                     36].value() * gl[3][38].value() + 8 * gl[4][36].value() * gl[4][
                                     38].value() + 8 * \
                                 gl[5][36].value() * gl[5][38].value() + 8 * gl[6][36].value() * gl[6][
                                     38].value() + 8 * \
                                 gl[7][36].value() * gl[7][38].value()

                        all_sek_a = [0, sek_a1, sek_a2, sek_a3, sek_a4, sek_a5, sek_a6, sek_a7, sek_a8, sek_a9]
                        if i == 0:
                            gl[i][40].setValue(
                                (
                                        (gl[i][38].value() - 1) * (
                                            a0 + 8 * self.primer_sarim_yukseklik_toplam + 8 * self.primer_izolasyon + 4 *
                                            gl[i][36].value())
                                        + 8 * gl[i][36].value() * (gl[i][38].value() - 1) * (
                                                    gl[i][38].value() - 2) / 2
                                )
                                / 1000 * gl[i][37].value() + (
                                            a0 + 8 * self.primer_sarim_yukseklik_toplam + 8 * self.primer_izolasyon + 4 *
                                            gl[i][36].value() + 8 * gl[i][36].value() *
                                            (gl[i][38].value() - 1)) / 1000 * gl[i][43].value()
                            )
                        elif i > 0:
                            if gl[i][38].value() == 0:
                                gl[i][40].setValue(
                                    (all_sek_a[i] + 8 * (gl[i - 1][38].value() - 1) * gl[i - 1][36].value()) *
                                    gl[i][
                                        43].value() / 1000)
                            elif gl[i][38].value() == 1:
                                gl[i][40].setValue(
                                    (all_sek_a[i] + 8 * (gl[i - 1][38].value() - 1) * gl[i - 1][36].value()) *
                                    math.floor(gl[i - 1][39].value() / gl[i][35].value()) / 1000 + (
                                            all_sek_a[i] + 8 * (gl[i - 1][38].value())
                                            * gl[i - 1][36].value()) * gl[i][43].value() / 1000)

                            else:
                                gl[i][40].setValue(
                                    (all_sek_a[i] + 8 * (gl[i - 1][38].value() - 1) * gl[i - 1][36].value())
                                    * math.floor(gl[i - 1][39].value() / gl[i][35].value()) / 1000 +
                                    ((gl[i][38].value() - 1) * (
                                            all_sek_a[i] + 8 * (gl[i - 1][38].value()) * gl[i - 1][36].value()) +
                                     4 * (gl[i][38].value() - 1) * (gl[i][38].value() - 2) * gl[i][36].value()) *
                                    gl[i][
                                        37].value() / 1000
                                    + (all_sek_a[i] + 8 * (gl[i - 1][38].value()) * gl[i - 1][36].value() + 8 * (
                                            gl[i][38].value() - 1) *
                                       gl[i][36].value()) * gl[i][43].value() / 1000)
                    # tel agirlik  ---------------------------
                    if gl[i][40].value() != 0:
                        gl[i][41].setValue(
                            hp.tel_agirlik_hesap_1(tel_uzunluk=gl[i][40].value(), kesit_2=gl[i][34].value(),
                                                tel_yogunluk=hp.tel_yogunlugu_1(
                                                    tel_turu=gl[i][11].currentText())))

                    else:
                        gl[i][41].setValue(0)
                self.karkas_hesaplama()
                self.bosluk_hesapla()
                self.agirlik_hesapla()
                self.olcu_hesapla()
                self.izolasyon_hesapla()
            else:
                gl[i][0].setValue(0)
                gl[i][5].setValue(0)
                gl[i][2].setValue(0)
                gl[i][4].setValue(0)
                gl[i][3].setValue(0)
                gl[i][1].setValue(0)
                gl[i][6].setValue(0)
                gl[i][12].setValue(0)
                gl[i][13].setValue(0)
                gl[i][14].setValue(0)
                gl[i][15].setValue(0)
                gl[i][16].setValue(0)
                gl[i][17].setValue(0)
                gl[i][18].setValue(0)
                gl[i][19].setValue(0)
                gl[i][20].setValue(0)
                gl[i][21].setValue(0)
                gl[i][22].setValue(0)
                gl[i][23].setValue(0)
                gl[i][24].setValue(0)
                gl[i][25].setValue(0)
                gl[i][26].setValue(0)
                gl[i][27].setValue(0)
                gl[i][28].setValue(0)
                gl[i][29].setValue(0)
                gl[i][30].setValue(0)
                gl[i][31].setValue(0)
                gl[i][34].setValue(0)
                gl[i][35].setValue(0)
                gl[i][36].setValue(0)
                gl[i][37].setValue(0)
                gl[i][38].setValue(0)
                gl[i][39].setValue(0)
                gl[i][40].setValue(0)
                gl[i][41].setValue(0)
                gl[i][42].setValue(0)
                gl[i][43].setValue(0)
                gl[i][8].setCurrentIndex(0)
                gl[i][9].setCurrentIndex(0)
                gl[i][10].setCurrentIndex(0)
                gl[i][11].setCurrentIndex(0)
                gl[i][50].setVisible(False)
                gl[i][51].setVisible(True)
                gl[i][52].setVisible(False)
                gl[i][53].setVisible(True)
                gl[i][54].setValue(0)
                gl[i][55].setValue(0)
                gl[i][56].setValue(0)
                gl[i][57].setValue(0)
                gl[i][32].setCurrentIndex(0)
        for index in range(0, 10):
            gl2[index][0].setValue(gl[index][7].value())
            gl2[index][1].setValue(gl[index][4].value())
            gl2[index][2].setValue(gl[index][5].value())
            gl2[index][3].setValue(gl[index][2].value())
            gl2[index][4].setValue(gl[index][0].value())
            gl2[index][5].setValue(gl[index][6].value())
            gl2[index][6].setValue(gl[index][34].value())
            gl2[index][7].setValue(gl[index][3].value())
            gl2[index][8].setValue(gl[index][1].value())
            gl2[index][9].setCurrentIndex(gl[index][11].currentIndex())
            if gl2[index][0].value() > 0:
                gl2[index][11].setVisible(False)
                gl2[index][10].setVisible(True)
            else:
                gl2[index][11].setVisible(True)
                gl2[index][10].setVisible(False)
    def hesap_sarim_uzunlugu(self):
        self.primer_sarim_yukseklik_toplam =0.0

        for i in range(0,10):
            self.primer_sarim_yukseklik_toplam =self.primer_sarim_yukseklik_toplam + self.group_name_list_1[i][42].value()
    def hesap_kademe_akimi(self,gl,guc):
        self.deger = 0
        if gl[9][7].value() > 0.0:

            self.deger = (hp.akim_hesap_1(guc=guc, gerilim=gl[9][7].value()))
        elif gl[8][7].value() > 0.0:
            self.deger = (hp.akim_hesap_1(guc=guc, gerilim=gl[8][7].value()))
        elif gl[7][7].value() > 0.0:
            self.deger = (hp.akim_hesap_1(guc=guc, gerilim=gl[7][7].value()))
        elif gl[6][7].value() > 0.0:
            self.deger = (hp.akim_hesap_1(guc=guc, gerilim=gl[6][7].value()))
        elif gl[5][7].value() > 0.0:
            self.deger = (hp.akim_hesap_1(guc=guc, gerilim=gl[5][7].value()))
        elif gl[4][7].value() > 0.0:
            self.deger = (hp.akim_hesap_1(guc=guc, gerilim=gl[4][7].value()))
        elif gl[3][7].value() > 0.0:
            self.deger = (hp.akim_hesap_1(guc=guc, gerilim=gl[3][7].value()))
        elif gl[2][7].value() > 0.0:
            self.deger = (hp.akim_hesap_1(guc=guc, gerilim=gl[2][7].value()))
        elif gl[1][7].value() > 0.0:
            self.deger = (hp.akim_hesap_1(guc=guc, gerilim=gl[1][7].value()))
        return self.deger
    def object_multi_connect(self,object,arg):
        if object.metaObject().className()== "QDoubleSpinBox":
            return object.valueChanged.connect(arg)
        elif object.metaObject().className()== "QComboBox":
            return object.currentTextChanged.connect(arg)
        elif object.metaObject().className()== "QLineEdit":
            return object.textChanged.connect(arg)
        elif object.metaObject().className()== "QPushButton":
            return object.clicked.connect(arg)
        elif object.metaObject().className()== "QCheckBox":
            return object.stateChanged.connect(arg)
        elif object.metaObject().className()== "QLabel":
            return object.textChanged.connect(arg)
    def object_multi_value_set(self,object,object2):
        if object.metaObject().className()== "QDoubleSpinBox":
            return object.setValue(object2.value())
        elif object.metaObject().className()== "QComboBox":
            return object.setCurrentIndex(object2.currentIndex())
        elif object.metaObject().className()== "QLineEdit":
            return object.setText(object2.text())
        elif object.metaObject().className()== "QPushButton":
            return True
        elif object.metaObject().className()== "QCheckBox":
            return object.setChecked(object2.isChecked())
        elif object.metaObject().className()== "QLabel":
            return object.setVisible(object2.isVisible())
    def kademe_goster(self,object,group_list):
        kademe_sayisi= int(object.currentText())
        self.hide_list(group_list)
        group_list[0].setVisible(True)
        for i in range(kademe_sayisi):
            group_list[i].setVisible(True)
    def kesit_man_spir_update(self):
        for i in range(0, 10):
            self.window3.gn1[i][49].setChecked(self.window3.group_name_list_sekonder[i][49].isChecked())
            self.window3.gn1[i][6].setValue(self.window3.group_name_list_sekonder[i][6].value())
    def kesit_parametrelerini_yaz(self,window, object, object2):
        if object[51].isVisible() or object2[53].isVisible():
            returnValue = warning_msjbox(title='Kesit Değerleri Hatası',
                                         text='Kesit değerleri önerilen değerlerin altındadır. Devam etmek için buotana basın.')
        else:
            returnValue = QMessageBox.Ok
        if returnValue == QMessageBox.Cancel:
            return False
        elif returnValue == QMessageBox.Ok:
            for i in range(0, 58):
                self.object_multi_value_set(object=object[i], object2=object2[i])
            window.close()
    def tum_degerleri_temizle(self):
        returnValue = clear_msjbox(
            text="Tüm veri girisleri temizlenecektir..\nDevam Etmek için Temizle tuşuna basın",
            title="DİKKAT - Veriler silinecektir")

        if returnValue == QMessageBox.Cancel:
            return False
        tekrar=1
        while tekrar !=3:
            self.ui.comboBox_primer.setCurrentIndex(0)

            self.ui.doubleSpinBox_toplamagirlik_al.setValue(0)
            self.ui.doubleSpinBox_toplamagirlik_cu.setValue(0)
            self.ui.doubleSpinBox_primeragirlik_al.setValue(0)
            self.ui.doubleSpinBox_primeragirlik_cu.setValue(0)

            primer_al_agirlik=0
            primer_toplam_agirlik=0
            primer_cu_agirlik=0

            self.ui.doubleSpinBox_olcu_a.setValue(0)
            self.ui.doubleSpinBox_olcu_b.setValue(0)
            self.ui.doubleSpinBox_olcu_c.setValue(0)
            self.ui.doubleSpinBox_trafoolcu_a.setValue(0)
            self.ui.doubleSpinBox_trafoolcu_c.setValue(0)
            self.ui.doubleSpinBox_sacagirlik.setValue(0)
            self.ui.doubleSpinBox_trafoolcu_b.setValue(0)
            self.ui.doubleSpinBox_trafoolcu_d.setValue(0)
            self.ui.doubleSpinBox_trafoolcu_e.setValue(0)
            self.ui.doubleSpinBox_trafoolcu_f.setValue(0)
            self.ui.doubleSpinBox_guc.setValue(500)
            self.ui.doubleSpinBox_karkas_en.setValue(50)
            self.ui.doubleSpinBox_karkas_boy.setValue(60)
            self.ui.doubleSpinBox_karkas_yukseklik.setValue(72)
            self.ui.doubleSpinBox_karkas_verim.setValue(100)
            self.ui.comboBox_sactipi.setCurrentIndex(0)
            self.ui.doubleSpinBox_sac.setValue(0.5)
            self.ui.doubleSpinBox_frekans.setValue(50)
            self.ui.doubleSpinBox_gauss.setValue(11500)
            self.ui.doubleSpinBox_c.setValue(7)
            # self.ui.doubleSpinBox_nuvebosluk.setValue(0)
            # self.ui.doubleSpinBox_primer_izo_deg.setValue(0)
            self.ui.doubleSpinBox_primer_izo_tur.setValue(0)

            self.ui.doubleSpinBox_pri_sek_izo_tur.setValue(0)
            self.ui.checkBox_ekran_sec.setChecked(False)
            self.ui.doubleSpinBox_ekran_izo_deg.setValue(0)
            self.ui.checkBox_ekstra.setChecked(False)
            self.ui.doubleSpinBox_ekstra_izo_deg.setValue(0)
            self.ui.lineEdit_klemens_adi.setText("")
            self.ui.doubleSpinBox_klemens_a_deg.setValue(0)
            self.ui.doubleSpinBox_klemens_b_deg.setValue(0)
            self.ui.doubleSpinBox_klemens_akim.setValue(0)
            self.ui.lineEdit_klemens.setText("")
            self.ui.lineEdit_ayak_adi.setText("")
            self.ui.doubleSpinBox_ayak_a_deg.setValue(0)
            self.ui.doubleSpinBox_ayak_b_deg.setValue(0)
            self.ui.doubleSpinBox_v_p_1.setValue(0)
            self.ui.doubleSpinBox_v_p_2.setValue(0)
            self.ui.doubleSpinBox_v_p_3.setValue(0)
            self.ui.doubleSpinBox_v_p_4.setValue(0)
            self.ui.doubleSpinBox_v_p_5.setValue(0)
            self.ui.doubleSpinBox_v_p_6.setValue(0)
            self.ui.doubleSpinBox_v_p_7.setValue(0)
            self.ui.doubleSpinBox_v_p_8.setValue(0)
            self.ui.doubleSpinBox_v_p_9.setValue(0)
            self.ui.doubleSpinBox_v_p_10.setValue(0)

            for y in range(0, 10):
                for i in range(0,57):

                    self.degerleri_temizle(object=self.group_name_list_1[y][i])
            tekrar+=1
    def degerleri_temizle(self,object):
        if object.metaObject().className() == "QDoubleSpinBox":
             return object.setValue(0)
        elif object.metaObject().className() == "QComboBox":
            return object.setCurrentIndex(0)
        elif object.metaObject().className() == "QLineEdit":
            return True
        elif object.metaObject().className() == "QLabel":
            return True
        elif object.metaObject().className()== "QCheckBox":
            return object.setChecked(False)
        elif object.metaObject().className()== "QPushButton":
            return True
# ===========================================================
    def printout_veri_kumesi(self):
        printout.primer_group_list = [
            [self.ui.doubleSpinBox_v_p_1.value(), self.ui.doubleSpinBox_sipir_2_p_1.value(),
             self.ui.doubleSpinBox_kesit_2_p_1.value(), self.ui.doubleSpinBox_cap_2_p_1.value(),
             self.ui.doubleSpinBox_akim_2_p_1.value(), self.ui.comboBox_tel_p1.currentText(),
             self.ui.doubleSpinBox_tel_agirlik_1.value(), self.ui.doubleSpinBox_spirkat_1.value()],
            [self.ui.doubleSpinBox_v_p_2.value(), self.ui.doubleSpinBox_sipir_2_p_2.value(),
             self.ui.doubleSpinBox_kesit_2_p_2.value(), self.ui.doubleSpinBox_cap_2_p_2.value(),
             self.ui.doubleSpinBox_akim_2_p_2.value(), self.ui.comboBox_tel_p2.currentText(),
             self.ui.doubleSpinBox_tel_agirlik_2.value(), self.ui.doubleSpinBox_spirkat_2.value()],
            [self.ui.doubleSpinBox_v_p_3.value(), self.ui.doubleSpinBox_sipir_2_p_3.value(),
             self.ui.doubleSpinBox_kesit_2_p_3.value(), self.ui.doubleSpinBox_cap_2_p_3.value(),
             self.ui.doubleSpinBox_akim_2_p_3.value(), self.ui.comboBox_tel_p3.currentText(),
             self.ui.doubleSpinBox_tel_agirlik_3.value(), self.ui.doubleSpinBox_spirkat_3.value()],
            [self.ui.doubleSpinBox_v_p_4.value(), self.ui.doubleSpinBox_sipir_2_p_4.value(),
             self.ui.doubleSpinBox_kesit_2_p_4.value(), self.ui.doubleSpinBox_cap_2_p_4.value(),
             self.ui.doubleSpinBox_akim_2_p_4.value(), self.ui.comboBox_tel_p4.currentText(),
             self.ui.doubleSpinBox_tel_agirlik_4.value(), self.ui.doubleSpinBox_spirkat_4.value()],
            [self.ui.doubleSpinBox_v_p_5.value(), self.ui.doubleSpinBox_sipir_2_p_5.value(),
             self.ui.doubleSpinBox_kesit_2_p_5.value(), self.ui.doubleSpinBox_cap_2_p_5.value(),
             self.ui.doubleSpinBox_akim_2_p_5.value(), self.ui.comboBox_tel_p5.currentText(),
             self.ui.doubleSpinBox_tel_agirlik_5.value(), self.ui.doubleSpinBox_spirkat_5.value()],
            [self.ui.doubleSpinBox_v_p_6.value(), self.ui.doubleSpinBox_sipir_2_p_6.value(),
             self.ui.doubleSpinBox_kesit_2_p_6.value(), self.ui.doubleSpinBox_cap_2_p_6.value(),
             self.ui.doubleSpinBox_akim_2_p_6.value(), self.ui.comboBox_tel_p6.currentText(),
             self.ui.doubleSpinBox_tel_agirlik_6.value(), self.ui.doubleSpinBox_spirkat_6.value()],
            [self.ui.doubleSpinBox_v_p_7.value(), self.ui.doubleSpinBox_sipir_2_p_7.value(),
             self.ui.doubleSpinBox_kesit_2_p_7.value(), self.ui.doubleSpinBox_cap_2_p_7.value(),
             self.ui.doubleSpinBox_akim_2_p_7.value(), self.ui.comboBox_tel_p7.currentText(),
             self.ui.doubleSpinBox_tel_agirlik_7.value(), self.ui.doubleSpinBox_spirkat_7.value()],
            [self.ui.doubleSpinBox_v_p_8.value(), self.ui.doubleSpinBox_sipir_2_p_8.value(),
             self.ui.doubleSpinBox_kesit_2_p_8.value(), self.ui.doubleSpinBox_cap_2_p_8.value(),
             self.ui.doubleSpinBox_akim_2_p_8.value(), self.ui.comboBox_tel_p8.currentText(),
             self.ui.doubleSpinBox_tel_agirlik_8.value(), self.ui.doubleSpinBox_spirkat_8.value()],
            [self.ui.doubleSpinBox_v_p_9.value(), self.ui.doubleSpinBox_sipir_2_p_9.value(),
             self.ui.doubleSpinBox_kesit_2_p_9.value(), self.ui.doubleSpinBox_cap_2_p_9.value(),
             self.ui.doubleSpinBox_akim_2_p_9.value(), self.ui.comboBox_tel_p9.currentText(),
             self.ui.doubleSpinBox_tel_agirlik_9.value(), self.ui.doubleSpinBox_spirkat_9.value()],
            [self.ui.doubleSpinBox_v_p_10.value(), self.ui.doubleSpinBox_sipir_2_p_10.value(),
             self.ui.doubleSpinBox_kesit_2_p_10.value(), self.ui.doubleSpinBox_cap_2_p_10.value(),
             self.ui.doubleSpinBox_akim_2_p_10.value(), self.ui.comboBox_tel_p10.currentText(),
             self.ui.doubleSpinBox_tel_agirlik_10.value(), self.ui.doubleSpinBox_spirkat_10.value()]]

    def printout_report(self):
        self.printout_veri_kumesi()
        printout.guc = self.ui.doubleSpinBox_guc.value()
        printout.trafo_tipi = " Izolasyon Trafosu Mono Faz Hesap Ozeti"

        printout.primer_kademe = int(self.ui.comboBox_primer.currentText())

        printout.primer_baglanti = "mono"

        printout.guc = str(self.ui.doubleSpinBox_guc.value()) + " VA"
        printout.gauss = str(self.ui.doubleSpinBox_gauss.value())
        printout.sac = str(self.ui.doubleSpinBox_sac.value()) + " mm"
        printout.c_sac = str(self.ui.doubleSpinBox_c.value())
        if self.ui.doubleSpinBox_v_p_1.value() != 0.0:
            printout.don_oran = self.ui.doubleSpinBox_v_p_1.value() / self.ui.doubleSpinBox_sipir_2_p_1.value()
        else:
            printout.don_oran = 1
        printout.frekans = str(self.ui.doubleSpinBox_frekans.value()) + " Hz"
        printout.p_tel_al_ag = str(self.ui.doubleSpinBox_primeragirlik_al.value()) + " kg"

        printout.p_tel_cu_ag = str(self.ui.doubleSpinBox_primeragirlik_cu.value()) + " kg"

        printout.toplam_ag = str(self.ui.doubleSpinBox_primeragirlik_al.value()  +\
            self.ui.doubleSpinBox_primeragirlik_cu.value() ) + "kg"
        printout.karkas = str(self.ui.doubleSpinBox_karkas_en.value()) + " x " + str(
            self.ui.doubleSpinBox_karkas_boy.value()) + " x " + str(self.ui.doubleSpinBox_karkas_yukseklik.value())
        printout.trafo_olcu = str(self.ui.doubleSpinBox_trafoolcu_a.value()) + " x " + str( \
            self.ui.doubleSpinBox_trafoolcu_b.value()) + " x " + str(self.ui.doubleSpinBox_trafoolcu_c.value()) \
            + " x " + str(self.ui.doubleSpinBox_trafoolcu_d.value()) + " x " + str(self.ui.doubleSpinBox_trafoolcu_e.value())
        printout.sac_agirlik = str(self.ui.doubleSpinBox_sacagirlik.value()) + " kg"
        printout.klemens = self.ui.lineEdit_klemens.text()
        printout.ayak = self.ui.lineEdit_ayak.text()
        printout.a_deg = str(self.ui.doubleSpinBox_olcu_a.value()) + " mm"
        printout.b_deg = str(self.ui.doubleSpinBox_olcu_b.value()) + " mm"
        printout.c_deg = str(self.ui.doubleSpinBox_olcu_c.value()) + " mm"
        printout.d_deg = ""
        printout.e_deg = ""
        printout.f_deg = ""
        printout.trafo_a_deg = str(self.ui.doubleSpinBox_trafoolcu_a.value()) + " mm"
        printout.trafo_b_deg = str(self.ui.doubleSpinBox_trafoolcu_b.value()) + " mm"
        printout.trafo_c_deg = str(self.ui.doubleSpinBox_trafoolcu_c.value()) + " mm"
        printout.trafo_d_deg = str(self.ui.doubleSpinBox_trafoolcu_d.value()) + " mm"
        printout.trafo_e_deg = str(self.ui.doubleSpinBox_trafoolcu_e.value()) + " mm"
        printout.trafo_f_deg = str(self.ui.doubleSpinBox_trafoolcu_f.value()) + " mm"
        printout.primer_izo_deg = self.ui.doubleSpinBox_primer_izo_deg.value()

        printout.pri_sek_izo_deg = self.ui.doubleSpinBox_pri_sek_izo_deg.value()
        printout.ekran_izo_deg = self.ui.doubleSpinBox_ekran_izo_deg.value()
        printout.ekstra_izo_deg = self.ui.doubleSpinBox_ekstra_izo_deg.value()
        printout.primer_izo_tur = self.ui.doubleSpinBox_primer_izo_tur.value()

        printout.pri_sek_izo_tur = self.ui.doubleSpinBox_pri_sek_izo_tur.value()
        printout.ekran_sec = self.ui.checkBox_ekran_sec.isChecked()
        printout.ekstra = self.ui.checkBox_ekstra.isChecked()
        printout.izolasyon_karsiligi=self.ui.doubleSpinBox_v_p_1.value()*self.ui.doubleSpinBox_akim_p_1.value()
        # printout.val2=self.object_multi_value_read(object=self.group_name_list_2)
        printout.ototrafo_monofaz_printout()

class KesitParamdialog(QDialog):
    def __init__(self, parent=None):
        super(KesitParamdialog, self).__init__(parent)
        self.ui = KesitParam_dialog()
        self.ui.setupUi(self)
        self.guc = 0.0
        self.frekans = 50
        self.karkas_en = 0.0
        self.karkas_boy = 0.0
        self.karkas_yukseklik = 0.0
        self.c = 0.0
        self.karkas_verim = 0.0
        self.gauss = 0.0

        self.cu_par = 0.0
        self.cu_yog = 0.0
        self.al_par = 0.0
        self.al_yog = 0.0
        self.dig_par = 0.0
        self.dig_yog = 0.0
        self.gn1 = []
        self.gn2 = []
        self.gl = []
        self.gl2 = []
        self.kademe = 0
        self.sarim = ""
        self.deger=0
        self.primer_sarim_yukseklik_toplam = 0.0
        self.sekonder_sarim_yukseklik_toplam = 0.0
        self.baglanti_turu=""
        self.primer_izolasyon = 0.0

        self.veri_kumesi()
        self.sekonder_kademe_goster()
        self.sekonder_object_signals()

    def hide_list(self, list_name):
        for i in list_name:
            i.setVisible(False)

    def veri_kumesi(self):

        self.group_list_sekonder_1 = [self.ui.doubleSpinBox_akim_sk_1, self.ui.doubleSpinBox_akim_2_sk_1,
                                      self.ui.doubleSpinBox_cap_sk_1,
                                      self.ui.doubleSpinBox_cap_2_sk_1, self.ui.doubleSpinBox_sipir_sk_1,
                                      self.ui.doubleSpinBox_kesit_sk_1,
                                      self.ui.doubleSpinBox_sipir_2_sk_1, self.ui.doubleSpinBox_v_sk_1,
                                      self.ui.comboBox_folyotel_sk_1,
                                      self.ui.comboBox_folyotel_sk_1, self.ui.comboBox_karetel_sk_1,  # 10
                                      self.ui.comboBox_tel_sk_1,
                                      self.ui.doubleSpinBox_folyotel_11_sk_1, self.ui.doubleSpinBox_folyotel_12_sk_1,
                                      self.ui.doubleSpinBox_folyotel_21_sk_1, self.ui.doubleSpinBox_folyotel_22_sk_1,
                                      self.ui.doubleSpinBox_folyotel_31_sk_1, self.ui.doubleSpinBox_folyotel_32_sk_1,
                                      self.ui.doubleSpinBox_folyotel_41_sk_1, self.ui.doubleSpinBox_folyotel_42_sk_1,
                                      self.ui.doubleSpinBox_kapton_1_sk_1, self.ui.doubleSpinBox_kapton_2_sk_1,
                                      self.ui.doubleSpinBox_kapton_3_sk_1, self.ui.doubleSpinBox_kapton_4_sk_1,
                                      self.ui.doubleSpinBox_kare_tel_11_sk_1, self.ui.doubleSpinBox_kare_tel_12_sk_1,
                                      self.ui.doubleSpinBox_kare_tel_21_sk_1, self.ui.doubleSpinBox_kare_tel_22_sk_1,
                                      self.ui.doubleSpinBox_kare_tel_31_sk_1, self.ui.doubleSpinBox_kare_tel_32_sk_1,
                                      self.ui.doubleSpinBox_kare_tel_41_sk_1, self.ui.doubleSpinBox_kare_tel_42_sk_1,
                                      # 31
                                      self.ui.comboBox_telkademe_sk_1, self.ui.lineEdit_no_sk_1,
                                      self.ui.doubleSpinBox_kesit_2_sk_1,
                                      self.ui.doubleSpinBox_tel_en_sk_1, self.ui.doubleSpinBox_tel_yuk_sk_1,
                                      self.ui.doubleSpinBox_spirkat_sk_1,  # 37
                                      self.ui.doubleSpinBox_kat_sk_1, self.ui.doubleSpinBox_katbosluk_sk_1,
                                      self.ui.doubleSpinBox_tel_uzunluk_sk_1,
                                      self.ui.doubleSpinBox_tel_agirlik_sk_1,
                                      self.ui.doubleSpinBox_sarim_yukseklik_sk_1,
                                      self.ui.doubleSpinBox_sonkat_spir_sk_1, self.ui.checkBox_sipir_man_sk_1,
                                      self.ui.pushButton_h1_p_buton_21_sk_1, self.ui.pushButton_karetel_sk_1,
                                      self.ui.pushButton_folyotel_sk_1, self.ui.pushButton_kapton_sk_1,
                                      self.ui.checkBox_sipir_man_sk_1,
                                      self.ui.label_kesit_ok_sk_1, self.ui.label_kesit_error_sk_1,
                                      self.ui.label_akim_ok_sk_1, self.ui.label_akim_error_sk_1,
                                      self.ui.doubleSpinBox_mancap_sk_11,  # 54
                                      self.ui.doubleSpinBox_mancap_sk_12, self.ui.doubleSpinBox_mancap_sk_13,
                                      self.ui.doubleSpinBox_mancap_sk_14]  # 57
        self.group_list_sekonder_2 = [self.ui.doubleSpinBox_akim_sk_2, self.ui.doubleSpinBox_akim_2_sk_2,
                                      self.ui.doubleSpinBox_cap_sk_2,
                                      self.ui.doubleSpinBox_cap_2_sk_2, self.ui.doubleSpinBox_sipir_sk_2,
                                      self.ui.doubleSpinBox_kesit_sk_2,
                                      self.ui.doubleSpinBox_sipir_2_sk_2, self.ui.doubleSpinBox_v_sk_2,
                                      self.ui.comboBox_folyotel_sk_2,
                                      self.ui.comboBox_folyotel_sk_2, self.ui.comboBox_karetel_sk_2,
                                      self.ui.comboBox_tel_sk_2,
                                      self.ui.doubleSpinBox_folyotel_11_sk_2, self.ui.doubleSpinBox_folyotel_12_sk_2,
                                      self.ui.doubleSpinBox_folyotel_21_sk_2, self.ui.doubleSpinBox_folyotel_22_sk_2,
                                      self.ui.doubleSpinBox_folyotel_31_sk_2, self.ui.doubleSpinBox_folyotel_32_sk_2,
                                      self.ui.doubleSpinBox_folyotel_41_sk_2, self.ui.doubleSpinBox_folyotel_42_sk_2,
                                      self.ui.doubleSpinBox_kapton_1_sk_2, self.ui.doubleSpinBox_kapton_2_sk_2,
                                      self.ui.doubleSpinBox_kapton_3_sk_2, self.ui.doubleSpinBox_kapton_4_sk_2,
                                      self.ui.doubleSpinBox_kare_tel_11_sk_2, self.ui.doubleSpinBox_kare_tel_12_sk_2,
                                      self.ui.doubleSpinBox_kare_tel_21_sk_2, self.ui.doubleSpinBox_kare_tel_22_sk_2,
                                      self.ui.doubleSpinBox_kare_tel_31_sk_2, self.ui.doubleSpinBox_kare_tel_32_sk_2,
                                      self.ui.doubleSpinBox_kare_tel_41_sk_2, self.ui.doubleSpinBox_kare_tel_42_sk_2,
                                      self.ui.comboBox_telkademe_sk_2, self.ui.lineEdit_no_sk_2,
                                      self.ui.doubleSpinBox_kesit_2_sk_2,
                                      self.ui.doubleSpinBox_tel_en_sk_2, self.ui.doubleSpinBox_tel_yuk_sk_2,
                                      self.ui.doubleSpinBox_spirkat_sk_2,  # 37
                                      self.ui.doubleSpinBox_kat_sk_2, self.ui.doubleSpinBox_katbosluk_sk_2,
                                      self.ui.doubleSpinBox_tel_uzunluk_sk_2,
                                      self.ui.doubleSpinBox_tel_agirlik_sk_2,
                                      self.ui.doubleSpinBox_sarim_yukseklik_sk_2,
                                      self.ui.doubleSpinBox_sonkat_spir_sk_2, self.ui.checkBox_sipir_man_sk_2,
                                      self.ui.pushButton_h1_p_buton_21_sk_2, self.ui.pushButton_karetel_sk_2,
                                      self.ui.pushButton_folyotel_sk_2, self.ui.pushButton_kapton_sk_2,
                                      self.ui.checkBox_sipir_man_sk_2,
                                      self.ui.label_kesit_ok_sk_2, self.ui.label_kesit_error_sk_2,
                                      self.ui.label_akim_ok_sk_2, self.ui.label_akim_error_sk_2,
                                      self.ui.doubleSpinBox_mancap_sk_21,  # 54
                                      self.ui.doubleSpinBox_mancap_sk_22, self.ui.doubleSpinBox_mancap_sk_23,
                                      self.ui.doubleSpinBox_mancap_sk_24]  # 57
        self.group_list_sekonder_3 = [self.ui.doubleSpinBox_akim_sk_3, self.ui.doubleSpinBox_akim_2_sk_3,
                                      self.ui.doubleSpinBox_cap_sk_3,
                                      self.ui.doubleSpinBox_cap_2_sk_3, self.ui.doubleSpinBox_sipir_sk_3,
                                      self.ui.doubleSpinBox_kesit_sk_3,
                                      self.ui.doubleSpinBox_sipir_2_sk_3, self.ui.doubleSpinBox_v_sk_3,
                                      self.ui.comboBox_folyotel_sk_3,
                                      self.ui.comboBox_folyotel_sk_3, self.ui.comboBox_karetel_sk_3,
                                      self.ui.comboBox_tel_sk_3,
                                      self.ui.doubleSpinBox_folyotel_11_sk_3, self.ui.doubleSpinBox_folyotel_12_sk_3,
                                      self.ui.doubleSpinBox_folyotel_21_sk_3, self.ui.doubleSpinBox_folyotel_22_sk_3,
                                      self.ui.doubleSpinBox_folyotel_31_sk_3, self.ui.doubleSpinBox_folyotel_32_sk_3,
                                      self.ui.doubleSpinBox_folyotel_41_sk_3, self.ui.doubleSpinBox_folyotel_42_sk_3,
                                      self.ui.doubleSpinBox_kapton_1_sk_3, self.ui.doubleSpinBox_kapton_2_sk_3,
                                      self.ui.doubleSpinBox_kapton_3_sk_3, self.ui.doubleSpinBox_kapton_4_sk_3,
                                      self.ui.doubleSpinBox_kare_tel_11_sk_3, self.ui.doubleSpinBox_kare_tel_12_sk_3,
                                      self.ui.doubleSpinBox_kare_tel_21_sk_3, self.ui.doubleSpinBox_kare_tel_22_sk_3,
                                      self.ui.doubleSpinBox_kare_tel_31_sk_3, self.ui.doubleSpinBox_kare_tel_32_sk_3,
                                      self.ui.doubleSpinBox_kare_tel_41_sk_3, self.ui.doubleSpinBox_kare_tel_42_sk_3,
                                      self.ui.comboBox_telkademe_sk_3, self.ui.lineEdit_no_sk_3,
                                      self.ui.doubleSpinBox_kesit_2_sk_3,
                                      self.ui.doubleSpinBox_tel_en_sk_3, self.ui.doubleSpinBox_tel_yuk_sk_3,
                                      self.ui.doubleSpinBox_spirkat_sk_3,  # 37
                                      self.ui.doubleSpinBox_kat_sk_3, self.ui.doubleSpinBox_katbosluk_sk_3,
                                      self.ui.doubleSpinBox_tel_uzunluk_sk_3,
                                      self.ui.doubleSpinBox_tel_agirlik_sk_3,
                                      self.ui.doubleSpinBox_sarim_yukseklik_sk_3,
                                      self.ui.doubleSpinBox_sonkat_spir_sk_3, self.ui.checkBox_sipir_man_sk_3,
                                      self.ui.pushButton_h1_p_buton_21_sk_3, self.ui.pushButton_karetel_sk_3,
                                      self.ui.pushButton_folyotel_sk_3, self.ui.pushButton_kapton_sk_3,
                                      self.ui.checkBox_sipir_man_sk_3,
                                      self.ui.label_kesit_ok_sk_3, self.ui.label_kesit_error_sk_3,
                                      self.ui.label_akim_ok_sk_3, self.ui.label_akim_error_sk_3,
                                      self.ui.doubleSpinBox_mancap_sk_31,  # 54
                                      self.ui.doubleSpinBox_mancap_sk_32, self.ui.doubleSpinBox_mancap_sk_33,
                                      self.ui.doubleSpinBox_mancap_sk_34]  # 57
        self.group_list_sekonder_4 = [self.ui.doubleSpinBox_akim_sk_4, self.ui.doubleSpinBox_akim_2_sk_4,
                                      self.ui.doubleSpinBox_cap_sk_4,
                                      self.ui.doubleSpinBox_cap_2_sk_4, self.ui.doubleSpinBox_sipir_sk_4,
                                      self.ui.doubleSpinBox_kesit_sk_4,
                                      self.ui.doubleSpinBox_sipir_2_sk_4, self.ui.doubleSpinBox_v_sk_4,
                                      self.ui.comboBox_folyotel_sk_4,
                                      self.ui.comboBox_folyotel_sk_4, self.ui.comboBox_karetel_sk_4,
                                      self.ui.comboBox_tel_sk_4,
                                      self.ui.doubleSpinBox_folyotel_11_sk_4, self.ui.doubleSpinBox_folyotel_12_sk_4,
                                      self.ui.doubleSpinBox_folyotel_21_sk_4, self.ui.doubleSpinBox_folyotel_22_sk_4,
                                      self.ui.doubleSpinBox_folyotel_31_sk_4, self.ui.doubleSpinBox_folyotel_32_sk_4,
                                      self.ui.doubleSpinBox_folyotel_41_sk_4, self.ui.doubleSpinBox_folyotel_42_sk_4,
                                      self.ui.doubleSpinBox_kapton_1_sk_4, self.ui.doubleSpinBox_kapton_2_sk_4,
                                      self.ui.doubleSpinBox_kapton_3_sk_4, self.ui.doubleSpinBox_kapton_4_sk_4,
                                      self.ui.doubleSpinBox_kare_tel_11_sk_4, self.ui.doubleSpinBox_kare_tel_12_sk_4,
                                      self.ui.doubleSpinBox_kare_tel_21_sk_4, self.ui.doubleSpinBox_kare_tel_22_sk_4,
                                      self.ui.doubleSpinBox_kare_tel_31_sk_4, self.ui.doubleSpinBox_kare_tel_32_sk_4,
                                      self.ui.doubleSpinBox_kare_tel_41_sk_4, self.ui.doubleSpinBox_kare_tel_42_sk_4,
                                      self.ui.comboBox_telkademe_sk_4, self.ui.lineEdit_no_sk_4,
                                      self.ui.doubleSpinBox_kesit_2_sk_4,
                                      self.ui.doubleSpinBox_tel_en_sk_4, self.ui.doubleSpinBox_tel_yuk_sk_4,
                                      self.ui.doubleSpinBox_spirkat_sk_4,  # 37
                                      self.ui.doubleSpinBox_kat_sk_4, self.ui.doubleSpinBox_katbosluk_sk_4,
                                      self.ui.doubleSpinBox_tel_uzunluk_sk_4,
                                      self.ui.doubleSpinBox_tel_agirlik_sk_4,
                                      self.ui.doubleSpinBox_sarim_yukseklik_sk_4,
                                      self.ui.doubleSpinBox_sonkat_spir_sk_4, self.ui.checkBox_sipir_man_sk_4,
                                      self.ui.pushButton_h1_p_buton_21_sk_4, self.ui.pushButton_karetel_sk_4,
                                      self.ui.pushButton_folyotel_sk_4, self.ui.pushButton_kapton_sk_4,
                                      self.ui.checkBox_sipir_man_sk_4,
                                      self.ui.label_kesit_ok_sk_4, self.ui.label_kesit_error_sk_4,
                                      self.ui.label_akim_ok_sk_4, self.ui.label_akim_error_sk_4,
                                      self.ui.doubleSpinBox_mancap_sk_41,  # 54
                                      self.ui.doubleSpinBox_mancap_sk_42, self.ui.doubleSpinBox_mancap_sk_43,
                                      self.ui.doubleSpinBox_mancap_sk_44]  # 57
        self.group_list_sekonder_5 = [self.ui.doubleSpinBox_akim_sk_5, self.ui.doubleSpinBox_akim_2_sk_5,
                                      self.ui.doubleSpinBox_cap_sk_5,
                                      self.ui.doubleSpinBox_cap_2_sk_5, self.ui.doubleSpinBox_sipir_sk_5,
                                      self.ui.doubleSpinBox_kesit_sk_5,
                                      self.ui.doubleSpinBox_sipir_2_sk_5, self.ui.doubleSpinBox_v_sk_5,
                                      self.ui.comboBox_folyotel_sk_5,
                                      self.ui.comboBox_folyotel_sk_5, self.ui.comboBox_karetel_sk_5,
                                      self.ui.comboBox_tel_sk_5,
                                      self.ui.doubleSpinBox_folyotel_11_sk_5, self.ui.doubleSpinBox_folyotel_12_sk_5,
                                      self.ui.doubleSpinBox_folyotel_21_sk_5, self.ui.doubleSpinBox_folyotel_22_sk_5,
                                      self.ui.doubleSpinBox_folyotel_31_sk_5, self.ui.doubleSpinBox_folyotel_32_sk_5,
                                      self.ui.doubleSpinBox_folyotel_41_sk_5, self.ui.doubleSpinBox_folyotel_42_sk_5,
                                      self.ui.doubleSpinBox_kapton_1_sk_5, self.ui.doubleSpinBox_kapton_2_sk_5,
                                      self.ui.doubleSpinBox_kapton_3_sk_5, self.ui.doubleSpinBox_kapton_4_sk_5,
                                      self.ui.doubleSpinBox_kare_tel_11_sk_5, self.ui.doubleSpinBox_kare_tel_12_sk_5,
                                      self.ui.doubleSpinBox_kare_tel_21_sk_5, self.ui.doubleSpinBox_kare_tel_22_sk_5,
                                      self.ui.doubleSpinBox_kare_tel_31_sk_5, self.ui.doubleSpinBox_kare_tel_32_sk_5,
                                      self.ui.doubleSpinBox_kare_tel_41_sk_5, self.ui.doubleSpinBox_kare_tel_42_sk_5,
                                      self.ui.comboBox_telkademe_sk_5, self.ui.lineEdit_no_sk_5,
                                      self.ui.doubleSpinBox_kesit_2_sk_5,
                                      self.ui.doubleSpinBox_tel_en_sk_5, self.ui.doubleSpinBox_tel_yuk_sk_5,
                                      self.ui.doubleSpinBox_spirkat_sk_5,  # 37
                                      self.ui.doubleSpinBox_kat_sk_5, self.ui.doubleSpinBox_katbosluk_sk_5,
                                      self.ui.doubleSpinBox_tel_uzunluk_sk_5,
                                      self.ui.doubleSpinBox_tel_agirlik_sk_5,
                                      self.ui.doubleSpinBox_sarim_yukseklik_sk_5,
                                      self.ui.doubleSpinBox_sonkat_spir_sk_5, self.ui.checkBox_sipir_man_sk_5,
                                      self.ui.pushButton_h1_p_buton_21_sk_5, self.ui.pushButton_karetel_sk_5,
                                      self.ui.pushButton_folyotel_sk_5, self.ui.pushButton_kapton_sk_5,
                                      self.ui.checkBox_sipir_man_sk_5,
                                      self.ui.label_kesit_ok_sk_5, self.ui.label_kesit_error_sk_5,
                                      self.ui.label_akim_ok_sk_5, self.ui.label_akim_error_sk_5,
                                      self.ui.doubleSpinBox_mancap_sk_51,  # 54
                                      self.ui.doubleSpinBox_mancap_sk_52, self.ui.doubleSpinBox_mancap_sk_53,
                                      self.ui.doubleSpinBox_mancap_sk_54]  # 57
        self.group_list_sekonder_6 = [self.ui.doubleSpinBox_akim_sk_6, self.ui.doubleSpinBox_akim_2_sk_6,
                                      self.ui.doubleSpinBox_cap_sk_6,
                                      self.ui.doubleSpinBox_cap_2_sk_6, self.ui.doubleSpinBox_sipir_sk_6,
                                      self.ui.doubleSpinBox_kesit_sk_6,
                                      self.ui.doubleSpinBox_sipir_2_sk_6, self.ui.doubleSpinBox_v_sk_6,
                                      self.ui.comboBox_folyotel_sk_6,
                                      self.ui.comboBox_folyotel_sk_6, self.ui.comboBox_karetel_sk_6,
                                      self.ui.comboBox_tel_sk_6,
                                      self.ui.doubleSpinBox_folyotel_11_sk_6, self.ui.doubleSpinBox_folyotel_12_sk_6,
                                      self.ui.doubleSpinBox_folyotel_21_sk_6, self.ui.doubleSpinBox_folyotel_22_sk_6,
                                      self.ui.doubleSpinBox_folyotel_31_sk_6, self.ui.doubleSpinBox_folyotel_32_sk_6,
                                      self.ui.doubleSpinBox_folyotel_41_sk_6, self.ui.doubleSpinBox_folyotel_42_sk_6,
                                      self.ui.doubleSpinBox_kapton_1_sk_6, self.ui.doubleSpinBox_kapton_2_sk_6,
                                      self.ui.doubleSpinBox_kapton_3_sk_6, self.ui.doubleSpinBox_kapton_4_sk_6,
                                      self.ui.doubleSpinBox_kare_tel_11_sk_6, self.ui.doubleSpinBox_kare_tel_12_sk_6,
                                      self.ui.doubleSpinBox_kare_tel_21_sk_6, self.ui.doubleSpinBox_kare_tel_22_sk_6,
                                      self.ui.doubleSpinBox_kare_tel_31_sk_6, self.ui.doubleSpinBox_kare_tel_32_sk_6,
                                      self.ui.doubleSpinBox_kare_tel_41_sk_6, self.ui.doubleSpinBox_kare_tel_42_sk_6,
                                      self.ui.comboBox_telkademe_sk_6, self.ui.lineEdit_no_sk_6,
                                      self.ui.doubleSpinBox_kesit_2_sk_6,
                                      self.ui.doubleSpinBox_tel_en_sk_6, self.ui.doubleSpinBox_tel_yuk_sk_6,
                                      self.ui.doubleSpinBox_spirkat_sk_6,  # 37
                                      self.ui.doubleSpinBox_kat_sk_6, self.ui.doubleSpinBox_katbosluk_sk_6,
                                      self.ui.doubleSpinBox_tel_uzunluk_sk_6,
                                      self.ui.doubleSpinBox_tel_agirlik_sk_6,
                                      self.ui.doubleSpinBox_sarim_yukseklik_sk_6,
                                      self.ui.doubleSpinBox_sonkat_spir_sk_6, self.ui.checkBox_sipir_man_sk_6,
                                      self.ui.pushButton_h1_p_buton_21_sk_6, self.ui.pushButton_karetel_sk_6,
                                      self.ui.pushButton_folyotel_sk_6, self.ui.pushButton_kapton_sk_6,
                                      self.ui.checkBox_sipir_man_sk_6,
                                      self.ui.label_kesit_ok_sk_6, self.ui.label_kesit_error_sk_6,
                                      self.ui.label_akim_ok_sk_6, self.ui.label_akim_error_sk_6,
                                      self.ui.doubleSpinBox_mancap_sk_61,  # 54
                                      self.ui.doubleSpinBox_mancap_sk_62, self.ui.doubleSpinBox_mancap_sk_63,
                                      self.ui.doubleSpinBox_mancap_sk_64]  # 57
        self.group_list_sekonder_7 = [self.ui.doubleSpinBox_akim_sk_7, self.ui.doubleSpinBox_akim_2_sk_7,
                                      self.ui.doubleSpinBox_cap_sk_7,
                                      self.ui.doubleSpinBox_cap_2_sk_7, self.ui.doubleSpinBox_sipir_sk_7,
                                      self.ui.doubleSpinBox_kesit_sk_7,
                                      self.ui.doubleSpinBox_sipir_2_sk_7, self.ui.doubleSpinBox_v_sk_7,
                                      self.ui.comboBox_folyotel_sk_7,
                                      self.ui.comboBox_folyotel_sk_7, self.ui.comboBox_karetel_sk_7,
                                      self.ui.comboBox_tel_sk_7,
                                      self.ui.doubleSpinBox_folyotel_11_sk_7, self.ui.doubleSpinBox_folyotel_12_sk_7,
                                      self.ui.doubleSpinBox_folyotel_21_sk_7, self.ui.doubleSpinBox_folyotel_22_sk_7,
                                      self.ui.doubleSpinBox_folyotel_31_sk_7, self.ui.doubleSpinBox_folyotel_32_sk_7,
                                      self.ui.doubleSpinBox_folyotel_41_sk_7, self.ui.doubleSpinBox_folyotel_42_sk_7,
                                      self.ui.doubleSpinBox_kapton_1_sk_7, self.ui.doubleSpinBox_kapton_2_sk_7,
                                      self.ui.doubleSpinBox_kapton_3_sk_7, self.ui.doubleSpinBox_kapton_4_sk_7,
                                      self.ui.doubleSpinBox_kare_tel_11_sk_7, self.ui.doubleSpinBox_kare_tel_12_sk_7,
                                      self.ui.doubleSpinBox_kare_tel_21_sk_7, self.ui.doubleSpinBox_kare_tel_22_sk_7,
                                      self.ui.doubleSpinBox_kare_tel_31_sk_7, self.ui.doubleSpinBox_kare_tel_32_sk_7,
                                      self.ui.doubleSpinBox_kare_tel_41_sk_7, self.ui.doubleSpinBox_kare_tel_42_sk_7,
                                      self.ui.comboBox_telkademe_sk_7, self.ui.lineEdit_no_sk_7,
                                      self.ui.doubleSpinBox_kesit_2_sk_7,
                                      self.ui.doubleSpinBox_tel_en_sk_7, self.ui.doubleSpinBox_tel_yuk_sk_7,
                                      self.ui.doubleSpinBox_spirkat_sk_7,  # 37
                                      self.ui.doubleSpinBox_kat_sk_7, self.ui.doubleSpinBox_katbosluk_sk_7,
                                      self.ui.doubleSpinBox_tel_uzunluk_sk_7,
                                      self.ui.doubleSpinBox_tel_agirlik_sk_7,
                                      self.ui.doubleSpinBox_sarim_yukseklik_sk_7,
                                      self.ui.doubleSpinBox_sonkat_spir_sk_7, self.ui.checkBox_sipir_man_sk_7,
                                      self.ui.pushButton_h1_p_buton_21_sk_7, self.ui.pushButton_karetel_sk_7,
                                      self.ui.pushButton_folyotel_sk_7, self.ui.pushButton_kapton_sk_7,
                                      self.ui.checkBox_sipir_man_sk_7,
                                      self.ui.label_kesit_ok_sk_7, self.ui.label_kesit_error_sk_7,
                                      self.ui.label_akim_ok_sk_7, self.ui.label_akim_error_sk_7,
                                      self.ui.doubleSpinBox_mancap_sk_71,  # 54
                                      self.ui.doubleSpinBox_mancap_sk_72, self.ui.doubleSpinBox_mancap_sk_73,
                                      self.ui.doubleSpinBox_mancap_sk_74]  # 57
        self.group_list_sekonder_8 = [self.ui.doubleSpinBox_akim_sk_8, self.ui.doubleSpinBox_akim_2_sk_8,
                                      self.ui.doubleSpinBox_cap_sk_8,
                                      self.ui.doubleSpinBox_cap_2_sk_8, self.ui.doubleSpinBox_sipir_sk_8,
                                      self.ui.doubleSpinBox_kesit_sk_8,
                                      self.ui.doubleSpinBox_sipir_2_sk_8, self.ui.doubleSpinBox_v_sk_8,
                                      self.ui.comboBox_folyotel_sk_8,
                                      self.ui.comboBox_folyotel_sk_8, self.ui.comboBox_karetel_sk_8,
                                      self.ui.comboBox_tel_sk_8,
                                      self.ui.doubleSpinBox_folyotel_11_sk_8, self.ui.doubleSpinBox_folyotel_12_sk_8,
                                      self.ui.doubleSpinBox_folyotel_21_sk_8, self.ui.doubleSpinBox_folyotel_22_sk_8,
                                      self.ui.doubleSpinBox_folyotel_31_sk_8, self.ui.doubleSpinBox_folyotel_32_sk_8,
                                      self.ui.doubleSpinBox_folyotel_41_sk_8, self.ui.doubleSpinBox_folyotel_42_sk_8,
                                      self.ui.doubleSpinBox_kapton_1_sk_8, self.ui.doubleSpinBox_kapton_2_sk_8,
                                      self.ui.doubleSpinBox_kapton_3_sk_8, self.ui.doubleSpinBox_kapton_4_sk_8,
                                      self.ui.doubleSpinBox_kare_tel_11_sk_8, self.ui.doubleSpinBox_kare_tel_12_sk_8,
                                      self.ui.doubleSpinBox_kare_tel_21_sk_8, self.ui.doubleSpinBox_kare_tel_22_sk_8,
                                      self.ui.doubleSpinBox_kare_tel_31_sk_8, self.ui.doubleSpinBox_kare_tel_32_sk_8,
                                      self.ui.doubleSpinBox_kare_tel_41_sk_8, self.ui.doubleSpinBox_kare_tel_42_sk_8,
                                      self.ui.comboBox_telkademe_sk_8, self.ui.lineEdit_no_sk_8,
                                      self.ui.doubleSpinBox_kesit_2_sk_8,
                                      self.ui.doubleSpinBox_tel_en_sk_8, self.ui.doubleSpinBox_tel_yuk_sk_8,
                                      self.ui.doubleSpinBox_spirkat_sk_8,  # 37
                                      self.ui.doubleSpinBox_kat_sk_8, self.ui.doubleSpinBox_katbosluk_sk_8,
                                      self.ui.doubleSpinBox_tel_uzunluk_sk_8,
                                      self.ui.doubleSpinBox_tel_agirlik_sk_8,
                                      self.ui.doubleSpinBox_sarim_yukseklik_sk_8,
                                      self.ui.doubleSpinBox_sonkat_spir_sk_8, self.ui.checkBox_sipir_man_sk_8,
                                      self.ui.pushButton_h1_p_buton_21_sk_8, self.ui.pushButton_karetel_sk_8,
                                      self.ui.pushButton_folyotel_sk_8, self.ui.pushButton_kapton_sk_8,
                                      self.ui.checkBox_sipir_man_sk_8,
                                      self.ui.label_kesit_ok_sk_8, self.ui.label_kesit_error_sk_8,
                                      self.ui.label_akim_ok_sk_8, self.ui.label_akim_error_sk_8,
                                      self.ui.doubleSpinBox_mancap_sk_81,  # 54
                                      self.ui.doubleSpinBox_mancap_sk_82, self.ui.doubleSpinBox_mancap_sk_83,
                                      self.ui.doubleSpinBox_mancap_sk_84]  # 57
        self.group_list_sekonder_9 = [self.ui.doubleSpinBox_akim_sk_9, self.ui.doubleSpinBox_akim_2_sk_9,
                                      self.ui.doubleSpinBox_cap_sk_9,
                                      self.ui.doubleSpinBox_cap_2_sk_9, self.ui.doubleSpinBox_sipir_sk_9,
                                      self.ui.doubleSpinBox_kesit_sk_9,
                                      self.ui.doubleSpinBox_sipir_2_sk_9, self.ui.doubleSpinBox_v_sk_9,
                                      self.ui.comboBox_folyotel_sk_9,
                                      self.ui.comboBox_folyotel_sk_9, self.ui.comboBox_karetel_sk_9,
                                      self.ui.comboBox_tel_sk_9,
                                      self.ui.doubleSpinBox_folyotel_11_sk_9, self.ui.doubleSpinBox_folyotel_12_sk_9,
                                      self.ui.doubleSpinBox_folyotel_21_sk_9, self.ui.doubleSpinBox_folyotel_22_sk_9,
                                      self.ui.doubleSpinBox_folyotel_31_sk_9, self.ui.doubleSpinBox_folyotel_32_sk_9,
                                      self.ui.doubleSpinBox_folyotel_41_sk_9, self.ui.doubleSpinBox_folyotel_42_sk_9,
                                      self.ui.doubleSpinBox_kapton_1_sk_9, self.ui.doubleSpinBox_kapton_2_sk_9,
                                      self.ui.doubleSpinBox_kapton_3_sk_9, self.ui.doubleSpinBox_kapton_4_sk_9,
                                      self.ui.doubleSpinBox_kare_tel_11_sk_9, self.ui.doubleSpinBox_kare_tel_12_sk_9,
                                      self.ui.doubleSpinBox_kare_tel_21_sk_9, self.ui.doubleSpinBox_kare_tel_22_sk_9,
                                      self.ui.doubleSpinBox_kare_tel_31_sk_9, self.ui.doubleSpinBox_kare_tel_32_sk_9,
                                      self.ui.doubleSpinBox_kare_tel_41_sk_9, self.ui.doubleSpinBox_kare_tel_42_sk_9,
                                      self.ui.comboBox_telkademe_sk_9, self.ui.lineEdit_no_sk_9,
                                      self.ui.doubleSpinBox_kesit_2_sk_9,
                                      self.ui.doubleSpinBox_tel_en_sk_9, self.ui.doubleSpinBox_tel_yuk_sk_9,
                                      self.ui.doubleSpinBox_spirkat_sk_9,  # 37
                                      self.ui.doubleSpinBox_kat_sk_9, self.ui.doubleSpinBox_katbosluk_sk_9,
                                      self.ui.doubleSpinBox_tel_uzunluk_sk_9,
                                      self.ui.doubleSpinBox_tel_agirlik_sk_9,
                                      self.ui.doubleSpinBox_sarim_yukseklik_sk_9,
                                      self.ui.doubleSpinBox_sonkat_spir_sk_9, self.ui.checkBox_sipir_man_sk_9,
                                      self.ui.pushButton_h1_p_buton_21_sk_9, self.ui.pushButton_karetel_sk_9,
                                      self.ui.pushButton_folyotel_sk_9, self.ui.pushButton_kapton_sk_9,
                                      self.ui.checkBox_sipir_man_sk_9,
                                      self.ui.label_kesit_ok_sk_9, self.ui.label_kesit_error_sk_9,
                                      self.ui.label_akim_ok_sk_9, self.ui.label_akim_error_sk_9,
                                      self.ui.doubleSpinBox_mancap_sk_91,  # 54
                                      self.ui.doubleSpinBox_mancap_sk_92, self.ui.doubleSpinBox_mancap_sk_93,
                                      self.ui.doubleSpinBox_mancap_sk_94]  # 57
        self.group_list_sekonder_10 = [self.ui.doubleSpinBox_akim_sk_10, self.ui.doubleSpinBox_akim_2_sk_10,
                                       self.ui.doubleSpinBox_cap_sk_10,
                                       self.ui.doubleSpinBox_cap_2_sk_10, self.ui.doubleSpinBox_sipir_sk_10,
                                       self.ui.doubleSpinBox_kesit_sk_10,
                                       self.ui.doubleSpinBox_sipir_2_sk_10, self.ui.doubleSpinBox_v_sk_10,
                                       self.ui.comboBox_folyotel_sk_10,
                                       self.ui.comboBox_folyotel_sk_10, self.ui.comboBox_karetel_sk_10,
                                       self.ui.comboBox_tel_sk_10,
                                       self.ui.doubleSpinBox_folyotel_11_sk_10, self.ui.doubleSpinBox_folyotel_12_sk_10,
                                       self.ui.doubleSpinBox_folyotel_21_sk_10, self.ui.doubleSpinBox_folyotel_22_sk_10,
                                       self.ui.doubleSpinBox_folyotel_31_sk_10, self.ui.doubleSpinBox_folyotel_32_sk_10,
                                       self.ui.doubleSpinBox_folyotel_41_sk_10, self.ui.doubleSpinBox_folyotel_42_sk_10,
                                       self.ui.doubleSpinBox_kapton_1_sk_10, self.ui.doubleSpinBox_kapton_2_sk_10,
                                       self.ui.doubleSpinBox_kapton_3_sk_10, self.ui.doubleSpinBox_kapton_4_sk_10,
                                       self.ui.doubleSpinBox_kare_tel_11_sk_10, self.ui.doubleSpinBox_kare_tel_12_sk_10,
                                       self.ui.doubleSpinBox_kare_tel_21_sk_10, self.ui.doubleSpinBox_kare_tel_22_sk_10,
                                       self.ui.doubleSpinBox_kare_tel_31_sk_10, self.ui.doubleSpinBox_kare_tel_32_sk_10,
                                       self.ui.doubleSpinBox_kare_tel_41_sk_10, self.ui.doubleSpinBox_kare_tel_42_sk_10,
                                       self.ui.comboBox_telkademe_sk_10, self.ui.lineEdit_no_sk_10,
                                       self.ui.doubleSpinBox_kesit_2_sk_10,
                                       self.ui.doubleSpinBox_tel_en_sk_10, self.ui.doubleSpinBox_tel_yuk_sk_10,
                                       self.ui.doubleSpinBox_spirkat_sk_10,  # 37
                                       self.ui.doubleSpinBox_kat_sk_10, self.ui.doubleSpinBox_katbosluk_sk_10,
                                       self.ui.doubleSpinBox_tel_uzunluk_sk_10,
                                       self.ui.doubleSpinBox_tel_agirlik_sk_10,
                                       self.ui.doubleSpinBox_sarim_yukseklik_sk_10,
                                       self.ui.doubleSpinBox_sonkat_spir_sk_10, self.ui.checkBox_sipir_man_sk_10,
                                       self.ui.pushButton_h1_p_buton_21_sk_10, self.ui.pushButton_karetel_sk_10,
                                       self.ui.pushButton_folyotel_sk_10, self.ui.pushButton_kapton_sk_10,
                                       self.ui.checkBox_sipir_man_sk_10,
                                       self.ui.label_kesit_ok_sk_10, self.ui.label_kesit_error_sk_10,
                                       self.ui.label_akim_ok_sk_10, self.ui.label_akim_error_sk_10,
                                       self.ui.doubleSpinBox_mancap_sk_101,  # 54
                                       self.ui.doubleSpinBox_mancap_sk_102, self.ui.doubleSpinBox_mancap_sk_103,
                                       self.ui.doubleSpinBox_mancap_sk_104]  # 57
        self.group_name_list_sekonder = [self.group_list_sekonder_1, self.group_list_sekonder_2,
                                         self.group_list_sekonder_3,
                                         self.group_list_sekonder_4, self.group_list_sekonder_5,
                                         self.group_list_sekonder_6, self.group_list_sekonder_7,
                                         self.group_list_sekonder_8, self.group_list_sekonder_9,
                                         self.group_list_sekonder_10]
        self.group_name_list_sekonder_2 = []
        self.kademe_list_sekonder = [[self.ui.groupBox_karetel_1_sk_1, self.ui.groupBox_karetel_2_sk_1,
                                      self.ui.groupBox_karetel_3_sk_1, self.ui.groupBox_karetel_4_sk_1],
                                     [self.ui.groupBox_karetel_1_sk_2, self.ui.groupBox_karetel_2_sk_2,
                                      self.ui.groupBox_karetel_3_sk_2, self.ui.groupBox_karetel_4_sk_2],
                                     [self.ui.groupBox_karetel_1_sk_3, self.ui.groupBox_karetel_2_sk_3,
                                      self.ui.groupBox_karetel_3_sk_3, self.ui.groupBox_karetel_4_sk_3],
                                     [self.ui.groupBox_karetel_1_sk_4, self.ui.groupBox_karetel_2_sk_4,
                                      self.ui.groupBox_karetel_3_sk_4, self.ui.groupBox_karetel_4_sk_4],
                                     [self.ui.groupBox_karetel_1_sk_5, self.ui.groupBox_karetel_2_sk_5,
                                      self.ui.groupBox_karetel_3_sk_5, self.ui.groupBox_karetel_4_sk_5],
                                     [self.ui.groupBox_karetel_1_sk_6, self.ui.groupBox_karetel_2_sk_6,
                                      self.ui.groupBox_karetel_3_sk_6, self.ui.groupBox_karetel_4_sk_6],
                                     [self.ui.groupBox_karetel_1_sk_7, self.ui.groupBox_karetel_2_sk_7,
                                      self.ui.groupBox_karetel_3_sk_7, self.ui.groupBox_karetel_4_sk_7],
                                     [self.ui.groupBox_karetel_1_sk_8, self.ui.groupBox_karetel_2_sk_8,
                                      self.ui.groupBox_karetel_3_sk_8, self.ui.groupBox_karetel_4_sk_8],
                                     [self.ui.groupBox_karetel_1_sk_9, self.ui.groupBox_karetel_2_sk_9,
                                      self.ui.groupBox_karetel_3_sk_9, self.ui.groupBox_karetel_4_sk_9],
                                     [self.ui.groupBox_karetel_1_sk_10, self.ui.groupBox_karetel_2_sk_10,
                                      self.ui.groupBox_karetel_3_sk_10, self.ui.groupBox_karetel_4_sk_10],
                                     [self.ui.groupBox_folyotel_1_sk_1, self.ui.groupBox_folyotel_2_sk_1,
                                      self.ui.groupBox_folyotel_3_sk_1, self.ui.groupBox_folyotel_4_sk_1],
                                     [self.ui.groupBox_folyotel_1_sk_2, self.ui.groupBox_folyotel_2_sk_2,
                                      self.ui.groupBox_folyotel_3_sk_2, self.ui.groupBox_folyotel_4_sk_2],
                                     [self.ui.groupBox_folyotel_1_sk_3, self.ui.groupBox_folyotel_2_sk_3,
                                      self.ui.groupBox_folyotel_3_sk_3, self.ui.groupBox_folyotel_4_sk_3],
                                     [self.ui.groupBox_folyotel_1_sk_4, self.ui.groupBox_folyotel_2_sk_4,
                                      self.ui.groupBox_folyotel_3_sk_4, self.ui.groupBox_folyotel_4_sk_4],
                                     [self.ui.groupBox_folyotel_1_sk_5, self.ui.groupBox_folyotel_2_sk_5,
                                      self.ui.groupBox_folyotel_3_sk_5, self.ui.groupBox_folyotel_4_sk_5],
                                     [self.ui.groupBox_folyotel_1_sk_6, self.ui.groupBox_folyotel_2_sk_6,
                                      self.ui.groupBox_folyotel_3_sk_6, self.ui.groupBox_folyotel_4_sk_6],
                                     [self.ui.groupBox_folyotel_1_sk_7, self.ui.groupBox_folyotel_2_sk_7,
                                      self.ui.groupBox_folyotel_3_sk_7, self.ui.groupBox_folyotel_4_sk_7],
                                     [self.ui.groupBox_folyotel_1_sk_8, self.ui.groupBox_folyotel_2_sk_8,
                                      self.ui.groupBox_folyotel_3_sk_8, self.ui.groupBox_folyotel_4_sk_8],
                                     [self.ui.groupBox_folyotel_1_sk_9, self.ui.groupBox_folyotel_2_sk_9,
                                      self.ui.groupBox_folyotel_3_sk_9, self.ui.groupBox_folyotel_4_sk_9],
                                     [self.ui.groupBox_folyotel_1_sk_10, self.ui.groupBox_folyotel_2_sk_10,
                                      self.ui.groupBox_folyotel_3_sk_10, self.ui.groupBox_folyotel_4_sk_10],
                                     [self.ui.doubleSpinBox_kapton_1_sk_1, self.ui.doubleSpinBox_kapton_2_sk_1,
                                      self.ui.doubleSpinBox_kapton_3_sk_1, self.ui.doubleSpinBox_kapton_4_sk_1],
                                     [self.ui.doubleSpinBox_kapton_1_sk_2, self.ui.doubleSpinBox_kapton_2_sk_2,
                                      self.ui.doubleSpinBox_kapton_3_sk_2, self.ui.doubleSpinBox_kapton_4_sk_2],
                                     [self.ui.doubleSpinBox_kapton_1_sk_3, self.ui.doubleSpinBox_kapton_2_sk_3,
                                      self.ui.doubleSpinBox_kapton_3_sk_3, self.ui.doubleSpinBox_kapton_4_sk_3],
                                     [self.ui.doubleSpinBox_kapton_1_sk_4, self.ui.doubleSpinBox_kapton_2_sk_4,
                                      self.ui.doubleSpinBox_kapton_3_sk_4, self.ui.doubleSpinBox_kapton_4_sk_4],
                                     [self.ui.doubleSpinBox_kapton_1_sk_5, self.ui.doubleSpinBox_kapton_2_sk_5,
                                      self.ui.doubleSpinBox_kapton_3_sk_5, self.ui.doubleSpinBox_kapton_4_sk_5],
                                     [self.ui.doubleSpinBox_kapton_1_sk_6, self.ui.doubleSpinBox_kapton_2_sk_6,
                                      self.ui.doubleSpinBox_kapton_3_sk_6, self.ui.doubleSpinBox_kapton_4_sk_6],
                                     [self.ui.doubleSpinBox_kapton_1_sk_7, self.ui.doubleSpinBox_kapton_2_sk_7,
                                      self.ui.doubleSpinBox_kapton_3_sk_7, self.ui.doubleSpinBox_kapton_4_sk_7],
                                     [self.ui.doubleSpinBox_kapton_1_sk_8, self.ui.doubleSpinBox_kapton_2_sk_8,
                                      self.ui.doubleSpinBox_kapton_3_sk_8, self.ui.doubleSpinBox_kapton_4_sk_8],
                                     [self.ui.doubleSpinBox_kapton_1_sk_9, self.ui.doubleSpinBox_kapton_2_sk_9,
                                      self.ui.doubleSpinBox_kapton_3_sk_9, self.ui.doubleSpinBox_kapton_4_sk_9],
                                     [self.ui.doubleSpinBox_kapton_1_sk_10, self.ui.doubleSpinBox_kapton_2_sk_10,
                                      self.ui.doubleSpinBox_kapton_3_sk_10, self.ui.doubleSpinBox_kapton_4_sk_10],
                                     [self.ui.doubleSpinBox_mancap_sk_11, self.ui.doubleSpinBox_mancap_sk_12,
                                      self.ui.doubleSpinBox_mancap_sk_13, self.ui.doubleSpinBox_mancap_sk_14],
                                     [self.ui.doubleSpinBox_mancap_sk_21, self.ui.doubleSpinBox_mancap_sk_22,
                                      self.ui.doubleSpinBox_mancap_sk_23, self.ui.doubleSpinBox_mancap_sk_24],
                                     [self.ui.doubleSpinBox_mancap_sk_31, self.ui.doubleSpinBox_mancap_sk_32,
                                      self.ui.doubleSpinBox_mancap_sk_33, self.ui.doubleSpinBox_mancap_sk_34],
                                     [self.ui.doubleSpinBox_mancap_sk_41, self.ui.doubleSpinBox_mancap_sk_42,
                                      self.ui.doubleSpinBox_mancap_sk_43, self.ui.doubleSpinBox_mancap_sk_44],
                                     [self.ui.doubleSpinBox_mancap_sk_51, self.ui.doubleSpinBox_mancap_sk_52,
                                      self.ui.doubleSpinBox_mancap_sk_53, self.ui.doubleSpinBox_mancap_sk_54],
                                     [self.ui.doubleSpinBox_mancap_sk_61, self.ui.doubleSpinBox_mancap_sk_62,
                                      self.ui.doubleSpinBox_mancap_sk_63, self.ui.doubleSpinBox_mancap_sk_64],
                                     [self.ui.doubleSpinBox_mancap_sk_71, self.ui.doubleSpinBox_mancap_sk_72,
                                      self.ui.doubleSpinBox_mancap_sk_73, self.ui.doubleSpinBox_mancap_sk_74],
                                     [self.ui.doubleSpinBox_mancap_sk_81, self.ui.doubleSpinBox_mancap_sk_82,
                                      self.ui.doubleSpinBox_mancap_sk_83, self.ui.doubleSpinBox_mancap_sk_84],
                                     [self.ui.doubleSpinBox_mancap_sk_91, self.ui.doubleSpinBox_mancap_sk_92,
                                      self.ui.doubleSpinBox_mancap_sk_93, self.ui.doubleSpinBox_mancap_sk_94],
                                     [self.ui.doubleSpinBox_mancap_sk_101, self.ui.doubleSpinBox_mancap_sk_102,
                                      self.ui.doubleSpinBox_mancap_sk_103, self.ui.doubleSpinBox_mancap_sk_104],
                                     ]

    def sekonder_kademe_secimi(self, mod, kademe=1):
        if mod == 0:
            self.ui.tabWidget_2.setCurrentIndex(kademe - 1)

        else:

            pass

    def sekonder_kademe_goster(self):

        self.sekonder_kademe_secimi(mod=0)
        self.sekonder_tel_kademeleri_resetle()
        self.hesap_guncelle()

    def sekonder_object_signals(self):

        self.group_name_list_sekonder[0][49].stateChanged.connect(
            lambda x: self.group_name_list_sekonder[0][6].setEnabled(self.group_name_list_sekonder[0][49].isChecked()))
        self.group_name_list_sekonder[1][49].stateChanged.connect(
            lambda x: self.group_name_list_sekonder[1][6].setEnabled(self.group_name_list_sekonder[1][49].isChecked()))
        self.group_name_list_sekonder[2][49].stateChanged.connect(
            lambda x: self.group_name_list_sekonder[2][6].setEnabled(self.group_name_list_sekonder[2][49].isChecked()))
        self.group_name_list_sekonder[3][49].stateChanged.connect(
            lambda x: self.group_name_list_sekonder[3][6].setEnabled(self.group_name_list_sekonder[3][49].isChecked()))
        self.group_name_list_sekonder[4][49].stateChanged.connect(
            lambda x: self.group_name_list_sekonder[4][6].setEnabled(self.group_name_list_sekonder[4][49].isChecked()))
        self.group_name_list_sekonder[5][49].stateChanged.connect(
            lambda x: self.group_name_list_sekonder[5][6].setEnabled(self.group_name_list_sekonder[5][49].isChecked()))
        self.group_name_list_sekonder[6][49].stateChanged.connect(
            lambda x: self.group_name_list_sekonder[6][6].setEnabled(self.group_name_list_sekonder[6][49].isChecked()))
        self.group_name_list_sekonder[7][49].stateChanged.connect(
            lambda x: self.group_name_list_sekonder[7][6].setEnabled(self.group_name_list_sekonder[7][49].isChecked()))
        self.group_name_list_sekonder[8][49].stateChanged.connect(
            lambda x: self.group_name_list_sekonder[8][6].setEnabled(self.group_name_list_sekonder[8][49].isChecked()))
        self.group_name_list_sekonder[9][49].stateChanged.connect(
            lambda x: self.group_name_list_sekonder[9][6].setEnabled(self.group_name_list_sekonder[9][49].isChecked()))
        for i in range(0, 10):

            self.group_name_list_sekonder[i][49].stateChanged.connect(self.hesap_guncelle)
            self.group_name_list_sekonder[i][45].clicked.connect(self.sekonder_open_tel_secim)
            self.group_name_list_sekonder[i][46].clicked.connect(self.sekonder_open_karetel_secim)
            self.group_name_list_sekonder[i][47].clicked.connect(self.sekonder_open_folyotel_secim)
            self.group_name_list_sekonder[i][48].clicked.connect(self.sekonder_open_kapton_secim)
            self.group_name_list_sekonder[i][32].currentTextChanged.connect(self.sekonder_yuvarlaktel_kademe_goster)
            self.group_name_list_sekonder[i][10].currentTextChanged.connect(self.sekonder_karetel_kademe_goster)
            self.group_name_list_sekonder[i][8].currentTextChanged.connect(self.sekonder_folyotel_kademe_goster)
            self.group_name_list_sekonder[i][9].currentTextChanged.connect(self.sekonder_kapton_kademe_goster)
            # self.group_name_list_sekonder[i][6].valueChanged.connect(lambda x:self.sekonder_man_spir_update())
            self.group_name_list_sekonder[i][6].valueChanged.connect(self.hesap_guncelle)
            self.group_name_list_sekonder[i][7].valueChanged.connect(self.hesap_guncelle)

            self.group_name_list_sekonder[i][41].valueChanged.connect(self.hesap_guncelle)
            for y in range(11, 33):
                self.object_multi_connect(object=self.group_name_list_sekonder[i][y],
                                          arg=self.hesap_guncelle)
            for y in range(54, 58):
                self.object_multi_connect(object=self.group_name_list_sekonder[i][y],
                                          arg=self.hesap_guncelle)

    def sekonder_open_tel_secim(self):
        sender = self.sender()
        index = int(sender.objectName().split("_")[len(sender.objectName().split("_")) - 1]) - 1

        self.open_telsecim(gl=self.group_name_list_sekonder, type="tel", index=index)

    def sekonder_open_karetel_secim(self):
        sender = self.sender()
        index = int(sender.objectName().split("_")[len(sender.objectName().split("_")) - 1]) - 1
        self.open_telsecim(gl=self.group_name_list_sekonder, type="karetel", index=index)

    def sekonder_open_folyotel_secim(self):
        sender = self.sender()
        index = int(sender.objectName().split("_")[len(sender.objectName().split("_")) - 1]) - 1
        self.open_telsecim(gl=self.group_name_list_sekonder, type="folyotel", index=index)

    def sekonder_open_kapton_secim(self):
        sender = self.sender()
        index = int(sender.objectName().split("_")[len(sender.objectName().split("_")) - 1]) - 1
        self.open_telsecim(gl=self.group_name_list_sekonder, type="kapton", index=index)

    def sekonder_yuvarlaktel_kademe_goster(self):
        sender = self.sender()
        index = int(sender.objectName().split("_")[len(sender.objectName().split("_")) - 1]) - 1
        self.kademe_goster(object=self.group_name_list_sekonder[index][32],
                           group_list=self.kademe_list_sekonder[index + 30])

    def sekonder_karetel_kademe_goster(self):
        sender = self.sender()
        index = int(sender.objectName().split("_")[len(sender.objectName().split("_")) - 1]) - 1
        self.kademe_goster(object=self.group_name_list_sekonder[index][10], group_list=self.kademe_list_sekonder[index])

    def sekonder_folyotel_kademe_goster(self):
        sender = self.sender()
        index = int(sender.objectName().split("_")[len(sender.objectName().split("_")) - 1]) - 1
        self.kademe_goster(object=self.group_name_list_sekonder[index][8],
                           group_list=self.kademe_list_sekonder[index + 10])

    def sekonder_kapton_kademe_goster(self):
        sender = self.sender()
        index = int(sender.objectName().split("_")[len(sender.objectName().split("_")) - 1]) - 1
        self.kademe_goster(object=self.group_name_list_sekonder[index][9],
                           group_list=self.kademe_list_sekonder[index + 20])

    def sekonder_tel_kademeleri_resetle(self):
        for index in range(0, 10):
            self.kademe_goster(object=self.group_name_list_sekonder[index][10],
                               group_list=self.kademe_list_sekonder[index])
            self.kademe_goster(object=self.group_name_list_sekonder[index][8],
                               group_list=self.kademe_list_sekonder[index + 10])
            self.kademe_goster(object=self.group_name_list_sekonder[index][9],
                               group_list=self.kademe_list_sekonder[index + 20])
            self.kademe_goster(object=self.group_name_list_sekonder[index][32],
                               group_list=self.kademe_list_sekonder[index + 30])

    def open_telsecim(self, gl, type="tel", index=1):
        self.window2 = Telselectdialog()

        if type == "tel":

            self.window2.setWindowTitle("Tel Seçim Sayfası")
            self.window2.ui.tabWidget.setCurrentIndex(0)
            self.window2.show()
            self.window2.ui.pushButton_sec.clicked.connect(
                lambda x: self.tel_deger_al(gl=gl, object=self.window2, type=type, index=index))
        elif type == "karetel":
            self.window2.setWindowTitle("Kare Tel Seçim Sayfası")
            self.window2.ui.tabWidget.setCurrentIndex(1)
            self.window2.show()
            self.window2.ui.pushButton_sec_2.clicked.connect(
                lambda x: self.tel_deger_al(gl=gl, object=self.window2, type=type, index=index))
        elif type == "folyotel":
            self.window2.setWindowTitle("Folyo Seçim Sayfası")
            self.window2.ui.tabWidget.setCurrentIndex(2)
            self.window2.show()
            self.window2.ui.pushButton_sec_3.clicked.connect(
                lambda x: self.tel_deger_al(gl=gl, object=self.window2, type=type, index=index))
        elif type == "kapton":
            self.window2.setWindowTitle("Kare Tel Seçim Sayfası")
            self.window2.ui.tabWidget.setCurrentIndex(3)
            self.window2.show()
            self.window2.ui.pushButton_sec_4.clicked.connect(
                lambda x: self.tel_deger_al(gl=gl, object=self.window2, type=type, index=index))
        else:
            pass

    def object_multi_connect(self, object, arg):
        if object.metaObject().className() == "QDoubleSpinBox":
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
            return object.textChanged.connect(arg)

    def kademe_temizle(self, gl, kadame_sayisi=1):
        for kademe in range(kadame_sayisi, 10):
            for index in range(0, 58):
                self.degerleri_temizle(gl[kademe][index])

    def degerleri_temizle(self, object):
        if object.metaObject().className() == "QDoubleSpinBox":
            return object.setValue(0)
        elif object.metaObject().className() == "QComboBox":
            return object.setCurrentIndex(0)
        elif object.metaObject().className() == "QLineEdit":
            return True
        elif object.metaObject().className() == "QLabel":
            return True
        elif object.metaObject().className() == "QCheckBox":
            return object.setChecked(False)
        elif object.metaObject().className() == "QPushButton":
            return True
        pass
    def hesap_guncelle(self):
        self.hesap_yap(gl=self.group_name_list_sekonder,
                         gl2=self.group_name_list_sekonder_2,
                         guc=self.guc,
                         frekans=self.frekans,
                         gauss=self.gauss,
                         karkas_en=self.karkas_en,
                         karkas_boy=self.karkas_boy,
                         karkas_yuk=self.karkas_yukseklik,
                         verim=self.karkas_verim,
                         sarim=self.sarim,
                         baglanti="mono",
                         cu_par=self.cu_par,
                         cu_yog=self.cu_yog,
                         al_par=self.al_par,
                         al_yog=self.al_yog,
                         dig_par=self.dig_par,
                         dig_yog=self.dig_yog,

                         kademe=self.kademe)
    def hesap_yap(self, gl,gl2,guc,frekans,gauss,karkas_en,karkas_boy,verim,karkas_yuk,baglanti,sarim,cu_par, cu_yog, al_par, al_yog, dig_par, dig_yog,kademe=1):
        self.veri_kumesi()


        for i in range(0, 10):
            if gl[i][7].value() > 0 and kademe > i:

                if baglanti == "Yıldız":
                    pass

                elif baglanti == "Üçgen":
                    pass
                elif baglanti == "mono":
                    # spir 1 Hesabı -------------------------
                    gl[i][4].setValue(hp.spir_hesap_1(
                        gerilim=gl[i][7].value(),
                        frekans=frekans,
                        gauss=gauss,
                        karkas_en=karkas_en,
                        karkas_boy=karkas_boy,
                        verim=verim))
                    # spir 2 Hesabı -------------------------
                    if gl[i][49].isChecked():
                        pass
                    else:
                        gl[i][6].setValue(hp.spir_hesap_6(
                            gerilim=gl[i][7].value(),
                            frekans=frekans,
                            gauss=gauss,
                            karkas_en=karkas_en,
                            karkas_boy=karkas_boy,
                            verim=verim))

                    # Akım 1 Hesabı -------------------------
                    if i == 0:
                        gl[i][0].setValue(
                            hp.akim_hesap_1(
                                guc=guc,
                                gerilim=gl[i][7].value()) - self.deger)
                    elif i >= 1:
                        gl[i][0].setValue(
                            hp.akim_hesap_1(
                                guc=guc,
                                gerilim=gl[i][7].value()))

                # Kesit 1 Hesabı -------------------------
                gl[i][5].setValue(hp.kesit_hesap_1(
                    akim=gl[i][0].value(),
                    akim_yogunlugu=hp.akim_yogunlugu_1(
                        tel_turu=gl[i][11].currentText(),cu_par=cu_par, cu_yog=cu_yog, al_par=al_par, al_yog=al_yog, dig_par=dig_par, dig_yog=dig_yog)))
                # cap 1 Hesabı -------------------------
                gl[i][2].setValue(hp.cap_hesap_1(
                    kesit=gl[i][5].value()))
                # Kesit 2 Hesabı -------------------------
                gl[i][34].setValue(hp.kesit_hesap_2(
                    cap=gl[i][54].value()) + hp.kesit_hesap_2(
                    cap=gl[i][55].value()) + hp.kesit_hesap_2(
                    cap=gl[i][56].value()) + hp.kesit_hesap_2(
                    cap=gl[i][57].value()) +
                                   (gl[i][12].value() * gl[i][13].value()) +
                                   (gl[i][14].value() * gl[i][15].value()) +
                                   (gl[i][16].value() * gl[i][
                                       17].value()) +
                                   (gl[i][18].value() * gl[i][
                                       19].value()) +
                                   gl[i][20].value() +
                                   gl[i][21].value() +
                                   gl[i][22].value() +
                                   gl[i][23].value() +
                                   (gl[i][24].value() * gl[i][
                                       25].value()) +
                                   (gl[i][26].value() * gl[i][
                                       27].value()) +
                                   (gl[i][28].value() * gl[i][
                                       29].value()) +
                                   (gl[i][30].value() * gl[i][
                                       31].value())
                                   )
                # Akım 2 Hesabı -------------------------
                gl[i][1].setValue(hp.akim_hesap_2(

                    kesit=gl[i][34].value(),
                    akim_yogunlugu=hp.akim_yogunlugu_1(
                        tel_turu=gl[i][11].currentText(),cu_par=cu_par, cu_yog=cu_yog, al_par=al_par, al_yog=al_yog, dig_par=dig_par, dig_yog=dig_yog)))
                # cap 1 Hesabı -------------------------
                gl[i][3].setValue(gl[i][54].value() + gl[i][55].value() + gl[i][56].value() + gl[i][57].value())
                # akım 2 ve kesit 2 kontrol -------------------------
                if gl[i][5].value() <= gl[i][34].value():
                    gl[i][50].setVisible(True)
                    gl[i][51].setVisible(False)
                else:
                    gl[i][50].setVisible(False)
                    gl[i][51].setVisible(True)
                if gl[i][0].value() <= gl[i][1].value():
                    gl[i][52].setVisible(True)
                    gl[i][53].setVisible(False)
                else:
                    gl[i][52].setVisible(False)
                    gl[i][53].setVisible(True)
                # -------------------------
                data = db.showfilter_tel_spir(
                    filter_value=gl[i][54].value(),
                    index=0)
                if gl[i][54].value() == 0:
                    tel_cap = 0
                elif data == [] and gl[i][54].value() > 0:
                    tel_cap = (gl[i][54].value() + gl[i][55].value() + gl[i][56].value() + gl[i][57].value())*1.02
                elif data != [] and gl[i][54].value() > 0:
                    tel_cap = data[0][4]
                    # tel yüksekliği Hesabı -------------------------
                gl[i][36].setValue(hp.tel_yukseklik_hesap_1(
                    tel_cap=tel_cap, karetel_yuk1=gl[i][24].value(),
                    karetel_yuk2=gl[i][26].value(),
                    karetel_yuk3=gl[i][28].value(), karetel_yuk4=gl[i][30].value(),
                    folyo_yuk1=gl[i][20].value(), folyo_yuk2=gl[i][21].value(),
                    folyo_yuk3=gl[i][22].value(), folyo_yuk4=gl[i][23].value(),
                    kapton1=gl[i][12].value(), kapton2=gl[i][14].value(),
                    kapton3=gl[i][16].value(), kapton4=gl[i][18].value()))
                # tel en Hesabı -------------------------
                gl[i][35].setValue(hp.tel_en_hesap_1(
                    tel_cap=tel_cap,
                    karetel_en1=gl[i][25].value(),
                    karetel_en2=gl[i][22].value(),
                    karetel_en3=gl[i][29].value(), karetel_en4=gl[i][31].value(),
                    folyo_en1=gl[i][20].value(), folyo_en2=gl[i][21].value(),
                    folyo_en3=gl[i][22].value(), folyo_en4=gl[i][23].value(),
                    kapton1=gl[i][13].value(), kapton2=gl[i][15].value(),
                    kapton3=gl[i][17].value(), kapton4=gl[i][19].value()))
                if gl[i][35].value() > 0:
                    # spir kat Hesabı -------------------------
                    gl[i][37].setValue(hp.spir_kat_hesap_1(
                        karkas_yuk=karkas_yuk,
                        tel_en=gl[i][35].value()))
                    #  kat sayısı -------------------------------
                    if i == 0:
                        if gl[i][37].value()!=0:
                            gl[i][38].setValue(hp.kat_sayisi_hesap_1(
                                spir=gl[i][6].value(),
                                spir_kat=gl[i][37].value()))
                        else :
                            gl[i][38].setValue(0)
                    elif i > 0:
                        gl[i][38].setValue(hp.kat_sayisi_hesap_2(
                            tel_spir_n=gl[i][6].value(),
                            tel_spri_n_1=gl[i - 1][6].value(),
                            kat_bosluk_n_1=gl[i - 1][39].value(),
                            tel_en=gl[i][35].value(),
                            spir_kat=gl[i][37].value()
                        ))
                    # sarım yuksekliği  -------------------------
                    gl[i][42].setValue(hp.sarim_yüksekligi_hesap_1(
                        tel_yuk=gl[i][36].value(),
                        kat_sayisi=gl[i][38].value()))

                    # son kat
                    if i == 0:
                        if math.fmod(gl[i][6].value(), gl[i][37].value()) == 0:
                            gl[i][43].setValue(gl[i][37].value())
                        else:
                            gl[i][43].setValue(hp.son_kat_hesap_1(
                                spir_2=gl[i][6].value(),
                                spir_kat=gl[i][37].value()))

                    elif i > 0:
                        if gl[i][38].value() == 0:
                            gl[i][43].setValue(hp.son_kat_hesap_2(
                                spir_2=gl[i][6].value(),
                                spir_2_n_1=gl[i - 1][6].value()))
                        else:
                            gl[i][43].setValue(hp.son_kat_hesap_3(
                                spir_2=gl[i][6].value(),
                                spir_2_n_1=gl[i - 1][6].value(),
                                kat_bosluk_n_1=gl[i - 1][39].value(),
                                tel_en=gl[i][35].value(),
                                spir_kat=gl[i][37].value()))

                    # kattaki bosluk ---------------------------
                    if i == 0:
                        gl[i][39].setValue(hp.kattaki_bosluk_hesap_1(
                            karkas_yuk=karkas_yuk,
                            tel_en=gl[i][35].value(),
                            son_kat=gl[i][43].value()
                        ))

                    elif i > 0:
                        if gl[i][38].value() == 0:
                            gl[i][39].setValue(hp.kattaki_bosluk_hesap_2(

                                kat_bosluk_n_1=gl[i - 1][39].value(),
                                tel_en=gl[i][35].value(),
                                spir_2=gl[i][6].value(),
                                spir_2_n_1=gl[i - 1][6].value()
                            ))
                        else:
                            gl[i][39].setValue(hp.kattaki_bosluk_hesap_3(
                                karkas_yuk=karkas_yuk,
                                spir_2=gl[i][6].value(),
                                spir_2_n_1=gl[i - 1][6].value(),
                                kat_bosluk_n_1=gl[i - 1][39].value(),
                                tel_en=gl[i][35].value(),
                                spir_kat=gl[i][37].value()

                            ))

                    else:
                        pass

                    # tel uzunluk  ---------------------------
                    a0 = 2 * (karkas_en + karkas_boy) + 8 * 0.05 * karkas_en
                    a1 = a0 + 4 * gl[1][36].value()
                    a2 = a0 + 4 * gl[2][36].value() + 8 * gl[0][36].value() * gl[0][38].value()
                    a3 = a0 + 4 * gl[3][36].value() + 8 * gl[0][36].value() * gl[0][38].value() + 8 * gl[1][
                        36].value() * gl[1][38].value()
                    a4 = a0 + 4 * gl[4][36].value() + 8 * gl[0][36].value() * gl[0][38].value() + 8 * gl[1][
                        36].value() * gl[1][38].value() + 8 * gl[2][36].value() * gl[2][38].value()
                    a5 = a0 + 4 * gl[5][36].value() + 8 * gl[0][36].value() * gl[0][38].value() + 8 * gl[1][
                        36].value() * gl[1][38].value() + 8 * gl[2][36].value() * gl[2][38].value() + 8 * gl[3][
                             36].value() * gl[3][38].value()
                    a6 = a0 + 4 * gl[6][36].value() + 8 * gl[0][36].value() * gl[0][38].value() + 8 * gl[1][
                        36].value() * gl[1][38].value() + 8 * gl[2][36].value() * gl[2][38].value() + 8 * gl[3][
                             36].value() * gl[3][38].value() + 8 * gl[4][36].value() * gl[4][38].value()
                    a7 = a0 + 4 * gl[7][36].value() + 8 * gl[0][36].value() * gl[0][38].value() + 8 * gl[1][
                        36].value() * gl[1][38].value() + 8 * gl[2][36].value() * gl[2][38].value() + 8 * gl[3][
                             36].value() * gl[3][38].value() + 8 * gl[4][36].value() * gl[4][38].value() + 8 * \
                         gl[5][36].value() * gl[5][38].value()
                    a8 = a0 + 4 * gl[8][36].value() + 8 * gl[0][36].value() * gl[0][38].value() + 8 * gl[1][
                        36].value() * gl[1][38].value() + 8 * gl[2][36].value() * gl[2][38].value() + 8 * gl[3][
                             36].value() * gl[3][38].value() + 8 * gl[4][36].value() * gl[4][38].value() + 8 * \
                         gl[5][36].value() * gl[5][38].value() + 8 * gl[6][36].value() * gl[6][38].value()
                    a9 = a0 + 4 * gl[9][36].value() + 8 * gl[0][36].value() * gl[0][38].value() + 8 * gl[1][
                        36].value() * gl[1][38].value() + 8 * gl[2][36].value() * gl[2][38].value() + 8 * gl[3][
                             36].value() * gl[3][38].value() + 8 * gl[4][36].value() * gl[4][38].value() + 8 * \
                         gl[5][36].value() * gl[5][38].value() + 8 * gl[6][36].value() * gl[6][38].value() + 8 * \
                         gl[7][36].value() * gl[7][38].value()
                    all_a = [0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
                    if i == 0:
                        gl[i][40].setValue(
                            ((gl[i][38].value() - 1) * ((2 * (karkas_en + karkas_boy)) +
                                                        8 * karkas_en * 0.05 + 4 * gl[i][36].value()) + \
                             (8 * gl[i][36].value() * (gl[i][38].value() - 1) * (
                                     gl[i][38].value() - 2) / 2)) / 1000 * gl[i][37].value() + \
                            ((2 * (karkas_en + karkas_boy)) + \
                             8 * karkas_en * 0.05 + 4 * gl[i][36].value() + \
                             (8 * gl[i][36].value() * (gl[i][38].value() - 1))) / 1000 * gl[i][43].value())
                    elif i > 0:
                        if gl[i][38].value() == 0:
                            gl[i][40].setValue(
                                (all_a[i] + 8 * (gl[i - 1][38].value() - 1) * gl[i - 1][36].value()) * gl[i][
                                    43].value() / 1000)
                        elif gl[i][38].value() == 1:
                            gl[i][40].setValue(
                                (all_a[i] + 8 * (gl[i - 1][38].value() - 1) * gl[i - 1][36].value()) *
                                math.floor(gl[i - 1][39].value() / gl[i][35].value()) / 1000 + (
                                        all_a[i] + 8 * (gl[i - 1][38].value())
                                        * gl[i - 1][36].value()) * gl[i][43].value() / 1000)

                        else:
                            gl[i][40].setValue(
                                (all_a[i] + 8 * (gl[i - 1][38].value() - 1) * gl[i - 1][36].value())
                                * math.floor(gl[i - 1][39].value() / gl[i][35].value()) / 1000 +
                                ((gl[i][38].value() - 1) * (
                                        all_a[i] + 8 * (gl[i - 1][38].value()) * gl[i - 1][36].value()) +
                                 4 * (gl[i][38].value() - 1) * (gl[i][38].value() - 2) * gl[i][36].value()) * gl[i][
                                    37].value() / 1000
                                + (all_a[i] + 8 * (gl[i - 1][38].value()) * gl[i - 1][36].value() + 8 * (
                                        gl[i][38].value() - 1) *
                                   gl[i][36].value()) * gl[i][43].value() / 1000
                            )

                    if sarim == "sekonder":

                        sek_a1 = a0 + 8 * self.primer_sarim_yukseklik_toplam + 8 * self.primer_izolasyon + 4 * \
                                 gl[1][36].value()
                        sek_a2 = a0 + 8 * self.primer_sarim_yukseklik_toplam + 4 * gl[2][36].value() + 8 * gl[0][
                            36].value() * gl[0][38].value()
                        sek_a3 = a0 + 8 * self.primer_sarim_yukseklik_toplam + 4 * gl[3][36].value() + 8 * gl[0][
                            36].value() * gl[0][38].value() + 8 * gl[1][
                                     36].value() * gl[1][38].value()
                        sek_a4 = a0 + 8 * self.primer_sarim_yukseklik_toplam + 4 * gl[4][36].value() + 8 * gl[0][
                            36].value() * gl[0][38].value() + 8 * gl[1][
                                     36].value() * gl[1][38].value() + 8 * gl[2][36].value() * gl[2][38].value()
                        sek_a5 = a0 + 8 * self.primer_sarim_yukseklik_toplam + 4 * gl[5][36].value() + 8 * gl[0][
                            36].value() * gl[0][38].value() + 8 * gl[1][
                                     36].value() * gl[1][38].value() + 8 * gl[2][36].value() * gl[2][
                                     38].value() + 8 * gl[3][
                                     36].value() * gl[3][38].value()
                        sek_a6 = a0 + 8 * self.primer_sarim_yukseklik_toplam + 4 * gl[6][36].value() + 8 * gl[0][
                            36].value() * gl[0][38].value() + 8 * gl[1][
                                     36].value() * gl[1][38].value() + 8 * gl[2][36].value() * gl[2][
                                     38].value() + 8 * gl[3][
                                     36].value() * gl[3][38].value() + 8 * gl[4][36].value() * gl[4][38].value()
                        sek_a7 = a0 + 8 * self.primer_sarim_yukseklik_toplam + 4 * gl[7][36].value() + 8 * gl[0][
                            36].value() * gl[0][38].value() + 8 * gl[1][
                                     36].value() * gl[1][38].value() + 8 * gl[2][36].value() * gl[2][
                                     38].value() + 8 * gl[3][
                                     36].value() * gl[3][38].value() + 8 * gl[4][36].value() * gl[4][
                                     38].value() + 8 * \
                                 gl[5][36].value() * gl[5][38].value()
                        sek_a8 = a0 + 8 * self.primer_sarim_yukseklik_toplam + 4 * gl[8][36].value() + 8 * gl[0][
                            36].value() * gl[0][38].value() + 8 * gl[1][
                                     36].value() * gl[1][38].value() + 8 * gl[2][36].value() * gl[2][
                                     38].value() + 8 * gl[3][
                                     36].value() * gl[3][38].value() + 8 * gl[4][36].value() * gl[4][
                                     38].value() + 8 * \
                                 gl[5][36].value() * gl[5][38].value() + 8 * gl[6][36].value() * gl[6][38].value()
                        sek_a9 = a0 + 8 * self.primer_sarim_yukseklik_toplam + 4 * gl[9][36].value() + 8 * gl[0][
                            36].value() * gl[0][38].value() + 8 * gl[1][
                                     36].value() * gl[1][38].value() + 8 * gl[2][36].value() * gl[2][
                                     38].value() + 8 * gl[3][
                                     36].value() * gl[3][38].value() + 8 * gl[4][36].value() * gl[4][
                                     38].value() + 8 * \
                                 gl[5][36].value() * gl[5][38].value() + 8 * gl[6][36].value() * gl[6][
                                     38].value() + 8 * \
                                 gl[7][36].value() * gl[7][38].value()

                        all_sek_a = [0, sek_a1, sek_a2, sek_a3, sek_a4, sek_a5, sek_a6, sek_a7, sek_a8, sek_a9]
                        if i == 0:
                            gl[i][40].setValue(
                                (
                                        (gl[i][38].value() - 1) * (
                                        a0 + 8 * self.primer_sarim_yukseklik_toplam + 8 * self.primer_izolasyon + 4 *
                                        gl[i][36].value())
                                        + 8 * gl[i][36].value() * (gl[i][38].value() - 1) * (
                                                gl[i][38].value() - 2) / 2
                                )
                                / 1000 * gl[i][37].value() + (
                                        a0 + 8 * self.primer_sarim_yukseklik_toplam + 8 * self.primer_izolasyon + 4 *
                                        gl[i][36].value() + 8 * gl[i][36].value() *
                                        (gl[i][38].value() - 1)) / 1000 * gl[i][43].value()
                            )
                        elif i > 0:
                            if gl[i][38].value() == 0:
                                gl[i][40].setValue(
                                    (all_sek_a[i] + 8 * (gl[i - 1][38].value() - 1) * gl[i - 1][36].value()) *
                                    gl[i][
                                        43].value() / 1000)
                            elif gl[i][38].value() == 1:
                                gl[i][40].setValue(
                                    (all_sek_a[i] + 8 * (gl[i - 1][38].value() - 1) * gl[i - 1][36].value()) *
                                    math.floor(gl[i - 1][39].value() / gl[i][35].value()) / 1000 + (
                                            all_sek_a[i] + 8 * (gl[i - 1][38].value())
                                            * gl[i - 1][36].value()) * gl[i][43].value() / 1000)

                            else:
                                gl[i][40].setValue(
                                    (all_sek_a[i] + 8 * (gl[i - 1][38].value() - 1) * gl[i - 1][36].value())
                                    * math.floor(gl[i - 1][39].value() / gl[i][35].value()) / 1000 +
                                    ((gl[i][38].value() - 1) * (
                                            all_sek_a[i] + 8 * (gl[i - 1][38].value()) * gl[i - 1][36].value()) +
                                     4 * (gl[i][38].value() - 1) * (gl[i][38].value() - 2) * gl[i][36].value()) *
                                    gl[i][
                                        37].value() / 1000
                                    + (all_sek_a[i] + 8 * (gl[i - 1][38].value()) * gl[i - 1][36].value() + 8 * (
                                            gl[i][38].value() - 1) *
                                       gl[i][36].value()) * gl[i][43].value() / 1000)
                    # tel agirlik  ---------------------------
                    if gl[i][40].value() != 0:
                        gl[i][41].setValue(
                            hp.tel_agirlik_hesap_1(tel_uzunluk=gl[i][40].value(), kesit_2=gl[i][34].value(),
                                                   tel_yogunluk=hp.tel_yogunlugu_1(
                                                       tel_turu=gl[i][11].currentText())))

                    else:
                        gl[i][41].setValue(0)


            else:
                gl[i][0].setValue(0)
                gl[i][5].setValue(0)
                gl[i][2].setValue(0)
                gl[i][4].setValue(0)
                gl[i][3].setValue(0)
                gl[i][1].setValue(0)
                gl[i][6].setValue(0)
                gl[i][12].setValue(0)
                gl[i][13].setValue(0)
                gl[i][14].setValue(0)
                gl[i][15].setValue(0)
                gl[i][16].setValue(0)
                gl[i][17].setValue(0)
                gl[i][18].setValue(0)
                gl[i][19].setValue(0)
                gl[i][20].setValue(0)
                gl[i][21].setValue(0)
                gl[i][22].setValue(0)
                gl[i][23].setValue(0)
                gl[i][24].setValue(0)
                gl[i][25].setValue(0)
                gl[i][26].setValue(0)
                gl[i][27].setValue(0)
                gl[i][28].setValue(0)
                gl[i][29].setValue(0)
                gl[i][30].setValue(0)
                gl[i][31].setValue(0)
                gl[i][34].setValue(0)
                gl[i][35].setValue(0)
                gl[i][36].setValue(0)
                gl[i][37].setValue(0)
                gl[i][38].setValue(0)
                gl[i][39].setValue(0)
                gl[i][40].setValue(0)
                gl[i][41].setValue(0)
                gl[i][42].setValue(0)
                gl[i][43].setValue(0)
                gl[i][8].setCurrentIndex(0)
                gl[i][9].setCurrentIndex(0)
                gl[i][10].setCurrentIndex(0)
                gl[i][11].setCurrentIndex(0)
                gl[i][50].setVisible(False)
                gl[i][51].setVisible(True)
                gl[i][52].setVisible(False)
                gl[i][53].setVisible(True)
                gl[i][54].setValue(0)
                gl[i][55].setValue(0)
                gl[i][56].setValue(0)
                gl[i][57].setValue(0)
                gl[i][32].setCurrentIndex(0)

        self.kademe_temizle(gl=gl, kadame_sayisi=int(kademe))

    def kademe_goster(self, object, group_list):
        if type(object) == int:
            kademe_sayisi = object
        else:
            kademe_sayisi = int(object.currentText())
        self.hide_list(group_list)
        group_list[0].setVisible(True)
        for i in range(kademe_sayisi):
            group_list[i].setVisible(True)

    def tel_deger_al(self, gl, object, type, index=1):
        if type == "tel":
            gl[index][54].setValue(object.ui.doubleSpinBox_tel_cap.value())
            if gl[index][32].currentText() == "2":
                gl[index][56].setValue(0)
                gl[index][55].setValue(object.ui.doubleSpinBox_tel_cap.value())
                gl[index][57].setValue(0)
            elif gl[index][32].currentText() == "3":
                gl[index][56].setValue(object.ui.doubleSpinBox_tel_cap.value())
                gl[index][55].setValue(object.ui.doubleSpinBox_tel_cap.value())
                gl[index][57].setValue(0)
            elif gl[index][32].currentText() == "3":
                gl[index][56].setValue(object.ui.doubleSpinBox_tel_cap.value())
                gl[index][55].setValue(object.ui.doubleSpinBox_tel_cap.value())
                gl[index][57].setValue(object.ui.doubleSpinBox_tel_cap.value())
        elif type == "karetel":
            gl[index][24].setValue(object.ui.doubleSpinBox_tel_cap_3.value())
            gl[index][25].setValue(object.ui.doubleSpinBox_tel_cap_2.value())

            if gl[index][10].currentText() == "2":
                gl[index][26].setValue(object.ui.doubleSpinBox_tel_cap_3.value())
                gl[index][27].setValue(object.ui.doubleSpinBox_tel_cap_2.value())
            elif gl[index][10].currentText() == "3":
                gl[index][26].setValue(object.ui.doubleSpinBox_tel_cap_3.value())
                gl[index][27].setValue(object.ui.doubleSpinBox_tel_cap_2.value())
                gl[index][28].setValue(object.ui.doubleSpinBox_tel_cap_3.value())
                gl[index][29].setValue(object.ui.doubleSpinBox_tel_cap_2.value())
            elif gl[index][10].currentText() == "4":
                gl[index][26].setValue(object.ui.doubleSpinBox_tel_cap_3.value())
                gl[index][27].setValue(object.ui.doubleSpinBox_tel_cap_2.value())
                gl[index][28].setValue(object.ui.doubleSpinBox_tel_cap_3.value())
                gl[index][29].setValue(object.ui.doubleSpinBox_tel_cap_2.value())
                gl[index][30].setValue(object.ui.doubleSpinBox_tel_cap_3.value())
                gl[index][31].setValue(object.ui.doubleSpinBox_tel_cap_2.value())
        elif type == "folyotel":
            gl[index][12].setValue(object.ui.doubleSpinBox_tel_cap_5.value())
            gl[index][13].setValue(object.ui.doubleSpinBox_tel_cap_4.value())
            if gl[index][8].currentText() == "2":
                gl[index][14].setValue(object.ui.doubleSpinBox_tel_cap_5.value())
                gl[index][15].setValue(object.ui.doubleSpinBox_tel_cap_4.value())
            elif gl[index][8].currentText() == "3":
                gl[index][14].setValue(object.ui.doubleSpinBox_tel_cap_5.value())
                gl[index][15].setValue(object.ui.doubleSpinBox_tel_cap_4.value())
                gl[index][16].setValue(object.ui.doubleSpinBox_tel_cap_5.value())
                gl[index][17].setValue(object.ui.doubleSpinBox_tel_cap_4.value())
            elif gl[index][8].currentText() == "4":
                gl[index][14].setValue(object.ui.doubleSpinBox_tel_cap_5.value())
                gl[index][15].setValue(object.ui.doubleSpinBox_tel_cap_4.value())
                gl[index][16].setValue(object.ui.doubleSpinBox_tel_cap_5.value())
                gl[index][17].setValue(object.ui.doubleSpinBox_tel_cap_4.value())
                gl[index][18].setValue(object.ui.doubleSpinBox_tel_cap_5.value())
                gl[index][19].setValue(object.ui.doubleSpinBox_tel_cap_4.value())
        elif type == "kapton":
            gl[index][20].setValue(object.ui.doubleSpinBox_tel_cap_6.value())
            if gl[index][9].currentText() == "2":
                gl[index][21].setValue(object.ui.doubleSpinBox_tel_cap_6.value())
            elif gl[index][9].currentText() == "3":
                gl[index][21].setValue(object.ui.doubleSpinBox_tel_cap_6.value())
                gl[index][22].setValue(object.ui.doubleSpinBox_tel_cap_6.value())
            elif gl[index][9].currentText() == "4":
                gl[index][21].setValue(object.ui.doubleSpinBox_tel_cap_6.value())
                gl[index][22].setValue(object.ui.doubleSpinBox_tel_cap_6.value())
                gl[index][23].setValue(object.ui.doubleSpinBox_tel_cap_6.value())
        else:
            pass
class Telselectdialog(QDialog):
    def __init__(self, parent=None):
        super(Telselectdialog, self).__init__(parent)
        self.ui = Telselect_dialog()
        self.ui.setupUi(self)
        self.handle_button()
        # self.db=db_sql.mydb()
        data = db.showall_teller()
        table_update(data, headers_teller, self.ui.tableWidget)
        data = db.showall_karetel()
        table_update(data, headers_kare_tel, self.ui.tableWidget_2)
        data = db.showall_folyotel()
        table_update(data, headers_folyotel_tel, self.ui.tableWidget_3)
        data = db.showall_kapton()
        table_update(data, headers_kapton, self.ui.tableWidget_4)

    def handle_button(self):
        self.ui.pushButton_ara.clicked.connect(self.filter_telsecim_table)
        self.ui.pushButton_sec.clicked.connect(self.telsecim_select)
        self.ui.tableWidget.itemClicked.connect(self.callback_from_telsecim_table)

        self.ui.pushButton_ara_2.clicked.connect(self.filter_karetelsecim_table)
        self.ui.pushButton_sec_2.clicked.connect(self.karetelsecim_select)
        self.ui.tableWidget_2.itemClicked.connect(self.callback_from_karetelsecim_table)

        self.ui.pushButton_ara_3.clicked.connect(self.filter_folyotelsecim_table)
        self.ui.pushButton_sec_3.clicked.connect(self.folyotelsecim_select)
        self.ui.tableWidget_3.itemClicked.connect(self.callback_from_folyotelsecim_table)

        self.ui.pushButton_ara_4.clicked.connect(self.filter_kaptonsecim_table)
        self.ui.pushButton_sec_4.clicked.connect(self.kaptonsecim_select)
        self.ui.tableWidget_4.itemClicked.connect(self.callback_from_kaptonsecim_table)

    def filter_telsecim_table(self):
        self.ui.lineEdit_3.text()
        self.ui.comboBox.currentIndex()

        data = db.showfilter_teller(index=self.ui.comboBox.currentIndex(), filter_value=self.ui.lineEdit_3.text())

        table_update(data, headers_teller, self.ui.tableWidget)
        pass

    def callback_from_telsecim_table(self):
        self.teller_ID = int(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 0).text())

        data = db.calldata_with_id_teller(self.teller_ID)
        if data != None:
            self.ui.lineEdit_ID.setText(str(data[0]))
            self.ui.lineEdit_tel_name.setText(str(data[1]))
            self.ui.doubleSpinBox_tel_cap.setValue(data[2])
            self.ui.lineEdit_tel_ozellik.setText(str(data[3]))
            return True
        else:
            return False
        pass

    def telsecim_select(self):

        self.close()
        return self.ui.doubleSpinBox_tel_cap.value()

    def filter_karetelsecim_table(self):
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
            self.ui.lineEdit_folyotel_ozellik_1.setText(str(data[5]))
            return True
        else:
            return False
        pass

    def folyotelsecim_select(self):

        self.close()
        return self.ui.doubleSpinBox_tel_cap_4.value(), self.ui.doubleSpinBox_tel_cap_5.value()

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

            self.ui.lineEdit_tel_ozellik_4.setText(str(data[3]))
            return True
        else:
            return False
        pass

    def kaptonsecim_select(self):

        self.close()
        return self.ui.doubleSpinBox_tel_cap_6.value()

        pass