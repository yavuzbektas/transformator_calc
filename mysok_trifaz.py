# ====================== Şok Trifaz Trafo =========================
import  math
from QT_file.mainsok_trifaz import Ui_MainWindow
import db_sql,myConfig,printout
from PySide2.QtWidgets import QMainWindow,QMessageBox, QTableWidgetItem
import hesaplamalar  as hp
import popups as popup
import veri_tipi as vt
import json
from collections import Counter
import logging,logging.handlers

# ======================  Şok Trifaz Trafo =========================
# ======================  Veri TAbanı Bağlantısı =========================
db=db_sql.mydb() # veri tabanı bağlantısı
# ===============================================
class SokTrifazwindow(QMainWindow):
    def __init__(self,parent=None):
        super(SokTrifazwindow, self).__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.veri_kumeleri()
        self.setWindowTitle("Şok TriFaz Trafosu - Trafo Hesaplama")
        self.handle_button()
        self.index=0

        self.degerler_sifirlama()
        
        self.karkas_hesaplama()
        self.izolasyon_hesapla()
        self.bosluk_hesapla()
    def veri_kumeleri(self):
        
        
        self.group_list_primer_kademe_1 = vt.kademe.copy()
        
        self.group_name_list_primer_kademe = [self.group_list_primer_kademe_1, ]
        self.kademe_list_1 = [self.ui.groupBox_5,]
        
        self.button_list_1 = [self.ui.pushButton_h1_p_buton_1,]

        self.group_list_primer_11 = [self.ui.doubleSpinBox_v_p1,self.ui.doubleSpinBox_h1_p_sipir_1,
                                     self.ui.doubleSpinBox_h1_p_kesit_1,self.ui.doubleSpinBox_h1_p_cap_1,
                                     self.ui.doubleSpinBox_h1_p_akim_1,self.ui.doubleSpinBox_h1_p_sipir_21,
                                     self.ui.doubleSpinBox_h1_p_kesit_21,self.ui.doubleSpinBox_h1_p_cap_21,
                                     self.ui.doubleSpinBox_h1_p_akim_21,self.ui.comboBox_tel_p1,
                                     self.ui.label_kesit_ok_1,self.ui.label_kesit_error_1]
        
        self.group_name_list_2 = [self.group_list_primer_11,]
        
        
        self.toplam_izolasyon=0
    def logout_myapp(self):
        import Trafo_app
        self.window = Trafo_app.Login()

        if self.close():
            self.window.show()
    def hide_list(self,list_name):
        for i in list_name:
            i.setVisible(False)
    def handle_button(self):
        self.ui.pushButton.clicked.connect(self.hesaplama_ekrani)
        self.ui.pushButton_35.clicked.connect(self.logout_myapp)
        self.ui.actionHakk_mda.triggered.connect(self.open_about)
        self.ui.pushButton_5.clicked.connect(self.open_recete)
        self.ui.pushButton_6.clicked.connect(self.open_karkas)
        self.ui.pushButton_4.clicked.connect(self.open_genel_parametre)
        self.ui.pushButton_8.clicked.connect(self.open_izolasyon)
        self.ui.pushButton_7.clicked.connect(self.printout_report)
        self.ui.pushButton_13.clicked.connect(self.tum_degerleri_temizle)
        self.ui.pushButton_klemens.clicked.connect(self.open_klemens)
        self.ui.pushButton_klemens_2.clicked.connect(self.open_klemens)
        self.ui.pushButton_ayak.clicked.connect(self.open_ayak)

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
        self.ui.doubleSpinBox_Lg_man.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_sacYogunluk.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_Kf.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_Ku.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_Um.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_58.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_59.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_62.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_63.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_64.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_65.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_58.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_primer_izo_deg.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_primer_izo_tur.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_ekran_izo_deg.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_ekstra_izo_deg.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_Lg_man.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_c.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_Kf.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_Ku.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_Um.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.pushButton_2.clicked.connect(lambda x: self.ekran_degistir(index=self.old_index))
        self.ui.doubleSpinBox_akim_t.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_enduktans_2.valueChanged.connect(self.hesaplamalari_guncelle)
        
        # Menu Butonları 
        self.ui.actionTeller.triggered.connect(lambda x: self.ekran_degistir(index=4))
        # diğer trafo hesapları
        self.ui.actionHakk_mda.triggered.connect(self.open_about)
        self.ui.actionTri_Faz.triggered.connect(lambda x: self.open_other_trafo(1))
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
        self.ui.actionMonoUI.triggered.connect(lambda x: self.open_other_trafo(10))
        # ======= signals ===========================
        self.primer_object_signals()
        
        
        self.karkas_object_signals()
        self.izolasyon_object_signals()
    def hesaplamalari_guncelle(self):
        
        self.hesap_1_gnl(gl=self.group_name_list_primer_kademe,
                    gl2=self.group_name_list_2,
                    guc=self.ui.doubleSpinBox_guc.value(),
                    frekans=self.ui.doubleSpinBox_frekans.value() ,
                    gauss=self.ui.doubleSpinBox_gauss.value(),
                    karkas_en=self.ui.doubleSpinBox_karkas_en.value(),
                    karkas_boy=self.ui.doubleSpinBox_karkas_boy.value(),
                    karkas_yuk=self.ui.doubleSpinBox_karkas_yukseklik.value(),
                    verim=self.ui.doubleSpinBox_karkas_verim.value(),
                    sarim="primer",
                    baglanti="",
                    kademe=1)

        self.izolasyon_hesapla()
        self.bosluk_hesapla()
        
        self.malzeme_listesi_yap()
        self.klemens_icon_update()
    def closeEvent(self, event):
        # do stuff
        returnValue = popup.warning_msjbox(
            text="Tüm veriler kaybolabilir. Kaydetmeniz Önerilir.\nYine de Kapatmak için 'Devam Et' tuşuna basın",
            title="DİKKAT - Veriler Kaybolacak")

        if returnValue == QMessageBox.Cancel:
            event.ignore()
            return False
        elif returnValue == QMessageBox.Ok:
            event.accept()
            return True
    # ======= Diyolog pencerelerin acilisi ===========================
    def tum_degerleri_temizle(self):
        returnValue = popup.clear_msjbox(
            text="Tüm veri girisleri temizlenecektir..\nDevam Etmek için Temizle tuşuna basın",
            title="DİKKAT - Veriler silinecektir")

        if returnValue == QMessageBox.Cancel:
            return False
        self.degerler_sifirlama()
    def degerler_sifirlama(self):
    
        
        
        self.ui.doubleSpinBox_guc.setValue(500)
        self.ui.doubleSpinBox_karkas_en.setValue(100)
        self.ui.doubleSpinBox_karkas_boy.setValue(120)
        self.ui.doubleSpinBox_karkas_yukseklik.setValue(72)
        self.ui.doubleSpinBox_karkas_verim.setValue(100)
        self.ui.lineEdit_mlz_karkas.setText("H0201001200TD")
        
        self.ui.doubleSpinBox_sac.setValue(0.5)
        self.ui.doubleSpinBox_frekans.setValue(50)
        self.ui.doubleSpinBox_gauss.setValue(11500)
        self.ui.doubleSpinBox_c.setValue(7)
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
        self.ui.lineEdit_ayak_adi.setText("")
        self.ui.doubleSpinBox_ayak_a_deg.setValue(0)
        self.ui.doubleSpinBox_ayak_b_deg.setValue(0)
        self.ui.doubleSpinBox_Lg_man.setValue(0)
        self.ui.doubleSpinBox_akim_t.setValue(0)
        self.ui.doubleSpinBox_enduktans_2.setValue(0)
        self.veri_kumeleri()
        self.hesaplamalari_guncelle()    
    # ======================  popups =========================
    def open_about(self):
        self.window3 = popup.Aboutwindow()

        self.window3.setWindowTitle("Hakkımda Sayfası")
        self.window3.show()
    def open_recete(self):
        self.window3 = popup.Reciepedialog()
        self.recete_veri_kumesi(self.window3)
        self.window3.setWindowTitle("Recete Sayfası - Şok Trifaz  Trafoları ")

        self.window3.read_data_from_mainwindow()
        self.window3.show()
        self.window3.filter_recete_table()
        #self.window3.read_data_app_write_field(self.window3.data)
        self.window3.ui.pushButton_sec.clicked.connect(lambda x:self.recete_deger_al(self.window3))
    def open_karkas(self):
        self.window3 = popup.Karkasdialog()

        self.window3.setWindowTitle("Karkas Seçim Sayfası")
        self.window3.show()
        self.window3.ui.pushButton_sec.clicked.connect(lambda x:self.karkas_deger_al(object=self.window3))
    def open_klemens(self):
        self.window3 = popup.Klemensdialog()
        self.window3.setWindowTitle("Klemens Seçim Sayfası")
        self.window3.ui.tabWidget.setCurrentIndex(0)
        self.window3.show()
        
        def klemens_data_tarnsfer():
            if self.window3.ui.lineEdit_klemens_name.text()!="":
                self.klemens_deger_al(klemens_name=self.window3.ui.lineEdit_klemens_name.text(),a=self.window3.ui.doubleSpinBox_klemens_a.value(),b=self.window3.ui.doubleSpinBox_klemens_b.value(),akim=self.window3.ui.doubleSpinBox_klemens_akim.value() )
            
            if self.window3.ui.lineEdit_ayak_name.text()!="":
                self.ayak_deger_al(ayak_name=self.window3.ui.lineEdit_ayak_name.text(),a=self.window3.ui.doubleSpinBox_ayak_a.value())
        
        self.window3.ui.pushButton_sec.clicked.connect(klemens_data_tarnsfer)
    def open_ayak(self):
        self.window3 = popup.Klemensdialog()
        
        self.window3.setWindowTitle("Klemens Seçim Sayfası")
        self.window3.ui.tabWidget.setCurrentIndex(1)
        self.window3.show()
        def klemens_data_tarnsfer():
            if self.window3.ui.lineEdit_klemens_name.text()!="":
                self.klemens_deger_al(klemens_name=self.window3.ui.lineEdit_klemens_name.text(),a=self.window3.ui.doubleSpinBox_klemens_a.value(),b=self.window3.ui.doubleSpinBox_klemens_b.value(),akim=self.window3.ui.doubleSpinBox_klemens_akim.value() )
            
            if self.window3.ui.lineEdit_ayak_name.text()!="":
                self.ayak_deger_al(ayak_name=self.window3.ui.lineEdit_ayak_name.text(),a=self.window3.ui.doubleSpinBox_ayak_a.value())
        
        self.window3.ui.pushButton_sec.clicked.connect(klemens_data_tarnsfer)
    def open_genel_parametre(self):
        self.window3 = popup.GenelParamdialog()

        self.window3.setWindowTitle("Genel Parametreler Sayfası")
        self.window3.show()
        self.window3.ui.pushButton_sec.clicked.connect(lambda x:self.genel_parametrelere_deger_al(object=self.window3))
        self.window3.ui.doubleSpinBox_sac.setValue(self.ui.doubleSpinBox_sac.value())
        self.window3.ui.doubleSpinBox_gauss.setValue(self.ui.doubleSpinBox_gauss.value())
        self.window3.ui.doubleSpinBox_frekans.setValue(self.ui.doubleSpinBox_frekans.value())
        self.window3.ui.doubleSpinBox_c.setValue(self.ui.doubleSpinBox_c.value())
    def open_kesit_hesaplama(self):
        self.window3 = popup.KesitParamdialog()
        sender = self.sender()
        baglanti_turu= sender.objectName().split("_")[2]
        index=0
        self.window3.trafoTipi="trifaz_sok"
        
        if baglanti_turu=="p":
            
            self.window3.guc = self.ui.doubleSpinBox_guc.value()
            self.window3.max_kademe=1
            self.window3.kademe = 1
            self.window3.kademe_button_show(self.window3.max_kademe)
            self.window3.load_allkademe_values(gl=self.group_name_list_primer_kademe)
            self.window3.load_selected_kademe(self.window3.kademe-1)

            self.window3.sarim = "primer"
            self.window3.ui.pushButton_kaydet.clicked.connect(lambda x: self.kesit_parametrelerini_al(window=self.window3,
                                                        gl_popup=self.window3.group_name_list_kademe,
                                                        gl_main=self.group_name_list_primer_kademe, kademe=int(
                        self.window3.ui.doubleSpinBox_kademe_no.value())))

        elif baglanti_turu=="sek":
            pass
            
        # if self.window3.guc==0:
        #     popup.error_msjbox(title='Hesap Hatası', text='Lütfen Önce gücü giriniz.')
        #     return False
        # else:
        #     pass
        self.window3.setWindowTitle("Kesit Parametreleri Sayfası")

        self.window3.karkas_yukseklik=self.ui.doubleSpinBox_karkas_yukseklik.value()
        self.window3.frekans=self.ui.doubleSpinBox_frekans.value()
        self.window3.karkas_en=self.ui.doubleSpinBox_karkas_en.value()
        self.window3.karkas_boy=self.ui.doubleSpinBox_karkas_boy.value()
        self.window3.c=self.ui.doubleSpinBox_c.value()
        self.window3.karkas_verim=self.ui.doubleSpinBox_karkas_verim.value()
        self.window3.gauss=self.ui.doubleSpinBox_gauss.value()
        self.window3.cu_yog = self.ui.doubleSpinBox_59.value()
        self.window3.al_yog = self.ui.doubleSpinBox_63.value()
        self.window3.di_yog = self.ui.doubleSpinBox_65.value()   
        self.window3.cu_par=self.ui.doubleSpinBox_58.value()
        self.window3.al_par=self.ui.doubleSpinBox_62.value()
        self.window3.dig_par=self.ui.doubleSpinBox_64.value() 
        self.window3.primer_sarim_yukseklik_toplam = self.primer_sarim_yukseklik_toplam
        self.window3.Kf =self.ui.doubleSpinBox_Kf.value()
        self.window3.Ku=self.ui.doubleSpinBox_Ku.value()
        self.window3.Um =self.ui.doubleSpinBox_Um.value()  
        
        self.window3.klemens_a=self.ui.doubleSpinBox_klemens_a_deg.value()
        self.window3.klemens_b=self.ui.doubleSpinBox_klemens_b_deg.value()
        self.window3.ayak_a=self.ui.doubleSpinBox_ayak_a_deg.value()
        self.window3.akim_m=self.ui.doubleSpinBox_akim_t.value()
        self.window3.enduktans_m=self.ui.doubleSpinBox_enduktans_2.value()
        self.window3.Lg_man = self.ui.doubleSpinBox_Lg_man.value()
        self.window3.show()

        self.window3.ui.pushButton_kaydet_2.clicked.connect(self.window3.close)
    def kesit_parametrelerini_al(self, window, gl_popup, gl_main,kademe):

        if gl_popup[kademe]["kesit_error"]==True or gl_popup[kademe]["akim_error"]==True:
            returnValue = popup.warning_msjbox(title='Kesit Değerleri Hatası', text='Kesit değerleri önerilen değerlerin altındadır. Devam etmek için butona basın.')
        else:
            returnValue = QMessageBox.Ok
        if returnValue == QMessageBox.Cancel:
            return False
        elif returnValue == QMessageBox.Ok:
            self.ui.doubleSpinBox_gauss.setValue(window.ui.doubleSpinBox_gauss.value())
            for i in range(0, len(gl_main)):

                for key in vt.kademe.keys():
                    gl_main[i][key] = gl_popup[i][key]

            window.close()
        self.hesaplamalari_guncelle()
    def open_izolasyon(self):
        self.window3 = popup.Izolasyondialog()

        self.window3.setWindowTitle("Izolasyon Parametreleri Sayfası")
        self.window3.ui.doubleSpinBox_2.setVisible(False)
        self.window3.ui.doubleSpinBox_7.setVisible(False)
        self.window3.ui.doubleSpinBox_3.setVisible(False)
        self.window3.ui.doubleSpinBox_8.setVisible(False)
        self.window3.ui.label_2.setVisible(False)
        self.window3.ui.label_3.setVisible(False)
        self.window3.ui.label_7.setVisible(False)
        #self.window3.ui.label_8.setVisible(False)
        
        self.window3.show()
        self.window3.ui.pushButton_sec.clicked.connect(lambda  x:self.izolasyon_verileri_guncelle(object=self.window3))
        self.izolasyon_deger_al(object=self.window3)
    def open_other_trafo(self,trafo_index):
        if trafo_index == 0:
            import myApp
            self.window = myApp.MyWindow()

            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            if self.close():
            
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0)
        elif trafo_index == 1:

            import myizole_trifaz
            self.window = myizole_trifaz.MyWindow()

            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            if self.close():
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0)
        elif trafo_index == 2:
            import mysont_monofaz
            self.window = mysont_monofaz.SontMonofazwindow()
            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            if self.close():
            
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0)
        elif trafo_index == 3:
            import mysont_trifaz
            self.window = mysont_trifaz.SontTrifazwindow()
            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            if self.close():
            
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0)
        elif trafo_index == 4:
            import mysok_monofaz
            self.window = mysok_monofaz.SokMonofazwindow()

            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            if self.close():
            
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0)
        elif trafo_index == 5:
            import mysok_trifaz
            self.window = mysok_trifaz.SokTrifazwindow()

            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            if self.close():
            
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0)
        elif trafo_index == 6:
            import myoto_monofaz
            self.window = myoto_monofaz.OtoMonofazwindow()

            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            if self.close():
            
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0)
        elif trafo_index == 7:
            import myoto_trifaz
            self.window = myoto_trifaz.OtoTrifazwindow()

            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            if self.close():
            
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0)
        elif trafo_index == 8:
            import myharmonik
            self.window = myharmonik.Harmonikwindow()

            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            if self.close():
            
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0)
        elif trafo_index == 9:
            import myups
            self.window = myups.UPSwindow()
            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            if self.close():
            
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0)
        elif trafo_index == 10:
            import mymonoUI
            self.window = mymonoUI.MonoUIwindow()
            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            if self.close():
            
                self.window.show()
                self.window.ui.stackedWidget.setCurrentIndex(0)
    # ========== RECETE ==========================
    def recete_veri_kumesi(self,veri_kumesi):
        veri_kumesi.rec_veriler["kullanici"] = self.ui.lineEdit_user.text()
        veri_kumesi.rec_veriler["primer_group_list"] = self.group_name_list_primer_kademe
        veri_kumesi.rec_veriler["guc"] = self.ui.doubleSpinBox_guc.value()
        veri_kumesi.rec_veriler["trafo_tipi" ]= " Şok Trafosu Trifaz "
        veri_kumesi.rec_veriler[ "gauss" ]= self.ui.doubleSpinBox_gauss.value()
        veri_kumesi.rec_veriler[ "sac" ]= self.ui.doubleSpinBox_sac.value()
        veri_kumesi.rec_veriler[ "c_sac" ]= self.ui.doubleSpinBox_c.value()
        veri_kumesi.rec_veriler[ "frekans" ]= self.ui.doubleSpinBox_frekans.value()
        veri_kumesi.rec_veriler["karkas" ]["adi"] =self.ui.lineEdit_mlz_karkas.text()
        veri_kumesi.rec_veriler["karkas"]["en"] =self.ui.doubleSpinBox_karkas_en.value()
        veri_kumesi.rec_veriler["karkas"]["boy"] =self.ui.doubleSpinBox_karkas_boy.value()
        veri_kumesi.rec_veriler["karkas"]["yukseklik"] =self.ui.doubleSpinBox_karkas_yukseklik.value()
        veri_kumesi.rec_veriler["karkas"]["verim"] =self.ui.doubleSpinBox_karkas_verim.value()
        veri_kumesi.rec_veriler["klemens" ]["adi"]= self.ui.lineEdit_klemens_adi.text()
        veri_kumesi.rec_veriler["klemens"] ["en"]= self.ui.doubleSpinBox_klemens_a_deg.value()
        veri_kumesi.rec_veriler["klemens"]["boy"] =self.ui.doubleSpinBox_klemens_b_deg.value()
        veri_kumesi.rec_veriler["klemens"]["akim"] = self.ui.doubleSpinBox_klemens_akim.value()
        veri_kumesi.rec_veriler["klemens"]["yukseklik"] =0
        veri_kumesi.rec_veriler["ayak"]["adi"]= self.ui.lineEdit_ayak_adi.text()
        veri_kumesi.rec_veriler["ayak"]["en"]= self.ui.doubleSpinBox_ayak_a_deg.value()
        veri_kumesi.rec_veriler["ayak"]["boy"] = self.ui.doubleSpinBox_ayak_b_deg.value()
        veri_kumesi.rec_veriler["ayak"]["yukseklik"]= 0
        veri_kumesi.rec_veriler["nuve_bosluk"] = self.ui.doubleSpinBox_nuvebosluk.value()
        veri_kumesi.rec_veriler["primer_izo_deg" ]= self.ui.doubleSpinBox_primer_izo_deg.value()    
        veri_kumesi.rec_veriler["ekran_izo_deg" ]= self.ui.doubleSpinBox_ekran_izo_deg.value()
        veri_kumesi.rec_veriler["ekstra_izo_deg" ]= self.ui.doubleSpinBox_ekstra_izo_deg.value()
        veri_kumesi.rec_veriler["primer_izo_tur" ]= self.ui.doubleSpinBox_primer_izo_tur.value()     
        veri_kumesi.rec_veriler["ekran_sec" ]= self.ui.checkBox_ekran_sec.isChecked()
        veri_kumesi.rec_veriler["ekstra" ]= self.ui.checkBox_ekstra.isChecked()
        veri_kumesi.rec_veriler["sac_tipi"] =self.ui.comboBox_sactipi.currentText()
        veri_kumesi.rec_veriler["alAkimYog"] =self.ui.doubleSpinBox_62.value()
        veri_kumesi.rec_veriler["alYogunluk"] =self.ui.doubleSpinBox_63.value()
        veri_kumesi.rec_veriler["cuAkimYog"] =self.ui.doubleSpinBox_58.value()
        veri_kumesi.rec_veriler["cuYogunluk"] =self.ui.doubleSpinBox_59.value()
        veri_kumesi.rec_veriler["diAkimYog"] =self.ui.doubleSpinBox_64.value()
        veri_kumesi.rec_veriler["diYogunluk"] =self.ui.doubleSpinBox_65.value()
        veri_kumesi.rec_veriler["sacYogunluk"] =self.ui.doubleSpinBox_sacYogunluk.value()
        veri_kumesi.rec_veriler["Lg_man"] =self.ui.doubleSpinBox_Lg_man.value()
        veri_kumesi.rec_veriler["Kf"] =self.ui.doubleSpinBox_Kf.value() 
        veri_kumesi.rec_veriler["Ku"] =self.ui.doubleSpinBox_Ku.value() 
        veri_kumesi.rec_veriler["Um"] =self.ui.doubleSpinBox_Um.value()
        veri_kumesi.rec_veriler["akim_t"] =self.ui.doubleSpinBox_akim_t.value()
        veri_kumesi.rec_veriler["enduktans_2"] =self.ui.doubleSpinBox_enduktans_2.value()
    def recete_deger_al(self,window):
        data = db.calldata_with_id_recete(window.ui.doubleSpinBox_ID.value())
        if data == None:
            return False
        self.degerler_sifirlama()
        self.rec_veriler = json.loads(data[9])

        
        self.ui.doubleSpinBox_guc.setValue(self.rec_veriler["guc"])
        self.ui.doubleSpinBox_karkas_en.setValue(self.rec_veriler["karkas"]["en"])
        self.ui.doubleSpinBox_karkas_boy.setValue(float(self.rec_veriler["karkas"]["boy"]))
        self.ui.doubleSpinBox_karkas_yukseklik.setValue(float(self.rec_veriler["karkas"]["yukseklik"]))
        self.ui.doubleSpinBox_karkas_verim.setValue(float(self.rec_veriler["karkas"]["verim"]))
        self.ui.lineEdit_mlz_karkas.setText(self.rec_veriler["karkas"]["adi"])
        self.ui.comboBox_sactipi.setCurrentText(self.rec_veriler["sac_tipi"])
        self.ui.doubleSpinBox_sac.setValue(self.rec_veriler["sac"])
        self.ui.doubleSpinBox_frekans.setValue(self.rec_veriler["frekans"])
        self.ui.doubleSpinBox_gauss.setValue(self.rec_veriler["gauss"])
        self.ui.doubleSpinBox_c.setValue(self.rec_veriler["c_sac"])
        self.ui.doubleSpinBox_nuvebosluk.setValue(self.rec_veriler["nuve_bosluk"])
        self.ui.doubleSpinBox_primer_izo_deg.setValue(self.rec_veriler["primer_izo_deg"])
        self.ui.doubleSpinBox_primer_izo_tur.setValue(self.rec_veriler["primer_izo_tur"])  
        self.ui.checkBox_ekran_sec.setChecked(bool(self.rec_veriler["ekran_sec"]))
        self.ui.doubleSpinBox_ekran_izo_deg.setValue(self.rec_veriler["ekran_izo_deg"])
        self.ui.checkBox_ekstra.setChecked(bool(self.rec_veriler["ekstra"]))
        self.ui.doubleSpinBox_ekstra_izo_deg.setValue(self.rec_veriler["ekstra_izo_deg"])
        self.ui.lineEdit_klemens_adi.setText(self.rec_veriler["klemens"]["adi"])
        self.ui.doubleSpinBox_klemens_a_deg.setValue(self.rec_veriler["klemens"]["en"])
        self.ui.doubleSpinBox_klemens_b_deg.setValue(self.rec_veriler["klemens"]["boy"])
        self.ui.doubleSpinBox_klemens_akim.setValue(self.rec_veriler["klemens"]["akim"])
        self.ui.lineEdit_ayak_adi.setText(self.rec_veriler["ayak"]["adi"])
        self.ui.doubleSpinBox_ayak_a_deg.setValue(self.rec_veriler["ayak"]["en"])
        self.ui.doubleSpinBox_ayak_b_deg.setValue(self.rec_veriler["ayak"]["boy"])
        self.ui.doubleSpinBox_62.setValue(self.rec_veriler["alAkimYog"])
        self.ui.doubleSpinBox_63.setValue(self.rec_veriler["alYogunluk"])
        self.ui.doubleSpinBox_58.setValue(self.rec_veriler["cuAkimYog"])
        self.ui.doubleSpinBox_59.setValue(self.rec_veriler["cuYogunluk"])
        self.ui.doubleSpinBox_64.setValue(self.rec_veriler["diAkimYog"])
        self.ui.doubleSpinBox_65.setValue(self.rec_veriler["diYogunluk"])
        self.ui.doubleSpinBox_sacYogunluk.setValue(self.rec_veriler["sacYogunluk"])
        self.ui.doubleSpinBox_Lg_man.setValue(self.rec_veriler["Lg_man"])
        self.ui.doubleSpinBox_Kf.setValue(self.rec_veriler["Kf"]) 
        self.ui.doubleSpinBox_Ku.setValue(self.rec_veriler["Ku"]) 
        self.ui.doubleSpinBox_Um.setValue(self.rec_veriler["Um"])
        self.ui.doubleSpinBox_akim_t.setValue(self.rec_veriler["akim_t"])
        self.ui.doubleSpinBox_enduktans_2.setValue(self.rec_veriler["enduktans_2"])
        self.group_name_list_primer_kademe[0]=self.rec_veriler["primer_group_list"][0]
            
        self.hesaplamalari_guncelle()
        
        # ======================  guc =========================
    # ========== genel parametreler ==========================
    def genel_parametrelere_deger_al(self,object):
        #global guc, frekans, sac, gauss, c_val
        self.ui.doubleSpinBox_sac.setValue(object.ui.doubleSpinBox_sac.value())
        self.ui.doubleSpinBox_gauss.setValue(object.ui.doubleSpinBox_gauss.value())
        self.ui.doubleSpinBox_frekans.setValue(object.ui.doubleSpinBox_frekans.value())
        self.ui.doubleSpinBox_c.setValue(object.ui.doubleSpinBox_c.value())
        self.ui.doubleSpinBox_gauss2.setValue(object.ui.doubleSpinBox_gauss2.value())
        self.ui.doubleSpinBox_c2.setValue(object.ui.doubleSpinBox_c2.value())
     # ================= karkas =====================================
    def karkas_deger_al(self,object):
        global karkas_en,karkas_boy
        karkas_en=object.ui.doubleSpinBox_karkas_en.value()
        karkas_boy = object.ui.doubleSpinBox_karkas_boy.value()
        self.ui.doubleSpinBox_karkas_en.setValue(object.ui.doubleSpinBox_karkas_en.value())
        self.ui.doubleSpinBox_karkas_boy.setValue(object.ui.doubleSpinBox_karkas_boy.value())
        self.ui.lineEdit_mlz_karkas.setText(object.ui.lineEdit_karkas_name.text())
        self.karkas_hesaplama()
    def karkas_hesaplama(self):
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
    #  Primer Hesabı    ===============
    def tel_deger_al(self, gl,object,type,index=1):
        if type == "tel":
            gl[index][54].setValue(object.ui.doubleSpinBox_tel_cap.value())
        elif type == "karetel":
            gl[index][24].setValue(object.ui.doubleSpinBox_tel_cap_3.value())
            gl[index][25].setValue(object.ui.doubleSpinBox_tel_cap_2.value())
            
            if  gl[index][10].currentText()=="2":
                 gl[index][26].setValue(object.ui.doubleSpinBox_tel_cap_3.value())
                 gl[index][27].setValue(object.ui.doubleSpinBox_tel_cap_2.value())
            elif  gl[index][10].currentText()=="3":
                 gl[index][26].setValue(object.ui.doubleSpinBox_tel_cap_3.value())
                 gl[index][27].setValue(object.ui.doubleSpinBox_tel_cap_2.value())
                 gl[index][28].setValue(object.ui.doubleSpinBox_tel_cap_3.value())
                 gl[index][29].setValue(object.ui.doubleSpinBox_tel_cap_2.value())
            elif  gl[index][10].currentText() == "4":
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
    def primer_object_signals(self):
        #self.ui.comboBox.currentTextChanged.connect(self.primer_kademe_goster)

        for i in range(0,len(self.button_list_1)):
            self.button_list_1[i].clicked.connect(self.open_kesit_hesaplama)
    # ======================  İzolasyon Hesabı =========================    
    def izolasyon_verileri_guncelle(self,object):
        self.ui.doubleSpinBox_primer_izo_deg.setValue(object.ui.doubleSpinBox.value())
        self.ui.doubleSpinBox_ekran_izo_deg.setValue(object.ui.doubleSpinBox_4.value())
        self.ui.doubleSpinBox_ekstra_izo_deg.setValue(object.ui.doubleSpinBox_5.value())
        self.ui.doubleSpinBox_primer_izo_tur.setValue(object.ui.doubleSpinBox_6.value())   
        self.ui.checkBox_ekran_sec.setChecked(object.ui.checkBox.isChecked())
        self.ui.checkBox_ekstra.setChecked(object.ui.checkBox_2.isChecked())
    def izolasyon_deger_al(self,object):
        object.ui.doubleSpinBox.setValue(self.ui.doubleSpinBox_primer_izo_deg.value())
        object.ui.doubleSpinBox_4.setValue(self.ui.doubleSpinBox_ekran_izo_deg.value())
        object.ui.doubleSpinBox_5.setValue(self.ui.doubleSpinBox_ekstra_izo_deg.value())
        object.ui.doubleSpinBox_6.setValue(self.ui.doubleSpinBox_primer_izo_tur.value())  
        object.ui.checkBox.setChecked(self.ui.checkBox_ekran_sec.isChecked())
        object.ui.checkBox_2.setChecked(self.ui.checkBox_ekstra.isChecked())
    def izolasyon_hesapla(self):
        self.primer_izolasyon= hp.primer_izolasyon_hesap(
            izo_deg=self.ui.doubleSpinBox_primer_izo_deg.value(),
            tur=self.ui.doubleSpinBox_primer_izo_tur.value(),
            kademe=1)
        
        self.toplam_izolasyon = self.primer_izolasyon+self.ui.doubleSpinBox_ekran_izo_deg.value() + \
                                self.ui.doubleSpinBox_ekstra_izo_deg.value() 
        
        return self.toplam_izolasyon
    def izolasyon_object_signals(self):
        self.ui.doubleSpinBox_primer_izo_deg.valueChanged.connect(self.hesaplamalari_guncelle)
        
        self.ui.doubleSpinBox_ekran_izo_deg.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_ekstra_izo_deg.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_primer_izo_tur.valueChanged.connect(self.hesaplamalari_guncelle)
        
        self.ui.checkBox_ekran_sec.stateChanged.connect(self.hesaplamalari_guncelle)
        self.ui.checkBox_ekstra.stateChanged.connect(self.hesaplamalari_guncelle)   
    # ======================  bosluk hesabı =========================  
    def bosluk_hesapla(self):
        self.izolasyon_hesapla()
        if self.ui.comboBox_sactipi.currentIndex()==0 :
            self.ui.doubleSpinBox_nuvebosluk.setEnabled(False)
        elif self.ui.comboBox_sactipi.currentIndex()==0 :
            self.ui.doubleSpinBox_nuvebosluk.setEnabled(False)
        
        elif self.ui.comboBox_sactipi.currentIndex()==1 :
            self.ui.doubleSpinBox_nuvebosluk.setEnabled(True)
        else:
            bosluk=0
        #self.ui.doubleSpinBox_8.setValue(bosluk)
        bosluk = self.ui.doubleSpinBox_8.value()
        if bosluk>0 :
            self.ui.comboBox_2.setCurrentIndex(0)
            self.ui.label_Ac_error_2.setVisible(False)
            self.ui.label_Ac_ok_2.setVisible(True)
        elif bosluk<0 :
            self.ui.comboBox_2.setCurrentIndex(1)
            self.ui.label_Ac_error_2.setVisible(True)
            self.ui.label_Ac_ok_2.setVisible(False)
        
        else:
            self.ui.label_Ac_error_2.setVisible(False)
            self.ui.label_Ac_ok_2.setVisible(False)
        
        if self.ui.doubleSpinBox_Ap.value()>self.ui.doubleSpinBox_apSacaGore.value():
            self.ui.comboBox_degerlendirme.setCurrentIndex(0)
            self.ui.comboBox_degerlendirme.setStyleSheet(" background-color:Red ; color:Yellow ")
        else:
            self.ui.comboBox_degerlendirme.setCurrentIndex(1)
            self.ui.comboBox_degerlendirme.setStyleSheet(" background-color:Green ; color:White ")
    # ======================  agırlık  hesabı ========================= 
    def agirlik_hesapla(self):
        gl=self.group_name_list_primer_kademe
        primer_al_agirlik=0
        primer_cu_agirlik=0
        for i in range (0,len(gl)):
            if gl[i]["teltipi"]=="Al":
                primer_al_agirlik +=gl[i]["tel_agirlik"]*3
            elif gl[i]["teltipi"]=="Cu":
                primer_cu_agirlik += gl[i]["tel_agirlik"]
        
        
        # Hesaplanan degerler ekrana yazdırılıyor ---------------------------------------
        self.ui.doubleSpinBox_toplamagirlik_al.setValue(primer_al_agirlik)
        self.ui.doubleSpinBox_toplamagirlik_cu.setValue(primer_cu_agirlik)
        self.ui.doubleSpinBox_primeragirlik_al.setValue(primer_al_agirlik)
        self.ui.doubleSpinBox_primeragirlik_cu.setValue(primer_cu_agirlik)
    # ======================  klemens ve Ayak Degerli  =========================
    def klemens_icon_update(self):
        if self.ui.lineEdit_klemens_adi.text()!="":
            self.ui.label_klemens_error.setVisible(False)
            #self.ui.lineEdit_klemens.setText(self.ui.lineEdit_klemens_adi.text() + " / "+ str(int(self.ui.doubleSpinBox_klemens_a_deg.value())) + " / " + str(int(self.ui.doubleSpinBox_klemens_b_deg.value())))

        else:
            self.ui.label_klemens_error.setVisible(True)
            #self.ui.lineEdit_klemens.setText("")
        if self.ui.lineEdit_ayak_adi.text()!="":
            self.ui.label_ayak_error.setVisible(False)
            #self.ui.lineEdit_ayak.setText(self.ui.lineEdit_ayak_adi.text() +  " / "+str(int(self.ui.doubleSpinBox_ayak_a_deg.value())))
            
        else:
            self.ui.label_ayak_error.setVisible(True)
            #self.ui.lineEdit_ayak.setText("")
    def klemens_deger_al(self,klemens_name,a,b,akim):
        self.ui.lineEdit_klemens_adi.setText(klemens_name)
        self.ui.doubleSpinBox_klemens_a_deg.setValue(a)
        self.ui.doubleSpinBox_klemens_b_deg.setValue(b)
        self.ui.doubleSpinBox_klemens_akim.setValue(akim)
    def ayak_deger_al(self,ayak_name,a):
        self.ui.lineEdit_ayak_adi.setText(ayak_name)
        self.ui.doubleSpinBox_ayak_a_deg.setValue(a)    
    # ======================  Genel Fonksiyonlar =========================
    def hesap_sarim_uzunlugu(self):
        self.primer_sarim_yukseklik_toplam =0.0
           
        for i in range(0,len(self.group_name_list_primer_kademe)):
            self.primer_sarim_yukseklik_toplam =self.primer_sarim_yukseklik_toplam + self.group_name_list_primer_kademe[i]["sarim_yukseklik"]
    def hesap_1_gnl(self,gl,gl2,guc,frekans,gauss,karkas_en,karkas_boy,karkas_yuk,verim,sarim,baglanti,kademe=1):
        self.hesap_sarim_uzunlugu()
        self.izolasyon_hesapla()
        self.voltaj_check(gl=gl)
        degerler={}
        degerler=hp.trafo_hesap_trifaz_sok(gl, guc, frekans,
                        gauss, karkas_en, karkas_boy,
                        karkas_yuk, verim, sarim,
                        primer_sarim_yukseklik_toplam=self.primer_sarim_yukseklik_toplam,
                        cu_par= self.ui.doubleSpinBox_58.value(),
                        cu_yog=self.ui.doubleSpinBox_59.value(),
                        al_par=self.ui.doubleSpinBox_62.value() ,
                        al_yog=self.ui.doubleSpinBox_63.value(),
                        dig_par=self.ui.doubleSpinBox_64.value(),
                        dig_yog=self.ui.doubleSpinBox_65.value(),
                        Lg_man=self.ui.doubleSpinBox_Lg_man.value(), 
                        c=self.ui.doubleSpinBox_c.value(), 
                        Kf=self.ui.doubleSpinBox_Kf.value(), 
                        Ku=self.ui.doubleSpinBox_Ku.value(), 
                        Um=self.ui.doubleSpinBox_Um.value(),
                        klemens_a=self.ui.doubleSpinBox_klemens_a_deg.value(),
                        klemens_b=self.ui.doubleSpinBox_klemens_b_deg.value(),
                        ayak_a=self.ui.doubleSpinBox_ayak_a_deg.value(),
                        akim_m=self.ui.doubleSpinBox_akim_t.value(),
                        enduktans_m=self.ui.doubleSpinBox_enduktans_2.value())

        self.karkas_hesaplama()
        self.bosluk_hesapla()
        self.agirlik_hesapla()
        
        
        # Baslangıcta degerler sıfırlanır -------------------------
        
        if len(degerler)>1:
            self.ui.doubleSpinBox_apSacaGore.setValue(degerler["ApSac"])
            #self.ui.doubleSpinBox_akim_t.setValue(degerler["akim_t"])
            self.ui.doubleSpinBox_enduktans.setValue(degerler["enduktans"])
            self.ui.doubleSpinBox_Sp1.setValue(degerler["sp1"])
            self.ui.doubleSpinBox_Lg_oto.setValue(degerler["Lg_oto"])
            self.ui.doubleSpinBox_f_oto.setValue(degerler["f_oto"])
            self.ui.doubleSpinBox_Sp_oto.setValue(degerler["sp1_oto"])
            self.ui.doubleSpinBox_Lg_mpl.setValue(degerler["Lg_mpl"])
            self.ui.doubleSpinBox_f_mpl.setValue(degerler["f_mpl"])
            self.ui.doubleSpinBox_Sp_mpl.setValue(degerler["sp1_mpl"])
            self.ui.doubleSpinBox_f_man.setValue(degerler["f_man"])
            self.ui.doubleSpinBox_Sp_man.setValue(degerler["sp1_man"])
            self.ui.doubleSpinBox_Ap.setValue(degerler["Ap"])
            self.ui.doubleSpinBox_mpl.setValue(degerler["mpl"])
            self.ui.doubleSpinBox_olcu_a.setValue(degerler["nuveOlcu_a"])
            self.ui.doubleSpinBox_olcu_b.setValue(degerler["nuveOlcu_b"])
            self.ui.doubleSpinBox_olcu_c.setValue(degerler["nuveOlcu_c"])
            self.ui.doubleSpinBox_sacagirlik.setValue(degerler["sac_agirlik"])
            self.ui.doubleSpinBox_karkas_cm_oto.setValue(degerler["karkas_man"])
            self.ui.doubleSpinBox_karkas_cm.setValue(degerler["karkas_oto"])
            self.ui.doubleSpinBox_8.setValue(degerler["bosluk"])
            self.ui.doubleSpinBox_karkas_yuk_oto.setValue(degerler["karkas_yuk_oto"])
            self.ui.doubleSpinBox_guc.setValue(degerler["guc_m"])
            self.ui.doubleSpinBox_volt_m.setValue(degerler["volt_m"])
        gl2[0][0].setValue(gl[0]["voltaj"])
        gl2[0][1].setValue(gl[0]["spir1"])
        gl2[0][2].setValue(gl[0]["kesit1"])
        gl2[0][3].setValue(gl[0]["cap1"])
        gl2[0][4].setValue(gl[0]["akim1"])
        gl2[0][5].setValue(gl[0]["spir2"])
        gl2[0][6].setValue(gl[0]["kesit2"])
        gl2[0][7].setValue(gl[0]["cap2"])
        gl2[0][8].setValue(gl[0]["akim2"])
        gl2[0][9].setCurrentText(gl[0]["teltipi"])
        if gl2[0][0].value() > 0:
            gl2[0][11].setVisible(False)
            gl2[0][10].setVisible(True)
        else:
                gl2[0][11].setVisible(True)
                gl2[0][10].setVisible(False)
        if gl[0]["check_spir_man"] ==True:
            self.ui.doubleSpinBox_Lg_man.setEnabled(False)
        else:
            self.ui.doubleSpinBox_Lg_man.setEnabled(True)
    def voltaj_check(self,gl):
        for i in range(0,len(gl)-1):
            if gl[i]["voltaj"]>0 and gl[i]["voltaj"]>gl[i+1]["voltaj"] and gl[i+1]["voltaj"]>0:
                popup.error_msjbox(title='Voltaj Değerleri Hatalı',
                             text=f'Lütfen Küçükten Büyüğe göre Voltaj Giriniz.Girdiğiniz {i} kademeli Voltaj değeri , {i+1} kademeli voltaj değerinden büyük olamaz. ')
                gl[i]["voltaj"]=0
    def ekran_degistir(self,index):
        self.old_index = self.ui.stackedWidget.currentIndex()
        self.ui.stackedWidget.setCurrentIndex(index)
    def kademe_goster(self,object,group_list):
        kademe_sayisi= int(object.currentText())
        self.hide_list(group_list)
        group_list[0].setVisible(True)
        for i in range(kademe_sayisi):
            group_list[i].setVisible(True)
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
        pass
    
    def hesaplama_ekrani(self):

        self.index = self.ui.stackedWidget.currentIndex()
        if self.index==0 :
            self.ekran_degistir(index=1)

            


        elif self.index==1 :  pass
        elif self.index==2 :
            self.ekran_degistir(index=3)

        elif self.index==3 :  pass

        else :
            self.ekran_degistir(index=0) 
    def object_multi_value_set(self,object,object2):
        if type(object)==str:
            return False
        elif object.metaObject().className()== "QDoubleSpinBox":
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
    def object_multi_value_set_clear(self,object):
        if type(object)==str:
            return True
        elif object.metaObject().className()== "QDoubleSpinBox":
            return object.setValue(0)
        elif object.metaObject().className()== "QComboBox":
            return object.setCurrentIndex(0)
        elif object.metaObject().className()== "QLineEdit":
            return object.setText(0)
        elif object.metaObject().className()== "QPushButton":
            return True
        elif object.metaObject().className()== "QCheckBox":
            return object.setChecked(0)
        elif object.metaObject().className()== "QLabel":
            return object.setVisible(0)
    # ======================  Yazdırma Ayarları ve Malzeme Listesinin Çıkartılması  =========================
    def malzeme_listesi_yap(self):
        malzeme_listesix =[]

        for i in range (0,len(self.group_name_list_primer_kademe)):

            for key,val in list(vt.malzeme_listesi["teller"].items()):
                if self.group_name_list_primer_kademe[i][key]!="":
                  malzeme_listesix.append({self.group_name_list_primer_kademe[i][key]:self.group_name_list_primer_kademe[i][val]})

                

        counter = Counter()
        for d in malzeme_listesix:
            counter.update(d)
        
        self.tum_malzeme_listesi = dict(counter)
        self.kesit_listesi=[]
        self.kesit_listesi.clear()
        
        for mlz in self.tum_malzeme_listesi.keys(): 
            cap = db.get_tell_byname( filter_value=mlz)  
            if cap!=None:
                self.kesit_listesi.append(str(cap[0]))
                cap=None
                continue
            
            data = db.get_karetell_byname( filter_value=mlz)
            
            if data != None:
                kesit1,kesit2 = data
                self.kesit_listesi.append(str(kesit1)+"x"+str(kesit2))
                kesit1,kesit2,=None,None
                continue
            data = db.get_folyotell_byname(filter_value=mlz)
            if data != None:
                kesit3,kesit4= data
                self.kesit_listesi.append(str(kesit3) + "x" + str(kesit4))
                kesit3,kesit4=None,None
                continue
            kesit5 = db.get_kapton_byname(filter_value=mlz)
            if  kesit5 != None:
                self.kesit_listesi.append(str( kesit5[0]))
                kesit5=None
                continue
        return self.tum_malzeme_listesi
        #self.group_name_list_sekonder_kademe
        #self.va_group_elementlist
    def printout_veri_kumesi(self):
        printout.primer_group_list =self.group_name_list_primer_kademe
        
        printout.primer_baglanti =""
        printout.guc = self.ui.doubleSpinBox_guc.value()
        printout.trafo_tipi = " Şok Trifaz Trafosu  Hesap Ozeti"

        printout.primer_kademe = 1
        
        printout.guc = str(self.ui.doubleSpinBox_guc.value()) + " VA"
        printout.gauss = str(self.ui.doubleSpinBox_gauss.value())
        printout.sac = str(self.ui.doubleSpinBox_sac.value()) + " mm"
        printout.c_sac = str(self.ui.doubleSpinBox_c.value())
        if self.group_name_list_primer_kademe[0]["voltaj"] != 0.0:
            printout.don_oran = self.group_name_list_primer_kademe[0]["voltaj"] / self.group_name_list_primer_kademe[0][
                "spir2"]
        else:
            printout.don_oran = 1
        printout.frekans = str(self.ui.doubleSpinBox_frekans.value()) + " Hz"
        printout.p_tel_al_ag = str(self.ui.doubleSpinBox_primeragirlik_al.value()) + " kg"
        
        printout.p_tel_cu_ag = str(self.ui.doubleSpinBox_primeragirlik_cu.value()) + " kg"
        
        printout.toplam_ag = str(self.ui.doubleSpinBox_toplamagirlik_al.value())
        printout.toplam_cu = str(self.ui.doubleSpinBox_toplamagirlik_cu.value())
        printout.karkas = str(self.ui.doubleSpinBox_karkas_en.value()) + " x " + str(
            self.ui.doubleSpinBox_karkas_boy.value()) + " x " + str(self.ui.doubleSpinBox_karkas_yukseklik.value())
        printout.trafo_olcu = (str(self.ui.doubleSpinBox_trafoolcu_a.value()) + " x " + 
            str(self.ui.doubleSpinBox_trafoolcu_b.value()) + 
            " x " + str(self.ui.doubleSpinBox_trafoolcu_c.value()) +
            " x " + str(self.ui.doubleSpinBox_trafoolcu_d.value()) +
            " x " + str(self.ui.doubleSpinBox_trafoolcu_e.value()))
        if self.ui.doubleSpinBox_kesmeSacAgirlik.value()>0:
            
            printout.sac_agirlik = str(self.ui.doubleSpinBox_kesmeSacAgirlik.value()) + " kg"
        else:
            printout.sac_agirlik = str(self.ui.doubleSpinBox_sacagirlik.value()) + " kg"
        printout.klemens = self.ui.lineEdit_klemens_adi.text() + " / "+ str(self.ui.doubleSpinBox_klemens_a_deg.value()) + " / "+str(self.ui.doubleSpinBox_klemens_b_deg.value())
        printout.ayak = self.ui.lineEdit_ayak_adi.text()
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
        
        printout.ekran_izo_deg = self.ui.doubleSpinBox_ekran_izo_deg.value()
        printout.ekstra_izo_deg = self.ui.doubleSpinBox_ekstra_izo_deg.value()
        printout.primer_izo_tur = self.ui.doubleSpinBox_primer_izo_tur.value()
        
        printout.ekran_sec = self.ui.checkBox_ekran_sec.isChecked()
        printout.ekstra = self.ui.checkBox_ekstra.isChecked()
        
        
        printout.mlz_listesi=self.tum_malzeme_listesi
        printout.kesit_listesi=self.kesit_listesi
        printout.sac_tipi=self.ui.comboBox_sactipi.currentText()
        printout.karkas_kod=self.ui.lineEdit_mlz_karkas.text()
        
        printout.akim_t=self.ui.doubleSpinBox_akim_t.value()
        printout.enduktans=self.ui.doubleSpinBox_enduktans.value()
        printout.Sp1=self.ui.doubleSpinBox_Sp1.value()
        printout.Lg_oto=self.ui.doubleSpinBox_Lg_oto.value()
        printout.f_oto=self.ui.doubleSpinBox_f_oto.value()
        printout.Sp_oto=self.ui.doubleSpinBox_Sp_oto.value()
        printout.Lg_mpl=self.ui.doubleSpinBox_Lg_mpl.value()
        printout.f_mpl=self.ui.doubleSpinBox_f_mpl.value()
        printout.Sp_mpl=self.ui.doubleSpinBox_Sp_mpl.value()
        printout.Lg_man=self.ui.doubleSpinBox_Lg_man.value()
        printout.f_man=self.ui.doubleSpinBox_f_man.value()
        printout.Sp_man=self.ui.doubleSpinBox_Sp_man.value()
        printout.Ap=self.ui.doubleSpinBox_Ap.value()
        printout.mpl=self.ui.doubleSpinBox_mpl.value()
        printout.karkas_cm_man = self.ui.doubleSpinBox_karkas_cm_oto.value()
        printout.karkas_cm_oto= self.ui.doubleSpinBox_karkas_cm.value()
        printout.bosluk =self.ui.doubleSpinBox_8.value()
        printout.karkas_yuk_oto = self.ui.doubleSpinBox_karkas_yuk_oto.value()
    def printout_report(self):
        self.printout_veri_kumesi()
        printout.trifazSok_printout()

    