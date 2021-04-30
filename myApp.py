import  math
from QT_file.mainwindow import Ui_MainWindow
import db_sql,myConfig,printout
from PySide2.QtWidgets import QMainWindow,QMessageBox, QTableWidgetItem
import hesaplamalar  as hp
import popups as popup
import veri_tipi as vt
import json
from collections import Counter
import logging,logging.handlers


# ======================  Veri TAbanı Bağlantısı =========================
db=db_sql.mydb() # veri tabanı bağlantısı
# ===============================================
class MyWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MyWindow, self).__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.veri_kumeleri()
        self.setWindowTitle("Mono Faz Izolasyon Trafosu - Trafo Hesaplama")
        self.handle_button()
        self.index=0

        self.degerler_sifirlama()
        self.kademeler_calistir()
        self.karkas_hesaplama()
        self.izolasyon_hesapla()
        self.bosluk_hesapla()
    def veri_kumeleri(self):
        

        self.group_list_primer_kademe_1 = vt.kademe.copy()
        self.group_list_primer_kademe_2 = vt.kademe.copy()
        self.group_list_primer_kademe_3 = vt.kademe.copy()
        self.group_list_primer_kademe_4 = vt.kademe.copy()
        self.group_list_primer_kademe_5 = vt.kademe.copy()
        self.group_list_primer_kademe_6 = vt.kademe.copy()
        self.group_list_primer_kademe_7 = vt.kademe.copy()
        self.group_list_primer_kademe_8 = vt.kademe.copy()
        self.group_list_primer_kademe_9 = vt.kademe.copy()
        self.group_list_primer_kademe_10 = vt.kademe.copy()
        self.group_name_list_primer_kademe = [self.group_list_primer_kademe_1, self.group_list_primer_kademe_2,
                                       self.group_list_primer_kademe_3,
                                       self.group_list_primer_kademe_4, self.group_list_primer_kademe_5,
                                       self.group_list_primer_kademe_6, self.group_list_primer_kademe_7,
                                       self.group_list_primer_kademe_8, self.group_list_primer_kademe_9,
                                       self.group_list_primer_kademe_10]

        
        self.kademe_list_1 = [self.ui.groupBox_5,self.ui.groupBox_6,self.ui.groupBox_7,self.ui.groupBox_8,self.ui.groupBox_9,
                         self.ui.groupBox_10,self.ui.groupBox_11,self.ui.groupBox_12,self.ui.groupBox_13,self.ui.groupBox_14]
        self.kademe_list_s1 = [self.ui.groupBox_s1_1, self.ui.groupBox_s1_2, self.ui.groupBox_s1_3,
                              self.ui.groupBox_s1_4,
                              self.ui.groupBox_s1_5, self.ui.groupBox_s1_6, self.ui.groupBox_s1_7,
                              self.ui.groupBox_s1_8,
                              self.ui.groupBox_s1_9, self.ui.groupBox_s1_10]
        self.kademe_list_4 = [self.ui.groupBox_sek1, self.ui.groupBox_sek2, self.ui.groupBox_sek3, self.ui.groupBox_sek4,
                              self.ui.groupBox_sek5, self.ui.groupBox_sek6, self.ui.groupBox_sek7, self.ui.groupBox_sek8,
                              self.ui.groupBox_sek9, self.ui.groupBox_sek10]
        self.kademe_list_s2 = [self.ui.groupBox_s2_1, self.ui.groupBox_s2_2, self.ui.groupBox_s2_3,
                              self.ui.groupBox_s2_4,
                              self.ui.groupBox_s2_5, self.ui.groupBox_s2_6, self.ui.groupBox_s2_7,
                              self.ui.groupBox_s2_8,
                              self.ui.groupBox_s2_9, self.ui.groupBox_s2_10]
        self.kademe_list_s3 = [self.ui.groupBox_s3_1, self.ui.groupBox_s3_2, self.ui.groupBox_s3_3,
                              self.ui.groupBox_s3_4,
                              self.ui.groupBox_s3_5, self.ui.groupBox_s3_6, self.ui.groupBox_s3_7,
                              self.ui.groupBox_s3_8,
                              self.ui.groupBox_s3_9, self.ui.groupBox_s3_10]
        self.kademe_list_s4 = [self.ui.groupBox_s4_1, self.ui.groupBox_s4_2, self.ui.groupBox_s4_3,
                              self.ui.groupBox_s4_4,
                              self.ui.groupBox_s4_5, self.ui.groupBox_s4_6, self.ui.groupBox_s4_7,
                              self.ui.groupBox_s4_8,
                              self.ui.groupBox_s4_9, self.ui.groupBox_s4_10]
        self.kademe_list_s5 = [self.ui.groupBox_s5_1, self.ui.groupBox_s5_2, self.ui.groupBox_s5_3,
                              self.ui.groupBox_s5_4,
                              self.ui.groupBox_s5_5, self.ui.groupBox_s5_6, self.ui.groupBox_s5_7,
                              self.ui.groupBox_s5_8,
                              self.ui.groupBox_s5_9, self.ui.groupBox_s5_10]
        self.kademe_list_s6 = [self.ui.groupBox_s6_1, self.ui.groupBox_s6_2, self.ui.groupBox_s6_3,
                              self.ui.groupBox_s6_4,
                              self.ui.groupBox_s6_5, self.ui.groupBox_s6_6, self.ui.groupBox_s6_7,
                              self.ui.groupBox_s6_8,
                              self.ui.groupBox_s6_9, self.ui.groupBox_s6_10]
        self.kademe_list_s7 = [self.ui.groupBox_s7_1, self.ui.groupBox_s7_2, self.ui.groupBox_s7_3,
                              self.ui.groupBox_s7_4,
                              self.ui.groupBox_s7_5, self.ui.groupBox_s7_6, self.ui.groupBox_s7_7,
                              self.ui.groupBox_s7_8,
                              self.ui.groupBox_s7_9, self.ui.groupBox_s7_10]
        self.kademe_list_s8 = [self.ui.groupBox_s8_1, self.ui.groupBox_s8_2, self.ui.groupBox_s8_3,
                              self.ui.groupBox_s8_4,
                              self.ui.groupBox_s8_5, self.ui.groupBox_s8_6, self.ui.groupBox_s8_7,
                              self.ui.groupBox_s8_8,
                              self.ui.groupBox_s8_9, self.ui.groupBox_s8_10]
        self.kademe_list_s9 = [self.ui.groupBox_s9_1, self.ui.groupBox_s9_2, self.ui.groupBox_s9_3,
                              self.ui.groupBox_s9_4,
                              self.ui.groupBox_s9_5, self.ui.groupBox_s9_6, self.ui.groupBox_s9_7,
                              self.ui.groupBox_s9_8,
                              self.ui.groupBox_s9_9, self.ui.groupBox_s9_10]
        self.kademe_list_s10 = [self.ui.groupBox_s10_1, self.ui.groupBox_s10_2, self.ui.groupBox_s10_3,
                              self.ui.groupBox_s10_4,
                              self.ui.groupBox_s10_5, self.ui.groupBox_s10_6, self.ui.groupBox_s10_7,
                              self.ui.groupBox_s10_8,
                              self.ui.groupBox_s10_9, self.ui.groupBox_s10_10]
        self.va_kademe_elemenlist =[self.kademe_list_s1,self.kademe_list_s2,self.kademe_list_s3,self.kademe_list_s4,
                                    self.kademe_list_s5,self.kademe_list_s6,self.kademe_list_s7,self.kademe_list_s8,
                                    self.kademe_list_s9,self.kademe_list_s10]
        self.button_list_1 = [self.ui.pushButton_h1_p_buton_1, self.ui.pushButton_h1_p_buton_2, self.ui.pushButton_h1_p_buton_3,
                                self.ui.pushButton_h1_p_buton_4, self.ui.pushButton_h1_p_buton_5, self.ui.pushButton_h1_p_buton_6, self.ui.pushButton_h1_p_buton_7,
                                self.ui.pushButton_h1_p_buton_8, self.ui.pushButton_h1_p_buton_9, self.ui.pushButton_h1_p_buton_10]





        self.group_list_primer_11 = [self.ui.doubleSpinBox_v_p1,self.ui.doubleSpinBox_h1_p_sipir_1,
                                     self.ui.doubleSpinBox_h1_p_kesit_1,self.ui.doubleSpinBox_h1_p_cap_1,
                                     self.ui.doubleSpinBox_h1_p_akim_1,self.ui.doubleSpinBox_h1_p_sipir_21,
                                     self.ui.doubleSpinBox_h1_p_kesit_21,self.ui.doubleSpinBox_h1_p_cap_21,
                                     self.ui.doubleSpinBox_h1_p_akim_21,self.ui.comboBox_tel_p1,
                                     self.ui.label_kesit_ok_1,self.ui.label_kesit_error_1]
        self.group_list_primer_12 = [self.ui.doubleSpinBox_v_p2, self.ui.doubleSpinBox_h1_p_sipir_2,
                                     self.ui.doubleSpinBox_h1_p_kesit_2, self.ui.doubleSpinBox_h1_p_cap_2,
                                     self.ui.doubleSpinBox_h1_p_akim_2, self.ui.doubleSpinBox_h1_p_sipir_22,
                                     self.ui.doubleSpinBox_h1_p_kesit_22, self.ui.doubleSpinBox_h1_p_cap_22,
                                     self.ui.doubleSpinBox_h1_p_akim_22,self.ui.comboBox_tel_p2,
                                     self.ui.label_kesit_ok_2,self.ui.label_kesit_error_2]
        self.group_list_primer_13 = [self.ui.doubleSpinBox_v_p3, self.ui.doubleSpinBox_h1_p_sipir_3,
                                     self.ui.doubleSpinBox_h1_p_kesit_3, self.ui.doubleSpinBox_h1_p_cap_3,
                                     self.ui.doubleSpinBox_h1_p_akim_3, self.ui.doubleSpinBox_h1_p_sipir_23,
                                     self.ui.doubleSpinBox_h1_p_kesit_23, self.ui.doubleSpinBox_h1_p_cap_23,
                                     self.ui.doubleSpinBox_h1_p_akim_23,self.ui.comboBox_tel_p3,
                                     self.ui.label_kesit_ok_3,self.ui.label_kesit_error_3]
        self.group_list_primer_14 = [self.ui.doubleSpinBox_v_p4, self.ui.doubleSpinBox_h1_p_sipir_4,
                                     self.ui.doubleSpinBox_h1_p_kesit_4, self.ui.doubleSpinBox_h1_p_cap_4,
                                     self.ui.doubleSpinBox_h1_p_akim_4, self.ui.doubleSpinBox_h1_p_sipir_24,
                                     self.ui.doubleSpinBox_h1_p_kesit_24, self.ui.doubleSpinBox_h1_p_cap_24,
                                     self.ui.doubleSpinBox_h1_p_akim_24,self.ui.comboBox_tel_p4,
                                     self.ui.label_kesit_ok_4,self.ui.label_kesit_error_4]
        self.group_list_primer_15 = [self.ui.doubleSpinBox_v_p5, self.ui.doubleSpinBox_h1_p_sipir_5,
                                     self.ui.doubleSpinBox_h1_p_kesit_5, self.ui.doubleSpinBox_h1_p_cap_5,
                                     self.ui.doubleSpinBox_h1_p_akim_5, self.ui.doubleSpinBox_h1_p_sipir_25,
                                     self.ui.doubleSpinBox_h1_p_kesit_25, self.ui.doubleSpinBox_h1_p_cap_25,
                                     self.ui.doubleSpinBox_h1_p_akim_25,self.ui.comboBox_tel_p5,
                                     self.ui.label_kesit_ok_5,self.ui.label_kesit_error_5]
        self.group_list_primer_16 = [self.ui.doubleSpinBox_v_p6, self.ui.doubleSpinBox_h1_p_sipir_6,
                                     self.ui.doubleSpinBox_h1_p_kesit_6, self.ui.doubleSpinBox_h1_p_cap_6,
                                     self.ui.doubleSpinBox_h1_p_akim_6, self.ui.doubleSpinBox_h1_p_sipir_26,
                                     self.ui.doubleSpinBox_h1_p_kesit_26, self.ui.doubleSpinBox_h1_p_cap_26,
                                     self.ui.doubleSpinBox_h1_p_akim_26,self.ui.comboBox_tel_p6,
                                     self.ui.label_kesit_ok_6,self.ui.label_kesit_error_6]
        self.group_list_primer_17 = [self.ui.doubleSpinBox_v_p7, self.ui.doubleSpinBox_h1_p_sipir_7,
                                     self.ui.doubleSpinBox_h1_p_kesit_7, self.ui.doubleSpinBox_h1_p_cap_7,
                                     self.ui.doubleSpinBox_h1_p_akim_7, self.ui.doubleSpinBox_h1_p_sipir_27,
                                     self.ui.doubleSpinBox_h1_p_kesit_27, self.ui.doubleSpinBox_h1_p_cap_27,
                                     self.ui.doubleSpinBox_h1_p_akim_27,self.ui.comboBox_tel_p7,
                                     self.ui.label_kesit_ok_7,self.ui.label_kesit_error_7]
        self.group_list_primer_18 = [self.ui.doubleSpinBox_v_p8, self.ui.doubleSpinBox_h1_p_sipir_8,
                                     self.ui.doubleSpinBox_h1_p_kesit_8, self.ui.doubleSpinBox_h1_p_cap_8,
                                     self.ui.doubleSpinBox_h1_p_akim_8, self.ui.doubleSpinBox_h1_p_sipir_28,
                                     self.ui.doubleSpinBox_h1_p_kesit_28, self.ui.doubleSpinBox_h1_p_cap_28,
                                     self.ui.doubleSpinBox_h1_p_akim_28,self.ui.comboBox_tel_p8,
                                     self.ui.label_kesit_ok_8,self.ui.label_kesit_error_8]
        self.group_list_primer_19 = [self.ui.doubleSpinBox_v_p9, self.ui.doubleSpinBox_h1_p_sipir_9,
                                     self.ui.doubleSpinBox_h1_p_kesit_9, self.ui.doubleSpinBox_h1_p_cap_9,
                                     self.ui.doubleSpinBox_h1_p_akim_9, self.ui.doubleSpinBox_h1_p_sipir_29,
                                     self.ui.doubleSpinBox_h1_p_kesit_29, self.ui.doubleSpinBox_h1_p_cap_29,
                                     self.ui.doubleSpinBox_h1_p_akim_29,self.ui.comboBox_tel_p9,
                                     self.ui.label_kesit_ok_9,self.ui.label_kesit_error_9]
        self.group_list_primer_20 = [self.ui.doubleSpinBox_v_p10, self.ui.doubleSpinBox_h1_p_sipir_10,
                                     self.ui.doubleSpinBox_h1_p_kesit_10, self.ui.doubleSpinBox_h1_p_cap_10,
                                     self.ui.doubleSpinBox_h1_p_akim_10, self.ui.doubleSpinBox_h1_p_sipir_30,
                                     self.ui.doubleSpinBox_h1_p_kesit_30, self.ui.doubleSpinBox_h1_p_cap_30,
                                     self.ui.doubleSpinBox_h1_p_akim_30,self.ui.comboBox_tel_p10,
                                     self.ui.label_kesit_ok_10,self.ui.label_kesit_error_10]
        self.group_name_list_2 = [self.group_list_primer_11,self.group_list_primer_12,self.group_list_primer_13,
                                  self.group_list_primer_14,self.group_list_primer_15,self.group_list_primer_16,
                                  self.group_list_primer_17,self.group_list_primer_18,self.group_list_primer_19,
                                  self.group_list_primer_20]
        self.sekonder_veri_kumesi()
        self.va_veri_kumesi()
        self.toplam_izolasyon=0
    def logout_myapp(self):
        import Trafo_app
        self.window = Trafo_app.Login()

        self.close()
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
        self.ui.pushButton_2.clicked.connect(lambda x: self.ekran_degistir(index=self.old_index))

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
        # ======= signals ===========================
        self.primer_object_signals()
        self.sekonder_object_signals()
        self.va_object_signals()
        self.karkas_object_signals()
        self.izolasyon_object_signals()
    def kademeler_calistir(self):
        self.primer_kademe_goster()
        self.sekonder_kademe_goster()
        self.va_kademe_goster()
    def hesaplamalari_guncelle(self):
        self.hesap_1_gnl(gl=self.group_name_list_sekonder_kademe,
                    gl2=self.group_name_list_sekonder_2,
                    guc=self.ui.doubleSpinBox_guc.value(),
                    frekans=self.ui.doubleSpinBox_frekans.value() ,
                    gauss=self.ui.doubleSpinBox_gauss.value(),
                    karkas_en=self.ui.doubleSpinBox_karkas_en.value(),
                    karkas_boy=self.ui.doubleSpinBox_karkas_boy.value(),
                    karkas_yuk=self.ui.doubleSpinBox_karkas_yukseklik.value(),
                    verim=self.ui.doubleSpinBox_karkas_verim.value(),
                    sarim="sekonder",
                    kademe=int(self.ui.comboBox_sek.currentText()))
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
                    kademe=int(self.ui.comboBox.currentText()))

        if self.ui.radioButton_vadagilim.isChecked():
            for index in range (1,11):

                self.hesap_1_gnl(gl=getattr(self, ("group_name_list_sva" + str(index) + "_kademe")),
                                 gl2=getattr(self, ("group_name_list_sva" + str(index) + "_2")),
                                 guc=getattr(self.ui, ("doubleSpinBox_sva" + str(index) + "_guc")).value(),
                                 frekans=self.ui.doubleSpinBox_frekans.value(),
                                 gauss=self.ui.doubleSpinBox_gauss.value(),
                                 karkas_en=self.ui.doubleSpinBox_karkas_en.value(),
                                 karkas_boy=self.ui.doubleSpinBox_karkas_boy.value(),
                                 karkas_yuk=self.ui.doubleSpinBox_karkas_yukseklik.value(),
                                 verim=100,
                                 sarim=f"sva{index}",
                                 kademe=int(getattr(self.ui, ("comboBox_sva" + str(index) + "_kad")).currentText()))

            self.va_kademe_guncelle()
            self.va_kalan_guc()
        self.izolasyon_hesapla()
        self.bosluk_hesapla()
        self.olcu_hesapla()
        self.malzeme_listesi_yap()
        self.klemens_icon_update()
    # ======= Diyolog pencerelerin acilisi ===========================
    def tum_degerleri_temizle(self):
        returnValue = popup.clear_msjbox(
            text="Tüm veri girisleri temizlenecektir..\nDevam Etmek için Temizle tuşuna basın",
            title="DİKKAT - Veriler silinecektir")

        if returnValue == QMessageBox.Cancel:
            return False
        self.degerler_sifirlama()
    def degerler_sifirlama(self):
        self.ui.radioButton_kademeli.setChecked(True)
        for i in range(0, 10):
            self.guclist_1[i].setValue(0)
            self.va_kademe_listesi[i].setCurrentText("0")
            self.va_guclist[i].setValue(0)
            for y in range(0,10):
                for z in range(0, 9):
                    self.object_multi_value_set_clear(self.va_altguplar[i][y][z])
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.comboBox_sek.setCurrentIndex(0)
        self.ui.comboBox_va.setCurrentIndex(0)
        self.ui.doubleSpinBox_guc.setValue(500)
        self.ui.doubleSpinBox_karkas_en.setValue(100)
        self.ui.doubleSpinBox_karkas_boy.setValue(120)
        self.ui.doubleSpinBox_karkas_yukseklik.setValue(72)
        self.ui.doubleSpinBox_karkas_verim.setValue(100)
        self.ui.lineEdit_mlz_karkas.setText("H0201001200TD")
        self.ui.comboBox_sactipi.setCurrentIndex(0)
        self.ui.doubleSpinBox_sac.setValue(0.5)
        self.ui.doubleSpinBox_frekans.setValue(50)
        self.ui.doubleSpinBox_gauss.setValue(11500)
        self.ui.doubleSpinBox_c.setValue(7)
        #self.ui.doubleSpinBox_nuvebosluk.setValue(0)
        #self.ui.doubleSpinBox_primer_izo_deg.setValue(0)
        self.ui.doubleSpinBox_primer_izo_tur.setValue(0)
        #self.ui.doubleSpinBox_sekonder_izo_deg.setValue(0)
        self.ui.doubleSpinBox_sekonder_izo_tur.setValue(0)
        #self.ui.doubleSpinBox_pri_sek_izo_deg.setValue(0)
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
        self.ui.radioButton_kademeli.setChecked(True)
        self.ui.comboBox_sva1_kad.setCurrentText("")
        self.ui.comboBox_sva2_kad.setCurrentText("")
        self.ui.comboBox_sva3_kad.setCurrentText("")
        self.ui.comboBox_sva4_kad.setCurrentText("")
        self.ui.comboBox_sva5_kad.setCurrentText("")
        self.ui.comboBox_sva6_kad.setCurrentText("")
        self.ui.comboBox_sva7_kad.setCurrentText("")
        self.ui.comboBox_sva8_kad.setCurrentText("")
        self.ui.comboBox_sva9_kad.setCurrentText("")
        self.ui.comboBox_sva10_kad.setCurrentText("")
        self.veri_kumeleri()
        self.sekonder_veri_kumesi()
        self.va_veri_kumesi()
        self.hesaplamalari_guncelle()

        self.kademeler_calistir()
    # ======================  popups =========================
    def open_about(self):
        self.window3 = popup.Aboutwindow()

        self.window3.setWindowTitle("Hakkımda Sayfası")
        self.window3.show()
    def open_recete(self):
        self.window3 = popup.Reciepedialog()
        self.recete_veri_kumesi(self.window3)
        
        self.window3.setWindowTitle("Recete Sayfası - İzolasyon MonoFaz Trafoları ")

        self.window3.read_data_from_mainwindow()
        self.window3.filter_recete_table()
        self.window3.show()
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
        self.window3.trafoTipi="mono_izole"
        if baglanti_turu=="p":
            self.window3.kademe = int(sender.objectName().split("_")[len(sender.objectName().split("_"))-1])
            self.window3.guc = self.ui.doubleSpinBox_guc.value()
            #self.window3.gn2=[]
            self.window3.max_kademe=int(self.ui.comboBox.currentText())
            self.window3.kademe_button_show(self.window3.max_kademe)
            self.window3.load_allkademe_values(gl=self.group_name_list_primer_kademe)
            self.window3.load_selected_kademe(self.window3.kademe-1)
            self.window3.sarim = "primer"
            self.window3.ui.pushButton_kaydet.clicked.connect(lambda x: self.kesit_parametrelerini_al(window=self.window3,
                                                        gl_popup=self.window3.group_name_list_kademe,
                                                        gl_main=self.group_name_list_primer_kademe, kademe=int(
                        self.window3.ui.doubleSpinBox_kademe_no.value())))

        elif baglanti_turu=="sek":
            self.window3.kademe = int(sender.objectName().split("_")[len(sender.objectName().split("_"))-1])
            self.window3.guc=self.ui.doubleSpinBox_guc.value()

            self.window3.sarim = "sekonder"
            self.window3.max_kademe = int(self.ui.comboBox_sek.currentText())
            self.window3.kademe_button_show(self.window3.max_kademe)
            self.window3.load_allkademe_values(gl=self.group_name_list_sekonder_kademe)
            self.window3.load_selected_kademe(self.window3.kademe - 1)
            
            self.window3.ui.pushButton_kaydet.clicked.connect(
                lambda x: self.kesit_parametrelerini_al(window=self.window3,
                                                        gl_popup=self.window3.group_name_list_kademe,
                                                        gl_main=self.group_name_list_sekonder_kademe, kademe=int(
                        self.window3.ui.doubleSpinBox_kademe_no.value())))
        else:
            self.window3.kademe = int(sender.objectName().split("_")[len(sender.objectName().split("_"))-1])
            if len(sender.objectName().split("_")[-2])==2:
                index = int((sender.objectName().split("_")[2])[-1])
            else:
                index = int((sender.objectName().split("_")[2])[-2]+(sender.objectName().split("_")[2])[-1])
            self.window3.guc= getattr(self.ui,("doubleSpinBox_sva"+str(index)+"_guc")).value()
            #self.window3.gn1=getattr(self,("group_name_list_sva"+str(index)))

            self.window3.sarim = "sva" + str(index)
            self.window3.max_kademe = int(getattr(self.ui,("comboBox_sva"+str(index)+"_kad")).currentText())
            self.window3.kademe_button_show(self.window3.max_kademe)
            self.window3.load_allkademe_values(getattr(self,("group_name_list_sva"+str(index)+"_kademe")))
            self.window3.load_selected_kademe(self.window3.kademe - 1)
            self.window3.ui.pushButton_kaydet.clicked.connect(
                lambda x: self.kesit_parametrelerini_al(window=self.window3,
                                                        gl_popup=self.window3.group_name_list_kademe,
                                                        gl_main=getattr(self,("group_name_list_sva"+str(index)+"_kademe")), kademe=int(
                        self.window3.ui.doubleSpinBox_kademe_no.value())))
        if self.window3.guc==0:
            popup.error_msjbox(title='Hesap Hatası', text='Lütfen Önce gücü giriniz.')
            return False
        else:
            
            self.window3.setWindowTitle("Kesit Parametreleri Sayfası")

        self.window3.karkas_yukseklik=self.ui.doubleSpinBox_karkas_yukseklik.value()
        self.window3.frekans=self.ui.doubleSpinBox_frekans.value()
        self.window3.karkas_en=self.ui.doubleSpinBox_karkas_en.value()
        self.window3.karkas_boy=self.ui.doubleSpinBox_karkas_boy.value()
        self.window3.c=self.ui.doubleSpinBox_c.value()
        self.window3.karkas_verim=self.ui.doubleSpinBox_karkas_verim.value()
        self.window3.gauss=self.ui.doubleSpinBox_gauss.value()
        self.window3.cu_yog = self.ui.doubleSpinBox_58.value()
        self.window3.al_yog = self.ui.doubleSpinBox_62.value()
        self.window3.di_yog = self.ui.doubleSpinBox_64.value()   

        self.window3.primer_sarim_yukseklik_toplam = self.primer_sarim_yukseklik_toplam
        self.window3.sekonder_sarim_yukseklik_toplam = self.sekonder_sarim_yukseklik_toplam
        self.window3.sva1_sarim_yukseklik_toplam = self.sva1_sarim_yukseklik_toplam
        self.window3.sva2_sarim_yukseklik_toplam = self.sva2_sarim_yukseklik_toplam
        self.window3.sva3_sarim_yukseklik_toplam = self.sva3_sarim_yukseklik_toplam
        self.window3.sva4_sarim_yukseklik_toplam = self.sva4_sarim_yukseklik_toplam
        self.window3.sva5_sarim_yukseklik_toplam = self.sva5_sarim_yukseklik_toplam
        self.window3.sva6_sarim_yukseklik_toplam = self.sva6_sarim_yukseklik_toplam
        self.window3.sva7_sarim_yukseklik_toplam = self.sva7_sarim_yukseklik_toplam
        self.window3.sva8_sarim_yukseklik_toplam = self.sva8_sarim_yukseklik_toplam
        self.window3.sva9_sarim_yukseklik_toplam = self.sva9_sarim_yukseklik_toplam
        self.window3.sva10_sarim_yukseklik_toplam = self.sva10_sarim_yukseklik_toplam
        self.window3.primer_izolasyon = self.primer_izolasyon
        self.window3.sva1_izolasyon = self.sva1_izolasyon
        self.window3.sva2_izolasyon = self.sva2_izolasyon
        self.window3.sva3_izolasyon = self.sva3_izolasyon
        self.window3.sva4_izolasyon = self.sva4_izolasyon
        self.window3.sva5_izolasyon = self.sva5_izolasyon
        self.window3.sva6_izolasyon = self.sva6_izolasyon
        self.window3.sva7_izolasyon = self.sva7_izolasyon
        self.window3.sva8_izolasyon = self.sva8_izolasyon
        self.window3.sva9_izolasyon = self.sva9_izolasyon
        self.window3.sva10_izolasyon = self.sva10_izolasyon

        self.window3.show()

        self.window3.ui.pushButton_kaydet_2.clicked.connect(self.window3.close)
    def kesit_parametrelerini_al(self, window, gl_popup, gl_main,kademe):

        if gl_popup[kademe]["kesit_error"]==True or gl_popup[kademe]["akim_error"]==True:
            returnValue = popup.warning_msjbox(title='Kesit Değerleri Hatası', text='Kesit değerleri önerilen değerlerin altındadır. Devam etmek için buotana basın.')
        else:
            returnValue = QMessageBox.Ok
        if returnValue == QMessageBox.Cancel:
            return False
        elif returnValue == QMessageBox.Ok:
            for i in range(0, 10):

                for key in vt.kademe.keys():
                    gl_main[i][key] = gl_popup[i][key]

            window.close()
        self.hesaplamalari_guncelle()
    def open_izolasyon(self):
        self.window3 = popup.Izolasyondialog()

        self.window3.setWindowTitle("Izolasyon Parametreleri Sayfası")

        self.window3.show()
        self.window3.ui.pushButton_sec.clicked.connect(lambda  x:self.izolasyon_verileri_guncelle(object=self.window3))
        self.izolasyon_deger_al(object=self.window3)
    def open_other_trafo(self,trafo_index):
        if trafo_index == 0:
            import myApp
            self.window = myApp.MyWindow()

            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            self.close()
            self.window.show()
            self.window.ui.stackedWidget.setCurrentIndex(0)
        elif trafo_index == 1:

            import myizole_trifaz
            self.window = myizole_trifaz.MyWindow()

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

            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            self.close()
            self.window.show()
            self.window.ui.stackedWidget.setCurrentIndex(0)
        elif trafo_index == 5:
            import mysok_trifaz
            self.window = mysok_trifaz.SokTrifazwindow()

            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            self.close()
            self.window.show()
            self.window.ui.stackedWidget.setCurrentIndex(0)
        elif trafo_index == 6:
            import myoto_monofaz
            self.window = myoto_monofaz.OtoMonofazwindow()

            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            self.close()
            self.window.show()
            self.window.ui.stackedWidget.setCurrentIndex(0)
        elif trafo_index == 7:
            import myoto_trifaz
            self.window = myoto_trifaz.OtoTrifazwindow()

            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            self.close()
            self.window.show()
            self.window.ui.stackedWidget.setCurrentIndex(0)
        elif trafo_index == 8:
            import myharmonik
            self.window = myharmonik.Harmonikwindow()

            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            self.close()
            self.window.show()
            self.window.ui.stackedWidget.setCurrentIndex(0)
        elif trafo_index == 9:
            import myups
            self.window = myups.UPSwindow()
            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            self.close()
            self.window.show()
            self.window.ui.stackedWidget.setCurrentIndex(0)
        elif trafo_index == 10:
            import mymonoUI
            self.window = mymonoUI.MonoUIwindow()
            self.window.ui.lineEdit_user.setText(self.ui.lineEdit_user.text())
            self.close()
            self.window.show()
            self.window.ui.stackedWidget.setCurrentIndex(0)
    # ========== RECETE ==========================
    def recete_veri_kumesi(self,veri_kumesi):
        veri_kumesi.rec_veriler["kullanici"] = self.ui.lineEdit_user.text()
        veri_kumesi.rec_veriler["primer_group_list"] = self.group_name_list_primer_kademe
        veri_kumesi.rec_veriler["sekonder_group_list"] = self.group_name_list_sekonder_kademe
        veri_kumesi.rec_veriler["va_group_list"][0] = self.group_name_list_sva1_kademe
        veri_kumesi.rec_veriler["va_group_list"][1] = self.group_name_list_sva2_kademe
        veri_kumesi.rec_veriler["va_group_list"][2] = self.group_name_list_sva3_kademe
        veri_kumesi.rec_veriler["va_group_list"][3] = self.group_name_list_sva4_kademe
        veri_kumesi.rec_veriler["va_group_list"][4] = self.group_name_list_sva5_kademe
        veri_kumesi.rec_veriler["va_group_list"][5] = self.group_name_list_sva6_kademe
        veri_kumesi.rec_veriler["va_group_list"][6] = self.group_name_list_sva7_kademe
        veri_kumesi.rec_veriler["va_group_list"][7] = self.group_name_list_sva8_kademe
        veri_kumesi.rec_veriler["va_group_list"][8] = self.group_name_list_sva9_kademe
                                   
        veri_kumesi.rec_veriler["guc"] = self.ui.doubleSpinBox_guc.value()
        veri_kumesi.rec_veriler["trafo_tipi" ]= " Izolasyon Trafosu Mono Faz " # bunu hiç değiştirme aksi hlde veri tabanındakilere ulasamazsın

        veri_kumesi.rec_veriler["primer_kademe" ]= int(self.ui.comboBox.currentText())
        veri_kumesi.rec_veriler[ "sekonder_kademe"] = int(self.ui.comboBox_sek.currentText())
        veri_kumesi.rec_veriler[ "va_kademe" ]= int(self.ui.comboBox_va.currentText())
        veri_kumesi.rec_veriler[ "va_altkademe" ]= self.va_kademe_listesi
        veri_kumesi.rec_veriler[ "va_enabled" ]= self.ui.radioButton_vadagilim.isChecked()

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
        veri_kumesi.rec_veriler["sekonder_izo_deg" ]= self.ui.doubleSpinBox_sekonder_izo_deg.value()
        veri_kumesi.rec_veriler["pri_sek_izo_deg" ]= self.ui.doubleSpinBox_pri_sek_izo_deg.value()
        veri_kumesi.rec_veriler["ekran_izo_deg" ]= self.ui.doubleSpinBox_ekran_izo_deg.value()
        veri_kumesi.rec_veriler["ekstra_izo_deg" ]= self.ui.doubleSpinBox_ekstra_izo_deg.value()
        veri_kumesi.rec_veriler["primer_izo_tur" ]= self.ui.doubleSpinBox_primer_izo_tur.value()
        veri_kumesi.rec_veriler["sekonder_izo_tur" ]= self.ui.doubleSpinBox_sekonder_izo_tur.value()
        veri_kumesi.rec_veriler["pri_sek_izo_tur" ]= self.ui.doubleSpinBox_pri_sek_izo_tur.value()
        veri_kumesi.rec_veriler["ekran_sec" ]= self.ui.checkBox_ekran_sec.isChecked()
        veri_kumesi.rec_veriler["ekstra" ]= self.ui.checkBox_ekstra.isChecked()
        veri_kumesi.rec_veriler["va_guclist"]=[guc.value() for guc in self.va_guclist]
        veri_kumesi.rec_veriler["va_altkademe"] = [float(kademe.currentText()) for kademe in self.va_kademe_listesi]
    def recete_deger_al(self,window):
        data = db.calldata_with_id_recete(window.ui.doubleSpinBox_ID.value())
        if data == None:
            return False
        self.degerler_sifirlama()
        self.rec_veriler = json.loads(data[9])

        if self.rec_veriler["va_enabled"]==False:

            self.ui.radioButton_kademeli.setChecked(True)
        else:

            self.ui.radioButton_vadagilim.setChecked(True)
        self.ui.comboBox.setCurrentText(str(self.rec_veriler["primer_kademe"]))
        self.ui.comboBox_sek.setCurrentText(str(self.rec_veriler["sekonder_kademe"]))
        self.ui.comboBox_va.setCurrentText(str(self.rec_veriler["va_kademe"]))
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
        self.ui.doubleSpinBox_sekonder_izo_deg.setValue(self.rec_veriler["sekonder_izo_deg"])
        self.ui.doubleSpinBox_sekonder_izo_tur.setValue(self.rec_veriler["sekonder_izo_tur"])
        self.ui.doubleSpinBox_pri_sek_izo_deg.setValue(self.rec_veriler["pri_sek_izo_deg"])
        self.ui.doubleSpinBox_pri_sek_izo_tur.setValue(self.rec_veriler["pri_sek_izo_tur"])
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

        for i in range(0, 10):
            self.group_name_list_primer_kademe[i]=self.rec_veriler["primer_group_list"][i]
            self.group_name_list_sekonder_kademe[i]=self.rec_veriler["sekonder_group_list"][i]
            self.va_guclist[i].setValue(float(self.rec_veriler["va_guclist"][i]))
            self.va_kademe_listesi[i].setCurrentText(str(self.rec_veriler["va_altkademe"][i]))

            for y in range(0, 10):
                self.va_group_elementlist[i][y]=self.rec_veriler["va_group_list"][i][y]

        self.hesaplamalari_guncelle()
        self.va_kademe_guncelle()
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
    def karkas_oto_man_secimi(self,mod):
        if mod==0:
            self.ui.doubleSpinBox_karkas_en.setEnabled(True)
            self.ui.doubleSpinBox_karkas_boy.setEnabled(True)
            self.ui.doubleSpinBox_karkas_yukseklik.setEnabled(True)
            self.ui.doubleSpinBox_karkas_adet.setEnabled(True)
            self.ui.doubleSpinBox_karkas_verim.setEnabled(True)
            self.ui.checkBox_karkas_bolmeli.setEnabled(True)
            self.ui.checkBox_karkas_kesme_sac.setEnabled(True)
        else:
            self.ui.doubleSpinBox_karkas_en.setEnabled(False)
            self.ui.doubleSpinBox_karkas_boy.setEnabled(False)
            self.ui.doubleSpinBox_karkas_yukseklik.setEnabled(False)
            self.ui.doubleSpinBox_karkas_adet.setEnabled(False)
            self.ui.doubleSpinBox_karkas_verim.setEnabled(False)
            self.ui.checkBox_karkas_bolmeli.setEnabled(False)
            self.ui.checkBox_karkas_kesme_sac.setEnabled(False)
    def karkas_deger_al(self,object):
        global karkas_en,karkas_boy
        karkas_en=object.ui.doubleSpinBox_karkas_en.value()
        karkas_boy = object.ui.doubleSpinBox_karkas_boy.value()
        self.ui.doubleSpinBox_karkas_en.setValue(object.ui.doubleSpinBox_karkas_en.value())
        self.ui.doubleSpinBox_karkas_boy.setValue(object.ui.doubleSpinBox_karkas_boy.value())
        self.ui.lineEdit_mlz_karkas.setText(object.ui.lineEdit_karkas_name.text())
        self.karkas_hesaplama()
    def karkas_hesaplama(self):
        self.ui.doubleSpinBox_karkas_yuk_oto.setValue(hp.karkas_yuk(karkas_en=self.ui.doubleSpinBox_karkas_en.value()))
        self.ui.doubleSpinBox_karkas_cm_oto.setValue(hp.karkas_Ac_oto(c=self.ui.doubleSpinBox_c.value(),
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
    # ==========Mono Faz İzolasyon Trafosu - sekonder ======================================
    def sekonder_veri_kumesi(self):
        

        self.group_list_sekonder_kademe_1 = vt.kademe.copy()
        self.group_list_sekonder_kademe_2 = vt.kademe.copy()
        self.group_list_sekonder_kademe_3 = vt.kademe.copy()
        self.group_list_sekonder_kademe_4 = vt.kademe.copy()
        self.group_list_sekonder_kademe_5 = vt.kademe.copy()
        self.group_list_sekonder_kademe_6 = vt.kademe.copy()
        self.group_list_sekonder_kademe_7 = vt.kademe.copy()
        self.group_list_sekonder_kademe_8 = vt.kademe.copy()
        self.group_list_sekonder_kademe_9 = vt.kademe.copy()
        self.group_list_sekonder_kademe_10 = vt.kademe.copy()
        self.group_name_list_sekonder_kademe = [self.group_list_sekonder_kademe_1, self.group_list_sekonder_kademe_2,
                                              self.group_list_sekonder_kademe_3,
                                              self.group_list_sekonder_kademe_4, self.group_list_sekonder_kademe_5,
                                              self.group_list_sekonder_kademe_6, self.group_list_sekonder_kademe_7,
                                              self.group_list_sekonder_kademe_8, self.group_list_sekonder_kademe_9,
                                              self.group_list_sekonder_kademe_10]
        

        self.group_list_sekonder_11 = [self.ui.doubleSpinBox_v_sek_1,self.ui.doubleSpinBox_sipir_1_sek_1,
                                     self.ui.doubleSpinBox_kesit_sek_1,self.ui.doubleSpinBox_cap_1_sek_1,
                                     self.ui.doubleSpinBox_akim_1_sek_1,self.ui.doubleSpinBox_sipir_2_sek_1,
                                     self.ui.doubleSpinBox_kesit_2_sek_1,self.ui.doubleSpinBox_cap_2_sek_1,
                                     self.ui.doubleSpinBox_akim_2_sek_1,self.ui.comboBox_tel_sek_1,
                                     self.ui.label_kesit_ok_sek_1,self.ui.label_kesit_error_sek_1]
        self.group_list_sekonder_22 = [self.ui.doubleSpinBox_v_sek_2,self.ui.doubleSpinBox_sipir_1_sek_2,
                                     self.ui.doubleSpinBox_kesit_sek_2,self.ui.doubleSpinBox_cap_1_sek_2,
                                     self.ui.doubleSpinBox_akim_1_sek_2,self.ui.doubleSpinBox_sipir_2_sek_2,
                                     self.ui.doubleSpinBox_kesit_2_sek_2,self.ui.doubleSpinBox_cap_2_sek_2,
                                     self.ui.doubleSpinBox_akim_2_sek_2,self.ui.comboBox_tel_sek_2,
                                     self.ui.label_kesit_ok_sek_2,self.ui.label_kesit_error_sek_2]
        self.group_list_sekonder_32 = [self.ui.doubleSpinBox_v_sek_3,self.ui.doubleSpinBox_sipir_1_sek_3,
                                     self.ui.doubleSpinBox_kesit_sek_3,self.ui.doubleSpinBox_cap_1_sek_3,
                                     self.ui.doubleSpinBox_akim_1_sek_3,self.ui.doubleSpinBox_sipir_2_sek_3,
                                     self.ui.doubleSpinBox_kesit_2_sek_3,self.ui.doubleSpinBox_cap_2_sek_3,
                                     self.ui.doubleSpinBox_akim_2_sek_3,self.ui.comboBox_tel_sek_3,
                                     self.ui.label_kesit_ok_sek_3,self.ui.label_kesit_error_sek_3]
        self.group_list_sekonder_42 = [self.ui.doubleSpinBox_v_sek_4,self.ui.doubleSpinBox_sipir_1_sek_4,
                                     self.ui.doubleSpinBox_kesit_sek_4,self.ui.doubleSpinBox_cap_1_sek_4,
                                     self.ui.doubleSpinBox_akim_1_sek_4,self.ui.doubleSpinBox_sipir_2_sek_4,
                                     self.ui.doubleSpinBox_kesit_2_sek_4,self.ui.doubleSpinBox_cap_2_sek_4,
                                     self.ui.doubleSpinBox_akim_2_sek_4,self.ui.comboBox_tel_sek_4,
                                     self.ui.label_kesit_ok_sek_4,self.ui.label_kesit_error_sek_4]
        self.group_list_sekonder_52 = [self.ui.doubleSpinBox_v_sek_5,self.ui.doubleSpinBox_sipir_1_sek_5,
                                     self.ui.doubleSpinBox_kesit_sek_5,self.ui.doubleSpinBox_cap_1_sek_5,
                                     self.ui.doubleSpinBox_akim_1_sek_5,self.ui.doubleSpinBox_sipir_2_sek_5,
                                     self.ui.doubleSpinBox_kesit_2_sek_5,self.ui.doubleSpinBox_cap_2_sek_5,
                                     self.ui.doubleSpinBox_akim_2_sek_5,self.ui.comboBox_tel_sek_5,
                                     self.ui.label_kesit_ok_sek_5,self.ui.label_kesit_error_sek_5]
        self.group_list_sekonder_62 = [self.ui.doubleSpinBox_v_sek_6,self.ui.doubleSpinBox_sipir_1_sek_6,
                                     self.ui.doubleSpinBox_kesit_sek_6,self.ui.doubleSpinBox_cap_1_sek_6,
                                     self.ui.doubleSpinBox_akim_1_sek_6,self.ui.doubleSpinBox_sipir_2_sek_6,
                                     self.ui.doubleSpinBox_kesit_2_sek_6,self.ui.doubleSpinBox_cap_2_sek_6,
                                     self.ui.doubleSpinBox_akim_2_sek_6,self.ui.comboBox_tel_sek_6,
                                     self.ui.label_kesit_ok_sek_6,self.ui.label_kesit_error_sek_6]
        self.group_list_sekonder_72 = [self.ui.doubleSpinBox_v_sek_7,self.ui.doubleSpinBox_sipir_1_sek_7,
                                     self.ui.doubleSpinBox_kesit_sek_7,self.ui.doubleSpinBox_cap_1_sek_7,
                                     self.ui.doubleSpinBox_akim_1_sek_7,self.ui.doubleSpinBox_sipir_2_sek_7,
                                     self.ui.doubleSpinBox_kesit_2_sek_7,self.ui.doubleSpinBox_cap_2_sek_7,
                                     self.ui.doubleSpinBox_akim_2_sek_7,self.ui.comboBox_tel_sek_7,
                                     self.ui.label_kesit_ok_sek_7,self.ui.label_kesit_error_sek_7]
        self.group_list_sekonder_82 = [self.ui.doubleSpinBox_v_sek_8,self.ui.doubleSpinBox_sipir_1_sek_8,
                                     self.ui.doubleSpinBox_kesit_sek_8,self.ui.doubleSpinBox_cap_1_sek_8,
                                     self.ui.doubleSpinBox_akim_1_sek_8,self.ui.doubleSpinBox_sipir_2_sek_8,
                                     self.ui.doubleSpinBox_kesit_2_sek_8,self.ui.doubleSpinBox_cap_2_sek_8,
                                     self.ui.doubleSpinBox_akim_2_sek_8,self.ui.comboBox_tel_sek_8,
                                     self.ui.label_kesit_ok_sek_8,self.ui.label_kesit_error_sek_8]     
        self.group_list_sekonder_92 = [self.ui.doubleSpinBox_v_sek_9,self.ui.doubleSpinBox_sipir_1_sek_9,
                                     self.ui.doubleSpinBox_kesit_sek_9,self.ui.doubleSpinBox_cap_1_sek_9,
                                     self.ui.doubleSpinBox_akim_1_sek_9,self.ui.doubleSpinBox_sipir_2_sek_9,
                                     self.ui.doubleSpinBox_kesit_2_sek_9,self.ui.doubleSpinBox_cap_2_sek_9,
                                     self.ui.doubleSpinBox_akim_2_sek_9,self.ui.comboBox_tel_sek_9,
                                     self.ui.label_kesit_ok_sek_9,self.ui.label_kesit_error_sek_9] 
        self.group_list_sekonder_102 = [self.ui.doubleSpinBox_v_sek_10,self.ui.doubleSpinBox_sipir_1_sek_10,
                                     self.ui.doubleSpinBox_kesit_sek_10,self.ui.doubleSpinBox_cap_1_sek_10,
                                     self.ui.doubleSpinBox_akim_1_sek_10,self.ui.doubleSpinBox_sipir_2_sek_10,
                                     self.ui.doubleSpinBox_kesit_2_sek_10,self.ui.doubleSpinBox_cap_2_sek_10,
                                     self.ui.doubleSpinBox_akim_2_sek_10,self.ui.comboBox_tel_sek_10,
                                     self.ui.label_kesit_ok_sek_10,self.ui.label_kesit_error_sek_10]                                                                                                             
        self.group_name_list_sekonder_2 = [self.group_list_sekonder_11,self.group_list_sekonder_22,self.group_list_sekonder_32,
                                        self.group_list_sekonder_42,self.group_list_sekonder_52,self.group_list_sekonder_62,
                                        self.group_list_sekonder_72,self.group_list_sekonder_82,self.group_list_sekonder_92,
                                        self.group_list_sekonder_102]
        self.button_list_sekonder = [self.ui.pushButton_buton_sek_1,self.ui.pushButton_buton_sek_2,
                                    self.ui.pushButton_buton_sek_3,self.ui.pushButton_buton_sek_4,
                                    self.ui.pushButton_buton_sek_5,self.ui.pushButton_buton_sek_6,
                                    self.ui.pushButton_buton_sek_7,self.ui.pushButton_buton_sek_8,
                                    self.ui.pushButton_buton_sek_9,self.ui.pushButton_buton_sek_10]
    def sekonder_kademe_secimi(self,mod,kademe=1):
        if mod==0:
            self.ui.stackedWidget_2.setCurrentIndex(0)
            self.kademe_goster(object=self.ui.comboBox_sek, group_list=self.kademe_list_4)
            self.ui.groupBox_VA_dagilim.setVisible(False)
            self.ui.comboBox_va.setCurrentIndex(0)
            self.ui.comboBox_va.setEnabled(False)
            self.ui.comboBox_sek.setEnabled(True)
            self.sekonder_veri_kumesi()
        elif mod==1:
            
            self.kademe_goster(object=self.ui.comboBox_sva1_kad, group_list=self.kademe_list_s1)
            self.ui.groupBox_VA_dagilim.setVisible(True)
            self.ui.comboBox_sek.setCurrentIndex(0)
            self.ui.comboBox_va.setEnabled(True)
            self.ui.comboBox_sek.setEnabled(False)
            self.ui.stackedWidget_2.setCurrentIndex(1)
            self.sekonder_veri_kumesi()
        self.hesaplamalari_guncelle()
            # self.hesap_1_gnl(gl=self.group_name_list_sekonder_kademe,
            #         gl2=self.group_name_list_sekonder_2,
            #         guc=self.ui.doubleSpinBox_guc.value(),
            #         frekans=self.ui.doubleSpinBox_frekans.value() ,
            #         gauss=self.ui.doubleSpinBox_gauss.value(),
            #         karkas_en=self.ui.doubleSpinBox_karkas_en.value(),
            #         karkas_boy=self.ui.doubleSpinBox_karkas_boy.value(),
            #         karkas_yuk=self.ui.doubleSpinBox_karkas_yukseklik.value(),
            #         verim=self.ui.doubleSpinBox_karkas_verim.value(),
            #         sarim="sekonder",
            #         kademe=int(self.ui.comboBox_sek.currentText()))
    def sekonder_kademe_goster(self):
        self.kademe_goster(object=self.ui.comboBox_sek, group_list=self.kademe_list_4)
        self.sekonder_kademe_secimi(mod=0)

        self.hesap_1_gnl(gl=self.group_name_list_sekonder_kademe,
                    gl2=self.group_name_list_sekonder_2,
                    guc=self.ui.doubleSpinBox_guc.value(),
                    frekans=self.ui.doubleSpinBox_frekans.value() ,
                    gauss=self.ui.doubleSpinBox_gauss.value(),
                    karkas_en=self.ui.doubleSpinBox_karkas_en.value(),
                    karkas_boy=self.ui.doubleSpinBox_karkas_boy.value(),
                    karkas_yuk=self.ui.doubleSpinBox_karkas_yukseklik.value(),
                    verim=self.ui.doubleSpinBox_karkas_verim.value(),
                    sarim="sekonder",
                    kademe=int(self.ui.comboBox_sek.currentText()))
    def sekonder_object_signals(self):
        self.ui.radioButton_kademeli.toggled.connect(lambda x:self.sekonder_kademe_secimi(mod=0))
        self.ui.radioButton_vadagilim.toggled.connect(lambda x:self.sekonder_kademe_secimi(mod=1))
        self.ui.radioButton_kademeli.toggled.connect(lambda x: self.sekonder_kademe_secimi(mod=0))
        self.ui.comboBox_sek.currentTextChanged.connect(self.sekonder_kademe_goster)

        for i in range(0,10):
            self.button_list_sekonder[i].clicked.connect(self.open_kesit_hesaplama)

    # ==========VA KAdeme ======================================
    def va_veri_kumesi(self):
        self.guclist_1 = [self.ui.doubleSpinBox_s1, self.ui.doubleSpinBox_s2, self.ui.doubleSpinBox_s3,
                          self.ui.doubleSpinBox_s4, self.ui.doubleSpinBox_s5, self.ui.doubleSpinBox_s6,
                          self.ui.doubleSpinBox_s7, self.ui.doubleSpinBox_s8, self.ui.doubleSpinBox_s9,
                          self.ui.doubleSpinBox_s10]
        self.va_kademe_listesi = [self.ui.comboBox_sva1_kad,
                                  self.ui.comboBox_sva2_kad,
                                  self.ui.comboBox_sva3_kad,
                                  self.ui.comboBox_sva4_kad,
                                  self.ui.comboBox_sva5_kad,
                                  self.ui.comboBox_sva6_kad,
                                  self.ui.comboBox_sva7_kad,
                                  self.ui.comboBox_sva8_kad,
                                  self.ui.comboBox_sva9_kad,
                                  self.ui.comboBox_sva10_kad]
        self.va_guclist = [self.ui.doubleSpinBox_sva1_guc,
                           self.ui.doubleSpinBox_sva2_guc,
                           self.ui.doubleSpinBox_sva3_guc,
                           self.ui.doubleSpinBox_sva4_guc,
                           self.ui.doubleSpinBox_sva5_guc,
                           self.ui.doubleSpinBox_sva6_guc,
                           self.ui.doubleSpinBox_sva7_guc,
                           self.ui.doubleSpinBox_sva8_guc,
                           self.ui.doubleSpinBox_sva9_guc,
                           self.ui.doubleSpinBox_sva10_guc
                           ]
        # ------------------------------------------------
        self.group_list_sva1_kademe_1 = vt.kademe.copy()
        self.group_list_sva1_kademe_2 = vt.kademe.copy()
        self.group_list_sva1_kademe_3 = vt.kademe.copy()
        self.group_list_sva1_kademe_4 = vt.kademe.copy()
        self.group_list_sva1_kademe_5 = vt.kademe.copy()
        self.group_list_sva1_kademe_6 = vt.kademe.copy()
        self.group_list_sva1_kademe_7 = vt.kademe.copy()
        self.group_list_sva1_kademe_8 = vt.kademe.copy()
        self.group_list_sva1_kademe_9 = vt.kademe.copy()
        self.group_list_sva1_kademe_10 = vt.kademe.copy()
        self.group_name_list_sva1_kademe = [self.group_list_sva1_kademe_1, self.group_list_sva1_kademe_2,
                                                self.group_list_sva1_kademe_3,
                                                self.group_list_sva1_kademe_4, self.group_list_sva1_kademe_5,
                                                self.group_list_sva1_kademe_6, self.group_list_sva1_kademe_7,
                                                self.group_list_sva1_kademe_8, self.group_list_sva1_kademe_9,
                                                self.group_list_sva1_kademe_10]

        self.group_list_sva2_kademe_1 = vt.kademe.copy()
        self.group_list_sva2_kademe_2 = vt.kademe.copy()
        self.group_list_sva2_kademe_3 = vt.kademe.copy()
        self.group_list_sva2_kademe_4 = vt.kademe.copy()
        self.group_list_sva2_kademe_5 = vt.kademe.copy()
        self.group_list_sva2_kademe_6 = vt.kademe.copy()
        self.group_list_sva2_kademe_7 = vt.kademe.copy()
        self.group_list_sva2_kademe_8 = vt.kademe.copy()
        self.group_list_sva2_kademe_9 = vt.kademe.copy()
        self.group_list_sva2_kademe_10 = vt.kademe.copy()
        self.group_name_list_sva2_kademe = [self.group_list_sva2_kademe_1, self.group_list_sva2_kademe_2,
                                            self.group_list_sva2_kademe_3,
                                            self.group_list_sva2_kademe_4, self.group_list_sva2_kademe_5,
                                            self.group_list_sva2_kademe_6, self.group_list_sva2_kademe_7,
                                            self.group_list_sva2_kademe_8, self.group_list_sva2_kademe_9,
                                            self.group_list_sva2_kademe_10]
        
        self.group_list_sva3_kademe_1 = vt.kademe.copy()
        self.group_list_sva3_kademe_2 = vt.kademe.copy()
        self.group_list_sva3_kademe_3 = vt.kademe.copy()
        self.group_list_sva3_kademe_4 = vt.kademe.copy()
        self.group_list_sva3_kademe_5 = vt.kademe.copy()
        self.group_list_sva3_kademe_6 = vt.kademe.copy()
        self.group_list_sva3_kademe_7 = vt.kademe.copy()
        self.group_list_sva3_kademe_8 = vt.kademe.copy()
        self.group_list_sva3_kademe_9 = vt.kademe.copy()
        self.group_list_sva3_kademe_10 = vt.kademe.copy()
        self.group_name_list_sva3_kademe = [self.group_list_sva3_kademe_1, self.group_list_sva3_kademe_2,
                                            self.group_list_sva3_kademe_3,
                                            self.group_list_sva3_kademe_4, self.group_list_sva3_kademe_5,
                                            self.group_list_sva3_kademe_6, self.group_list_sva3_kademe_7,
                                            self.group_list_sva3_kademe_8, self.group_list_sva3_kademe_9,
                                            self.group_list_sva3_kademe_10]
        self.group_list_sva4_kademe_1 = vt.kademe.copy()
        self.group_list_sva4_kademe_2 = vt.kademe.copy()
        self.group_list_sva4_kademe_3 = vt.kademe.copy()
        self.group_list_sva4_kademe_4 = vt.kademe.copy()
        self.group_list_sva4_kademe_5 = vt.kademe.copy()
        self.group_list_sva4_kademe_6 = vt.kademe.copy()
        self.group_list_sva4_kademe_7 = vt.kademe.copy()
        self.group_list_sva4_kademe_8 = vt.kademe.copy()
        self.group_list_sva4_kademe_9 = vt.kademe.copy()
        self.group_list_sva4_kademe_10 = vt.kademe.copy()
        self.group_name_list_sva4_kademe = [self.group_list_sva4_kademe_1, self.group_list_sva4_kademe_2,
                                            self.group_list_sva4_kademe_3,
                                            self.group_list_sva4_kademe_4, self.group_list_sva4_kademe_5,
                                            self.group_list_sva4_kademe_6, self.group_list_sva4_kademe_7,
                                            self.group_list_sva4_kademe_8, self.group_list_sva4_kademe_9,
                                            self.group_list_sva4_kademe_10]
        self.group_list_sva5_kademe_1 = vt.kademe.copy()
        self.group_list_sva5_kademe_2 = vt.kademe.copy()
        self.group_list_sva5_kademe_3 = vt.kademe.copy()
        self.group_list_sva5_kademe_4 = vt.kademe.copy()
        self.group_list_sva5_kademe_5 = vt.kademe.copy()
        self.group_list_sva5_kademe_6 = vt.kademe.copy()
        self.group_list_sva5_kademe_7 = vt.kademe.copy()
        self.group_list_sva5_kademe_8 = vt.kademe.copy()
        self.group_list_sva5_kademe_9 = vt.kademe.copy()
        self.group_list_sva5_kademe_10 = vt.kademe.copy()
        self.group_name_list_sva5_kademe = [self.group_list_sva5_kademe_1, self.group_list_sva5_kademe_2,
                                            self.group_list_sva5_kademe_3,
                                            self.group_list_sva5_kademe_4, self.group_list_sva5_kademe_5,
                                            self.group_list_sva5_kademe_6, self.group_list_sva5_kademe_7,
                                            self.group_list_sva5_kademe_8, self.group_list_sva5_kademe_9,
                                            self.group_list_sva5_kademe_10]
        self.group_list_sva6_kademe_1 = vt.kademe.copy()
        self.group_list_sva6_kademe_2 = vt.kademe.copy()
        self.group_list_sva6_kademe_3 = vt.kademe.copy()
        self.group_list_sva6_kademe_4 = vt.kademe.copy()
        self.group_list_sva6_kademe_5 = vt.kademe.copy()
        self.group_list_sva6_kademe_6 = vt.kademe.copy()
        self.group_list_sva6_kademe_7 = vt.kademe.copy()
        self.group_list_sva6_kademe_8 = vt.kademe.copy()
        self.group_list_sva6_kademe_9 = vt.kademe.copy()
        self.group_list_sva6_kademe_10 = vt.kademe.copy()
        self.group_name_list_sva6_kademe = [self.group_list_sva6_kademe_1, self.group_list_sva6_kademe_2,
                                            self.group_list_sva6_kademe_3,
                                            self.group_list_sva6_kademe_4, self.group_list_sva6_kademe_5,
                                            self.group_list_sva6_kademe_6, self.group_list_sva6_kademe_7,
                                            self.group_list_sva6_kademe_8, self.group_list_sva6_kademe_9,
                                            self.group_list_sva6_kademe_10]
        self.group_list_sva7_kademe_1 = vt.kademe.copy()
        self.group_list_sva7_kademe_2 = vt.kademe.copy()
        self.group_list_sva7_kademe_3 = vt.kademe.copy()
        self.group_list_sva7_kademe_4 = vt.kademe.copy()
        self.group_list_sva7_kademe_5 = vt.kademe.copy()
        self.group_list_sva7_kademe_6 = vt.kademe.copy()
        self.group_list_sva7_kademe_7 = vt.kademe.copy()
        self.group_list_sva7_kademe_8 = vt.kademe.copy()
        self.group_list_sva7_kademe_9 = vt.kademe.copy()
        self.group_list_sva7_kademe_10 = vt.kademe.copy()
        self.group_name_list_sva7_kademe = [self.group_list_sva7_kademe_1, self.group_list_sva7_kademe_2,
                                            self.group_list_sva7_kademe_3,
                                            self.group_list_sva7_kademe_4, self.group_list_sva7_kademe_5,
                                            self.group_list_sva7_kademe_6, self.group_list_sva7_kademe_7,
                                            self.group_list_sva7_kademe_8, self.group_list_sva7_kademe_9,
                                            self.group_list_sva7_kademe_10]
        self.group_list_sva8_kademe_1 = vt.kademe.copy()
        self.group_list_sva8_kademe_2 = vt.kademe.copy()
        self.group_list_sva8_kademe_3 = vt.kademe.copy()
        self.group_list_sva8_kademe_4 = vt.kademe.copy()
        self.group_list_sva8_kademe_5 = vt.kademe.copy()
        self.group_list_sva8_kademe_6 = vt.kademe.copy()
        self.group_list_sva8_kademe_7 = vt.kademe.copy()
        self.group_list_sva8_kademe_8 = vt.kademe.copy()
        self.group_list_sva8_kademe_9 = vt.kademe.copy()
        self.group_list_sva8_kademe_10 = vt.kademe.copy()
        self.group_name_list_sva8_kademe = [self.group_list_sva8_kademe_1, self.group_list_sva8_kademe_2,
                                            self.group_list_sva8_kademe_3,
                                            self.group_list_sva8_kademe_4, self.group_list_sva8_kademe_5,
                                            self.group_list_sva8_kademe_6, self.group_list_sva8_kademe_7,
                                            self.group_list_sva8_kademe_8, self.group_list_sva8_kademe_9,
                                            self.group_list_sva8_kademe_10]
        self.group_list_sva9_kademe_1 = vt.kademe.copy()
        self.group_list_sva9_kademe_2 = vt.kademe.copy()
        self.group_list_sva9_kademe_3 = vt.kademe.copy()
        self.group_list_sva9_kademe_4 = vt.kademe.copy()
        self.group_list_sva9_kademe_5 = vt.kademe.copy()
        self.group_list_sva9_kademe_6 = vt.kademe.copy()
        self.group_list_sva9_kademe_7 = vt.kademe.copy()
        self.group_list_sva9_kademe_8 = vt.kademe.copy()
        self.group_list_sva9_kademe_9 = vt.kademe.copy()
        self.group_list_sva9_kademe_10 = vt.kademe.copy()
        self.group_name_list_sva9_kademe = [self.group_list_sva9_kademe_1, self.group_list_sva9_kademe_2,
                                            self.group_list_sva9_kademe_3,
                                            self.group_list_sva9_kademe_4, self.group_list_sva9_kademe_5,
                                            self.group_list_sva9_kademe_6, self.group_list_sva9_kademe_7,
                                            self.group_list_sva9_kademe_8, self.group_list_sva9_kademe_9,
                                            self.group_list_sva9_kademe_10]
        self.group_list_sva10_kademe_1 = vt.kademe.copy()
        self.group_list_sva10_kademe_2 = vt.kademe.copy()
        self.group_list_sva10_kademe_3 = vt.kademe.copy()
        self.group_list_sva10_kademe_4 = vt.kademe.copy()
        self.group_list_sva10_kademe_5 = vt.kademe.copy()
        self.group_list_sva10_kademe_6 = vt.kademe.copy()
        self.group_list_sva10_kademe_7 = vt.kademe.copy()
        self.group_list_sva10_kademe_8 = vt.kademe.copy()
        self.group_list_sva10_kademe_9 = vt.kademe.copy()
        self.group_list_sva10_kademe_10 = vt.kademe.copy()
        self.group_name_list_sva10_kademe = [self.group_list_sva10_kademe_1, self.group_list_sva10_kademe_2,
                                            self.group_list_sva10_kademe_3,
                                            self.group_list_sva10_kademe_4, self.group_list_sva10_kademe_5,
                                            self.group_list_sva10_kademe_6, self.group_list_sva10_kademe_7,
                                            self.group_list_sva10_kademe_8, self.group_list_sva10_kademe_9,
                                            self.group_list_sva10_kademe_10]
        self.va_group_elementlist = [self.group_name_list_sva1_kademe,
                                     self.group_name_list_sva2_kademe,
                                     self.group_name_list_sva3_kademe,
                                     self.group_name_list_sva4_kademe,
                                     self.group_name_list_sva5_kademe,
                                     self.group_name_list_sva6_kademe,
                                     self.group_name_list_sva7_kademe,
                                     self.group_name_list_sva8_kademe,
                                     self.group_name_list_sva9_kademe,
                                     self.group_name_list_sva10_kademe]

        #-------------------------------------------------------------------
        if self.ui.radioButton_vadagilim.isChecked() or self.ui.comboBox_va.currentIndex()>=0:

            self.group_list_sva1_11 = [self.ui.doubleSpinBox_v_s1_1,self.ui.doubleSpinBox_sipir_1_s1_1,
                                     self.ui.doubleSpinBox_kesit_s1_1,self.ui.doubleSpinBox_cap_1_s1_1,
                                     self.ui.doubleSpinBox_akim_1_s1_1,self.ui.doubleSpinBox_sipir_2_s1_1,
                                     self.ui.doubleSpinBox_kesit_2_s1_1,self.ui.doubleSpinBox_cap_2_s1_1,
                                     self.ui.doubleSpinBox_akim_2_s1_1,self.ui.comboBox_tel_s1_1,
                                     self.ui.label_kesit_ok_s1_1,self.ui.label_kesit_error_s1_1]
            self.group_list_sva1_22 = [self.ui.doubleSpinBox_v_s1_2,self.ui.doubleSpinBox_sipir_1_s1_2,
                                     self.ui.doubleSpinBox_kesit_s1_2,self.ui.doubleSpinBox_cap_1_s1_2,
                                     self.ui.doubleSpinBox_akim_1_s1_2,self.ui.doubleSpinBox_sipir_2_s1_2,
                                     self.ui.doubleSpinBox_kesit_2_s1_2,self.ui.doubleSpinBox_cap_2_s1_2,
                                     self.ui.doubleSpinBox_akim_2_s1_2,self.ui.comboBox_tel_s1_2,
                                     self.ui.label_kesit_ok_s1_2,self.ui.label_kesit_error_s1_2]
            self.group_list_sva1_32 = [self.ui.doubleSpinBox_v_s1_3,self.ui.doubleSpinBox_sipir_1_s1_3,
                                     self.ui.doubleSpinBox_kesit_s1_3,self.ui.doubleSpinBox_cap_1_s1_3,
                                     self.ui.doubleSpinBox_akim_1_s1_3,self.ui.doubleSpinBox_sipir_2_s1_3,
                                     self.ui.doubleSpinBox_kesit_2_s1_3,self.ui.doubleSpinBox_cap_2_s1_3,
                                     self.ui.doubleSpinBox_akim_2_s1_3,self.ui.comboBox_tel_s1_3,
                                     self.ui.label_kesit_ok_s1_3,self.ui.label_kesit_error_s1_3]
            self.group_list_sva1_42 = [self.ui.doubleSpinBox_v_s1_4,self.ui.doubleSpinBox_sipir_1_s1_4,
                                     self.ui.doubleSpinBox_kesit_s1_4,self.ui.doubleSpinBox_cap_1_s1_4,
                                     self.ui.doubleSpinBox_akim_1_s1_4,self.ui.doubleSpinBox_sipir_2_s1_4,
                                     self.ui.doubleSpinBox_kesit_2_s1_4,self.ui.doubleSpinBox_cap_2_s1_4,
                                     self.ui.doubleSpinBox_akim_2_s1_4,self.ui.comboBox_tel_s1_4,
                                     self.ui.label_kesit_ok_s1_4,self.ui.label_kesit_error_s1_4]
            self.group_list_sva1_52 = [self.ui.doubleSpinBox_v_s1_5,self.ui.doubleSpinBox_sipir_1_s1_5,
                                     self.ui.doubleSpinBox_kesit_s1_5,self.ui.doubleSpinBox_cap_1_s1_5,
                                     self.ui.doubleSpinBox_akim_1_s1_5,self.ui.doubleSpinBox_sipir_2_s1_5,
                                     self.ui.doubleSpinBox_kesit_2_s1_5,self.ui.doubleSpinBox_cap_2_s1_5,
                                     self.ui.doubleSpinBox_akim_2_s1_5,self.ui.comboBox_tel_s1_5,
                                     self.ui.label_kesit_ok_s1_5,self.ui.label_kesit_error_s1_5]
            self.group_list_sva1_62 = [self.ui.doubleSpinBox_v_s1_6,self.ui.doubleSpinBox_sipir_1_s1_6,
                                     self.ui.doubleSpinBox_kesit_s1_6,self.ui.doubleSpinBox_cap_1_s1_6,
                                     self.ui.doubleSpinBox_akim_1_s1_6,self.ui.doubleSpinBox_sipir_2_s1_6,
                                     self.ui.doubleSpinBox_kesit_2_s1_6,self.ui.doubleSpinBox_cap_2_s1_6,
                                     self.ui.doubleSpinBox_akim_2_s1_6,self.ui.comboBox_tel_s1_6,
                                     self.ui.label_kesit_ok_s1_6,self.ui.label_kesit_error_s1_6]
            self.group_list_sva1_72 = [self.ui.doubleSpinBox_v_s1_7,self.ui.doubleSpinBox_sipir_1_s1_7,
                                     self.ui.doubleSpinBox_kesit_s1_7,self.ui.doubleSpinBox_cap_1_s1_7,
                                     self.ui.doubleSpinBox_akim_1_s1_7,self.ui.doubleSpinBox_sipir_2_s1_7,
                                     self.ui.doubleSpinBox_kesit_2_s1_7,self.ui.doubleSpinBox_cap_2_s1_7,
                                     self.ui.doubleSpinBox_akim_2_s1_7,self.ui.comboBox_tel_s1_7,
                                     self.ui.label_kesit_ok_s1_7,self.ui.label_kesit_error_s1_7]
            self.group_list_sva1_82 = [self.ui.doubleSpinBox_v_s1_8,self.ui.doubleSpinBox_sipir_1_s1_8,
                                     self.ui.doubleSpinBox_kesit_s1_8,self.ui.doubleSpinBox_cap_1_s1_8,
                                     self.ui.doubleSpinBox_akim_1_s1_8,self.ui.doubleSpinBox_sipir_2_s1_8,
                                     self.ui.doubleSpinBox_kesit_2_s1_8,self.ui.doubleSpinBox_cap_2_s1_8,
                                     self.ui.doubleSpinBox_akim_2_s1_8,self.ui.comboBox_tel_s1_8,
                                     self.ui.label_kesit_ok_s1_8,self.ui.label_kesit_error_s1_8]     
            self.group_list_sva1_92 = [self.ui.doubleSpinBox_v_s1_9,self.ui.doubleSpinBox_sipir_1_s1_9,
                                     self.ui.doubleSpinBox_kesit_s1_9,self.ui.doubleSpinBox_cap_1_s1_9,
                                     self.ui.doubleSpinBox_akim_1_s1_9,self.ui.doubleSpinBox_sipir_2_s1_9,
                                     self.ui.doubleSpinBox_kesit_2_s1_9,self.ui.doubleSpinBox_cap_2_s1_9,
                                     self.ui.doubleSpinBox_akim_2_s1_9,self.ui.comboBox_tel_s1_9,
                                     self.ui.label_kesit_ok_s1_9,self.ui.label_kesit_error_s1_9] 
            self.group_list_sva1_102 = [self.ui.doubleSpinBox_v_s1_10,self.ui.doubleSpinBox_sipir_1_s1_10,
                                     self.ui.doubleSpinBox_kesit_s1_10,self.ui.doubleSpinBox_cap_1_s1_10,
                                     self.ui.doubleSpinBox_akim_1_s1_10,self.ui.doubleSpinBox_sipir_2_s1_10,
                                     self.ui.doubleSpinBox_kesit_2_s1_10,self.ui.doubleSpinBox_cap_2_s1_10,
                                     self.ui.doubleSpinBox_akim_2_s1_10,self.ui.comboBox_tel_s1_10,
                                     self.ui.label_kesit_ok_s1_10,self.ui.label_kesit_error_s1_10]                                                                                                             
            self.group_name_list_sva1_2 = [self.group_list_sva1_11,self.group_list_sva1_22,self.group_list_sva1_32,
                                        self.group_list_sva1_42,self.group_list_sva1_52,self.group_list_sva1_62,
                                        self.group_list_sva1_72,self.group_list_sva1_82,self.group_list_sva1_92,
                                        self.group_list_sva1_102]
            self.button_list_sva1 = [self.ui.pushButton_buton_s1_1,self.ui.pushButton_buton_s1_2,
                                    self.ui.pushButton_buton_s1_3,self.ui.pushButton_buton_s1_4,
                                    self.ui.pushButton_buton_s1_5,self.ui.pushButton_buton_s1_6,
                                    self.ui.pushButton_buton_s1_7,self.ui.pushButton_buton_s1_8,
                                    self.ui.pushButton_buton_s1_9,self.ui.pushButton_buton_s1_10]

        if self.ui.radioButton_vadagilim.isChecked() or self.ui.comboBox_va.currentIndex()>=0:

            self.group_list_sva2_11 = [self.ui.doubleSpinBox_v_s2_1,self.ui.doubleSpinBox_sipir_1_s2_1,
                                     self.ui.doubleSpinBox_kesit_s2_1,self.ui.doubleSpinBox_cap_1_s2_1,
                                     self.ui.doubleSpinBox_akim_1_s2_1,self.ui.doubleSpinBox_sipir_2_s2_1,
                                     self.ui.doubleSpinBox_kesit_2_s2_1,self.ui.doubleSpinBox_cap_2_s2_1,
                                     self.ui.doubleSpinBox_akim_2_s2_1,self.ui.comboBox_tel_s2_1,
                                     self.ui.label_kesit_ok_s2_1,self.ui.label_kesit_error_s2_1]
            self.group_list_sva2_22 = [self.ui.doubleSpinBox_v_s2_2,self.ui.doubleSpinBox_sipir_1_s2_2,
                                     self.ui.doubleSpinBox_kesit_s2_2,self.ui.doubleSpinBox_cap_1_s2_2,
                                     self.ui.doubleSpinBox_akim_1_s2_2,self.ui.doubleSpinBox_sipir_2_s2_2,
                                     self.ui.doubleSpinBox_kesit_2_s2_2,self.ui.doubleSpinBox_cap_2_s2_2,
                                     self.ui.doubleSpinBox_akim_2_s2_2,self.ui.comboBox_tel_s2_2,
                                     self.ui.label_kesit_ok_s2_2,self.ui.label_kesit_error_s2_2]
            self.group_list_sva2_32 = [self.ui.doubleSpinBox_v_s2_3,self.ui.doubleSpinBox_sipir_1_s2_3,
                                     self.ui.doubleSpinBox_kesit_s2_3,self.ui.doubleSpinBox_cap_1_s2_3,
                                     self.ui.doubleSpinBox_akim_1_s2_3,self.ui.doubleSpinBox_sipir_2_s2_3,
                                     self.ui.doubleSpinBox_kesit_2_s2_3,self.ui.doubleSpinBox_cap_2_s2_3,
                                     self.ui.doubleSpinBox_akim_2_s2_3,self.ui.comboBox_tel_s2_3,
                                     self.ui.label_kesit_ok_s2_3,self.ui.label_kesit_error_s2_3]
            self.group_list_sva2_42 = [self.ui.doubleSpinBox_v_s2_4,self.ui.doubleSpinBox_sipir_1_s2_4,
                                     self.ui.doubleSpinBox_kesit_s2_4,self.ui.doubleSpinBox_cap_1_s2_4,
                                     self.ui.doubleSpinBox_akim_1_s2_4,self.ui.doubleSpinBox_sipir_2_s2_4,
                                     self.ui.doubleSpinBox_kesit_2_s2_4,self.ui.doubleSpinBox_cap_2_s2_4,
                                     self.ui.doubleSpinBox_akim_2_s2_4,self.ui.comboBox_tel_s2_4,
                                     self.ui.label_kesit_ok_s2_4,self.ui.label_kesit_error_s2_4]
            self.group_list_sva2_52 = [self.ui.doubleSpinBox_v_s2_5,self.ui.doubleSpinBox_sipir_1_s2_5,
                                     self.ui.doubleSpinBox_kesit_s2_5,self.ui.doubleSpinBox_cap_1_s2_5,
                                     self.ui.doubleSpinBox_akim_1_s2_5,self.ui.doubleSpinBox_sipir_2_s2_5,
                                     self.ui.doubleSpinBox_kesit_2_s2_5,self.ui.doubleSpinBox_cap_2_s2_5,
                                     self.ui.doubleSpinBox_akim_2_s2_5,self.ui.comboBox_tel_s2_5,
                                     self.ui.label_kesit_ok_s2_5,self.ui.label_kesit_error_s2_5]
            self.group_list_sva2_62 = [self.ui.doubleSpinBox_v_s2_6,self.ui.doubleSpinBox_sipir_1_s2_6,
                                     self.ui.doubleSpinBox_kesit_s2_6,self.ui.doubleSpinBox_cap_1_s2_6,
                                     self.ui.doubleSpinBox_akim_1_s2_6,self.ui.doubleSpinBox_sipir_2_s2_6,
                                     self.ui.doubleSpinBox_kesit_2_s2_6,self.ui.doubleSpinBox_cap_2_s2_6,
                                     self.ui.doubleSpinBox_akim_2_s2_6,self.ui.comboBox_tel_s2_6,
                                     self.ui.label_kesit_ok_s2_6,self.ui.label_kesit_error_s2_6]
            self.group_list_sva2_72 = [self.ui.doubleSpinBox_v_s2_7,self.ui.doubleSpinBox_sipir_1_s2_7,
                                     self.ui.doubleSpinBox_kesit_s2_7,self.ui.doubleSpinBox_cap_1_s2_7,
                                     self.ui.doubleSpinBox_akim_1_s2_7,self.ui.doubleSpinBox_sipir_2_s2_7,
                                     self.ui.doubleSpinBox_kesit_2_s2_7,self.ui.doubleSpinBox_cap_2_s2_7,
                                     self.ui.doubleSpinBox_akim_2_s2_7,self.ui.comboBox_tel_s2_7,
                                     self.ui.label_kesit_ok_s2_7,self.ui.label_kesit_error_s2_7]
            self.group_list_sva2_82 = [self.ui.doubleSpinBox_v_s2_8,self.ui.doubleSpinBox_sipir_1_s2_8,
                                     self.ui.doubleSpinBox_kesit_s2_8,self.ui.doubleSpinBox_cap_1_s2_8,
                                     self.ui.doubleSpinBox_akim_1_s2_8,self.ui.doubleSpinBox_sipir_2_s2_8,
                                     self.ui.doubleSpinBox_kesit_2_s2_8,self.ui.doubleSpinBox_cap_2_s2_8,
                                     self.ui.doubleSpinBox_akim_2_s2_8,self.ui.comboBox_tel_s2_8,
                                     self.ui.label_kesit_ok_s2_8,self.ui.label_kesit_error_s2_8]     
            self.group_list_sva2_92 = [self.ui.doubleSpinBox_v_s2_9,self.ui.doubleSpinBox_sipir_1_s2_9,
                                     self.ui.doubleSpinBox_kesit_s2_9,self.ui.doubleSpinBox_cap_1_s2_9,
                                     self.ui.doubleSpinBox_akim_1_s2_9,self.ui.doubleSpinBox_sipir_2_s2_9,
                                     self.ui.doubleSpinBox_kesit_2_s2_9,self.ui.doubleSpinBox_cap_2_s2_9,
                                     self.ui.doubleSpinBox_akim_2_s2_9,self.ui.comboBox_tel_s2_9,
                                     self.ui.label_kesit_ok_s2_9,self.ui.label_kesit_error_s2_9] 
            self.group_list_sva2_102 = [self.ui.doubleSpinBox_v_s2_10,self.ui.doubleSpinBox_sipir_1_s2_10,
                                     self.ui.doubleSpinBox_kesit_s2_10,self.ui.doubleSpinBox_cap_1_s2_10,
                                     self.ui.doubleSpinBox_akim_1_s2_10,self.ui.doubleSpinBox_sipir_2_s2_10,
                                     self.ui.doubleSpinBox_kesit_2_s2_10,self.ui.doubleSpinBox_cap_2_s2_10,
                                     self.ui.doubleSpinBox_akim_2_s2_10,self.ui.comboBox_tel_s2_10,
                                     self.ui.label_kesit_ok_s2_10,self.ui.label_kesit_error_s2_10]                                                                                                             
            self.group_name_list_sva2_2 = [self.group_list_sva2_11,self.group_list_sva2_22,self.group_list_sva2_32,
                                        self.group_list_sva2_42,self.group_list_sva2_52,self.group_list_sva2_62,
                                        self.group_list_sva2_72,self.group_list_sva2_82,self.group_list_sva2_92,
                                        self.group_list_sva2_102]
            self.button_list_sva2 = [self.ui.pushButton_buton_s2_1,self.ui.pushButton_buton_s2_2,
                                    self.ui.pushButton_buton_s2_3,self.ui.pushButton_buton_s2_4,
                                    self.ui.pushButton_buton_s2_5,self.ui.pushButton_buton_s2_6,
                                    self.ui.pushButton_buton_s2_7,self.ui.pushButton_buton_s2_8,
                                    self.ui.pushButton_buton_s2_9,self.ui.pushButton_buton_s2_10]

        if self.ui.radioButton_vadagilim.isChecked() or self.ui.comboBox_va.currentIndex()>=0:

            self.group_list_sva3_11 = [self.ui.doubleSpinBox_v_s3_1,self.ui.doubleSpinBox_sipir_1_s3_1,
                                     self.ui.doubleSpinBox_kesit_s3_1,self.ui.doubleSpinBox_cap_1_s3_1,
                                     self.ui.doubleSpinBox_akim_1_s3_1,self.ui.doubleSpinBox_sipir_2_s3_1,
                                     self.ui.doubleSpinBox_kesit_2_s3_1,self.ui.doubleSpinBox_cap_2_s3_1,
                                     self.ui.doubleSpinBox_akim_2_s3_1,self.ui.comboBox_tel_s3_1,
                                     self.ui.label_kesit_ok_s3_1,self.ui.label_kesit_error_s3_1]
            self.group_list_sva3_22 = [self.ui.doubleSpinBox_v_s3_2,self.ui.doubleSpinBox_sipir_1_s3_2,
                                     self.ui.doubleSpinBox_kesit_s3_2,self.ui.doubleSpinBox_cap_1_s3_2,
                                     self.ui.doubleSpinBox_akim_1_s3_2,self.ui.doubleSpinBox_sipir_2_s3_2,
                                     self.ui.doubleSpinBox_kesit_2_s3_2,self.ui.doubleSpinBox_cap_2_s3_2,
                                     self.ui.doubleSpinBox_akim_2_s3_2,self.ui.comboBox_tel_s3_2,
                                     self.ui.label_kesit_ok_s3_2,self.ui.label_kesit_error_s3_2]
            self.group_list_sva3_32 = [self.ui.doubleSpinBox_v_s3_3,self.ui.doubleSpinBox_sipir_1_s3_3,
                                     self.ui.doubleSpinBox_kesit_s3_3,self.ui.doubleSpinBox_cap_1_s3_3,
                                     self.ui.doubleSpinBox_akim_1_s3_3,self.ui.doubleSpinBox_sipir_2_s3_3,
                                     self.ui.doubleSpinBox_kesit_2_s3_3,self.ui.doubleSpinBox_cap_2_s3_3,
                                     self.ui.doubleSpinBox_akim_2_s3_3,self.ui.comboBox_tel_s3_3,
                                     self.ui.label_kesit_ok_s3_3,self.ui.label_kesit_error_s3_3]
            self.group_list_sva3_42 = [self.ui.doubleSpinBox_v_s3_4,self.ui.doubleSpinBox_sipir_1_s3_4,
                                     self.ui.doubleSpinBox_kesit_s3_4,self.ui.doubleSpinBox_cap_1_s3_4,
                                     self.ui.doubleSpinBox_akim_1_s3_4,self.ui.doubleSpinBox_sipir_2_s3_4,
                                     self.ui.doubleSpinBox_kesit_2_s3_4,self.ui.doubleSpinBox_cap_2_s3_4,
                                     self.ui.doubleSpinBox_akim_2_s3_4,self.ui.comboBox_tel_s3_4,
                                     self.ui.label_kesit_ok_s3_4,self.ui.label_kesit_error_s3_4]
            self.group_list_sva3_52 = [self.ui.doubleSpinBox_v_s3_5,self.ui.doubleSpinBox_sipir_1_s3_5,
                                     self.ui.doubleSpinBox_kesit_s3_5,self.ui.doubleSpinBox_cap_1_s3_5,
                                     self.ui.doubleSpinBox_akim_1_s3_5,self.ui.doubleSpinBox_sipir_2_s3_5,
                                     self.ui.doubleSpinBox_kesit_2_s3_5,self.ui.doubleSpinBox_cap_2_s3_5,
                                     self.ui.doubleSpinBox_akim_2_s3_5,self.ui.comboBox_tel_s3_5,
                                     self.ui.label_kesit_ok_s3_5,self.ui.label_kesit_error_s3_5]
            self.group_list_sva3_62 = [self.ui.doubleSpinBox_v_s3_6,self.ui.doubleSpinBox_sipir_1_s3_6,
                                     self.ui.doubleSpinBox_kesit_s3_6,self.ui.doubleSpinBox_cap_1_s3_6,
                                     self.ui.doubleSpinBox_akim_1_s3_6,self.ui.doubleSpinBox_sipir_2_s3_6,
                                     self.ui.doubleSpinBox_kesit_2_s3_6,self.ui.doubleSpinBox_cap_2_s3_6,
                                     self.ui.doubleSpinBox_akim_2_s3_6,self.ui.comboBox_tel_s3_6,
                                     self.ui.label_kesit_ok_s3_6,self.ui.label_kesit_error_s3_6]
            self.group_list_sva3_72 = [self.ui.doubleSpinBox_v_s3_7,self.ui.doubleSpinBox_sipir_1_s3_7,
                                     self.ui.doubleSpinBox_kesit_s3_7,self.ui.doubleSpinBox_cap_1_s3_7,
                                     self.ui.doubleSpinBox_akim_1_s3_7,self.ui.doubleSpinBox_sipir_2_s3_7,
                                     self.ui.doubleSpinBox_kesit_2_s3_7,self.ui.doubleSpinBox_cap_2_s3_7,
                                     self.ui.doubleSpinBox_akim_2_s3_7,self.ui.comboBox_tel_s3_7,
                                     self.ui.label_kesit_ok_s3_7,self.ui.label_kesit_error_s3_7]
            self.group_list_sva3_82 = [self.ui.doubleSpinBox_v_s3_8,self.ui.doubleSpinBox_sipir_1_s3_8,
                                     self.ui.doubleSpinBox_kesit_s3_8,self.ui.doubleSpinBox_cap_1_s3_8,
                                     self.ui.doubleSpinBox_akim_1_s3_8,self.ui.doubleSpinBox_sipir_2_s3_8,
                                     self.ui.doubleSpinBox_kesit_2_s3_8,self.ui.doubleSpinBox_cap_2_s3_8,
                                     self.ui.doubleSpinBox_akim_2_s3_8,self.ui.comboBox_tel_s3_8,
                                     self.ui.label_kesit_ok_s3_8,self.ui.label_kesit_error_s3_8]     
            self.group_list_sva3_92 = [self.ui.doubleSpinBox_v_s3_9,self.ui.doubleSpinBox_sipir_1_s3_9,
                                     self.ui.doubleSpinBox_kesit_s3_9,self.ui.doubleSpinBox_cap_1_s3_9,
                                     self.ui.doubleSpinBox_akim_1_s3_9,self.ui.doubleSpinBox_sipir_2_s3_9,
                                     self.ui.doubleSpinBox_kesit_2_s3_9,self.ui.doubleSpinBox_cap_2_s3_9,
                                     self.ui.doubleSpinBox_akim_2_s3_9,self.ui.comboBox_tel_s3_9,
                                     self.ui.label_kesit_ok_s3_9,self.ui.label_kesit_error_s3_9] 
            self.group_list_sva3_102 = [self.ui.doubleSpinBox_v_s3_10,self.ui.doubleSpinBox_sipir_1_s3_10,
                                     self.ui.doubleSpinBox_kesit_s3_10,self.ui.doubleSpinBox_cap_1_s3_10,
                                     self.ui.doubleSpinBox_akim_1_s3_10,self.ui.doubleSpinBox_sipir_2_s3_10,
                                     self.ui.doubleSpinBox_kesit_2_s3_10,self.ui.doubleSpinBox_cap_2_s3_10,
                                     self.ui.doubleSpinBox_akim_2_s3_10,self.ui.comboBox_tel_s3_10,
                                     self.ui.label_kesit_ok_s3_10,self.ui.label_kesit_error_s3_10]                                                                                                             
            self.group_name_list_sva3_2 = [self.group_list_sva3_11,self.group_list_sva3_22,self.group_list_sva3_32,
                                        self.group_list_sva3_42,self.group_list_sva3_52,self.group_list_sva3_62,
                                        self.group_list_sva3_72,self.group_list_sva3_82,self.group_list_sva3_92,
                                        self.group_list_sva3_102]
            self.button_list_sva3 = [self.ui.pushButton_buton_s3_1,self.ui.pushButton_buton_s3_2,
                                    self.ui.pushButton_buton_s3_3,self.ui.pushButton_buton_s3_4,
                                    self.ui.pushButton_buton_s3_5,self.ui.pushButton_buton_s3_6,
                                    self.ui.pushButton_buton_s3_7,self.ui.pushButton_buton_s3_8,
                                    self.ui.pushButton_buton_s3_9,self.ui.pushButton_buton_s3_10]

        if self.ui.radioButton_vadagilim.isChecked() or self.ui.comboBox_va.currentIndex()>=0:

            self.group_list_sva4_11 = [self.ui.doubleSpinBox_v_s4_1,self.ui.doubleSpinBox_sipir_1_s4_1,
                                     self.ui.doubleSpinBox_kesit_s4_1,self.ui.doubleSpinBox_cap_1_s4_1,
                                     self.ui.doubleSpinBox_akim_1_s4_1,self.ui.doubleSpinBox_sipir_2_s4_1,
                                     self.ui.doubleSpinBox_kesit_2_s4_1,self.ui.doubleSpinBox_cap_2_s4_1,
                                     self.ui.doubleSpinBox_akim_2_s4_1,self.ui.comboBox_tel_s4_1,
                                     self.ui.label_kesit_ok_s4_1,self.ui.label_kesit_error_s4_1]
            self.group_list_sva4_22 = [self.ui.doubleSpinBox_v_s4_2,self.ui.doubleSpinBox_sipir_1_s4_2,
                                     self.ui.doubleSpinBox_kesit_s4_2,self.ui.doubleSpinBox_cap_1_s4_2,
                                     self.ui.doubleSpinBox_akim_1_s4_2,self.ui.doubleSpinBox_sipir_2_s4_2,
                                     self.ui.doubleSpinBox_kesit_2_s4_2,self.ui.doubleSpinBox_cap_2_s4_2,
                                     self.ui.doubleSpinBox_akim_2_s4_2,self.ui.comboBox_tel_s4_2,
                                     self.ui.label_kesit_ok_s4_2,self.ui.label_kesit_error_s4_2]
            self.group_list_sva4_32 = [self.ui.doubleSpinBox_v_s4_3,self.ui.doubleSpinBox_sipir_1_s4_3,
                                     self.ui.doubleSpinBox_kesit_s4_3,self.ui.doubleSpinBox_cap_1_s4_3,
                                     self.ui.doubleSpinBox_akim_1_s4_3,self.ui.doubleSpinBox_sipir_2_s4_3,
                                     self.ui.doubleSpinBox_kesit_2_s4_3,self.ui.doubleSpinBox_cap_2_s4_3,
                                     self.ui.doubleSpinBox_akim_2_s4_3,self.ui.comboBox_tel_s4_3,
                                     self.ui.label_kesit_ok_s4_3,self.ui.label_kesit_error_s4_3]
            self.group_list_sva4_42 = [self.ui.doubleSpinBox_v_s4_4,self.ui.doubleSpinBox_sipir_1_s4_4,
                                     self.ui.doubleSpinBox_kesit_s4_4,self.ui.doubleSpinBox_cap_1_s4_4,
                                     self.ui.doubleSpinBox_akim_1_s4_4,self.ui.doubleSpinBox_sipir_2_s4_4,
                                     self.ui.doubleSpinBox_kesit_2_s4_4,self.ui.doubleSpinBox_cap_2_s4_4,
                                     self.ui.doubleSpinBox_akim_2_s4_4,self.ui.comboBox_tel_s4_4,
                                     self.ui.label_kesit_ok_s4_4,self.ui.label_kesit_error_s4_4]
            self.group_list_sva4_52 = [self.ui.doubleSpinBox_v_s4_5,self.ui.doubleSpinBox_sipir_1_s4_5,
                                     self.ui.doubleSpinBox_kesit_s4_5,self.ui.doubleSpinBox_cap_1_s4_5,
                                     self.ui.doubleSpinBox_akim_1_s4_5,self.ui.doubleSpinBox_sipir_2_s4_5,
                                     self.ui.doubleSpinBox_kesit_2_s4_5,self.ui.doubleSpinBox_cap_2_s4_5,
                                     self.ui.doubleSpinBox_akim_2_s4_5,self.ui.comboBox_tel_s4_5,
                                     self.ui.label_kesit_ok_s4_5,self.ui.label_kesit_error_s4_5]
            self.group_list_sva4_62 = [self.ui.doubleSpinBox_v_s4_6,self.ui.doubleSpinBox_sipir_1_s4_6,
                                     self.ui.doubleSpinBox_kesit_s4_6,self.ui.doubleSpinBox_cap_1_s4_6,
                                     self.ui.doubleSpinBox_akim_1_s4_6,self.ui.doubleSpinBox_sipir_2_s4_6,
                                     self.ui.doubleSpinBox_kesit_2_s4_6,self.ui.doubleSpinBox_cap_2_s4_6,
                                     self.ui.doubleSpinBox_akim_2_s4_6,self.ui.comboBox_tel_s4_6,
                                     self.ui.label_kesit_ok_s4_6,self.ui.label_kesit_error_s4_6]
            self.group_list_sva4_72 = [self.ui.doubleSpinBox_v_s4_7,self.ui.doubleSpinBox_sipir_1_s4_7,
                                     self.ui.doubleSpinBox_kesit_s4_7,self.ui.doubleSpinBox_cap_1_s4_7,
                                     self.ui.doubleSpinBox_akim_1_s4_7,self.ui.doubleSpinBox_sipir_2_s4_7,
                                     self.ui.doubleSpinBox_kesit_2_s4_7,self.ui.doubleSpinBox_cap_2_s4_7,
                                     self.ui.doubleSpinBox_akim_2_s4_7,self.ui.comboBox_tel_s4_7,
                                     self.ui.label_kesit_ok_s4_7,self.ui.label_kesit_error_s4_7]
            self.group_list_sva4_82 = [self.ui.doubleSpinBox_v_s4_8,self.ui.doubleSpinBox_sipir_1_s4_8,
                                     self.ui.doubleSpinBox_kesit_s4_8,self.ui.doubleSpinBox_cap_1_s4_8,
                                     self.ui.doubleSpinBox_akim_1_s4_8,self.ui.doubleSpinBox_sipir_2_s4_8,
                                     self.ui.doubleSpinBox_kesit_2_s4_8,self.ui.doubleSpinBox_cap_2_s4_8,
                                     self.ui.doubleSpinBox_akim_2_s4_8,self.ui.comboBox_tel_s4_8,
                                     self.ui.label_kesit_ok_s4_8,self.ui.label_kesit_error_s4_8]     
            self.group_list_sva4_92 = [self.ui.doubleSpinBox_v_s4_9,self.ui.doubleSpinBox_sipir_1_s4_9,
                                     self.ui.doubleSpinBox_kesit_s4_9,self.ui.doubleSpinBox_cap_1_s4_9,
                                     self.ui.doubleSpinBox_akim_1_s4_9,self.ui.doubleSpinBox_sipir_2_s4_9,
                                     self.ui.doubleSpinBox_kesit_2_s4_9,self.ui.doubleSpinBox_cap_2_s4_9,
                                     self.ui.doubleSpinBox_akim_2_s4_9,self.ui.comboBox_tel_s4_9,
                                     self.ui.label_kesit_ok_s4_9,self.ui.label_kesit_error_s4_9] 
            self.group_list_sva4_102 = [self.ui.doubleSpinBox_v_s4_10,self.ui.doubleSpinBox_sipir_1_s4_10,
                                     self.ui.doubleSpinBox_kesit_s4_10,self.ui.doubleSpinBox_cap_1_s4_10,
                                     self.ui.doubleSpinBox_akim_1_s4_10,self.ui.doubleSpinBox_sipir_2_s4_10,
                                     self.ui.doubleSpinBox_kesit_2_s4_10,self.ui.doubleSpinBox_cap_2_s4_10,
                                     self.ui.doubleSpinBox_akim_2_s4_10,self.ui.comboBox_tel_s4_10,
                                     self.ui.label_kesit_ok_s4_10,self.ui.label_kesit_error_s4_10]                                                                                                             
            self.group_name_list_sva4_2 = [self.group_list_sva4_11,self.group_list_sva4_22,self.group_list_sva4_32,
                                        self.group_list_sva4_42,self.group_list_sva4_52,self.group_list_sva4_62,
                                        self.group_list_sva4_72,self.group_list_sva4_82,self.group_list_sva4_92,
                                        self.group_list_sva4_102]
            self.button_list_sva4 = [self.ui.pushButton_buton_s4_1,self.ui.pushButton_buton_s4_2,
                                    self.ui.pushButton_buton_s4_3,self.ui.pushButton_buton_s4_4,
                                    self.ui.pushButton_buton_s4_5,self.ui.pushButton_buton_s4_6,
                                    self.ui.pushButton_buton_s4_7,self.ui.pushButton_buton_s4_8,
                                    self.ui.pushButton_buton_s4_9,self.ui.pushButton_buton_s4_10]

        if self.ui.radioButton_vadagilim.isChecked() or self.ui.comboBox_va.currentIndex()>=0:

            self.group_list_sva5_11 = [self.ui.doubleSpinBox_v_s5_1,self.ui.doubleSpinBox_sipir_1_s5_1,
                                     self.ui.doubleSpinBox_kesit_s5_1,self.ui.doubleSpinBox_cap_1_s5_1,
                                     self.ui.doubleSpinBox_akim_1_s5_1,self.ui.doubleSpinBox_sipir_2_s5_1,
                                     self.ui.doubleSpinBox_kesit_2_s5_1,self.ui.doubleSpinBox_cap_2_s5_1,
                                     self.ui.doubleSpinBox_akim_2_s5_1,self.ui.comboBox_tel_s5_1,
                                     self.ui.label_kesit_ok_s5_1,self.ui.label_kesit_error_s5_1]
            self.group_list_sva5_22 = [self.ui.doubleSpinBox_v_s5_2,self.ui.doubleSpinBox_sipir_1_s5_2,
                                     self.ui.doubleSpinBox_kesit_s5_2,self.ui.doubleSpinBox_cap_1_s5_2,
                                     self.ui.doubleSpinBox_akim_1_s5_2,self.ui.doubleSpinBox_sipir_2_s5_2,
                                     self.ui.doubleSpinBox_kesit_2_s5_2,self.ui.doubleSpinBox_cap_2_s5_2,
                                     self.ui.doubleSpinBox_akim_2_s5_2,self.ui.comboBox_tel_s5_2,
                                     self.ui.label_kesit_ok_s5_2,self.ui.label_kesit_error_s5_2]
            self.group_list_sva5_32 = [self.ui.doubleSpinBox_v_s5_3,self.ui.doubleSpinBox_sipir_1_s5_3,
                                     self.ui.doubleSpinBox_kesit_s5_3,self.ui.doubleSpinBox_cap_1_s5_3,
                                     self.ui.doubleSpinBox_akim_1_s5_3,self.ui.doubleSpinBox_sipir_2_s5_3,
                                     self.ui.doubleSpinBox_kesit_2_s5_3,self.ui.doubleSpinBox_cap_2_s5_3,
                                     self.ui.doubleSpinBox_akim_2_s5_3,self.ui.comboBox_tel_s5_3,
                                     self.ui.label_kesit_ok_s5_3,self.ui.label_kesit_error_s5_3]
            self.group_list_sva5_42 = [self.ui.doubleSpinBox_v_s5_4,self.ui.doubleSpinBox_sipir_1_s5_4,
                                     self.ui.doubleSpinBox_kesit_s5_4,self.ui.doubleSpinBox_cap_1_s5_4,
                                     self.ui.doubleSpinBox_akim_1_s5_4,self.ui.doubleSpinBox_sipir_2_s5_4,
                                     self.ui.doubleSpinBox_kesit_2_s5_4,self.ui.doubleSpinBox_cap_2_s5_4,
                                     self.ui.doubleSpinBox_akim_2_s5_4,self.ui.comboBox_tel_s5_4,
                                     self.ui.label_kesit_ok_s5_4,self.ui.label_kesit_error_s5_4]
            self.group_list_sva5_52 = [self.ui.doubleSpinBox_v_s5_5,self.ui.doubleSpinBox_sipir_1_s5_5,
                                     self.ui.doubleSpinBox_kesit_s5_5,self.ui.doubleSpinBox_cap_1_s5_5,
                                     self.ui.doubleSpinBox_akim_1_s5_5,self.ui.doubleSpinBox_sipir_2_s5_5,
                                     self.ui.doubleSpinBox_kesit_2_s5_5,self.ui.doubleSpinBox_cap_2_s5_5,
                                     self.ui.doubleSpinBox_akim_2_s5_5,self.ui.comboBox_tel_s5_5,
                                     self.ui.label_kesit_ok_s5_5,self.ui.label_kesit_error_s5_5]
            self.group_list_sva5_62 = [self.ui.doubleSpinBox_v_s5_6,self.ui.doubleSpinBox_sipir_1_s5_6,
                                     self.ui.doubleSpinBox_kesit_s5_6,self.ui.doubleSpinBox_cap_1_s5_6,
                                     self.ui.doubleSpinBox_akim_1_s5_6,self.ui.doubleSpinBox_sipir_2_s5_6,
                                     self.ui.doubleSpinBox_kesit_2_s5_6,self.ui.doubleSpinBox_cap_2_s5_6,
                                     self.ui.doubleSpinBox_akim_2_s5_6,self.ui.comboBox_tel_s5_6,
                                     self.ui.label_kesit_ok_s5_6,self.ui.label_kesit_error_s5_6]
            self.group_list_sva5_72 = [self.ui.doubleSpinBox_v_s5_7,self.ui.doubleSpinBox_sipir_1_s5_7,
                                     self.ui.doubleSpinBox_kesit_s5_7,self.ui.doubleSpinBox_cap_1_s5_7,
                                     self.ui.doubleSpinBox_akim_1_s5_7,self.ui.doubleSpinBox_sipir_2_s5_7,
                                     self.ui.doubleSpinBox_kesit_2_s5_7,self.ui.doubleSpinBox_cap_2_s5_7,
                                     self.ui.doubleSpinBox_akim_2_s5_7,self.ui.comboBox_tel_s5_7,
                                     self.ui.label_kesit_ok_s5_7,self.ui.label_kesit_error_s5_7]
            self.group_list_sva5_82 = [self.ui.doubleSpinBox_v_s5_8,self.ui.doubleSpinBox_sipir_1_s5_8,
                                     self.ui.doubleSpinBox_kesit_s5_8,self.ui.doubleSpinBox_cap_1_s5_8,
                                     self.ui.doubleSpinBox_akim_1_s5_8,self.ui.doubleSpinBox_sipir_2_s5_8,
                                     self.ui.doubleSpinBox_kesit_2_s5_8,self.ui.doubleSpinBox_cap_2_s5_8,
                                     self.ui.doubleSpinBox_akim_2_s5_8,self.ui.comboBox_tel_s5_8,
                                     self.ui.label_kesit_ok_s5_8,self.ui.label_kesit_error_s5_8]     
            self.group_list_sva5_92 = [self.ui.doubleSpinBox_v_s5_9,self.ui.doubleSpinBox_sipir_1_s5_9,
                                     self.ui.doubleSpinBox_kesit_s5_9,self.ui.doubleSpinBox_cap_1_s5_9,
                                     self.ui.doubleSpinBox_akim_1_s5_9,self.ui.doubleSpinBox_sipir_2_s5_9,
                                     self.ui.doubleSpinBox_kesit_2_s5_9,self.ui.doubleSpinBox_cap_2_s5_9,
                                     self.ui.doubleSpinBox_akim_2_s5_9,self.ui.comboBox_tel_s5_9,
                                     self.ui.label_kesit_ok_s5_9,self.ui.label_kesit_error_s5_9] 
            self.group_list_sva5_102 = [self.ui.doubleSpinBox_v_s5_10,self.ui.doubleSpinBox_sipir_1_s5_10,
                                     self.ui.doubleSpinBox_kesit_s5_10,self.ui.doubleSpinBox_cap_1_s5_10,
                                     self.ui.doubleSpinBox_akim_1_s5_10,self.ui.doubleSpinBox_sipir_2_s5_10,
                                     self.ui.doubleSpinBox_kesit_2_s5_10,self.ui.doubleSpinBox_cap_2_s5_10,
                                     self.ui.doubleSpinBox_akim_2_s5_10,self.ui.comboBox_tel_s5_10,
                                     self.ui.label_kesit_ok_s5_10,self.ui.label_kesit_error_s5_10]                                                                                                             
            self.group_name_list_sva5_2 = [self.group_list_sva5_11,self.group_list_sva5_22,self.group_list_sva5_32,
                                        self.group_list_sva5_42,self.group_list_sva5_52,self.group_list_sva5_62,
                                        self.group_list_sva5_72,self.group_list_sva5_82,self.group_list_sva5_92,
                                        self.group_list_sva5_102]
            self.button_list_sva5 = [self.ui.pushButton_buton_s5_1,self.ui.pushButton_buton_s5_2,
                                    self.ui.pushButton_buton_s5_3,self.ui.pushButton_buton_s5_4,
                                    self.ui.pushButton_buton_s5_5,self.ui.pushButton_buton_s5_6,
                                    self.ui.pushButton_buton_s5_7,self.ui.pushButton_buton_s5_8,
                                    self.ui.pushButton_buton_s5_9,self.ui.pushButton_buton_s5_10]

        if self.ui.radioButton_vadagilim.isChecked() or self.ui.comboBox_va.currentIndex()>=0:

            self.group_list_sva6_11 = [self.ui.doubleSpinBox_v_s6_1,self.ui.doubleSpinBox_sipir_1_s6_1,
                                     self.ui.doubleSpinBox_kesit_s6_1,self.ui.doubleSpinBox_cap_1_s6_1,
                                     self.ui.doubleSpinBox_akim_1_s6_1,self.ui.doubleSpinBox_sipir_2_s6_1,
                                     self.ui.doubleSpinBox_kesit_2_s6_1,self.ui.doubleSpinBox_cap_2_s6_1,
                                     self.ui.doubleSpinBox_akim_2_s6_1,self.ui.comboBox_tel_s6_1,
                                     self.ui.label_kesit_ok_s6_1,self.ui.label_kesit_error_s6_1]
            self.group_list_sva6_22 = [self.ui.doubleSpinBox_v_s6_2,self.ui.doubleSpinBox_sipir_1_s6_2,
                                     self.ui.doubleSpinBox_kesit_s6_2,self.ui.doubleSpinBox_cap_1_s6_2,
                                     self.ui.doubleSpinBox_akim_1_s6_2,self.ui.doubleSpinBox_sipir_2_s6_2,
                                     self.ui.doubleSpinBox_kesit_2_s6_2,self.ui.doubleSpinBox_cap_2_s6_2,
                                     self.ui.doubleSpinBox_akim_2_s6_2,self.ui.comboBox_tel_s6_2,
                                     self.ui.label_kesit_ok_s6_2,self.ui.label_kesit_error_s6_2]
            self.group_list_sva6_32 = [self.ui.doubleSpinBox_v_s6_3,self.ui.doubleSpinBox_sipir_1_s6_3,
                                     self.ui.doubleSpinBox_kesit_s6_3,self.ui.doubleSpinBox_cap_1_s6_3,
                                     self.ui.doubleSpinBox_akim_1_s6_3,self.ui.doubleSpinBox_sipir_2_s6_3,
                                     self.ui.doubleSpinBox_kesit_2_s6_3,self.ui.doubleSpinBox_cap_2_s6_3,
                                     self.ui.doubleSpinBox_akim_2_s6_3,self.ui.comboBox_tel_s6_3,
                                     self.ui.label_kesit_ok_s6_3,self.ui.label_kesit_error_s6_3]
            self.group_list_sva6_42 = [self.ui.doubleSpinBox_v_s6_4,self.ui.doubleSpinBox_sipir_1_s6_4,
                                     self.ui.doubleSpinBox_kesit_s6_4,self.ui.doubleSpinBox_cap_1_s6_4,
                                     self.ui.doubleSpinBox_akim_1_s6_4,self.ui.doubleSpinBox_sipir_2_s6_4,
                                     self.ui.doubleSpinBox_kesit_2_s6_4,self.ui.doubleSpinBox_cap_2_s6_4,
                                     self.ui.doubleSpinBox_akim_2_s6_4,self.ui.comboBox_tel_s6_4,
                                     self.ui.label_kesit_ok_s6_4,self.ui.label_kesit_error_s6_4]
            self.group_list_sva6_52 = [self.ui.doubleSpinBox_v_s6_5,self.ui.doubleSpinBox_sipir_1_s6_5,
                                     self.ui.doubleSpinBox_kesit_s6_5,self.ui.doubleSpinBox_cap_1_s6_5,
                                     self.ui.doubleSpinBox_akim_1_s6_5,self.ui.doubleSpinBox_sipir_2_s6_5,
                                     self.ui.doubleSpinBox_kesit_2_s6_5,self.ui.doubleSpinBox_cap_2_s6_5,
                                     self.ui.doubleSpinBox_akim_2_s6_5,self.ui.comboBox_tel_s6_5,
                                     self.ui.label_kesit_ok_s6_5,self.ui.label_kesit_error_s6_5]
            self.group_list_sva6_62 = [self.ui.doubleSpinBox_v_s6_6,self.ui.doubleSpinBox_sipir_1_s6_6,
                                     self.ui.doubleSpinBox_kesit_s6_6,self.ui.doubleSpinBox_cap_1_s6_6,
                                     self.ui.doubleSpinBox_akim_1_s6_6,self.ui.doubleSpinBox_sipir_2_s6_6,
                                     self.ui.doubleSpinBox_kesit_2_s6_6,self.ui.doubleSpinBox_cap_2_s6_6,
                                     self.ui.doubleSpinBox_akim_2_s6_6,self.ui.comboBox_tel_s6_6,
                                     self.ui.label_kesit_ok_s6_6,self.ui.label_kesit_error_s6_6]
            self.group_list_sva6_72 = [self.ui.doubleSpinBox_v_s6_7,self.ui.doubleSpinBox_sipir_1_s6_7,
                                     self.ui.doubleSpinBox_kesit_s6_7,self.ui.doubleSpinBox_cap_1_s6_7,
                                     self.ui.doubleSpinBox_akim_1_s6_7,self.ui.doubleSpinBox_sipir_2_s6_7,
                                     self.ui.doubleSpinBox_kesit_2_s6_7,self.ui.doubleSpinBox_cap_2_s6_7,
                                     self.ui.doubleSpinBox_akim_2_s6_7,self.ui.comboBox_tel_s6_7,
                                     self.ui.label_kesit_ok_s6_7,self.ui.label_kesit_error_s6_7]
            self.group_list_sva6_82 = [self.ui.doubleSpinBox_v_s6_8,self.ui.doubleSpinBox_sipir_1_s6_8,
                                     self.ui.doubleSpinBox_kesit_s6_8,self.ui.doubleSpinBox_cap_1_s6_8,
                                     self.ui.doubleSpinBox_akim_1_s6_8,self.ui.doubleSpinBox_sipir_2_s6_8,
                                     self.ui.doubleSpinBox_kesit_2_s6_8,self.ui.doubleSpinBox_cap_2_s6_8,
                                     self.ui.doubleSpinBox_akim_2_s6_8,self.ui.comboBox_tel_s6_8,
                                     self.ui.label_kesit_ok_s6_8,self.ui.label_kesit_error_s6_8]     
            self.group_list_sva6_92 = [self.ui.doubleSpinBox_v_s6_9,self.ui.doubleSpinBox_sipir_1_s6_9,
                                     self.ui.doubleSpinBox_kesit_s6_9,self.ui.doubleSpinBox_cap_1_s6_9,
                                     self.ui.doubleSpinBox_akim_1_s6_9,self.ui.doubleSpinBox_sipir_2_s6_9,
                                     self.ui.doubleSpinBox_kesit_2_s6_9,self.ui.doubleSpinBox_cap_2_s6_9,
                                     self.ui.doubleSpinBox_akim_2_s6_9,self.ui.comboBox_tel_s6_9,
                                     self.ui.label_kesit_ok_s6_9,self.ui.label_kesit_error_s6_9] 
            self.group_list_sva6_102 = [self.ui.doubleSpinBox_v_s6_10,self.ui.doubleSpinBox_sipir_1_s6_10,
                                     self.ui.doubleSpinBox_kesit_s6_10,self.ui.doubleSpinBox_cap_1_s6_10,
                                     self.ui.doubleSpinBox_akim_1_s6_10,self.ui.doubleSpinBox_sipir_2_s6_10,
                                     self.ui.doubleSpinBox_kesit_2_s6_10,self.ui.doubleSpinBox_cap_2_s6_10,
                                     self.ui.doubleSpinBox_akim_2_s6_10,self.ui.comboBox_tel_s6_10,
                                     self.ui.label_kesit_ok_s6_10,self.ui.label_kesit_error_s6_10]                                                                                                             
            self.group_name_list_sva6_2 = [self.group_list_sva6_11,self.group_list_sva6_22,self.group_list_sva6_32,
                                        self.group_list_sva6_42,self.group_list_sva6_52,self.group_list_sva6_62,
                                        self.group_list_sva6_72,self.group_list_sva6_82,self.group_list_sva6_92,
                                        self.group_list_sva6_102]
            self.button_list_sva6 = [self.ui.pushButton_buton_s6_1,self.ui.pushButton_buton_s6_2,
                                    self.ui.pushButton_buton_s6_3,self.ui.pushButton_buton_s6_4,
                                    self.ui.pushButton_buton_s6_5,self.ui.pushButton_buton_s6_6,
                                    self.ui.pushButton_buton_s6_7,self.ui.pushButton_buton_s6_8,
                                    self.ui.pushButton_buton_s6_9,self.ui.pushButton_buton_s6_10]

        if self.ui.radioButton_vadagilim.isChecked() or self.ui.comboBox_va.currentIndex()>=0:

            self.group_list_sva7_11 = [self.ui.doubleSpinBox_v_s7_1,self.ui.doubleSpinBox_sipir_1_s7_1,
                                     self.ui.doubleSpinBox_kesit_s7_1,self.ui.doubleSpinBox_cap_1_s7_1,
                                     self.ui.doubleSpinBox_akim_1_s7_1,self.ui.doubleSpinBox_sipir_2_s7_1,
                                     self.ui.doubleSpinBox_kesit_2_s7_1,self.ui.doubleSpinBox_cap_2_s7_1,
                                     self.ui.doubleSpinBox_akim_2_s7_1,self.ui.comboBox_tel_s7_1,
                                     self.ui.label_kesit_ok_s7_1,self.ui.label_kesit_error_s7_1]
            self.group_list_sva7_22 = [self.ui.doubleSpinBox_v_s7_2,self.ui.doubleSpinBox_sipir_1_s7_2,
                                     self.ui.doubleSpinBox_kesit_s7_2,self.ui.doubleSpinBox_cap_1_s7_2,
                                     self.ui.doubleSpinBox_akim_1_s7_2,self.ui.doubleSpinBox_sipir_2_s7_2,
                                     self.ui.doubleSpinBox_kesit_2_s7_2,self.ui.doubleSpinBox_cap_2_s7_2,
                                     self.ui.doubleSpinBox_akim_2_s7_2,self.ui.comboBox_tel_s7_2,
                                     self.ui.label_kesit_ok_s7_2,self.ui.label_kesit_error_s7_2]
            self.group_list_sva7_32 = [self.ui.doubleSpinBox_v_s7_3,self.ui.doubleSpinBox_sipir_1_s7_3,
                                     self.ui.doubleSpinBox_kesit_s7_3,self.ui.doubleSpinBox_cap_1_s7_3,
                                     self.ui.doubleSpinBox_akim_1_s7_3,self.ui.doubleSpinBox_sipir_2_s7_3,
                                     self.ui.doubleSpinBox_kesit_2_s7_3,self.ui.doubleSpinBox_cap_2_s7_3,
                                     self.ui.doubleSpinBox_akim_2_s7_3,self.ui.comboBox_tel_s7_3,
                                     self.ui.label_kesit_ok_s7_3,self.ui.label_kesit_error_s7_3]
            self.group_list_sva7_42 = [self.ui.doubleSpinBox_v_s7_4,self.ui.doubleSpinBox_sipir_1_s7_4,
                                     self.ui.doubleSpinBox_kesit_s7_4,self.ui.doubleSpinBox_cap_1_s7_4,
                                     self.ui.doubleSpinBox_akim_1_s7_4,self.ui.doubleSpinBox_sipir_2_s7_4,
                                     self.ui.doubleSpinBox_kesit_2_s7_4,self.ui.doubleSpinBox_cap_2_s7_4,
                                     self.ui.doubleSpinBox_akim_2_s7_4,self.ui.comboBox_tel_s7_4,
                                     self.ui.label_kesit_ok_s7_4,self.ui.label_kesit_error_s7_4]
            self.group_list_sva7_52 = [self.ui.doubleSpinBox_v_s7_5,self.ui.doubleSpinBox_sipir_1_s7_5,
                                     self.ui.doubleSpinBox_kesit_s7_5,self.ui.doubleSpinBox_cap_1_s7_5,
                                     self.ui.doubleSpinBox_akim_1_s7_5,self.ui.doubleSpinBox_sipir_2_s7_5,
                                     self.ui.doubleSpinBox_kesit_2_s7_5,self.ui.doubleSpinBox_cap_2_s7_5,
                                     self.ui.doubleSpinBox_akim_2_s7_5,self.ui.comboBox_tel_s7_5,
                                     self.ui.label_kesit_ok_s7_5,self.ui.label_kesit_error_s7_5]
            self.group_list_sva7_62 = [self.ui.doubleSpinBox_v_s7_6,self.ui.doubleSpinBox_sipir_1_s7_6,
                                     self.ui.doubleSpinBox_kesit_s7_6,self.ui.doubleSpinBox_cap_1_s7_6,
                                     self.ui.doubleSpinBox_akim_1_s7_6,self.ui.doubleSpinBox_sipir_2_s7_6,
                                     self.ui.doubleSpinBox_kesit_2_s7_6,self.ui.doubleSpinBox_cap_2_s7_6,
                                     self.ui.doubleSpinBox_akim_2_s7_6,self.ui.comboBox_tel_s7_6,
                                     self.ui.label_kesit_ok_s7_6,self.ui.label_kesit_error_s7_6]
            self.group_list_sva7_72 = [self.ui.doubleSpinBox_v_s7_7,self.ui.doubleSpinBox_sipir_1_s7_7,
                                     self.ui.doubleSpinBox_kesit_s7_7,self.ui.doubleSpinBox_cap_1_s7_7,
                                     self.ui.doubleSpinBox_akim_1_s7_7,self.ui.doubleSpinBox_sipir_2_s7_7,
                                     self.ui.doubleSpinBox_kesit_2_s7_7,self.ui.doubleSpinBox_cap_2_s7_7,
                                     self.ui.doubleSpinBox_akim_2_s7_7,self.ui.comboBox_tel_s7_7,
                                     self.ui.label_kesit_ok_s7_7,self.ui.label_kesit_error_s7_7]
            self.group_list_sva7_82 = [self.ui.doubleSpinBox_v_s7_8,self.ui.doubleSpinBox_sipir_1_s7_8,
                                     self.ui.doubleSpinBox_kesit_s7_8,self.ui.doubleSpinBox_cap_1_s7_8,
                                     self.ui.doubleSpinBox_akim_1_s7_8,self.ui.doubleSpinBox_sipir_2_s7_8,
                                     self.ui.doubleSpinBox_kesit_2_s7_8,self.ui.doubleSpinBox_cap_2_s7_8,
                                     self.ui.doubleSpinBox_akim_2_s7_8,self.ui.comboBox_tel_s7_8,
                                     self.ui.label_kesit_ok_s7_8,self.ui.label_kesit_error_s7_8]     
            self.group_list_sva7_92 = [self.ui.doubleSpinBox_v_s7_9,self.ui.doubleSpinBox_sipir_1_s7_9,
                                     self.ui.doubleSpinBox_kesit_s7_9,self.ui.doubleSpinBox_cap_1_s7_9,
                                     self.ui.doubleSpinBox_akim_1_s7_9,self.ui.doubleSpinBox_sipir_2_s7_9,
                                     self.ui.doubleSpinBox_kesit_2_s7_9,self.ui.doubleSpinBox_cap_2_s7_9,
                                     self.ui.doubleSpinBox_akim_2_s7_9,self.ui.comboBox_tel_s7_9,
                                     self.ui.label_kesit_ok_s7_9,self.ui.label_kesit_error_s7_9] 
            self.group_list_sva7_102 = [self.ui.doubleSpinBox_v_s7_10,self.ui.doubleSpinBox_sipir_1_s7_10,
                                     self.ui.doubleSpinBox_kesit_s7_10,self.ui.doubleSpinBox_cap_1_s7_10,
                                     self.ui.doubleSpinBox_akim_1_s7_10,self.ui.doubleSpinBox_sipir_2_s7_10,
                                     self.ui.doubleSpinBox_kesit_2_s7_10,self.ui.doubleSpinBox_cap_2_s7_10,
                                     self.ui.doubleSpinBox_akim_2_s7_10,self.ui.comboBox_tel_s7_10,
                                     self.ui.label_kesit_ok_s7_10,self.ui.label_kesit_error_s7_10]                                                                                                             
            self.group_name_list_sva7_2 = [self.group_list_sva7_11,self.group_list_sva7_22,self.group_list_sva7_32,
                                        self.group_list_sva7_42,self.group_list_sva7_52,self.group_list_sva7_62,
                                        self.group_list_sva7_72,self.group_list_sva7_82,self.group_list_sva7_92,
                                        self.group_list_sva7_102]
            self.button_list_sva7 = [self.ui.pushButton_buton_s7_1,self.ui.pushButton_buton_s7_2,
                                    self.ui.pushButton_buton_s7_3,self.ui.pushButton_buton_s7_4,
                                    self.ui.pushButton_buton_s7_5,self.ui.pushButton_buton_s7_6,
                                    self.ui.pushButton_buton_s7_7,self.ui.pushButton_buton_s7_8,
                                    self.ui.pushButton_buton_s7_9,self.ui.pushButton_buton_s7_10]

        if self.ui.radioButton_vadagilim.isChecked() or self.ui.comboBox_va.currentIndex()>=0:

            self.group_list_sva8_11 = [self.ui.doubleSpinBox_v_s8_1,self.ui.doubleSpinBox_sipir_1_s8_1,
                                     self.ui.doubleSpinBox_kesit_s8_1,self.ui.doubleSpinBox_cap_1_s8_1,
                                     self.ui.doubleSpinBox_akim_1_s8_1,self.ui.doubleSpinBox_sipir_2_s8_1,
                                     self.ui.doubleSpinBox_kesit_2_s8_1,self.ui.doubleSpinBox_cap_2_s8_1,
                                     self.ui.doubleSpinBox_akim_2_s8_1,self.ui.comboBox_tel_s8_1,
                                     self.ui.label_kesit_ok_s8_1,self.ui.label_kesit_error_s8_1]
            self.group_list_sva8_22 = [self.ui.doubleSpinBox_v_s8_2,self.ui.doubleSpinBox_sipir_1_s8_2,
                                     self.ui.doubleSpinBox_kesit_s8_2,self.ui.doubleSpinBox_cap_1_s8_2,
                                     self.ui.doubleSpinBox_akim_1_s8_2,self.ui.doubleSpinBox_sipir_2_s8_2,
                                     self.ui.doubleSpinBox_kesit_2_s8_2,self.ui.doubleSpinBox_cap_2_s8_2,
                                     self.ui.doubleSpinBox_akim_2_s8_2,self.ui.comboBox_tel_s8_2,
                                     self.ui.label_kesit_ok_s8_2,self.ui.label_kesit_error_s8_2]
            self.group_list_sva8_32 = [self.ui.doubleSpinBox_v_s8_3,self.ui.doubleSpinBox_sipir_1_s8_3,
                                     self.ui.doubleSpinBox_kesit_s8_3,self.ui.doubleSpinBox_cap_1_s8_3,
                                     self.ui.doubleSpinBox_akim_1_s8_3,self.ui.doubleSpinBox_sipir_2_s8_3,
                                     self.ui.doubleSpinBox_kesit_2_s8_3,self.ui.doubleSpinBox_cap_2_s8_3,
                                     self.ui.doubleSpinBox_akim_2_s8_3,self.ui.comboBox_tel_s8_3,
                                     self.ui.label_kesit_ok_s8_3,self.ui.label_kesit_error_s8_3]
            self.group_list_sva8_42 = [self.ui.doubleSpinBox_v_s8_4,self.ui.doubleSpinBox_sipir_1_s8_4,
                                     self.ui.doubleSpinBox_kesit_s8_4,self.ui.doubleSpinBox_cap_1_s8_4,
                                     self.ui.doubleSpinBox_akim_1_s8_4,self.ui.doubleSpinBox_sipir_2_s8_4,
                                     self.ui.doubleSpinBox_kesit_2_s8_4,self.ui.doubleSpinBox_cap_2_s8_4,
                                     self.ui.doubleSpinBox_akim_2_s8_4,self.ui.comboBox_tel_s8_4,
                                     self.ui.label_kesit_ok_s8_4,self.ui.label_kesit_error_s8_4]
            self.group_list_sva8_52 = [self.ui.doubleSpinBox_v_s8_5,self.ui.doubleSpinBox_sipir_1_s8_5,
                                     self.ui.doubleSpinBox_kesit_s8_5,self.ui.doubleSpinBox_cap_1_s8_5,
                                     self.ui.doubleSpinBox_akim_1_s8_5,self.ui.doubleSpinBox_sipir_2_s8_5,
                                     self.ui.doubleSpinBox_kesit_2_s8_5,self.ui.doubleSpinBox_cap_2_s8_5,
                                     self.ui.doubleSpinBox_akim_2_s8_5,self.ui.comboBox_tel_s8_5,
                                     self.ui.label_kesit_ok_s8_5,self.ui.label_kesit_error_s8_5]
            self.group_list_sva8_62 = [self.ui.doubleSpinBox_v_s8_6,self.ui.doubleSpinBox_sipir_1_s8_6,
                                     self.ui.doubleSpinBox_kesit_s8_6,self.ui.doubleSpinBox_cap_1_s8_6,
                                     self.ui.doubleSpinBox_akim_1_s8_6,self.ui.doubleSpinBox_sipir_2_s8_6,
                                     self.ui.doubleSpinBox_kesit_2_s8_6,self.ui.doubleSpinBox_cap_2_s8_6,
                                     self.ui.doubleSpinBox_akim_2_s8_6,self.ui.comboBox_tel_s8_6,
                                     self.ui.label_kesit_ok_s8_6,self.ui.label_kesit_error_s8_6]
            self.group_list_sva8_72 = [self.ui.doubleSpinBox_v_s8_7,self.ui.doubleSpinBox_sipir_1_s8_7,
                                     self.ui.doubleSpinBox_kesit_s8_7,self.ui.doubleSpinBox_cap_1_s8_7,
                                     self.ui.doubleSpinBox_akim_1_s8_7,self.ui.doubleSpinBox_sipir_2_s8_7,
                                     self.ui.doubleSpinBox_kesit_2_s8_7,self.ui.doubleSpinBox_cap_2_s8_7,
                                     self.ui.doubleSpinBox_akim_2_s8_7,self.ui.comboBox_tel_s8_7,
                                     self.ui.label_kesit_ok_s8_7,self.ui.label_kesit_error_s8_7]
            self.group_list_sva8_82 = [self.ui.doubleSpinBox_v_s8_8,self.ui.doubleSpinBox_sipir_1_s8_8,
                                     self.ui.doubleSpinBox_kesit_s8_8,self.ui.doubleSpinBox_cap_1_s8_8,
                                     self.ui.doubleSpinBox_akim_1_s8_8,self.ui.doubleSpinBox_sipir_2_s8_8,
                                     self.ui.doubleSpinBox_kesit_2_s8_8,self.ui.doubleSpinBox_cap_2_s8_8,
                                     self.ui.doubleSpinBox_akim_2_s8_8,self.ui.comboBox_tel_s8_8,
                                     self.ui.label_kesit_ok_s8_8,self.ui.label_kesit_error_s8_8]     
            self.group_list_sva8_92 = [self.ui.doubleSpinBox_v_s8_9,self.ui.doubleSpinBox_sipir_1_s8_9,
                                     self.ui.doubleSpinBox_kesit_s8_9,self.ui.doubleSpinBox_cap_1_s8_9,
                                     self.ui.doubleSpinBox_akim_1_s8_9,self.ui.doubleSpinBox_sipir_2_s8_9,
                                     self.ui.doubleSpinBox_kesit_2_s8_9,self.ui.doubleSpinBox_cap_2_s8_9,
                                     self.ui.doubleSpinBox_akim_2_s8_9,self.ui.comboBox_tel_s8_9,
                                     self.ui.label_kesit_ok_s8_9,self.ui.label_kesit_error_s8_9] 
            self.group_list_sva8_102 = [self.ui.doubleSpinBox_v_s8_10,self.ui.doubleSpinBox_sipir_1_s8_10,
                                     self.ui.doubleSpinBox_kesit_s8_10,self.ui.doubleSpinBox_cap_1_s8_10,
                                     self.ui.doubleSpinBox_akim_1_s8_10,self.ui.doubleSpinBox_sipir_2_s8_10,
                                     self.ui.doubleSpinBox_kesit_2_s8_10,self.ui.doubleSpinBox_cap_2_s8_10,
                                     self.ui.doubleSpinBox_akim_2_s8_10,self.ui.comboBox_tel_s8_10,
                                     self.ui.label_kesit_ok_s8_10,self.ui.label_kesit_error_s8_10]                                                                                                             
            self.group_name_list_sva8_2 = [self.group_list_sva8_11,self.group_list_sva8_22,self.group_list_sva8_32,
                                        self.group_list_sva8_42,self.group_list_sva8_52,self.group_list_sva8_62,
                                        self.group_list_sva8_72,self.group_list_sva8_82,self.group_list_sva8_92,
                                        self.group_list_sva8_102]
            self.button_list_sva8 = [self.ui.pushButton_buton_s8_1,self.ui.pushButton_buton_s8_2,
                                    self.ui.pushButton_buton_s8_3,self.ui.pushButton_buton_s8_4,
                                    self.ui.pushButton_buton_s8_5,self.ui.pushButton_buton_s8_6,
                                    self.ui.pushButton_buton_s8_7,self.ui.pushButton_buton_s8_8,
                                    self.ui.pushButton_buton_s8_9,self.ui.pushButton_buton_s8_10]

        if self.ui.radioButton_vadagilim.isChecked() or self.ui.comboBox_va.currentIndex()>=0:

            self.group_list_sva9_11 = [self.ui.doubleSpinBox_v_s9_1,self.ui.doubleSpinBox_sipir_1_s9_1,
                                     self.ui.doubleSpinBox_kesit_s9_1,self.ui.doubleSpinBox_cap_1_s9_1,
                                     self.ui.doubleSpinBox_akim_1_s9_1,self.ui.doubleSpinBox_sipir_2_s9_1,
                                     self.ui.doubleSpinBox_kesit_2_s9_1,self.ui.doubleSpinBox_cap_2_s9_1,
                                     self.ui.doubleSpinBox_akim_2_s9_1,self.ui.comboBox_tel_s9_1,
                                     self.ui.label_kesit_ok_s9_1,self.ui.label_kesit_error_s9_1]
            self.group_list_sva9_22 = [self.ui.doubleSpinBox_v_s9_2,self.ui.doubleSpinBox_sipir_1_s9_2,
                                     self.ui.doubleSpinBox_kesit_s9_2,self.ui.doubleSpinBox_cap_1_s9_2,
                                     self.ui.doubleSpinBox_akim_1_s9_2,self.ui.doubleSpinBox_sipir_2_s9_2,
                                     self.ui.doubleSpinBox_kesit_2_s9_2,self.ui.doubleSpinBox_cap_2_s9_2,
                                     self.ui.doubleSpinBox_akim_2_s9_2,self.ui.comboBox_tel_s9_2,
                                     self.ui.label_kesit_ok_s9_2,self.ui.label_kesit_error_s9_2]
            self.group_list_sva9_32 = [self.ui.doubleSpinBox_v_s9_3,self.ui.doubleSpinBox_sipir_1_s9_3,
                                     self.ui.doubleSpinBox_kesit_s9_3,self.ui.doubleSpinBox_cap_1_s9_3,
                                     self.ui.doubleSpinBox_akim_1_s9_3,self.ui.doubleSpinBox_sipir_2_s9_3,
                                     self.ui.doubleSpinBox_kesit_2_s9_3,self.ui.doubleSpinBox_cap_2_s9_3,
                                     self.ui.doubleSpinBox_akim_2_s9_3,self.ui.comboBox_tel_s9_3,
                                     self.ui.label_kesit_ok_s9_3,self.ui.label_kesit_error_s9_3]
            self.group_list_sva9_42 = [self.ui.doubleSpinBox_v_s9_4,self.ui.doubleSpinBox_sipir_1_s9_4,
                                     self.ui.doubleSpinBox_kesit_s9_4,self.ui.doubleSpinBox_cap_1_s9_4,
                                     self.ui.doubleSpinBox_akim_1_s9_4,self.ui.doubleSpinBox_sipir_2_s9_4,
                                     self.ui.doubleSpinBox_kesit_2_s9_4,self.ui.doubleSpinBox_cap_2_s9_4,
                                     self.ui.doubleSpinBox_akim_2_s9_4,self.ui.comboBox_tel_s9_4,
                                     self.ui.label_kesit_ok_s9_4,self.ui.label_kesit_error_s9_4]
            self.group_list_sva9_52 = [self.ui.doubleSpinBox_v_s9_5,self.ui.doubleSpinBox_sipir_1_s9_5,
                                     self.ui.doubleSpinBox_kesit_s9_5,self.ui.doubleSpinBox_cap_1_s9_5,
                                     self.ui.doubleSpinBox_akim_1_s9_5,self.ui.doubleSpinBox_sipir_2_s9_5,
                                     self.ui.doubleSpinBox_kesit_2_s9_5,self.ui.doubleSpinBox_cap_2_s9_5,
                                     self.ui.doubleSpinBox_akim_2_s9_5,self.ui.comboBox_tel_s9_5,
                                     self.ui.label_kesit_ok_s9_5,self.ui.label_kesit_error_s9_5]
            self.group_list_sva9_62 = [self.ui.doubleSpinBox_v_s9_6,self.ui.doubleSpinBox_sipir_1_s9_6,
                                     self.ui.doubleSpinBox_kesit_s9_6,self.ui.doubleSpinBox_cap_1_s9_6,
                                     self.ui.doubleSpinBox_akim_1_s9_6,self.ui.doubleSpinBox_sipir_2_s9_6,
                                     self.ui.doubleSpinBox_kesit_2_s9_6,self.ui.doubleSpinBox_cap_2_s9_6,
                                     self.ui.doubleSpinBox_akim_2_s9_6,self.ui.comboBox_tel_s9_6,
                                     self.ui.label_kesit_ok_s9_6,self.ui.label_kesit_error_s9_6]
            self.group_list_sva9_72 = [self.ui.doubleSpinBox_v_s9_7,self.ui.doubleSpinBox_sipir_1_s9_7,
                                     self.ui.doubleSpinBox_kesit_s9_7,self.ui.doubleSpinBox_cap_1_s9_7,
                                     self.ui.doubleSpinBox_akim_1_s9_7,self.ui.doubleSpinBox_sipir_2_s9_7,
                                     self.ui.doubleSpinBox_kesit_2_s9_7,self.ui.doubleSpinBox_cap_2_s9_7,
                                     self.ui.doubleSpinBox_akim_2_s9_7,self.ui.comboBox_tel_s9_7,
                                     self.ui.label_kesit_ok_s9_7,self.ui.label_kesit_error_s9_7]
            self.group_list_sva9_82 = [self.ui.doubleSpinBox_v_s9_8,self.ui.doubleSpinBox_sipir_1_s9_8,
                                     self.ui.doubleSpinBox_kesit_s9_8,self.ui.doubleSpinBox_cap_1_s9_8,
                                     self.ui.doubleSpinBox_akim_1_s9_8,self.ui.doubleSpinBox_sipir_2_s9_8,
                                     self.ui.doubleSpinBox_kesit_2_s9_8,self.ui.doubleSpinBox_cap_2_s9_8,
                                     self.ui.doubleSpinBox_akim_2_s9_8,self.ui.comboBox_tel_s9_8,
                                     self.ui.label_kesit_ok_s9_8,self.ui.label_kesit_error_s9_8]     
            self.group_list_sva9_92 = [self.ui.doubleSpinBox_v_s9_9,self.ui.doubleSpinBox_sipir_1_s9_9,
                                     self.ui.doubleSpinBox_kesit_s9_9,self.ui.doubleSpinBox_cap_1_s9_9,
                                     self.ui.doubleSpinBox_akim_1_s9_9,self.ui.doubleSpinBox_sipir_2_s9_9,
                                     self.ui.doubleSpinBox_kesit_2_s9_9,self.ui.doubleSpinBox_cap_2_s9_9,
                                     self.ui.doubleSpinBox_akim_2_s9_9,self.ui.comboBox_tel_s9_9,
                                     self.ui.label_kesit_ok_s9_9,self.ui.label_kesit_error_s9_9] 
            self.group_list_sva9_102 = [self.ui.doubleSpinBox_v_s9_10,self.ui.doubleSpinBox_sipir_1_s9_10,
                                     self.ui.doubleSpinBox_kesit_s9_10,self.ui.doubleSpinBox_cap_1_s9_10,
                                     self.ui.doubleSpinBox_akim_1_s9_10,self.ui.doubleSpinBox_sipir_2_s9_10,
                                     self.ui.doubleSpinBox_kesit_2_s9_10,self.ui.doubleSpinBox_cap_2_s9_10,
                                     self.ui.doubleSpinBox_akim_2_s9_10,self.ui.comboBox_tel_s9_10,
                                     self.ui.label_kesit_ok_s9_10,self.ui.label_kesit_error_s9_10]                                                                                                             
            self.group_name_list_sva9_2 = [self.group_list_sva9_11,self.group_list_sva9_22,self.group_list_sva9_32,
                                        self.group_list_sva9_42,self.group_list_sva9_52,self.group_list_sva9_62,
                                        self.group_list_sva9_72,self.group_list_sva9_82,self.group_list_sva9_92,
                                        self.group_list_sva9_102]
            self.button_list_sva9 = [self.ui.pushButton_buton_s9_1,self.ui.pushButton_buton_s9_2,
                                    self.ui.pushButton_buton_s9_3,self.ui.pushButton_buton_s9_4,
                                    self.ui.pushButton_buton_s9_5,self.ui.pushButton_buton_s9_6,
                                    self.ui.pushButton_buton_s9_7,self.ui.pushButton_buton_s9_8,
                                    self.ui.pushButton_buton_s9_9,self.ui.pushButton_buton_s9_10]

        if self.ui.radioButton_vadagilim.isChecked() or self.ui.comboBox_va.currentIndex()>=0:

            self.group_list_sva10_11 = [self.ui.doubleSpinBox_v_s10_1,self.ui.doubleSpinBox_sipir_1_s10_1,
                                     self.ui.doubleSpinBox_kesit_s10_1,self.ui.doubleSpinBox_cap_1_s10_1,
                                     self.ui.doubleSpinBox_akim_1_s10_1,self.ui.doubleSpinBox_sipir_2_s10_1,
                                     self.ui.doubleSpinBox_kesit_2_s10_1,self.ui.doubleSpinBox_cap_2_s10_1,
                                     self.ui.doubleSpinBox_akim_2_s10_1,self.ui.comboBox_tel_s10_1,
                                     self.ui.label_kesit_ok_s10_1,self.ui.label_kesit_error_s10_1]
            self.group_list_sva10_22 = [self.ui.doubleSpinBox_v_s10_2,self.ui.doubleSpinBox_sipir_1_s10_2,
                                     self.ui.doubleSpinBox_kesit_s10_2,self.ui.doubleSpinBox_cap_1_s10_2,
                                     self.ui.doubleSpinBox_akim_1_s10_2,self.ui.doubleSpinBox_sipir_2_s10_2,
                                     self.ui.doubleSpinBox_kesit_2_s10_2,self.ui.doubleSpinBox_cap_2_s10_2,
                                     self.ui.doubleSpinBox_akim_2_s10_2,self.ui.comboBox_tel_s10_2,
                                     self.ui.label_kesit_ok_s10_2,self.ui.label_kesit_error_s10_2]
            self.group_list_sva10_32 = [self.ui.doubleSpinBox_v_s10_3,self.ui.doubleSpinBox_sipir_1_s10_3,
                                     self.ui.doubleSpinBox_kesit_s10_3,self.ui.doubleSpinBox_cap_1_s10_3,
                                     self.ui.doubleSpinBox_akim_1_s10_3,self.ui.doubleSpinBox_sipir_2_s10_3,
                                     self.ui.doubleSpinBox_kesit_2_s10_3,self.ui.doubleSpinBox_cap_2_s10_3,
                                     self.ui.doubleSpinBox_akim_2_s10_3,self.ui.comboBox_tel_s10_3,
                                     self.ui.label_kesit_ok_s10_3,self.ui.label_kesit_error_s10_3]
            self.group_list_sva10_42 = [self.ui.doubleSpinBox_v_s10_4,self.ui.doubleSpinBox_sipir_1_s10_4,
                                     self.ui.doubleSpinBox_kesit_s10_4,self.ui.doubleSpinBox_cap_1_s10_4,
                                     self.ui.doubleSpinBox_akim_1_s10_4,self.ui.doubleSpinBox_sipir_2_s10_4,
                                     self.ui.doubleSpinBox_kesit_2_s10_4,self.ui.doubleSpinBox_cap_2_s10_4,
                                     self.ui.doubleSpinBox_akim_2_s10_4,self.ui.comboBox_tel_s10_4,
                                     self.ui.label_kesit_ok_s10_4,self.ui.label_kesit_error_s10_4]
            self.group_list_sva10_52 = [self.ui.doubleSpinBox_v_s10_5,self.ui.doubleSpinBox_sipir_1_s10_5,
                                     self.ui.doubleSpinBox_kesit_s10_5,self.ui.doubleSpinBox_cap_1_s10_5,
                                     self.ui.doubleSpinBox_akim_1_s10_5,self.ui.doubleSpinBox_sipir_2_s10_5,
                                     self.ui.doubleSpinBox_kesit_2_s10_5,self.ui.doubleSpinBox_cap_2_s10_5,
                                     self.ui.doubleSpinBox_akim_2_s10_5,self.ui.comboBox_tel_s10_5,
                                     self.ui.label_kesit_ok_s10_5,self.ui.label_kesit_error_s10_5]
            self.group_list_sva10_62 = [self.ui.doubleSpinBox_v_s10_6,self.ui.doubleSpinBox_sipir_1_s10_6,
                                     self.ui.doubleSpinBox_kesit_s10_6,self.ui.doubleSpinBox_cap_1_s10_6,
                                     self.ui.doubleSpinBox_akim_1_s10_6,self.ui.doubleSpinBox_sipir_2_s10_6,
                                     self.ui.doubleSpinBox_kesit_2_s10_6,self.ui.doubleSpinBox_cap_2_s10_6,
                                     self.ui.doubleSpinBox_akim_2_s10_6,self.ui.comboBox_tel_s10_6,
                                     self.ui.label_kesit_ok_s10_6,self.ui.label_kesit_error_s10_6]
            self.group_list_sva10_72 = [self.ui.doubleSpinBox_v_s10_7,self.ui.doubleSpinBox_sipir_1_s10_7,
                                     self.ui.doubleSpinBox_kesit_s10_7,self.ui.doubleSpinBox_cap_1_s10_7,
                                     self.ui.doubleSpinBox_akim_1_s10_7,self.ui.doubleSpinBox_sipir_2_s10_7,
                                     self.ui.doubleSpinBox_kesit_2_s10_7,self.ui.doubleSpinBox_cap_2_s10_7,
                                     self.ui.doubleSpinBox_akim_2_s10_7,self.ui.comboBox_tel_s10_7,
                                     self.ui.label_kesit_ok_s10_7,self.ui.label_kesit_error_s10_7]
            self.group_list_sva10_82 = [self.ui.doubleSpinBox_v_s10_8,self.ui.doubleSpinBox_sipir_1_s10_8,
                                     self.ui.doubleSpinBox_kesit_s10_8,self.ui.doubleSpinBox_cap_1_s10_8,
                                     self.ui.doubleSpinBox_akim_1_s10_8,self.ui.doubleSpinBox_sipir_2_s10_8,
                                     self.ui.doubleSpinBox_kesit_2_s10_8,self.ui.doubleSpinBox_cap_2_s10_8,
                                     self.ui.doubleSpinBox_akim_2_s10_8,self.ui.comboBox_tel_s10_8,
                                     self.ui.label_kesit_ok_s10_8,self.ui.label_kesit_error_s10_8]     
            self.group_list_sva10_92 = [self.ui.doubleSpinBox_v_s10_9,self.ui.doubleSpinBox_sipir_1_s10_9,
                                     self.ui.doubleSpinBox_kesit_s10_9,self.ui.doubleSpinBox_cap_1_s10_9,
                                     self.ui.doubleSpinBox_akim_1_s10_9,self.ui.doubleSpinBox_sipir_2_s10_9,
                                     self.ui.doubleSpinBox_kesit_2_s10_9,self.ui.doubleSpinBox_cap_2_s10_9,
                                     self.ui.doubleSpinBox_akim_2_s10_9,self.ui.comboBox_tel_s10_9,
                                     self.ui.label_kesit_ok_s10_9,self.ui.label_kesit_error_s10_9] 
            self.group_list_sva10_102 = [self.ui.doubleSpinBox_v_s10_10,self.ui.doubleSpinBox_sipir_1_s10_10,
                                     self.ui.doubleSpinBox_kesit_s10_10,self.ui.doubleSpinBox_cap_1_s10_10,
                                     self.ui.doubleSpinBox_akim_1_s10_10,self.ui.doubleSpinBox_sipir_2_s10_10,
                                     self.ui.doubleSpinBox_kesit_2_s10_10,self.ui.doubleSpinBox_cap_2_s10_10,
                                     self.ui.doubleSpinBox_akim_2_s10_10,self.ui.comboBox_tel_s10_10,
                                     self.ui.label_kesit_ok_s10_10,self.ui.label_kesit_error_s10_10]                                                                                                             
            self.group_name_list_sva10_2 = [self.group_list_sva10_11,self.group_list_sva10_22,self.group_list_sva10_32,
                                        self.group_list_sva10_42,self.group_list_sva10_52,self.group_list_sva10_62,
                                        self.group_list_sva10_72,self.group_list_sva10_82,self.group_list_sva10_92,
                                        self.group_list_sva10_102]
            self.button_list_sva10 = [self.ui.pushButton_buton_s10_1,self.ui.pushButton_buton_s10_2,
                                    self.ui.pushButton_buton_s10_3,self.ui.pushButton_buton_s10_4,
                                    self.ui.pushButton_buton_s10_5,self.ui.pushButton_buton_s10_6,
                                    self.ui.pushButton_buton_s10_7,self.ui.pushButton_buton_s10_8,
                                    self.ui.pushButton_buton_s10_9,self.ui.pushButton_buton_s10_10]
        self.va_altguplar=[self.group_name_list_sva1_2,self.group_name_list_sva2_2,self.group_name_list_sva3_2,self.group_name_list_sva4_2,
                           self.group_name_list_sva5_2,self.group_name_list_sva6_2,self.group_name_list_sva7_2,self.group_name_list_sva8_2,
                           self.group_name_list_sva9_2,self.group_name_list_sva10_2]
    def va_kademe_goster(self):
        self.kademe_goster(object=self.ui.comboBox_sva1_kad, group_list=self.kademe_list_s1)
        self.kademe_goster(object=self.ui.comboBox_sva2_kad, group_list=self.kademe_list_s2)
        self.kademe_goster(object=self.ui.comboBox_sva3_kad, group_list=self.kademe_list_s3)
        self.kademe_goster(object=self.ui.comboBox_sva4_kad, group_list=self.kademe_list_s4)
        self.kademe_goster(object=self.ui.comboBox_sva5_kad, group_list=self.kademe_list_s5)
        self.kademe_goster(object=self.ui.comboBox_sva6_kad, group_list=self.kademe_list_s6)
        self.kademe_goster(object=self.ui.comboBox_sva7_kad, group_list=self.kademe_list_s7)
        self.kademe_goster(object=self.ui.comboBox_sva8_kad, group_list=self.kademe_list_s8)
        self.kademe_goster(object=self.ui.comboBox_sva9_kad, group_list=self.kademe_list_s9)
        self.kademe_goster(object=self.ui.comboBox_sva10_kad, group_list=self.kademe_list_s10)
    def va_guc_deger_kenar_rengi(self):
        index = self.ui.stackedWidget_2.currentIndex()
        for i in range(0,11):
            if index==i:
                self.guclist_1[i-1].setStyleSheet("background-color: green")
            else:
                self.guclist_1[i-1].setStyleSheet("background-color: grey")
    def va_sayfa_ileri_butonu(self):
        index_say=int(self.ui.comboBox_va.currentText())
        if self.ui.stackedWidget_2.currentIndex()<index_say:
            self.ui.stackedWidget_2.setCurrentIndex(self.ui.stackedWidget_2.currentIndex()+1)
    def va_sayfa_geri_butonu(self):
        index_say=int(self.ui.comboBox_va.currentText())
        if index_say>1:
            self.ui.stackedWidget_2.setCurrentIndex(self.ui.stackedWidget_2.currentIndex()-1)       
    def va_object_signals(self):
        # =========  VA dağılımı sayfa geçişleri ================================================
        self.ui.pushButton_15.clicked.connect(lambda x: self.va_sayfa_ileri_butonu())
        self.ui.pushButton_16.clicked.connect(lambda x: self.va_sayfa_ileri_butonu())
        self.ui.pushButton_18.clicked.connect(lambda x: self.va_sayfa_ileri_butonu())
        self.ui.pushButton_20.clicked.connect(lambda x: self.va_sayfa_ileri_butonu())
        self.ui.pushButton_22.clicked.connect(lambda x: self.va_sayfa_ileri_butonu())
        self.ui.pushButton_24.clicked.connect(lambda x: self.va_sayfa_ileri_butonu())
        self.ui.pushButton_26.clicked.connect(lambda x: self.va_sayfa_ileri_butonu())
        self.ui.pushButton_28.clicked.connect(lambda x: self.va_sayfa_ileri_butonu())
        self.ui.pushButton_30.clicked.connect(lambda x: self.va_sayfa_ileri_butonu())

        self.ui.pushButton_17.clicked.connect(lambda x: self.va_sayfa_geri_butonu())
        self.ui.pushButton_19.clicked.connect(lambda x: self.va_sayfa_geri_butonu())
        self.ui.pushButton_21.clicked.connect(lambda x: self.va_sayfa_geri_butonu())
        self.ui.pushButton_23.clicked.connect(lambda x: self.va_sayfa_geri_butonu())
        self.ui.pushButton_25.clicked.connect(lambda x: self.va_sayfa_geri_butonu())
        self.ui.pushButton_27.clicked.connect(lambda x: self.va_sayfa_geri_butonu())
        self.ui.pushButton_29.clicked.connect(lambda x: self.va_sayfa_geri_butonu())
        self.ui.pushButton_31.clicked.connect(lambda x: self.va_sayfa_geri_butonu())
        self.ui.pushButton_33.clicked.connect(lambda x: self.va_sayfa_geri_butonu())

        self.ui.pushButton_sa_1.clicked.connect(self.va_guc_tab_clicked)
        self.ui.pushButton_sa_2.clicked.connect(self.va_guc_tab_clicked)
        self.ui.pushButton_sa_3.clicked.connect(self.va_guc_tab_clicked)
        self.ui.pushButton_sa_4.clicked.connect(self.va_guc_tab_clicked)
        self.ui.pushButton_sa_5.clicked.connect(self.va_guc_tab_clicked)
        self.ui.pushButton_sa_6.clicked.connect(self.va_guc_tab_clicked)
        self.ui.pushButton_sa_7.clicked.connect(self.va_guc_tab_clicked)
        self.ui.pushButton_sa_8.clicked.connect(self.va_guc_tab_clicked)
        self.ui.pushButton_sa_9.clicked.connect(self.va_guc_tab_clicked)
        self.ui.pushButton_sa_10.clicked.connect(self.va_guc_tab_clicked)
        # =========================================================
        self.ui.radioButton_vadagilim.toggled.connect(lambda x: self.va_veri_kumesi())
        self.ui.radioButton_vadagilim.toggled.connect(self.va_kademe_guncelle)
        #self.ui.comboBox_va.currentTextChanged.connect(lambda x: self.va_veri_kumesi())
        self.ui.comboBox_va.currentTextChanged.connect(self.va_kademe_guncelle)


        for index in range(1,11):
            getattr(self.ui,("doubleSpinBox_sva"+str(index)+"_guc")).valueChanged.connect(self.hesaplamalari_guncelle)

            for kademe in range(0,10):
                getattr(self, ("button_list_sva" + str(index)))[kademe].clicked.connect(self.open_kesit_hesaplama)


        self.ui.comboBox_sva1_kad.currentTextChanged.connect(self.hesaplamalari_guncelle)
        self.ui.comboBox_sva2_kad.currentTextChanged.connect(self.hesaplamalari_guncelle)
        self.ui.comboBox_sva3_kad.currentTextChanged.connect(self.hesaplamalari_guncelle)
        self.ui.comboBox_sva4_kad.currentTextChanged.connect(self.hesaplamalari_guncelle)
        self.ui.comboBox_sva5_kad.currentTextChanged.connect(self.hesaplamalari_guncelle)
        self.ui.comboBox_sva6_kad.currentTextChanged.connect(self.hesaplamalari_guncelle)
        self.ui.comboBox_sva7_kad.currentTextChanged.connect(self.hesaplamalari_guncelle)
        self.ui.comboBox_sva8_kad.currentTextChanged.connect(self.hesaplamalari_guncelle)
        self.ui.comboBox_sva9_kad.currentTextChanged.connect(self.hesaplamalari_guncelle)
        self.ui.comboBox_sva10_kad.currentTextChanged.connect(self.hesaplamalari_guncelle)
        self.ui.comboBox_sva1_kad.currentTextChanged.connect(
            lambda x: self.kademe_goster(object=self.ui.comboBox_sva1_kad, group_list=self.kademe_list_s1))
        
        self.ui.comboBox_sva2_kad.currentTextChanged.connect(
            lambda x: self.kademe_goster(object=self.ui.comboBox_sva2_kad, group_list=self.kademe_list_s2))
        
        self.ui.comboBox_sva3_kad.currentTextChanged.connect(
            lambda x: self.kademe_goster(object=self.ui.comboBox_sva3_kad, group_list=self.kademe_list_s3))
        
        self.ui.comboBox_sva4_kad.currentTextChanged.connect(
            lambda x: self.kademe_goster(object=self.ui.comboBox_sva4_kad, group_list=self.kademe_list_s4))
        
        self.ui.comboBox_sva5_kad.currentTextChanged.connect(
            lambda x: self.kademe_goster(object=self.ui.comboBox_sva5_kad, group_list=self.kademe_list_s5))
        
        self.ui.comboBox_sva6_kad.currentTextChanged.connect(
            lambda x: self.kademe_goster(object=self.ui.comboBox_sva6_kad, group_list=self.kademe_list_s6))
        
        self.ui.comboBox_sva7_kad.currentTextChanged.connect(
            lambda x: self.kademe_goster(object=self.ui.comboBox_sva7_kad, group_list=self.kademe_list_s7))
        
        self.ui.comboBox_sva8_kad.currentTextChanged.connect(
            lambda x: self.kademe_goster(object=self.ui.comboBox_sva8_kad, group_list=self.kademe_list_s8))
        
        self.ui.comboBox_sva9_kad.currentTextChanged.connect(
            lambda x: self.kademe_goster(object=self.ui.comboBox_sva9_kad, group_list=self.kademe_list_s9))
        
        self.ui.comboBox_sva10_kad.currentTextChanged.connect(
            lambda x: self.kademe_goster(object=self.ui.comboBox_sva10_kad, group_list=self.kademe_list_s10))
    def va_kalan_guc(self):
        self.ui.doubleSpinBox_s1.setValue(self.ui.doubleSpinBox_sva1_guc.value())
        self.ui.doubleSpinBox_s2.setValue(self.ui.doubleSpinBox_sva2_guc.value())
        self.ui.doubleSpinBox_s3.setValue(self.ui.doubleSpinBox_sva3_guc.value())
        self.ui.doubleSpinBox_s4.setValue(self.ui.doubleSpinBox_sva4_guc.value())
        self.ui.doubleSpinBox_s5.setValue(self.ui.doubleSpinBox_sva5_guc.value())
        self.ui.doubleSpinBox_s6.setValue(self.ui.doubleSpinBox_sva6_guc.value())
        self.ui.doubleSpinBox_s7.setValue(self.ui.doubleSpinBox_sva7_guc.value())
        self.ui.doubleSpinBox_s8.setValue(self.ui.doubleSpinBox_sva8_guc.value())
        self.ui.doubleSpinBox_s9.setValue(self.ui.doubleSpinBox_sva9_guc.value())
        self.ui.doubleSpinBox_s10.setValue(self.ui.doubleSpinBox_sva10_guc.value())
        self.ui.doubleSpinBox_total.setValue(self.ui.doubleSpinBox_sva1_guc.value()+self.ui.doubleSpinBox_sva2_guc.value()+self.ui.doubleSpinBox_sva3_guc.value()+self.ui.doubleSpinBox_sva4_guc.value()+self.ui.doubleSpinBox_sva5_guc.value()+self.ui.doubleSpinBox_sva6_guc.value()+self.ui.doubleSpinBox_sva7_guc.value()+self.ui.doubleSpinBox_sva8_guc.value()+self.ui.doubleSpinBox_sva9_guc.value()+self.ui.doubleSpinBox_sva10_guc.value())
        self.ui.doubleSpinBox_total_fark.setValue(self.ui.doubleSpinBox_guc.value()-self.ui.doubleSpinBox_total.value())
        if self.ui.doubleSpinBox_total.value()>self.ui.doubleSpinBox_guc.value():
            popup.error_msjbox(title='Kademe Güç değerleri Haatalı', text=f'Lütfen Toplam Güce uygun değerler giriniz.Girdiğiniz Güç {-self.ui.doubleSpinBox_total_fark.value()} kadar fazla.')
            self.ui.label_guc_err.setVisible(True)
            self.ui.doubleSpinBox_total_fark.setStyleSheet("background-color : red;")
        else:
            self.ui.label_guc_err.setVisible(False)
            self.ui.doubleSpinBox_total_fark.setStyleSheet("background-color : lightgreen;")
    def va_kademe_guncelle(self):

        if int(self.ui.comboBox_va.currentText())==1:
            self.ui.doubleSpinBox_s1.setVisible(True)
            self.ui.doubleSpinBox_s2.setVisible(False)
            self.ui.doubleSpinBox_s3.setVisible(False)
            self.ui.doubleSpinBox_s4.setVisible(False)
            self.ui.doubleSpinBox_s5.setVisible(False)
            self.ui.doubleSpinBox_s6.setVisible(False)
            self.ui.doubleSpinBox_s7.setVisible(False)
            self.ui.doubleSpinBox_s8.setVisible(False)
            self.ui.doubleSpinBox_s9.setVisible(False)
            self.ui.doubleSpinBox_s10.setVisible(False)

            self.ui.pushButton_sa_1.setEnabled(True)
            self.ui.pushButton_sa_2.setEnabled(False)
            self.ui.pushButton_sa_3.setEnabled(False)
            self.ui.pushButton_sa_4.setEnabled(False)
            self.ui.pushButton_sa_5.setEnabled(False)
            self.ui.pushButton_sa_6.setEnabled(False)
            self.ui.pushButton_sa_7.setEnabled(False)
            self.ui.pushButton_sa_8.setEnabled(False)
            self.ui.pushButton_sa_9.setEnabled(False)
            self.ui.pushButton_sa_10.setEnabled(False)

        elif int(self.ui.comboBox_va.currentText())==2:
            self.ui.doubleSpinBox_s1.setVisible(True)
            self.ui.doubleSpinBox_s2.setVisible(True)
            self.ui.doubleSpinBox_s3.setVisible(False)
            self.ui.doubleSpinBox_s4.setVisible(False)
            self.ui.doubleSpinBox_s5.setVisible(False)
            self.ui.doubleSpinBox_s6.setVisible(False)
            self.ui.doubleSpinBox_s7.setVisible(False)
            self.ui.doubleSpinBox_s8.setVisible(False)
            self.ui.doubleSpinBox_s9.setVisible(False)
            self.ui.doubleSpinBox_s10.setVisible(False)

            self.ui.pushButton_sa_1.setEnabled(True)
            self.ui.pushButton_sa_2.setEnabled(True)
            self.ui.pushButton_sa_3.setEnabled(False)
            self.ui.pushButton_sa_4.setEnabled(False)
            self.ui.pushButton_sa_5.setEnabled(False)
            self.ui.pushButton_sa_6.setEnabled(False)
            self.ui.pushButton_sa_7.setEnabled(False)
            self.ui.pushButton_sa_8.setEnabled(False)
            self.ui.pushButton_sa_9.setEnabled(False)
            self.ui.pushButton_sa_10.setEnabled(False)
        elif int(self.ui.comboBox_va.currentText())==3:
            self.ui.doubleSpinBox_s1.setVisible(True)
            self.ui.doubleSpinBox_s2.setVisible(True)
            self.ui.doubleSpinBox_s3.setVisible(True)
            self.ui.doubleSpinBox_s4.setVisible(False)
            self.ui.doubleSpinBox_s5.setVisible(False)
            self.ui.doubleSpinBox_s6.setVisible(False)
            self.ui.doubleSpinBox_s7.setVisible(False)
            self.ui.doubleSpinBox_s8.setVisible(False)
            self.ui.doubleSpinBox_s9.setVisible(False)
            self.ui.doubleSpinBox_s10.setVisible(False)

            self.ui.pushButton_sa_1.setEnabled(True)
            self.ui.pushButton_sa_2.setEnabled(True)
            self.ui.pushButton_sa_3.setEnabled(True)
            self.ui.pushButton_sa_4.setEnabled(False)
            self.ui.pushButton_sa_5.setEnabled(False)
            self.ui.pushButton_sa_6.setEnabled(False)
            self.ui.pushButton_sa_7.setEnabled(False)
            self.ui.pushButton_sa_8.setEnabled(False)
            self.ui.pushButton_sa_9.setEnabled(False)
            self.ui.pushButton_sa_10.setEnabled(False)
        elif int(self.ui.comboBox_va.currentText())==4:
            self.ui.doubleSpinBox_s1.setVisible(True)
            self.ui.doubleSpinBox_s2.setVisible(True)
            self.ui.doubleSpinBox_s3.setVisible(True)
            self.ui.doubleSpinBox_s4.setVisible(True)
            self.ui.doubleSpinBox_s5.setVisible(False)
            self.ui.doubleSpinBox_s6.setVisible(False)
            self.ui.doubleSpinBox_s7.setVisible(False)
            self.ui.doubleSpinBox_s8.setVisible(False)
            self.ui.doubleSpinBox_s9.setVisible(False)
            self.ui.doubleSpinBox_s10.setVisible(False)

            self.ui.pushButton_sa_1.setEnabled(True)
            self.ui.pushButton_sa_2.setEnabled(True)
            self.ui.pushButton_sa_3.setEnabled(True)
            self.ui.pushButton_sa_4.setEnabled(True)
            self.ui.pushButton_sa_5.setEnabled(False)
            self.ui.pushButton_sa_6.setEnabled(False)
            self.ui.pushButton_sa_7.setEnabled(False)
            self.ui.pushButton_sa_8.setEnabled(False)
            self.ui.pushButton_sa_9.setEnabled(False)
            self.ui.pushButton_sa_10.setEnabled(False)
        elif int(self.ui.comboBox_va.currentText())==5:
            self.ui.doubleSpinBox_s1.setVisible(True)
            self.ui.doubleSpinBox_s2.setVisible(True)
            self.ui.doubleSpinBox_s3.setVisible(True)
            self.ui.doubleSpinBox_s4.setVisible(True)
            self.ui.doubleSpinBox_s5.setVisible(True)
            self.ui.doubleSpinBox_s6.setVisible(False)
            self.ui.doubleSpinBox_s7.setVisible(False)
            self.ui.doubleSpinBox_s8.setVisible(False)
            self.ui.doubleSpinBox_s9.setVisible(False)
            self.ui.doubleSpinBox_s10.setVisible(False)

            self.ui.pushButton_sa_1.setEnabled(True)
            self.ui.pushButton_sa_2.setEnabled(True)
            self.ui.pushButton_sa_3.setEnabled(True)
            self.ui.pushButton_sa_4.setEnabled(True)
            self.ui.pushButton_sa_5.setEnabled(True)
            self.ui.pushButton_sa_6.setEnabled(False)
            self.ui.pushButton_sa_7.setEnabled(False)
            self.ui.pushButton_sa_8.setEnabled(False)
            self.ui.pushButton_sa_9.setEnabled(False)
            self.ui.pushButton_sa_10.setEnabled(False)
        elif int(self.ui.comboBox_va.currentText())==6:
            self.ui.doubleSpinBox_s1.setVisible(True)
            self.ui.doubleSpinBox_s2.setVisible(True)
            self.ui.doubleSpinBox_s3.setVisible(True)
            self.ui.doubleSpinBox_s4.setVisible(True)
            self.ui.doubleSpinBox_s5.setVisible(True)
            self.ui.doubleSpinBox_s6.setVisible(True)
            self.ui.doubleSpinBox_s7.setVisible(False)
            self.ui.doubleSpinBox_s8.setVisible(False)
            self.ui.doubleSpinBox_s9.setVisible(False)
            self.ui.doubleSpinBox_s10.setVisible(False)

            self.ui.pushButton_sa_1.setEnabled(True)
            self.ui.pushButton_sa_2.setEnabled(True)
            self.ui.pushButton_sa_3.setEnabled(True)
            self.ui.pushButton_sa_4.setEnabled(True)
            self.ui.pushButton_sa_5.setEnabled(True)
            self.ui.pushButton_sa_6.setEnabled(True)
            self.ui.pushButton_sa_7.setEnabled(False)
            self.ui.pushButton_sa_8.setEnabled(False)
            self.ui.pushButton_sa_9.setEnabled(False)
            self.ui.pushButton_sa_10.setEnabled(False)
        elif int(self.ui.comboBox_va.currentText())==7:
            self.ui.doubleSpinBox_s1.setVisible(True)
            self.ui.doubleSpinBox_s2.setVisible(True)
            self.ui.doubleSpinBox_s3.setVisible(True)
            self.ui.doubleSpinBox_s4.setVisible(True)
            self.ui.doubleSpinBox_s5.setVisible(True)
            self.ui.doubleSpinBox_s6.setVisible(True)
            self.ui.doubleSpinBox_s7.setVisible(True)
            self.ui.doubleSpinBox_s8.setVisible(False)
            self.ui.doubleSpinBox_s9.setVisible(False)
            self.ui.doubleSpinBox_s10.setVisible(False)

            self.ui.pushButton_sa_1.setEnabled(True)
            self.ui.pushButton_sa_2.setEnabled(True)
            self.ui.pushButton_sa_3.setEnabled(True)
            self.ui.pushButton_sa_4.setEnabled(True)
            self.ui.pushButton_sa_5.setEnabled(True)
            self.ui.pushButton_sa_6.setEnabled(True)
            self.ui.pushButton_sa_7.setEnabled(True)
            self.ui.pushButton_sa_8.setEnabled(False)
            self.ui.pushButton_sa_9.setEnabled(False)
            self.ui.pushButton_sa_10.setEnabled(False)
        elif int(self.ui.comboBox_va.currentText())==8:
            self.ui.doubleSpinBox_s1.setVisible(True)
            self.ui.doubleSpinBox_s2.setVisible(True)
            self.ui.doubleSpinBox_s3.setVisible(True)
            self.ui.doubleSpinBox_s4.setVisible(True)
            self.ui.doubleSpinBox_s5.setVisible(True)
            self.ui.doubleSpinBox_s6.setVisible(True)
            self.ui.doubleSpinBox_s7.setVisible(True)
            self.ui.doubleSpinBox_s8.setVisible(True)
            self.ui.doubleSpinBox_s9.setVisible(False)
            self.ui.doubleSpinBox_s10.setVisible(False)

            self.ui.pushButton_sa_1.setEnabled(True)
            self.ui.pushButton_sa_2.setEnabled(True)
            self.ui.pushButton_sa_3.setEnabled(True)
            self.ui.pushButton_sa_4.setEnabled(True)
            self.ui.pushButton_sa_5.setEnabled(True)
            self.ui.pushButton_sa_6.setEnabled(True)
            self.ui.pushButton_sa_7.setEnabled(True)
            self.ui.pushButton_sa_8.setEnabled(True)
            self.ui.pushButton_sa_9.setEnabled(False)
            self.ui.pushButton_sa_10.setEnabled(False)
        elif int(self.ui.comboBox_va.currentText()) == 9:
            self.ui.doubleSpinBox_s1.setVisible(True)
            self.ui.doubleSpinBox_s2.setVisible(True)
            self.ui.doubleSpinBox_s3.setVisible(True)
            self.ui.doubleSpinBox_s4.setVisible(True)
            self.ui.doubleSpinBox_s5.setVisible(True)
            self.ui.doubleSpinBox_s6.setVisible(True)
            self.ui.doubleSpinBox_s7.setVisible(True)
            self.ui.doubleSpinBox_s8.setVisible(True)
            self.ui.doubleSpinBox_s9.setVisible(True)
            self.ui.doubleSpinBox_s10.setVisible(False)

            self.ui.pushButton_sa_1.setEnabled(True)
            self.ui.pushButton_sa_2.setEnabled(True)
            self.ui.pushButton_sa_3.setEnabled(True)
            self.ui.pushButton_sa_4.setEnabled(True)
            self.ui.pushButton_sa_5.setEnabled(True)
            self.ui.pushButton_sa_6.setEnabled(True)
            self.ui.pushButton_sa_7.setEnabled(True)
            self.ui.pushButton_sa_8.setEnabled(True)
            self.ui.pushButton_sa_9.setEnabled(True)
            self.ui.pushButton_sa_10.setEnabled(False)
        elif int(self.ui.comboBox_va.currentText())==10:
            self.ui.doubleSpinBox_s1.setVisible(True)
            self.ui.doubleSpinBox_s2.setVisible(True)
            self.ui.doubleSpinBox_s3.setVisible(True)
            self.ui.doubleSpinBox_s4.setVisible(True)
            self.ui.doubleSpinBox_s5.setVisible(True)
            self.ui.doubleSpinBox_s6.setVisible(True)
            self.ui.doubleSpinBox_s7.setVisible(True)
            self.ui.doubleSpinBox_s8.setVisible(True)
            self.ui.doubleSpinBox_s9.setVisible(True)
            self.ui.doubleSpinBox_s10.setVisible(True)

            self.ui.pushButton_sa_1.setEnabled(True)
            self.ui.pushButton_sa_2.setEnabled(True)
            self.ui.pushButton_sa_3.setEnabled(True)
            self.ui.pushButton_sa_4.setEnabled(True)
            self.ui.pushButton_sa_5.setEnabled(True)
            self.ui.pushButton_sa_6.setEnabled(True)
            self.ui.pushButton_sa_7.setEnabled(True)
            self.ui.pushButton_sa_8.setEnabled(True)
            self.ui.pushButton_sa_9.setEnabled(True)
            self.ui.pushButton_sa_10.setEnabled(True)

        else:
            self.ui.doubleSpinBox_s1.setVisible(False)
            self.ui.doubleSpinBox_s2.setVisible(False)
            self.ui.doubleSpinBox_s3.setVisible(False)
            self.ui.doubleSpinBox_s4.setVisible(False)
            self.ui.doubleSpinBox_s5.setVisible(False)
            self.ui.doubleSpinBox_s6.setVisible(False)
            self.ui.doubleSpinBox_s7.setVisible(False)
            self.ui.doubleSpinBox_s8.setVisible(False)
            self.ui.doubleSpinBox_s9.setVisible(False)
            self.ui.doubleSpinBox_s10.setVisible(False)

            self.ui.pushButton_sa_1.setEnabled(False)
            self.ui.pushButton_sa_2.setEnabled(False)
            self.ui.pushButton_sa_3.setEnabled(False)
            self.ui.pushButton_sa_4.setEnabled(False)
            self.ui.pushButton_sa_5.setEnabled(False)
            self.ui.pushButton_sa_6.setEnabled(False)
            self.ui.pushButton_sa_7.setEnabled(False)
            self.ui.pushButton_sa_8.setEnabled(False)
            self.ui.pushButton_sa_9.setEnabled(False)
            self.ui.pushButton_sa_10.setEnabled(False)
    def va_guc_tab_clicked(self):
        sender = self.sender()
        kademe = int(sender.objectName().split("_")[len(sender.objectName().split("_"))-1])

        self.ui.stackedWidget_2.setCurrentIndex(kademe)
    # Mono Faz İzolasyon Trafosu - Primer Hesabı    ===============

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
        self.ui.comboBox.currentTextChanged.connect(self.primer_kademe_goster)

        for i in range(0,10):
            self.button_list_1[i].clicked.connect(self.open_kesit_hesaplama)
    def primer_kademe_goster(self):
        self.kademe_goster(object=self.ui.comboBox, group_list=self.kademe_list_1)
        
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
                    kademe=int(self.ui.comboBox.currentText()))
    # ======================  İzolasyon Hesabı =========================    
    def izolasyon_verileri_guncelle(self,object):
        self.ui.doubleSpinBox_primer_izo_deg.setValue(object.ui.doubleSpinBox.value())
        self.ui.doubleSpinBox_sekonder_izo_deg.setValue(object.ui.doubleSpinBox_2.value())
        self.ui.doubleSpinBox_pri_sek_izo_deg.setValue(object.ui.doubleSpinBox_3.value())
        self.ui.doubleSpinBox_ekran_izo_deg.setValue(object.ui.doubleSpinBox_4.value())
        self.ui.doubleSpinBox_ekstra_izo_deg.setValue(object.ui.doubleSpinBox_5.value())
        self.ui.doubleSpinBox_primer_izo_tur.setValue(object.ui.doubleSpinBox_6.value())
        self.ui.doubleSpinBox_sekonder_izo_tur.setValue(object.ui.doubleSpinBox_7.value())
        self.ui.doubleSpinBox_pri_sek_izo_tur.setValue(object.ui.doubleSpinBox_8.value())
        self.ui.checkBox_ekran_sec.setChecked(object.ui.checkBox.isChecked())
        self.ui.checkBox_ekstra.setChecked(object.ui.checkBox_2.isChecked())
    def izolasyon_deger_al(self,object):
        object.ui.doubleSpinBox.setValue(self.ui.doubleSpinBox_primer_izo_deg.value())
        object.ui.doubleSpinBox_2.setValue(self.ui.doubleSpinBox_sekonder_izo_deg.value())
        object.ui.doubleSpinBox_3.setValue(self.ui.doubleSpinBox_pri_sek_izo_deg.value())
        object.ui.doubleSpinBox_4.setValue(self.ui.doubleSpinBox_ekran_izo_deg.value())
        object.ui.doubleSpinBox_5.setValue(self.ui.doubleSpinBox_ekstra_izo_deg.value())
        object.ui.doubleSpinBox_6.setValue(self.ui.doubleSpinBox_primer_izo_tur.value())
        object.ui.doubleSpinBox_7.setValue(self.ui.doubleSpinBox_sekonder_izo_tur.value())
        object.ui.doubleSpinBox_8.setValue(self.ui.doubleSpinBox_pri_sek_izo_tur.value())
        object.ui.checkBox.setChecked(self.ui.checkBox_ekran_sec.isChecked())
        object.ui.checkBox_2.setChecked(self.ui.checkBox_ekstra.isChecked())
    def izolasyon_hesapla(self):
        self.primer_izolasyon= hp.primer_izolasyon_hesap(
            izo_deg=self.ui.doubleSpinBox_primer_izo_deg.value(),
            tur=self.ui.doubleSpinBox_primer_izo_tur.value(),
            kademe=int(self.ui.comboBox.currentText()))
        if self.ui.radioButton_vadagilim.isChecked() and self.ui.comboBox_va.currentIndex()>=0: 
            self.sva1_izolasyon =hp.va_izolasyon_hesap(
                izo_deg=self.ui.doubleSpinBox_sekonder_izo_deg.value(),
                tur=self.ui.doubleSpinBox_sekonder_izo_tur.value(),
                kademe=int(self.ui.comboBox_sva1_kad.currentText()))
        else:
            self.sva1_izolasyon = 0
        if self.ui.radioButton_vadagilim.isChecked() and self.ui.comboBox_va.currentIndex()>=1:
            self.sva2_izolasyon =hp.va_izolasyon_hesap(
                izo_deg=self.ui.doubleSpinBox_sekonder_izo_deg.value(),
                tur=self.ui.doubleSpinBox_sekonder_izo_tur.value(),
                kademe=int(self.ui.comboBox_sva2_kad.currentText()))
        else:
            self.sva2_izolasyon = 0
        if self.ui.radioButton_vadagilim.isChecked() and self.ui.comboBox_va.currentIndex()>=2:
            self.sva3_izolasyon =hp.va_izolasyon_hesap(
                izo_deg=self.ui.doubleSpinBox_sekonder_izo_deg.value(),
                tur=self.ui.doubleSpinBox_sekonder_izo_tur.value(),
                kademe=int(self.ui.comboBox_sva3_kad.currentText()))
        else:
            self.sva3_izolasyon = 0
        if self.ui.radioButton_vadagilim.isChecked() and self.ui.comboBox_va.currentIndex()>=3:
            self.sva4_izolasyon =hp.va_izolasyon_hesap(
                izo_deg=self.ui.doubleSpinBox_sekonder_izo_deg.value(),
                tur=self.ui.doubleSpinBox_sekonder_izo_tur.value(),
                kademe=int(self.ui.comboBox_sva4_kad.currentText()))
        else:
            self.sva4_izolasyon = 0
        if self.ui.radioButton_vadagilim.isChecked() and self.ui.comboBox_va.currentIndex()>=4:
            self.sva5_izolasyon =hp.va_izolasyon_hesap(
                izo_deg=self.ui.doubleSpinBox_sekonder_izo_deg.value(),
                tur=self.ui.doubleSpinBox_sekonder_izo_tur.value(),
                kademe=int(self.ui.comboBox_sva5_kad.currentText()))
        else:
            self.sva5_izolasyon = 0
        if self.ui.radioButton_vadagilim.isChecked() and self.ui.comboBox_va.currentIndex()>=5:
            self.sva6_izolasyon =hp.va_izolasyon_hesap(
                izo_deg=self.ui.doubleSpinBox_sekonder_izo_deg.value(),
                tur=self.ui.doubleSpinBox_sekonder_izo_tur.value(),
                kademe=int(self.ui.comboBox_sva6_kad.currentText()))
        else:
            self.sva6_izolasyon = 0
        if self.ui.radioButton_vadagilim.isChecked() and self.ui.comboBox_va.currentIndex()>=6:
            self.sva7_izolasyon =hp.va_izolasyon_hesap(
                izo_deg=self.ui.doubleSpinBox_sekonder_izo_deg.value(),
                tur=self.ui.doubleSpinBox_sekonder_izo_tur.value(),
                kademe=int(self.ui.comboBox_sva7_kad.currentText()))
        else:
            self.sva7_izolasyon = 0
        if self.ui.radioButton_vadagilim.isChecked() and self.ui.comboBox_va.currentIndex()>=7:
            self.sva8_izolasyon =hp.va_izolasyon_hesap(
                izo_deg=self.ui.doubleSpinBox_sekonder_izo_deg.value(),
                tur=self.ui.doubleSpinBox_sekonder_izo_tur.value(),
                kademe=int(self.ui.comboBox_sva8_kad.currentText()))
        else:
            self.sva8_izolasyon = 0
        if self.ui.radioButton_vadagilim.isChecked() and self.ui.comboBox_va.currentIndex()>=8:
            self.sva9_izolasyon =hp.va_izolasyon_hesap(
                izo_deg=self.ui.doubleSpinBox_sekonder_izo_deg.value(),
                tur=self.ui.doubleSpinBox_sekonder_izo_tur.value(),
                kademe=int(self.ui.comboBox_sva9_kad.currentText()))
        else:
            self.sva9_izolasyon = 0
        if self.ui.radioButton_vadagilim.isChecked() and self.ui.comboBox_va.currentIndex()>=9:
            self.sva10_izolasyon =hp.va_izolasyon_hesap(
                izo_deg=self.ui.doubleSpinBox_sekonder_izo_deg.value(),
                tur=self.ui.doubleSpinBox_sekonder_izo_tur.value(),
                kademe=int(self.ui.comboBox_sva10_kad.currentText()))
        else:
            self.sva10_izolasyon = 0

        self.toplam_izolasyon = self.primer_izolasyon+self.ui.doubleSpinBox_pri_sek_izo_deg.value()*\
                                self.ui.doubleSpinBox_pri_sek_izo_tur.value()+self.ui.doubleSpinBox_ekran_izo_deg.value() + \
                                self.ui.doubleSpinBox_ekstra_izo_deg.value() + self.sva1_izolasyon + self.sva2_izolasyon + \
                                self.sva3_izolasyon + self.sva4_izolasyon +  self.sva5_izolasyon + self.sva6_izolasyon + \
                                self.sva7_izolasyon + self.sva8_izolasyon + self.sva9_izolasyon + self.sva10_izolasyon
        
        return self.toplam_izolasyon
    def izolasyon_object_signals(self):
        self.ui.doubleSpinBox_primer_izo_deg.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_sekonder_izo_deg.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_pri_sek_izo_deg.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_ekran_izo_deg.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_ekstra_izo_deg.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_primer_izo_tur.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_sekonder_izo_tur.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.doubleSpinBox_pri_sek_izo_tur.valueChanged.connect(self.hesaplamalari_guncelle)
        self.ui.checkBox_ekran_sec.stateChanged.connect(self.hesaplamalari_guncelle)
        self.ui.checkBox_ekstra.stateChanged.connect(self.hesaplamalari_guncelle)
        self.ui.comboBox.currentTextChanged.connect(self.hesaplamalari_guncelle)
    # ======================  bosluk hesabı =========================  
    def bosluk_hesapla(self):
        self.izolasyon_hesapla()
        gl=self.group_name_list_primer_kademe
        primer_top_yuk = gl[0]["sarim_yukseklik"]+gl[1]["sarim_yukseklik"]+gl[2]["sarim_yukseklik"]+gl[3]["sarim_yukseklik"]+gl[4]["sarim_yukseklik"]+gl[5]["sarim_yukseklik"]+gl[6]["sarim_yukseklik"]+gl[7]["sarim_yukseklik"]+gl[8]["sarim_yukseklik"]+gl[9]["sarim_yukseklik"]
        gl=self.group_name_list_sekonder_kademe
        sekonder_top_yuk = gl[0]["sarim_yukseklik"]+gl[1]["sarim_yukseklik"]+gl[2]["sarim_yukseklik"]+gl[3]["sarim_yukseklik"]+gl[4]["sarim_yukseklik"]+gl[5]["sarim_yukseklik"]+gl[6]["sarim_yukseklik"]+gl[7]["sarim_yukseklik"]+gl[8]["sarim_yukseklik"]+gl[9]["sarim_yukseklik"]
        gl=self.group_name_list_sva1_kademe
        sva1_yuk = gl[0]["sarim_yukseklik"]+gl[1]["sarim_yukseklik"]+gl[2]["sarim_yukseklik"]+gl[3]["sarim_yukseklik"]+gl[4]["sarim_yukseklik"]+gl[5]["sarim_yukseklik"]+gl[6]["sarim_yukseklik"]+gl[7]["sarim_yukseklik"]+gl[8]["sarim_yukseklik"]+gl[9]["sarim_yukseklik"]
        gl=self.group_name_list_sva2_kademe
        sva2_yuk = gl[0]["sarim_yukseklik"]+gl[1]["sarim_yukseklik"]+gl[2]["sarim_yukseklik"]+gl[3]["sarim_yukseklik"]+gl[4]["sarim_yukseklik"]+gl[5]["sarim_yukseklik"]+gl[6]["sarim_yukseklik"]+gl[7]["sarim_yukseklik"]+gl[8]["sarim_yukseklik"]+gl[9]["sarim_yukseklik"]
        gl=self.group_name_list_sva3_kademe
        sva3_yuk = gl[0]["sarim_yukseklik"]+gl[1]["sarim_yukseklik"]+gl[2]["sarim_yukseklik"]+gl[3]["sarim_yukseklik"]+gl[4]["sarim_yukseklik"]+gl[5]["sarim_yukseklik"]+gl[6]["sarim_yukseklik"]+gl[7]["sarim_yukseklik"]+gl[8]["sarim_yukseklik"]+gl[9]["sarim_yukseklik"]
        gl=self.group_name_list_sva4_kademe
        sva4_yuk = gl[0]["sarim_yukseklik"]+gl[1]["sarim_yukseklik"]+gl[2]["sarim_yukseklik"]+gl[3]["sarim_yukseklik"]+gl[4]["sarim_yukseklik"]+gl[5]["sarim_yukseklik"]+gl[6]["sarim_yukseklik"]+gl[7]["sarim_yukseklik"]+gl[8]["sarim_yukseklik"]+gl[9]["sarim_yukseklik"]
        gl=self.group_name_list_sva5_kademe
        sva5_yuk = gl[0]["sarim_yukseklik"]+gl[1]["sarim_yukseklik"]+gl[2]["sarim_yukseklik"]+gl[3]["sarim_yukseklik"]+gl[4]["sarim_yukseklik"]+gl[5]["sarim_yukseklik"]+gl[6]["sarim_yukseklik"]+gl[7]["sarim_yukseklik"]+gl[8]["sarim_yukseklik"]+gl[9]["sarim_yukseklik"]
        gl=self.group_name_list_sva6_kademe
        sva6_yuk = gl[0]["sarim_yukseklik"]+gl[1]["sarim_yukseklik"]+gl[2]["sarim_yukseklik"]+gl[3]["sarim_yukseklik"]+gl[4]["sarim_yukseklik"]+gl[5]["sarim_yukseklik"]+gl[6]["sarim_yukseklik"]+gl[7]["sarim_yukseklik"]+gl[8]["sarim_yukseklik"]+gl[9]["sarim_yukseklik"]
        gl=self.group_name_list_sva7_kademe
        sva7_yuk = gl[0]["sarim_yukseklik"]+gl[1]["sarim_yukseklik"]+gl[2]["sarim_yukseklik"]+gl[3]["sarim_yukseklik"]+gl[4]["sarim_yukseklik"]+gl[5]["sarim_yukseklik"]+gl[6]["sarim_yukseklik"]+gl[7]["sarim_yukseklik"]+gl[8]["sarim_yukseklik"]+gl[9]["sarim_yukseklik"]
        gl=self.group_name_list_sva8_kademe
        sva8_yuk = gl[0]["sarim_yukseklik"]+gl[1]["sarim_yukseklik"]+gl[2]["sarim_yukseklik"]+gl[3]["sarim_yukseklik"]+gl[4]["sarim_yukseklik"]+gl[5]["sarim_yukseklik"]+gl[6]["sarim_yukseklik"]+gl[7]["sarim_yukseklik"]+gl[8]["sarim_yukseklik"]+gl[9]["sarim_yukseklik"]
        gl=self.group_name_list_sva9_kademe
        sva9_yuk = gl[0]["sarim_yukseklik"]+gl[1]["sarim_yukseklik"]+gl[2]["sarim_yukseklik"]+gl[3]["sarim_yukseklik"]+gl[4]["sarim_yukseklik"]+gl[5]["sarim_yukseklik"]+gl[6]["sarim_yukseklik"]+gl[7]["sarim_yukseklik"]+gl[8]["sarim_yukseklik"]+gl[9]["sarim_yukseklik"]
        gl=self.group_name_list_sva10_kademe
        sva10_yuk = gl[0]["sarim_yukseklik"]+gl[1]["sarim_yukseklik"]+gl[2]["sarim_yukseklik"]+gl[3]["sarim_yukseklik"]+gl[4]["sarim_yukseklik"]+gl[5]["sarim_yukseklik"]+gl[6]["sarim_yukseklik"]+gl[7]["sarim_yukseklik"]+gl[8]["sarim_yukseklik"]+gl[9]["sarim_yukseklik"]
        if self.ui.comboBox_sactipi.currentIndex()==0 and self.ui.radioButton_kademeli.isChecked():
            bosluk = hp.bosluk_hesap_1(karkas_en=self.ui.doubleSpinBox_karkas_en.value(),
            primer_top_yuk=primer_top_yuk,sekonder_top_yuk =sekonder_top_yuk ,primer_izolasyon=self.primer_izolasyon)
            self.ui.doubleSpinBox_nuvebosluk.setEnabled(False)
        elif self.ui.comboBox_sactipi.currentIndex()==0 and self.ui.radioButton_kademeli.isChecked()==False:
            self.ui.doubleSpinBox_nuvebosluk.setEnabled(False)
            bosluk=hp.bosluk_hesap_2(
                karkas_en=self.ui.doubleSpinBox_karkas_en.value(),
                primer_top_yuk= primer_top_yuk,
                sekonder_top_yuk=sekonder_top_yuk,
                sva1_yuk= sva1_yuk,sva2_yuk= sva2_yuk,sva3_yuk= sva3_yuk,sva4_yuk= sva4_yuk,sva5_yuk= sva5_yuk,
                sva6_yuk= sva6_yuk,sva7_yuk= sva7_yuk,sva8_yuk= sva8_yuk,sva9_yuk= sva9_yuk,sva10_yuk= sva10_yuk,toplam_izolasyon=self.toplam_izolasyon)
        elif self.ui.comboBox_sactipi.currentIndex()==1 and self.ui.radioButton_kademeli.isChecked():
            bosluk = hp.bosluk_hesap_3(karkas_en=self.ui.doubleSpinBox_karkas_en.value(),
            primer_top_yuk=primer_top_yuk,sekonder_top_yuk=sekonder_top_yuk,primer_izolasyon=self.primer_izolasyon,kesme_sac_bosluk=self.ui.doubleSpinBox_nuvebosluk.value())
            self.ui.doubleSpinBox_nuvebosluk.setEnabled(True)
        else:
            bosluk=0
        self.ui.doubleSpinBox_8.setValue(bosluk)
        if bosluk>0 and self.ui.comboBox_sactipi.currentIndex()==0:
            self.ui.comboBox_2.setCurrentIndex(0)
            self.ui.label_Ac_error_2.setVisible(False)
            self.ui.label_Ac_ok_2.setVisible(True)
        elif bosluk<0 and self.ui.comboBox_sactipi.currentIndex()==0:
            self.ui.comboBox_2.setCurrentIndex(1)
            self.ui.label_Ac_error_2.setVisible(True)
            self.ui.label_Ac_ok_2.setVisible(False)
        elif self.ui.comboBox_sactipi.currentIndex()==1:
            self.ui.comboBox_2.setCurrentIndex(2)
            self.ui.label_Ac_error_2.setVisible(False)
            self.ui.label_Ac_ok_2.setVisible(False)
        else:
            pass
    # ======================  agırlık  hesabı ========================= 
    def agirlik_hesapla(self):
        gl=self.group_name_list_primer_kademe
        primer_al_agirlik=0
        primer_cu_agirlik=0
        for i in range (0,10):
            if gl[i]["teltipi"]=="Al":
                primer_al_agirlik +=gl[i]["tel_agirlik"]
            elif gl[i]["teltipi"]=="Cu":
                primer_cu_agirlik += gl[i]["tel_agirlik"]

        primer_toplam_agirlik = gl[0]["tel_agirlik"]+gl[1]["tel_agirlik"]+gl[2]["tel_agirlik"]+gl[3]["tel_agirlik"]+gl[4]["tel_agirlik"]+gl[5]["tel_agirlik"]+gl[6]["tel_agirlik"]+gl[7]["tel_agirlik"]+gl[8]["tel_agirlik"]+gl[9]["tel_agirlik"]

        
        gl=self.group_name_list_sekonder_kademe
        sekonder_al_agirlik = 0
        sekonder_cu_agirlik = 0
        for i in range(0, 10):
            if gl[i]["teltipi"] == "Al":
                sekonder_al_agirlik += gl[i]["tel_agirlik"]
            elif gl[i]["teltipi"] == "Cu":
                sekonder_cu_agirlik += gl[i]["tel_agirlik"]
        sekonder_toplam_agirlik = gl[0]["tel_agirlik"]+gl[1]["tel_agirlik"]+gl[2]["tel_agirlik"]+gl[3]["tel_agirlik"]+gl[4]["tel_agirlik"]+gl[5]["tel_agirlik"]+gl[6]["tel_agirlik"]+gl[7]["tel_agirlik"]+gl[8]["tel_agirlik"]+gl[9]["tel_agirlik"]
        
        
        gl=self.group_name_list_sva1_kademe
        sva1_cu_agirlik = 0
        sva1_al_agirlik = 0
        for i in range(0, 10):
            if gl[i]["teltipi"] == "Al":
                sva1_al_agirlik += gl[i]["tel_agirlik"]
            elif gl[i]["teltipi"] == "Cu":
                sva1_cu_agirlik  += gl[i]["tel_agirlik"]
        sva1_toplam_agirlik = gl[0]["tel_agirlik"]+gl[1]["tel_agirlik"]+gl[2]["tel_agirlik"]+gl[3]["tel_agirlik"]+gl[4]["tel_agirlik"]+gl[5]["tel_agirlik"]+gl[6]["tel_agirlik"]+gl[7]["tel_agirlik"]+gl[8]["tel_agirlik"]+gl[9]["tel_agirlik"]
        

        gl=self.group_name_list_sva2_kademe
        sva2_cu_agirlik = 0
        sva2_al_agirlik = 0
        for i in range(0, 10):
            if gl[i]["teltipi"] == "Al":
                sva2_al_agirlik += gl[i]["tel_agirlik"]
            elif gl[i]["teltipi"] == "Cu":
                sva2_cu_agirlik  += gl[i]["tel_agirlik"]
        sva2_toplam_agirlik = gl[0]["tel_agirlik"]+gl[1]["tel_agirlik"]+gl[2]["tel_agirlik"]+gl[3]["tel_agirlik"]+gl[4]["tel_agirlik"]+gl[5]["tel_agirlik"]+gl[6]["tel_agirlik"]+gl[7]["tel_agirlik"]+gl[8]["tel_agirlik"]+gl[9]["tel_agirlik"]
        

        gl=self.group_name_list_sva3_kademe
        sva3_cu_agirlik = 0
        sva3_al_agirlik = 0
        for i in range(0, 10):
            if gl[i]["teltipi"] == "Al":
                sva3_al_agirlik += gl[i]["tel_agirlik"]
            elif gl[i]["teltipi"] == "Cu":
                sva3_cu_agirlik  += gl[i]["tel_agirlik"]
        sva3_toplam_agirlik = gl[0]["tel_agirlik"]+gl[1]["tel_agirlik"]+gl[2]["tel_agirlik"]+gl[3]["tel_agirlik"]+gl[4]["tel_agirlik"]+gl[5]["tel_agirlik"]+gl[6]["tel_agirlik"]+gl[7]["tel_agirlik"]+gl[8]["tel_agirlik"]+gl[9]["tel_agirlik"]
        

        gl=self.group_name_list_sva4_kademe
        sva4_cu_agirlik = 0
        sva4_al_agirlik = 0
        for i in range(0, 10):
            if gl[i]["teltipi"] == "Al":
                sva4_al_agirlik += gl[i]["tel_agirlik"]
            elif gl[i]["teltipi"] == "Cu":
                sva4_cu_agirlik  += gl[i]["tel_agirlik"]
        sva4_toplam_agirlik = gl[0]["tel_agirlik"]+gl[1]["tel_agirlik"]+gl[2]["tel_agirlik"]+gl[3]["tel_agirlik"]+gl[4]["tel_agirlik"]+gl[5]["tel_agirlik"]+gl[6]["tel_agirlik"]+gl[7]["tel_agirlik"]+gl[8]["tel_agirlik"]+gl[9]["tel_agirlik"]
        

        gl=self.group_name_list_sva5_kademe
        sva5_cu_agirlik = 0
        sva5_al_agirlik = 0
        for i in range(0, 10):
            if gl[i]["teltipi"] == "Al":
                sva5_al_agirlik += gl[i]["tel_agirlik"]
            elif gl[i]["teltipi"] == "Cu":
                sva5_cu_agirlik  += gl[i]["tel_agirlik"]
        sva5_toplam_agirlik = gl[0]["tel_agirlik"]+gl[1]["tel_agirlik"]+gl[2]["tel_agirlik"]+gl[3]["tel_agirlik"]+gl[4]["tel_agirlik"]+gl[5]["tel_agirlik"]+gl[6]["tel_agirlik"]+gl[7]["tel_agirlik"]+gl[8]["tel_agirlik"]+gl[9]["tel_agirlik"]
        

        gl=self.group_name_list_sva6_kademe
        sva6_cu_agirlik = 0
        sva6_al_agirlik = 0
        for i in range(0, 10):
            if gl[i]["teltipi"] == "Al":
                sva6_al_agirlik += gl[i]["tel_agirlik"]
            elif gl[i]["teltipi"] == "Cu":
                sva6_cu_agirlik  += gl[i]["tel_agirlik"]
        sva6_toplam_agirlik = gl[0]["tel_agirlik"]+gl[1]["tel_agirlik"]+gl[2]["tel_agirlik"]+gl[3]["tel_agirlik"]+gl[4]["tel_agirlik"]+gl[5]["tel_agirlik"]+gl[6]["tel_agirlik"]+gl[7]["tel_agirlik"]+gl[8]["tel_agirlik"]+gl[9]["tel_agirlik"]
        

        gl=self.group_name_list_sva7_kademe
        sva7_cu_agirlik = 0
        sva7_al_agirlik = 0
        for i in range(0, 10):
            if gl[i]["teltipi"] == "Al":
                sva7_al_agirlik += gl[i]["tel_agirlik"]
            elif gl[i]["teltipi"] == "Cu":
                sva7_cu_agirlik  += gl[i]["tel_agirlik"]
        sva7_toplam_agirlik = gl[0]["tel_agirlik"]+gl[1]["tel_agirlik"]+gl[2]["tel_agirlik"]+gl[3]["tel_agirlik"]+gl[4]["tel_agirlik"]+gl[5]["tel_agirlik"]+gl[6]["tel_agirlik"]+gl[7]["tel_agirlik"]+gl[8]["tel_agirlik"]+gl[9]["tel_agirlik"]
        

        gl=self.group_name_list_sva8_kademe
        sva8_cu_agirlik = 0
        sva8_al_agirlik = 0
        for i in range(0, 10):
            if gl[i]["teltipi"] == "Al":
                sva8_al_agirlik += gl[i]["tel_agirlik"]
            elif gl[i]["teltipi"] == "Cu":
                sva8_cu_agirlik  += gl[i]["tel_agirlik"]
        sva8_toplam_agirlik = gl[0]["tel_agirlik"]+gl[1]["tel_agirlik"]+gl[2]["tel_agirlik"]+gl[3]["tel_agirlik"]+gl[4]["tel_agirlik"]+gl[5]["tel_agirlik"]+gl[6]["tel_agirlik"]+gl[7]["tel_agirlik"]+gl[8]["tel_agirlik"]+gl[9]["tel_agirlik"]
        

        gl=self.group_name_list_sva9_kademe
        sva9_cu_agirlik = 0
        sva9_al_agirlik = 0
        for i in range(0, 10):
            if gl[i]["teltipi"] == "Al":
                sva9_al_agirlik += gl[i]["tel_agirlik"]
            elif gl[i]["teltipi"] == "Cu":
                sva9_cu_agirlik  += gl[i]["tel_agirlik"]
        sva9_toplam_agirlik = gl[0]["tel_agirlik"]+gl[1]["tel_agirlik"]+gl[2]["tel_agirlik"]+gl[3]["tel_agirlik"]+gl[4]["tel_agirlik"]+gl[5]["tel_agirlik"]+gl[6]["tel_agirlik"]+gl[7]["tel_agirlik"]+gl[8]["tel_agirlik"]+gl[9]["tel_agirlik"]
        

        gl=self.group_name_list_sva10_kademe
        sva10_cu_agirlik = 0
        sva10_al_agirlik = 0
        for i in range(0, 10):
            if gl[i]["teltipi"] == "Al":
                sva10_al_agirlik += gl[i]["tel_agirlik"]
            elif gl[i]["teltipi"] == "Cu":
                sva10_cu_agirlik  += gl[i]["tel_agirlik"]
        sva10_toplam_agirlik = gl[0]["tel_agirlik"]+gl[1]["tel_agirlik"]+gl[2]["tel_agirlik"]+gl[3]["tel_agirlik"]+gl[4]["tel_agirlik"]+gl[5]["tel_agirlik"]+gl[6]["tel_agirlik"]+gl[7]["tel_agirlik"]+gl[8]["tel_agirlik"]+gl[9]["tel_agirlik"]
        
        
        self.ui.doubleSpinBox_toplamagirlik_al.setValue(primer_al_agirlik+sekonder_al_agirlik+sva1_al_agirlik+sva2_al_agirlik+sva3_al_agirlik+sva4_al_agirlik+sva5_al_agirlik+sva6_al_agirlik+sva7_al_agirlik+sva8_al_agirlik+sva9_al_agirlik+sva10_al_agirlik)
        
        self.ui.doubleSpinBox_toplamagirlik_cu.setValue(primer_cu_agirlik+sekonder_cu_agirlik+sva1_cu_agirlik+sva2_cu_agirlik+sva3_cu_agirlik+sva4_cu_agirlik+sva5_cu_agirlik+sva6_cu_agirlik+sva7_cu_agirlik+sva8_cu_agirlik+sva9_cu_agirlik+sva10_cu_agirlik)

        self.ui.doubleSpinBox_primeragirlik_al.setValue(primer_al_agirlik)

        self.ui.doubleSpinBox_primeragirlik_cu.setValue(primer_cu_agirlik)

        self.ui.doubleSpinBox_sekonderagirlik_al.setValue(sekonder_al_agirlik+sva1_al_agirlik+sva2_al_agirlik+sva3_al_agirlik+sva4_al_agirlik+sva5_al_agirlik+sva6_al_agirlik+sva7_al_agirlik+sva8_al_agirlik+sva9_al_agirlik+sva10_al_agirlik)
        
        self.ui.doubleSpinBox_sekonderagirlik_cu.setValue(sekonder_cu_agirlik+sva1_cu_agirlik+sva2_cu_agirlik+sva3_cu_agirlik+sva4_cu_agirlik+sva5_cu_agirlik+sva6_cu_agirlik+sva7_cu_agirlik+sva8_cu_agirlik+sva9_cu_agirlik+sva10_cu_agirlik)
    # ======================  olcu hesabı  =========================
    def olcu_hesapla(self):
        #self.ui.doubleSpinBox_olcu_a.setValue(self.ui.doubleSpinBox_karkas_en.value()*3)
        #self.ui.doubleSpinBox_olcu_b.setValue(self.ui.doubleSpinBox_karkas_boy.value() +self.ui.doubleSpinBox_klemens_a_deg.value() + self.ui.doubleSpinBox_ayak_a_deg.value())
        #self.ui.doubleSpinBox_olcu_c.setValue(self.ui.doubleSpinBox_karkas_en.value()*2.5 +self.ui.doubleSpinBox_klemens_b_deg.value())
        a,b,c = hp.nuve_olcu_hesapla(
            karkas_en = self.ui.doubleSpinBox_karkas_en.value(),
            karkas_boy = self.ui.doubleSpinBox_karkas_boy.value(),
            klemens_a = self.ui.doubleSpinBox_klemens_a_deg.value(),
            klemens_b=self.ui.doubleSpinBox_klemens_b_deg.value(),
            ayak_a=self.ui.doubleSpinBox_ayak_a_deg.value()
            )
        self.ui.doubleSpinBox_olcu_a.setValue(a)
        self.ui.doubleSpinBox_olcu_b.setValue(  b)
        self.ui.doubleSpinBox_olcu_c.setValue(  c)
        self.trafoolcu_hesapla()    
    def trafoolcu_hesapla(self):
        if self.ui.comboBox_sactipi.currentIndex()==1:
            sactipi="kesme_sac"
            #self.ui.doubleSpinBox_trafoolcu_a.setValue( math.ceil(self.ui.doubleSpinBox_karkas_en.value()*2+2*(self.ui.doubleSpinBox_karkas_en.value()/2+self.ui.doubleSpinBox_nuvebosluk.value())))
            #self.ui.doubleSpinBox_trafoolcu_c.setValue( math.ceil(self.ui.doubleSpinBox_karkas_yukseklik.value()+self.ui.doubleSpinBox_karkas_en.value()*0.15 +self.ui.doubleSpinBox_karkas_en.value()))
            self.ui.doubleSpinBox_sacagirlik.setValue(0)
        else:
            sactipi="ei_sac"
            #self.ui.doubleSpinBox_trafoolcu_a.setValue( math.ceil(self.ui.doubleSpinBox_karkas_en.value()*3))
            #self.ui.doubleSpinBox_trafoolcu_c.setValue( math.ceil(self.ui.doubleSpinBox_karkas_en.value()*2.5 ))
            self.ui.doubleSpinBox_sacagirlik.setValue(hp.sac_agirlik(karkas_en=self.ui.doubleSpinBox_karkas_en.value(),karkas_boy=self.ui.doubleSpinBox_karkas_boy.value()))

        #self.ui.doubleSpinBox_trafoolcu_b.setValue(self.ui.doubleSpinBox_karkas_boy.value() +self.ui.doubleSpinBox_karkas_en.value())
        
        #self.ui.doubleSpinBox_trafoolcu_d.setValue(self.ui.doubleSpinBox_trafoolcu_a.value()-self.ui.doubleSpinBox_karkas_en.value()/2-10)
        #self.ui.doubleSpinBox_trafoolcu_e.setValue(self.ui.doubleSpinBox_karkas_boy.value()+self.ui.doubleSpinBox_karkas_en.value()/2+2+2)
        #self.ui.doubleSpinBox_trafoolcu_f.setValue(0)
        a,b,c,d,e,f  = hp.trafo_olcu_hesapla_1(
            sac_tipi =sactipi,
            karkas_en=self.ui.doubleSpinBox_karkas_en.value(),
            karkas_boy=self.ui.doubleSpinBox_karkas_boy.value(),
            karkas_yuk=self.ui.doubleSpinBox_karkas_yukseklik.value(),
            nuve_bosluk=self.ui.doubleSpinBox_nuvebosluk.value()
        )
        self.ui.doubleSpinBox_trafoolcu_a.setValue(a)
        self.ui.doubleSpinBox_trafoolcu_b.setValue(b)
        self.ui.doubleSpinBox_trafoolcu_c.setValue(c)
        self.ui.doubleSpinBox_trafoolcu_d.setValue(d)
        self.ui.doubleSpinBox_trafoolcu_e.setValue(e)
        self.ui.doubleSpinBox_trafoolcu_f.setValue(f)
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
        
        self.olcu_hesapla()
    def ayak_deger_al(self,ayak_name,a):
        self.ui.lineEdit_ayak_adi.setText(ayak_name)
        self.ui.doubleSpinBox_ayak_a_deg.setValue(a)
        
        self.olcu_hesapla()
    
    # ======================  Genel Fonksiyonlar =========================
    def hesap_sarim_uzunlugu(self):
        self.primer_sarim_yukseklik_toplam =0.0
        self.sekonder_sarim_yukseklik_toplam =0.0
        self.sva1_sarim_yukseklik_toplam=0.0
        self.sva2_sarim_yukseklik_toplam = 0.0
        self.sva3_sarim_yukseklik_toplam = 0.0
        self.sva4_sarim_yukseklik_toplam = 0.0
        self.sva5_sarim_yukseklik_toplam = 0.0
        self.sva6_sarim_yukseklik_toplam = 0.0
        self.sva7_sarim_yukseklik_toplam = 0.0
        self.sva8_sarim_yukseklik_toplam = 0.0
        self.sva9_sarim_yukseklik_toplam = 0.0
        self.sva10_sarim_yukseklik_toplam = 0.0
        for i in range(0,10):
            self.primer_sarim_yukseklik_toplam =self.primer_sarim_yukseklik_toplam + self.group_name_list_primer_kademe[i]["sarim_yukseklik"]
            self.sekonder_sarim_yukseklik_toplam =self.sekonder_sarim_yukseklik_toplam + self.group_name_list_sekonder_kademe[i]["sarim_yukseklik"]
            self.sva1_sarim_yukseklik_toplam =self.sva1_sarim_yukseklik_toplam + self.group_name_list_sva1_kademe[i]["sarim_yukseklik"]
            self.sva2_sarim_yukseklik_toplam =self.sva2_sarim_yukseklik_toplam + self.group_name_list_sva2_kademe[i]["sarim_yukseklik"]
            self.sva3_sarim_yukseklik_toplam =self.sva3_sarim_yukseklik_toplam + self.group_name_list_sva3_kademe[i]["sarim_yukseklik"]
            self.sva4_sarim_yukseklik_toplam =self.sva4_sarim_yukseklik_toplam + self.group_name_list_sva4_kademe[i]["sarim_yukseklik"]
            self.sva5_sarim_yukseklik_toplam =self.sva5_sarim_yukseklik_toplam + self.group_name_list_sva5_kademe[i]["sarim_yukseklik"]
            self.sva6_sarim_yukseklik_toplam =self.sva6_sarim_yukseklik_toplam + self.group_name_list_sva6_kademe[i]["sarim_yukseklik"]
            self.sva7_sarim_yukseklik_toplam =self.sva7_sarim_yukseklik_toplam + self.group_name_list_sva7_kademe[i]["sarim_yukseklik"]
            self.sva8_sarim_yukseklik_toplam =self.sva8_sarim_yukseklik_toplam + self.group_name_list_sva8_kademe[i]["sarim_yukseklik"]
            self.sva9_sarim_yukseklik_toplam =self.sva9_sarim_yukseklik_toplam + self.group_name_list_sva9_kademe[i]["sarim_yukseklik"]
            self.sva10_sarim_yukseklik_toplam =self.sva10_sarim_yukseklik_toplam + self.group_name_list_sva10_kademe[i]["sarim_yukseklik"]
    def hesap_1_gnl(self,gl,gl2,guc,frekans,gauss,karkas_en,karkas_boy,karkas_yuk,verim,sarim,kademe=1):
        self.hesap_sarim_uzunlugu()
        self.izolasyon_hesapla()
        self.voltaj_check(gl=gl)
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
                         kademe=kademe)

        self.karkas_hesaplama()
        self.bosluk_hesapla()
        self.agirlik_hesapla()
        self.olcu_hesapla()

        # Baslangıcta degerler sıfırlanır -------------------------
        for index in range(0, 10):
            gl2[index][0].setValue(gl[index]["voltaj"])
            gl2[index][1].setValue(gl[index]["spir1"])
            gl2[index][2].setValue(gl[index]["kesit1"])
            gl2[index][3].setValue(gl[index]["cap1"])
            gl2[index][4].setValue(gl[index]["akim1"])
            gl2[index][5].setValue(gl[index]["spir2"])
            gl2[index][6].setValue(gl[index]["kesit2"])
            gl2[index][7].setValue(gl[index]["cap2"])
            gl2[index][8].setValue(gl[index]["akim2"])
            gl2[index][9].setCurrentText(gl[index]["teltipi"])
            if gl2[index][0].value() > 0:
                gl2[index][11].setVisible(False)
                gl2[index][10].setVisible(True)
            else:
                gl2[index][11].setVisible(True)
                gl2[index][10].setVisible(False)
    def voltaj_check(self,gl):
        for i in range(0,9):
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

            self.kademe_goster(object=self.ui.comboBox_sek, group_list=self.kademe_list_4)


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

        for i in range (0,10):

            for key,val in list(vt.malzeme_listesi["teller"].items()):
                if self.group_name_list_primer_kademe[i][key]!="":
                  malzeme_listesix.append({self.group_name_list_primer_kademe[i][key]:self.group_name_list_primer_kademe[i][val]})

                if self.group_name_list_sekonder_kademe[i][key]!="":
                  malzeme_listesix.append({self.group_name_list_sekonder_kademe[i][key]:self.group_name_list_sekonder_kademe[i][val]})
                for y in range(0, 10):
                    if self.va_group_elementlist[i][y][key]!="":
                      malzeme_listesix.append({self.va_group_elementlist[i][y][key]:self.va_group_elementlist[i][y][val]})

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
            kesit1,kesit2, = db.get_karetell_byname( filter_value=mlz)
            
            if kesit1 != None:
                self.kesit_listesi.append(str(kesit1)+"x"+str(kesit2))
                kesit1,kesit2,=None,None
                continue
            kesit3,kesit4, = db.get_folyotell_byname(filter_value=mlz)
            if kesit3 != None:
                self.kesit_listesi.append(str(kesit3) + "x" + str(kesit4))
                kesit3,kesit4=None,None
                continue
            kesit5, = db.get_kapton_byname(filter_value=mlz)
            if  kesit5 != None:
                self.kesit_listesi.append(str( kesit5[0]))
                kesit5=None
                continue
        return self.tum_malzeme_listesi
        #self.group_name_list_sekonder_kademe
        #self.va_group_elementlist
    def printout_veri_kumesi(self):
        printout.primer_group_list =self.group_name_list_primer_kademe
        printout.sekonder_group_list = self.group_name_list_sekonder_kademe
        printout.va_group_list_1 = self.group_name_list_sva1_kademe
        printout.va_group_list_2 = self.group_name_list_sva2_kademe
        printout.va_group_list_3 = self.group_name_list_sva3_kademe
        printout.va_group_list_4 = self.group_name_list_sva4_kademe
        printout.va_group_list_5 = self.group_name_list_sva5_kademe
        printout.va_group_list_6 = self.group_name_list_sva6_kademe
        printout.va_group_list_7 = self.group_name_list_sva7_kademe
        printout.va_group_list_8 = self.group_name_list_sva8_kademe
        printout.va_group_list_9 = self.group_name_list_sva9_kademe
        printout.va_group_list_10 = self.group_name_list_sva10_kademe

        printout.va_group_list=[printout.va_group_list_1,printout.va_group_list_2,printout.va_group_list_3,printout.va_group_list_4,printout.va_group_list_5,printout.va_group_list_6,printout.va_group_list_7,printout.va_group_list_8,printout.va_group_list_9,printout.va_group_list_10]
        printout.guc = self.ui.doubleSpinBox_guc.value()
        printout.trafo_tipi = " Izolasyon Trafosu Mono Faz Hesap Ozeti"

        printout.primer_kademe = int(self.ui.comboBox.currentText())
        printout.sekonder_kademe = int(self.ui.comboBox_sek.currentText())
        printout.va_kademe = int(self.ui.comboBox_va.currentText())
        printout.va_altkademe = [int(self.ui.comboBox_sva1_kad.currentText()),
                                 int(self.ui.comboBox_sva2_kad.currentText()),
                                 int(self.ui.comboBox_sva3_kad.currentText()),
                                 int(self.ui.comboBox_sva4_kad.currentText()),
                                 int(self.ui.comboBox_sva5_kad.currentText()),
                                 int(self.ui.comboBox_sva6_kad.currentText()),
                                 int(self.ui.comboBox_sva7_kad.currentText()),
                                 int(self.ui.comboBox_sva8_kad.currentText()),
                                 int(self.ui.comboBox_sva9_kad.currentText()),
                                 int(self.ui.comboBox_sva10_kad.currentText())]
        printout.va_enabled = self.ui.radioButton_vadagilim.isChecked()
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
        printout.s_tel_al_ag = str(self.ui.doubleSpinBox_sekonderagirlik_al.value()) + " kg"
        printout.p_tel_cu_ag = str(self.ui.doubleSpinBox_primeragirlik_cu.value()) + " kg"
        printout.s_tel_cu_ag = str(self.ui.doubleSpinBox_sekonderagirlik_cu.value()) + " kg"
        printout.toplam_ag = str(self.ui.doubleSpinBox_toplamagirlik_al.value())
        printout.toplam_cu = str(self.ui.doubleSpinBox_toplamagirlik_cu.value())
        printout.karkas = str(self.ui.doubleSpinBox_karkas_en.value()) + " x " + str(
            self.ui.doubleSpinBox_karkas_boy.value()) + " x " + str(self.ui.doubleSpinBox_karkas_yukseklik.value())
        printout.trafo_olcu = str(self.ui.doubleSpinBox_trafoolcu_a.value()) + " x " + str(
            self.ui.doubleSpinBox_trafoolcu_b.value()) + " x " + str(self.ui.doubleSpinBox_trafoolcu_c.value())
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
        printout.sekonder_izo_deg = self.ui.doubleSpinBox_sekonder_izo_deg.value()
        printout.pri_sek_izo_deg = self.ui.doubleSpinBox_pri_sek_izo_deg.value()
        printout.ekran_izo_deg = self.ui.doubleSpinBox_ekran_izo_deg.value()
        printout.ekstra_izo_deg = self.ui.doubleSpinBox_ekstra_izo_deg.value()
        printout.primer_izo_tur = self.ui.doubleSpinBox_primer_izo_tur.value()
        printout.sekonder_izo_tur = self.ui.doubleSpinBox_sekonder_izo_tur.value()
        printout.pri_sek_izo_tur = self.ui.doubleSpinBox_pri_sek_izo_tur.value()
        printout.ekran_sec = self.ui.checkBox_ekran_sec.isChecked()
        printout.ekstra = self.ui.checkBox_ekstra.isChecked()
        printout.va_guclist.clear()
        printout.va_guclist.append(self.guclist_1[0].value())
        printout.va_guclist.append(self.guclist_1[1].value())
        printout.va_guclist.append(self.guclist_1[2].value())
        printout.va_guclist.append(self.guclist_1[3].value())
        printout.va_guclist.append(self.guclist_1[4].value())
        printout.va_guclist.append(self.guclist_1[5].value())
        printout.va_guclist.append(self.guclist_1[6].value())
        printout.va_guclist.append(self.guclist_1[7].value())
        printout.va_guclist.append(self.guclist_1[8].value())
        printout.va_guclist.append(self.guclist_1[9].value())
        printout.mlz_listesi=self.tum_malzeme_listesi
        printout.kesit_listesi=self.kesit_listesi
    def printout_report(self):
        self.printout_veri_kumesi()
        printout.izolasyon_mono_printout()


# def kademe_temizle(self,gl,kadame_sayisi=1):
    #         for kademe in range (kadame_sayisi,10):
    #             for index in range(0,58):
    #                 self.degerleri_temizle(gl[kademe][index])
# def object_multi_connect(self,object,arg):
    #     if object.metaObject().className()== "QDoubleSpinBox":
    #         return object.valueChanged.connect(arg)
    #     elif object.metaObject().className()== "QComboBox":
    #         return object.currentTextChanged.connect(arg)
    #     elif object.metaObject().className()== "QLineEdit":
    #         return object.textChanged.connect(arg)
    #     elif object.metaObject().className()== "QPushButton":
    #         return object.clicked.connect(arg)
    #     elif object.metaObject().className()== "QCheckBox":
    #         return object.stateChanged.connect(arg)
    #     elif object.metaObject().className()== "QLabel":
    #          return object.textChanged.connect(arg)
# def sender_object_index(self):
    #     sender = self.sender()
    #     index = sender.objectName().split("_")[len(sender.objectName().split("_"))-1]
    # def object_multi_value_read(self,object):
    #     if type(object)== str:
    #         return object
    #     elif object.metaObject().className()== "QDoubleSpinBox":
    #         return object.value()
    #     elif object.metaObject().className()== "QComboBox":
    #         return object.currentText()
    #     elif object.metaObject().className()== "QLineEdit":
    #         return object.text()
    #     elif object.metaObject().className()== "QPushButton":
    #         return True
    #     elif object.metaObject().className()== "QCheckBox":
    #         return True
    #     elif object.metaObject().className()== "QLabel":
    #        return True