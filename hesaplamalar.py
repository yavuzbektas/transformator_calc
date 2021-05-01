import math
import db_sql
db=db_sql.mydb()
# ======================  Formüller =========================
def spir_hesap_1(gerilim, frekans, gauss, karkas_en, karkas_boy, verim, Kf=4.44):
    # spir= gerilim * * (10 ** 8)) / (Kf * frekans * gauss *  (en * boy / 100))) / (verim / 100)
    return ((gerilim * (10 ** 8)) / (Kf * frekans * gauss * (karkas_en * karkas_boy / 100))) / (verim / 100)
def spir_hesap_2(gerilim, frekans, gauss, karkas_en, karkas_boy, verim, Kf=4.44):
    # spir= gerilim * * (10 ** 8)) / (Kf * frekans * gauss *  (en * boy / 100))) / (verim / 100)
    return ((gerilim * (10 ** 8)) / (Kf * frekans * gauss * (karkas_en * karkas_boy / 100)))
def spir_hesap_3(gerilim, frekans, gauss, karkas_en, karkas_boy, verim, Kf=4.44):
    return round(((gerilim * (10 ** 8)) / (Kf * frekans * gauss * (karkas_en * karkas_boy / 100)*math.sqrt(3)))/(verim/100) ,2)
def spir_hesap_4(gerilim, frekans, gauss, karkas_en, karkas_boy, verim, Kf=4.44):
    return round(((gerilim * (10 ** 8)) / (Kf * frekans * gauss * (karkas_en * karkas_boy / 100))) / (verim / 100),2)
def spir_hesap_5(gerilim, frekans, gauss, karkas_en, karkas_boy, verim, Kf=4.44):
    return round(((gerilim * (10 ** 8)) / (Kf * frekans * gauss * (karkas_en * karkas_boy / 100)*math.sqrt(3)))/ (verim / 100) ,0)
def spir_hesap_6(gerilim, frekans, gauss, karkas_en, karkas_boy, verim, Kf=4.44):
    return round(((gerilim * (10 ** 8)) / (Kf * frekans * gauss * (karkas_en * karkas_boy / 100))) / (verim / 100),0)
def akim_hesap_1(guc, gerilim):
    return guc / gerilim
def akim_hesap_2(kesit, akim_yogunlugu):
    return kesit * akim_yogunlugu
def akim_hesap_3(guc, gerilim):
    return guc / (gerilim*math.sqrt(3))
def akim_hesap_4(guc, gerilim):
    return guc / (gerilim*3)
def kesit_hesap_1(akim, akim_yogunlugu):  # akım yogunluguna göre
    return akim / akim_yogunlugu
def kesit_hesap_2(cap):  # çap değerine göre
    return cap ** 2 * math.pi / 4
def kesit_hesap_3(kenar1, kenar2):
    return kenar1 * kenar2
def cap_hesap_1(kesit):
    return math.sqrt(kesit * 4 / math.pi)
def akim_yogunlugu_1(tel_turu, cu_par=3, cu_yog=8700, al_par=1.6, al_yog=2700, dig_par=1, dig_yog=8700):
    if tel_turu == "Cu":
        global akim_yogunlugu
        akim_yogunlugu = cu_par
        tel_yogunluk = cu_yog
    elif tel_turu == "Al":
        akim_yogunlugu = al_par
        tel_yogunluk = al_yog
    elif tel_turu == "Dg":
        akim_yogunlugu = dig_par
        tel_yogunluk = dig_yog
    else:
        akim_yogunlugu = al_par
    return akim_yogunlugu
def tel_yogunlugu_1(tel_turu, cu_yog=8700, al_yog=2700, dig_yog=8700):
    if tel_turu == "Cu":
        tel_yogunluk = cu_yog
    elif tel_turu == "Al":
        tel_yogunluk = al_yog
    elif tel_turu == "Dg":
        tel_yogunluk = dig_yog
    else:
        tel_yogunluk=al_yog
    return tel_yogunluk
def karkas_yuk(karkas_en):
    return karkas_en * 1.5 - math.floor(karkas_en * 0.15)
def karkas_yuk_2(karkas_en):
    return karkas_en * 3 - math.floor(karkas_en * 0.15)
def karkas_Ac_oto(c, guc, frekans):
    return c * math.sqrt(guc / (2 * frekans))
def karkas_Ac_oto_2(c, guc, frekans):
    return c * math.sqrt(guc / (3 * frekans))
def karkas_Ac(karkas_en, karkas_boy):
    return karkas_en * karkas_boy / 100
def tel_yukseklik_hesap_1(tel_cap, karetel_yuk1, karetel_yuk2, karetel_yuk3, karetel_yuk4, folyo_yuk1, folyo_yuk2,
                          folyo_yuk3, folyo_yuk4, kapton1, kapton2, kapton3, kapton4):
    yukseklik = tel_cap + (karetel_yuk1 + karetel_yuk2 + karetel_yuk3 + karetel_yuk4) * 1.0625 + (
                folyo_yuk1 + folyo_yuk2 + folyo_yuk3 + folyo_yuk4) + (kapton1 + kapton2 + kapton3 + kapton4)
    return yukseklik
def tel_en_hesap_1(tel_cap, karetel_en1, karetel_en2, karetel_en3, karetel_en4, folyo_en1, folyo_en2, folyo_en3,
                   folyo_en4):
    en = tel_cap  + (karetel_en1 + karetel_en2 + karetel_en3 + karetel_en4) * 1.0625 + (
                folyo_en1 + folyo_en2 + folyo_en3 + folyo_en4)
    return en
def spir_kat_hesap_1(karkas_yuk, tel_en):
    return math.floor(karkas_yuk / tel_en)
def kat_sayisi_hesap_1(spir, spir_kat):
    if spir_kat>0 :
        return math.ceil(spir / spir_kat)
    else:
        return 0

def kat_sayisi_hesap_2(tel_spir_n, tel_spri_n_1, kat_bosluk_n_1, tel_en, spir_kat):
    try:
        sonuc= math.ceil((tel_spir_n - tel_spri_n_1 - math.floor(kat_bosluk_n_1 / tel_en)) / spir_kat)
    except Exception as error:
        sonuc=0
        print(error)
    return sonuc
def sarim_yüksekligi_hesap_1(tel_yuk, kat_sayisi):
    return tel_yuk * kat_sayisi
def son_kat_hesap_1(spir_2, spir_kat):
    return math.fmod(spir_2, spir_kat)
def son_kat_hesap_2(spir_2, spir_2_n_1):
    return (spir_2 - spir_2_n_1)
def son_kat_hesap_3(spir_2, spir_2_n_1, kat_bosluk_n_1, tel_en, spir_kat):
    return math.fmod(spir_2 - spir_2_n_1 - math.floor(kat_bosluk_n_1 / tel_en), spir_kat)
def kattaki_bosluk_hesap_1(karkas_yuk, tel_en, son_kat):
    return karkas_yuk - (tel_en * son_kat)
def kattaki_bosluk_hesap_2(kat_bosluk_n_1, tel_en, spir_2, spir_2_n_1):
    return (kat_bosluk_n_1 - (tel_en * (spir_2 - spir_2_n_1)))
def kattaki_bosluk_hesap_3(karkas_yuk, kat_bosluk_n_1, tel_en, spir_2, spir_2_n_1, spir_kat):
    return karkas_yuk - (math.fmod(spir_2 - spir_2_n_1 - math.floor(kat_bosluk_n_1 / tel_en), spir_kat) * tel_en)
def tel_uzunluk_hesap_1():
    pass
def tel_agirlik_hesap_1(tel_uzunluk, kesit_2, tel_yogunluk):
    return tel_uzunluk * kesit_2 / 1000000 * tel_yogunluk
def tel_agirlik_trifaz(sarim_agirlik):
    return sarim_agirlik * 3 # trifazlarda 3 faz oldugundan 3 ile carpılıyor
def primer_izolasyon_hesap(izo_deg, tur, kademe):
    return izo_deg * tur
def va_izolasyon_hesap(izo_deg, tur, kademe):
    return izo_deg * tur
def primer_sekonder_ara_izolasyon_hesap(izo_deg, tur):
    return izo_deg * tur
def bosluk_hesap_1(karkas_en, primer_top_yuk, sekonder_top_yuk, primer_izolasyon):
    return karkas_en / 2 - (primer_top_yuk + sekonder_top_yuk + karkas_en * 0.05 + primer_izolasyon)
def bosluk_hesap_2(karkas_en, primer_top_yuk, sekonder_top_yuk, sva1_yuk, sva2_yuk, sva3_yuk, sva4_yuk, sva5_yuk,
                   sva6_yuk, sva7_yuk, sva8_yuk, sva9_yuk, sva10_yuk, toplam_izolasyon):
    deger = karkas_en / 2 - (
                primer_top_yuk + sekonder_top_yuk + sva1_yuk + sva2_yuk + sva3_yuk + sva4_yuk + sva5_yuk + sva6_yuk + sva7_yuk + sva8_yuk + sva9_yuk + sva10_yuk +
                karkas_en * 0.05 + toplam_izolasyon)
    return deger
def bosluk_hesap_3(karkas_en, primer_top_yuk, sekonder_top_yuk, primer_izolasyon, kesme_sac_bosluk):
    return karkas_en / 2 - (
            primer_top_yuk + sekonder_top_yuk + karkas_en * 0.05 + primer_izolasyon - kesme_sac_bosluk)
def bosluk_hesap_4(karkas_en, primer_top_yuk, sekonder_top_yuk, toplam_izolasyon):
    deger = karkas_en / 2 - (
                primer_top_yuk + sekonder_top_yuk  + karkas_en * 0.05 + toplam_izolasyon)
    return deger
def sac_agirlik(karkas_en,karkas_boy,):
    if karkas_en>0.0:
        try:

            data, = db.show_nearest_value_tekfaz(filter_value=karkas_en*3)
            sac_agirlik=data[13]*karkas_boy*2/1000

        except Exception as err:
            print(err)
            return 0.0
    else:
        return 0.0
    return sac_agirlik
def sac_agirlik_trifaz(karkas_en,karkas_boy,):
    if karkas_en>0.0:
        try:

            data, = db.show_nearest_value_trifaz(filter_value=karkas_en*5)
            sac_agirlik=(data[13])*karkas_boy*2/1000

        except Exception as err:
            print(err)
            return 0.0
    else:
        return 0.0
    return sac_agirlik
def gauss_onerilen_hesapla(sac):
    if sac==0.3:
        gauss=15000
        c_deg=5.6
    elif sac==0.35:
        gauss=12000
        c_deg = 6
    elif sac==0.5:
        gauss=10500
        c_deg = 7
    else:
        gauss = 10500
        c_deg = 7
    return gauss,c_deg

def trafo_olcu_hesapla_1(sac_tipi,karkas_en,karkas_boy,karkas_yuk,nuve_bosluk):
    if sac_tipi=="ei_sac":
        olcu_a=math.ceil(karkas_en*2+2*(karkas_en/2+nuve_bosluk))
        olcu_c=math.ceil(karkas_yuk+karkas_en*0.15+karkas_en)
    elif sac_tipi=="kesme_sac":
        olcu_a=math.ceil(karkas_en*3)
        olcu_c=math.ceil(karkas_en*2.5)
    else:
        olcu_a=0
        olcu_c=0
    olcu_b = karkas_en+karkas_boy
    olcu_d=olcu_a-karkas_en/2-10
    olcu_e=karkas_boy+karkas_en/2+2+2
    olcu_f=0
    return (olcu_a,olcu_b,olcu_c,olcu_d,olcu_e,olcu_f)
def trafo_olcu_hesapla_2(sac_tipi,karkas_en,karkas_boy,karkas_yuk,nuve_bosluk,sarim_yukseklik_toplam,primer_izolasyon):
    if sac_tipi=="ei_sac":
        olcu_a=math.ceil(karkas_en*6 )
        olcu_c=math.ceil(3*karkas_en+2*karkas_en)
    elif sac_tipi=="kesme_sac":
        olcu_a=math.ceil(karkas_en*3+4*(karkas_en/2+nuve_bosluk)+2*(sarim_yukseklik_toplam +karkas_en*0.05+primer_izolasyon ))
        olcu_c=math.ceil(karkas_yuk+karkas_en*0.15+2*karkas_en)
    else:
        olcu_a=0
        olcu_c=0
    olcu_b = karkas_boy+2*karkas_en*0.7+2
    olcu_d=olcu_a-karkas_en
    olcu_e=karkas_boy+karkas_en*0.7+5+1
    olcu_f=0
    return (olcu_a,olcu_b,olcu_c,olcu_d,olcu_e,olcu_f)
def nuve_olcu_hesapla(karkas_en,karkas_boy,klemens_a,klemens_b,ayak_a):
    nuve_olcu_a=karkas_en*3
    nuve_olcu_b=karkas_boy +klemens_a + ayak_a
    nuve_olcu_c=karkas_en*2.5 +klemens_b
    return (nuve_olcu_a,nuve_olcu_b,nuve_olcu_c)
def yanSacAgirlik_hesap_1(sac_tipi,karkas_en,toplam_sarim_Yukseklik,primer_izolasyon,nuveBosluk):
    yanSac=0
    if sac_tipi=="ei_sac":
        yanSac=0
    elif sac_tipi=="kesme_sac":    
        yanSac=math.ceil(karkas_en+(2*(toplam_sarim_Yukseklik+karkas_en*0.05+primer_izolasyon + nuveBosluk)))
    else:
        yanSac=0
    return yanSac
def gobekSacAgirlik_hesap_1(sac_tipi,karkas_en,karkas_yuk):
    gobekSac=0
    if sac_tipi=="ei_sac":
        gobekSac=karkas_en*3
    elif sac_tipi=="kesme_sac":    
        gobekSac=karkas_yuk+karkas_en*0.15
    else:
        gobekSac=0
    return gobekSac
def kesmeSacAgirlik_hesap_1(sac_tipi,karkas_en,karkas_boy,nuve_bosluk,gobek_sac,yan_sac,sac_yogunluk):
    kesmeSac=0
    if sac_tipi=="ei_sac":
        kesmeSac=0
    elif sac_tipi=="kesme_sac":    
        kesmeSac=(3*((gobek_sac+(karkas_en*2))*karkas_boy*karkas_en)+(4*(yan_sac-karkas_en)*karkas_boy*karkas_en))/10**9*sac_yogunluk
    else:
        kesmeSac=0
    return kesmeSac    
def trafo_hesap_1( gl, guc, frekans, 
                   gauss, karkas_en, karkas_boy, 
                   karkas_yuk, verim, sarim, 
                   primer_sarim_yukseklik_toplam,
                   primer_izolasyon,
                   sva1_sarim_yukseklik_toplam=0,
                   sva1_izolasyon=0,
                   sva2_sarim_yukseklik_toplam=0,
                   sva2_izolasyon=0,
                   sva3_sarim_yukseklik_toplam=0,
                   sva3_izolasyon=0,
                   sva4_sarim_yukseklik_toplam=0,
                   sva4_izolasyon=0,
                   sva5_sarim_yukseklik_toplam=0,
                   sva5_izolasyon=0,
                   sva6_sarim_yukseklik_toplam=0,
                   sva6_izolasyon=0,
                   sva7_sarim_yukseklik_toplam=0,
                   sva7_izolasyon=0,
                   sva8_sarim_yukseklik_toplam=0,
                   sva8_izolasyon=0,
                   sva9_sarim_yukseklik_toplam=0,
                   sva9_izolasyon=0,
                   kademe=1):
        

        for i in range(0, 10):

            if gl[i]["voltaj"]> 0 :
                # Akım 1 Hesabı -------------------------
                gl[i]["akim1"]=akim_hesap_1(
                        guc=guc,
                        gerilim=gl[i]["voltaj"])
                # Kesit 1 Hesabı -------------------------
                gl[i]["kesit1"]=kesit_hesap_1(
                    akim=gl[i]["akim1"],
                    akim_yogunlugu=akim_yogunlugu_1(
                        tel_turu=gl[i]["teltipi"]))
                # cap 1 Hesabı -------------------------
                gl[i]["cap1"]=cap_hesap_1(
                    kesit=gl[i]["kesit1"])
                # spir 1 Hesabı -------------------------
                gl[i]["spir1"]=spir_hesap_2(
                    gerilim=gl[i]["voltaj"],
                    frekans=frekans,
                    gauss=gauss,
                    karkas_en=karkas_en,
                    karkas_boy=karkas_boy,
                    verim=verim)
                # spir 2 Hesabı -------------------------
                if gl[i]["check_spir_man"]==True:
                    pass
                else:
                    gl[i]["spir2"]=round(gl[i]["spir1"])
                # Kesit 2 Hesabı -------------------------
                gl[i]["kesit2"]= kesit_hesap_2(cap=gl[i]["mancap_1"]) + \
                    kesit_hesap_2(cap=gl[i]["mancap_2"]) +\
                    kesit_hesap_2(cap=gl[i]["mancap_3"]) +\
                    kesit_hesap_2(cap=gl[i]["mancap_4"]) +\
                    (gl[i]["folyotel11"] * gl[i]["folyotel12"]) +\
                    (gl[i]["folyotel21"] * gl[i]["folyotel22"]) +\
                    (gl[i]["folyotel31"] * gl[i]["folyotel32"]) +\
                    (gl[i]["folyotel41"] * gl[i]["folyotel42"]) +\
                    (gl[i]["karetel11"] * gl[i]["karetel12"]) +\
                    (gl[i]["karetel21"] * gl[i]["karetel22"]) +\
                    (gl[i]["karetel31"] * gl[i]["karetel32"]) +\
                    (gl[i]["karetel41"] * gl[i]["karetel42"])
                # Akım 2 Hesabı -------------------------
                gl[i]["akim2"]=akim_hesap_2(

                    kesit=gl[i]["kesit2"],
                    akim_yogunlugu=akim_yogunlugu_1(
                        tel_turu=gl[i]["teltipi"]))
                # cap 2 Hesabı -------------------------
                gl[i]["cap2"]= gl[i]["mancap_1"] + gl[i]["mancap_2"] + gl[i]["mancap_3"] + gl[i]["mancap_4"]
                # akım 2 ve kesit 2 kontrol -------------------------
                if gl[i]["kesit1"] <= gl[i]["kesit2"]:
                    gl[i]["kesit_ok"]=True
                    gl[i]["kesit_error"]=False
                else:
                    gl[i]["kesit_ok"]=False
                    gl[i]["kesit_error"]=True
                if gl[i]["akim1"] <= gl[i]["akim2"]:
                    gl[i]["akim_ok"]=True
                    gl[i]["akim_error"]=False
                else:
                    gl[i]["akim_ok"]=False
                    gl[i]["akim_error"]=True
                # -------------------------
                tel_cap = 0

                for tel_kademe in range(1, 5):

                    data = db.showfilter_tel_spir(filter_value=gl[i][f"mancap_{tel_kademe}"] , index=0)

                    if data == [] and gl[i][f"mancap_{tel_kademe}"] > 0:
                        tel_cap +=  (gl[i]["mancap_1"]) * 1.02
                    elif data != [] and gl[i][f"mancap_{tel_kademe}"] > 0:
                        tel_cap += data[0][4]
                
                # tel yüksekliği Hesabı -------------------------
                gl[i]["tel_yuk"]=tel_yukseklik_hesap_1(
                    tel_cap=tel_cap, karetel_yuk1=gl[i]["karetel12"],
                    karetel_yuk2=gl[i]["karetel22"],
                    karetel_yuk3=gl[i]["karetel32"], karetel_yuk4=gl[i]["karetel42"],
                    folyo_yuk1=gl[i]["folyotel12"], folyo_yuk2=gl[i]["folyotel22"],
                    folyo_yuk3=gl[i]["folyotel32"], folyo_yuk4=gl[i]["folyotel42"],
                    kapton1=gl[i]["kapton1"], kapton2=gl[i]["kapton2"],
                    kapton3=gl[i]["kapton3"], kapton4=gl[i]["kapton4"])
                # tel en Hesabı -------------------------
                gl[i]["tel_en"]= tel_en_hesap_1(
                    tel_cap=tel_cap,
                    karetel_en1=gl[i]["karetel11"],
                    karetel_en2=gl[i]["karetel21"],
                    karetel_en3=gl[i]["karetel31"], karetel_en4=gl[i]["karetel41"],
                    folyo_en1=gl[i]["folyotel11"], folyo_en2=gl[i]["folyotel21"],
                    folyo_en3=gl[i]["folyotel31"], folyo_en4=gl[i]["folyotel41"],
                    )

                if gl[i]["tel_en"] > 0:
                    # spir kat Hesabı -------------------------
                    gl[i]["spirkat"]=spir_kat_hesap_1(
                        karkas_yuk=karkas_yuk,
                        tel_en=gl[i]["tel_en"])

                    #  kat sayısı -------------------------------
                    if i == 0:
                        gl[i]["kat"]=kat_sayisi_hesap_1(
                            spir=gl[i]["spir2"],
                            spir_kat=gl[i]["spirkat"])

                    elif i > 0:
                        gl[i]["kat"]=kat_sayisi_hesap_2(
                            tel_spir_n=gl[i]["spir2"],
                            tel_spri_n_1=gl[i - 1]["spir2"],
                            kat_bosluk_n_1=gl[i - 1]["katbosluk"],
                            tel_en=gl[i]["tel_en"],
                            spir_kat=gl[i]["spirkat"]
                        )
                    # sarım yuksekliği  -------------------------
                    gl[i]["sarim_yukseklik"]=sarim_yüksekligi_hesap_1(
                        tel_yuk=gl[i]["tel_yuk"],
                        kat_sayisi=gl[i]["kat"])

                    # son kat
                    if i == 0:

                        try :
                            if math.fmod(gl[i]["spir2"], gl[i]["spirkat"]) == 0:
                                gl[i]["sonkat_spir"]=gl[i]["spirkat"]
                            else:
                                gl[i]["sonkat_spir"]=son_kat_hesap_1(
                                    spir_2=gl[i]["spir2"],
                                    spir_kat=gl[i]["spirkat"])
                        except Exception as err:
                            print(err)
                            # gl[i]["sonkat_spir"].setValue(math.fmod(gl[i]["spir2"].value(), gl[i]["spirkat"].value()))
                    elif i > 0:
                        if gl[i]["kat"] == 0:
                            gl[i]["sonkat_spir"]=son_kat_hesap_2(
                                spir_2=gl[i]["spir2"],
                                spir_2_n_1=gl[i - 1]["spir2"])
                            # gl[i]["sonkat_spir"].setValue(gl[i]["spir2"].value() - gl[i - 1]["spir2"])
                        else:
                            gl[i]["sonkat_spir"]=son_kat_hesap_3(
                                spir_2=gl[i]["spir2"],
                                spir_2_n_1=gl[i - 1]["spir2"],
                                kat_bosluk_n_1=gl[i - 1]["katbosluk"],
                                tel_en=gl[i]["tel_en"],
                                spir_kat=gl[i]["spirkat"])

                            # gl[i]["sonkat_spir"].setValue( math.fmod(gl[i]["spir2"].value()-gl[i-1]["spir2"] - math.floor(gl[i-1]["katbosluk"] / gl[i]["tel_en"].value()) ,gl[i]["spirkat"].value()))
                    # kattaki bosluk ---------------------------
                    if i == 0:
                        gl[i]["katbosluk"]=kattaki_bosluk_hesap_1(
                            karkas_yuk=karkas_yuk,
                            tel_en=gl[i]["tel_en"],
                            son_kat=gl[i]["sonkat_spir"]
                        )
                        # gl[i]["katbosluk"]setValue(self.ui.doubleSpinBox_karkas_yukseklik.value()-
                        #                                   (gl[i]["tel_en"].value()*gl[i]["sonkat_spir"]))
                    elif i > 0:
                        if gl[i]["kat"] == 0:
                            gl[i]["katbosluk"]=kattaki_bosluk_hesap_2(

                                kat_bosluk_n_1=gl[i - 1]["katbosluk"],
                                tel_en=gl[i]["tel_en"],
                                spir_2=gl[i]["spir2"],
                                spir_2_n_1=gl[i - 1]["spir2"]
                            )
                            # gl[i]["katbosluk"]setValue(gl[i-1]["katbosluk"]-(gl[i]["tel_en"].value()*(gl[i]["spir2"].value()-gl[i-1]["spir2"] )))
                        else:
                            gl[i]["katbosluk"]=kattaki_bosluk_hesap_3(
                                karkas_yuk=karkas_yuk,
                                spir_2=gl[i]["spir2"],
                                spir_2_n_1=gl[i - 1]["spir2"],
                                kat_bosluk_n_1=gl[i - 1]["katbosluk"],
                                tel_en=gl[i]["tel_en"],
                                spir_kat=gl[i]["spirkat"]

                            )
                            # gl[i]["katbosluk"]setValue(self.ui.doubleSpinBox_karkas_yukseklik.value()-
                            #                   math.fmod(gl[i]["spir2"].value()-gl[i-1]["spir2"] - math.floor(gl[i-1]["katbosluk"] /
                            #                                                                              gl[i]["tel_en"].value()) ,gl[i]["spirkat"].value())*gl[i]["tel_en"].value())
                    else:
                        pass

                    # tel uzunluk  ---------------------------
                    a0 = 2 * (karkas_en + karkas_boy) + 8 * 0.05 * karkas_en
                    a1 = a0 + 4 * gl[1]["tel_yuk"]
                    a2 = a0 + 4 * gl[2]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"]
                    a3 = a0 + 4 * gl[3]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"]
                    a4 = a0 + 4 * gl[4]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"]
                    a5 = a0 + 4 * gl[5]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * gl[3]["tel_yuk"] * gl[3]["kat"]
                    a6 = a0 + 4 * gl[6]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"]
                    a7 = a0 + 4 * gl[7]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * gl[5]["tel_yuk"] * gl[5]["kat"]
                    a8 = a0 + 4 * gl[8]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * gl[5]["tel_yuk"] * gl[5]["kat"] + 8 * gl[6]["tel_yuk"] * gl[6]["kat"]
                    a9 = a0 + 4 * gl[9]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * gl[5]["tel_yuk"] * gl[5]["kat"] + 8 * gl[6]["tel_yuk"] * gl[6]["kat"] + 8 * gl[7]["tel_yuk"] * gl[7]["kat"]
                    all_a = [0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
                    if i == 0:
                        gl[i]["tel_uzunluk"]=((gl[i]["kat"] - 1) * ((2 * (karkas_en + karkas_boy)) +
                                                        8 * karkas_en * 0.05 + 4 * gl[i]["tel_yuk"]) + \
                             (8 * gl[i]["tel_yuk"] * (gl[i]["kat"] - 1) * (gl[i]["kat"] - 2) / 2)) / 1000 *\
                            gl[i]["spirkat"] + \
                            ((2 * (karkas_en + karkas_boy)) + \
                             8 * karkas_en * 0.05 + 4 * gl[i]["tel_yuk"] + \
                             (8 * gl[i]["tel_yuk"] * (gl[i]["kat"] - 1))) / 1000 * gl[i]["sonkat_spir"]
                    elif i > 0:
                        if gl[i]["kat"] == 0:
                            gl[i]["tel_uzunluk"]=(all_a[i] + 8 * (gl[i - 1]["kat"] - 1) * gl[i - 1]["tel_yuk"]) * gl[i]["sonkat_spir"] / 1000
                        elif gl[i]["kat"] == 1:
                            gl[i]["tel_uzunluk"]=(all_a[i] + 8 * (gl[i - 1]["kat"] - 1) * gl[i - 1]["tel_yuk"]) *\
                                               math.floor(gl[i - 1]["katbosluk"] / gl[i]["tel_en"]) / 1000 + (
                                                       all_a[i] + 8 * (gl[i - 1]["kat"])
                                                       * gl[i - 1]["tel_yuk"]) * gl[i]["sonkat_spir"] / 1000

                        else:
                            gl[i]["tel_uzunluk"]=(all_a[i] + 8 * (gl[i - 1]["kat"] - 1) * gl[i - 1]["tel_yuk"]) *\
                                math.floor(gl[i - 1]["katbosluk"] / gl[i]["tel_en"]) / 1000 +\
                                ((gl[i]["kat"] - 1) * (
                                        all_a[i] + 8 * (gl[i - 1]["kat"]) * gl[i - 1]["tel_yuk"]) +
                                 4 * (gl[i]["kat"] - 1) * (gl[i]["kat"] - 2) * gl[i]["tel_yuk"]) * gl[i]["spirkat"] / 1000 + (all_a[i] + 8 * (gl[i - 1]["kat"]) * gl[i - 1]["tel_yuk"] + 8 * (
                                        gl[i]["kat"] - 1) *
                                   gl[i]["tel_yuk"]) * gl[i]["sonkat_spir"] / 1000


                    if sarim == "sekonder":

                        sek_a1 = a0 + 8 * primer_sarim_yukseklik_toplam + 8 * primer_izolasyon + 4 * gl[1]["tel_yuk"]
                        sek_a2 = a0 + 8 * primer_sarim_yukseklik_toplam + 4 * gl[2]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"]
                        sek_a3 = a0 + 8 * primer_sarim_yukseklik_toplam + 4 * gl[3]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"]
                        sek_a4 = a0 + 8 * primer_sarim_yukseklik_toplam + 4 * gl[4]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"]
                        sek_a5 = a0 + 8 * primer_sarim_yukseklik_toplam + 4 * gl[5]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                 gl[3]["tel_yuk"] * gl[3]["kat"]
                        sek_a6 = a0 + 8 * primer_sarim_yukseklik_toplam + 4 * gl[6]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                 gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"]
                        sek_a7 = a0 + 8 * primer_sarim_yukseklik_toplam + 4 * gl[7]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                 gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * \
                                 gl[5]["tel_yuk"] * gl[5]["kat"]
                        sek_a8 = a0 + 8 * primer_sarim_yukseklik_toplam + 4 * gl[8]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                 gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * \
                                 gl[5]["tel_yuk"] * gl[5]["kat"] + 8 * gl[6]["tel_yuk"] * gl[6]["kat"]
                        sek_a9 = a0 + 8 * primer_sarim_yukseklik_toplam + 4 * gl[9]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                 gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * \
                                 gl[5]["tel_yuk"] * gl[5]["kat"] + 8 * gl[6]["tel_yuk"] * gl[6]["kat"] + 8 * \
                                 gl[7]["tel_yuk"] * gl[7]["kat"]

                        all_sek_a = [0, sek_a1, sek_a2, sek_a3, sek_a4, sek_a5, sek_a6, sek_a7, sek_a8, sek_a9]
                        if i == 0:
                            gl[i]["tel_uzunluk"]=(
                                        (gl[i]["kat"] - 1) * (
                                        a0 + 8 * primer_sarim_yukseklik_toplam + 8 * primer_izolasyon + 4 *
                                        gl[i]["tel_yuk"])
                                        + 8 * gl[i]["tel_yuk"] * (gl[i]["kat"] - 1) * (gl[i]["kat"] - 2) / 2
                                )/ 1000 * gl[i]["spirkat"] + (
                                        a0 + 8 * primer_sarim_yukseklik_toplam + 8 * primer_izolasyon + 4 *
                                        gl[i]["tel_yuk"] + 8 * gl[i]["tel_yuk"] *
                                        (gl[i]["kat"] - 1)) / 1000 * gl[i]["sonkat_spir"]

                        elif i > 0:
                            if gl[i]["kat"] == 0:
                                gl[i]["tel_uzunluk"]=(all_sek_a[i] + 8 * (gl[i - 1]["kat"] - 1) * gl[i - 1]["tel_yuk"]) * gl[i]["sonkat_spir"] / 1000
                            elif gl[i]["kat"] == 1:
                                gl[i]["tel_uzunluk"]=(all_sek_a[i] + 8 * (gl[i - 1]["kat"] - 1) * gl[i - 1]["tel_yuk"]) *\
                                    math.floor(gl[i - 1]["katbosluk"] / gl[i]["tel_en"]) / 1000 + (
                                            all_sek_a[i] + 8 * (gl[i - 1]["kat"])
                                            * gl[i - 1]["tel_yuk"]) * gl[i]["sonkat_spir"] / 1000

                            else:
                                gl[i]["tel_uzunluk"]=(all_sek_a[i] + 8 * (gl[i - 1]["kat"] - 1) * gl[i - 1]["tel_yuk"]) *\
                                    math.floor(gl[i - 1]["katbosluk"] / gl[i]["tel_en"]) / 1000 +\
                                    ((gl[i]["kat"] - 1) * (
                                            all_sek_a[i] + 8 * (gl[i - 1]["kat"]) * gl[i - 1]["tel_yuk"]) +
                                     4 * (gl[i]["kat"] - 1) * (gl[i]["kat"] - 2) * gl[i]["tel_yuk"]) * gl[i]["spirkat"] / 1000 + \
                                    (all_sek_a[i] + 8 * (gl[i - 1]["kat"]) * gl[i - 1]["tel_yuk"] + 8 * (
                                            gl[i]["kat"] - 1) *
                                       gl[i]["tel_yuk"]) * gl[i]["sonkat_spir"] / 1000
                    elif sarim != "primer" and sarim != "sekonder":
                        all_sva1_a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        a_genel = 0
                        if sarim == "sva1":
                            a_genel = a0 + 8 * primer_sarim_yukseklik_toplam + 8 * primer_izolasyon
                            sva1_a1 = a0 + 8 * primer_sarim_yukseklik_toplam + 8 * primer_izolasyon + 4 * \
                                      gl[1]["tel_yuk"]
                            sva1_a2 = a0 + 8 * primer_sarim_yukseklik_toplam + 4 * gl[2]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"]
                            sva1_a3 = a0 + 8 * primer_sarim_yukseklik_toplam + 4 * gl[3]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"]
                            sva1_a4 = a0 + 8 * primer_sarim_yukseklik_toplam + 4 * gl[4]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"]
                            sva1_a5 = a0 + 8 * primer_sarim_yukseklik_toplam + 4 * gl[5]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"]
                            sva1_a6 = a0 + 8 * primer_sarim_yukseklik_toplam + 4 * gl[6]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"]
                            sva1_a7 = a0 + 8 * primer_sarim_yukseklik_toplam + 4 * gl[7]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * \
                                      gl[5]["tel_yuk"] * gl[5]["kat"]
                            sva1_a8 = a0 + 8 * primer_sarim_yukseklik_toplam + 4 * gl[8]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * \
                                      gl[5]["tel_yuk"] * gl[5]["kat"] + 8 * gl[6]["tel_yuk"] * gl[6]["kat"]
                            sva1_a9 = a0 + 8 * primer_sarim_yukseklik_toplam + 4 * gl[9]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * \
                                      gl[5]["tel_yuk"] * gl[5]["kat"] + 8 * gl[6]["tel_yuk"] * gl[6]["kat"] + 8 * \
                                      gl[7]["tel_yuk"] * gl[7]["kat"]

                            all_sva1_a = [0, sva1_a1, sva1_a2, sva1_a3, sva1_a4, sva1_a5, sva1_a6, sva1_a7, sva1_a8,
                                          sva1_a9]
                        if sarim == "sva2":
                            a_genel = a0 + 8 * primer_sarim_yukseklik_toplam + 8 * primer_izolasyon + \
                                      8 * sva1_sarim_yukseklik_toplam + 8 * sva1_izolasyon
                            sva2_a1 = a_genel + 4 * gl[1]["tel_yuk"]
                            sva2_a2 = a_genel + 4 * gl[2]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"]
                            sva2_a3 = a_genel + 4 * gl[3]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * \
                                      gl[1]["tel_yuk"] * gl[1]["kat"]
                            sva2_a4 = a_genel + 4 * gl[4]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"]
                            sva2_a5 = a_genel + 4 * gl[5]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"]
                            sva2_a6 = a_genel + 4 * gl[6]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"]
                            sva2_a7 = a_genel + 4 * gl[7]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * \
                                      gl[5]["tel_yuk"] * gl[5]["kat"]
                            sva2_a8 = a_genel + 4 * gl[8]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * gl[5]["tel_yuk"] * gl[5]["kat"] + 8 * gl[6]["tel_yuk"] \
                                      * gl[6]["kat"]
                            sva2_a9 = a_genel + 4 * gl[9]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * gl[5]["tel_yuk"] * gl[5]["kat"] + 8 * gl[6]["tel_yuk"] \
                                      * gl[6]["kat"] + 8 * gl[7]["tel_yuk"] * gl[7]["kat"]

                            all_sva1_a = [0, sva2_a1, sva2_a2, sva2_a3, sva2_a4, sva2_a5, sva2_a6, sva2_a7, sva2_a8,
                                          sva2_a9]
                        if sarim == "sva3":
                            a_genel = a0 + 8 * primer_sarim_yukseklik_toplam + 8 * primer_izolasyon + \
                                      8 * sva1_sarim_yukseklik_toplam + 8 * sva1_izolasyon + \
                                      8 * sva2_sarim_yukseklik_toplam + 8 * sva2_izolasyon
                            sva3_a1 = a_genel + 4 * gl[1]["tel_yuk"]
                            sva3_a2 = a_genel + 4 * gl[2]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"]
                            sva3_a3 = a_genel + 4 * gl[3]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * \
                                      gl[1]["tel_yuk"] * gl[1]["kat"]
                            sva3_a4 = a_genel + 4 * gl[4]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"]
                            sva3_a5 = a_genel + 4 * gl[5]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"]
                            sva3_a6 = a_genel + 4 * gl[6]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"]
                            sva3_a7 = a_genel + 4 * gl[7]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * \
                                      gl[5]["tel_yuk"] * gl[5]["kat"]
                            sva3_a8 = a_genel + 4 * gl[8]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * gl[5]["tel_yuk"] * gl[5]["kat"] + 8 * gl[6]["tel_yuk"] \
                                      * gl[6]["kat"]
                            sva3_a9 = a_genel + 4 * gl[9]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * gl[5]["tel_yuk"] * gl[5]["kat"] + 8 * gl[6]["tel_yuk"] \
                                      * gl[6]["kat"] + 8 * gl[7]["tel_yuk"] * gl[7]["kat"]

                            all_sva1_a = [0, sva3_a1, sva3_a2, sva3_a3, sva3_a4, sva3_a5, sva3_a6, sva3_a7, sva3_a8,
                                          sva3_a9]
                        if sarim == "sva4":
                            a_genel = a0 + 8 * primer_sarim_yukseklik_toplam + 8 * primer_izolasyon + \
                                      8 * sva1_sarim_yukseklik_toplam + 8 * sva1_izolasyon + \
                                      8 * sva2_sarim_yukseklik_toplam + 8 * sva2_izolasyon + \
                                      8 * sva3_sarim_yukseklik_toplam + 8 * sva3_izolasyon
                            sva4_a1 = a_genel + 4 * gl[1]["tel_yuk"]
                            sva4_a2 = a_genel + 4 * gl[2]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"]
                            sva4_a3 = a_genel + 4 * gl[3]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * \
                                      gl[1]["tel_yuk"] * gl[1]["kat"]
                            sva4_a4 = a_genel + 4 * gl[4]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"]
                            sva4_a5 = a_genel + 4 * gl[5]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"]
                            sva4_a6 = a_genel + 4 * gl[6]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"]
                            sva4_a7 = a_genel + 4 * gl[7]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * \
                                      gl[5]["tel_yuk"] * gl[5]["kat"]
                            sva4_a8 = a_genel + 4 * gl[8]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * gl[5]["tel_yuk"] * gl[5]["kat"] + 8 * gl[6]["tel_yuk"] \
                                      * gl[6]["kat"]
                            sva4_a9 = a_genel + 4 * gl[9]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * gl[5]["tel_yuk"] * gl[5]["kat"] + 8 * gl[6]["tel_yuk"] \
                                      * gl[6]["kat"] + 8 * gl[7]["tel_yuk"] * gl[7]["kat"]

                            all_sva1_a = [0, sva4_a1, sva4_a2, sva4_a3, sva4_a4, sva4_a5, sva4_a6, sva4_a7, sva4_a8,
                                          sva4_a9]
                        if sarim == "sva5":
                            a_genel = a0 + 8 * primer_sarim_yukseklik_toplam + 8 * primer_izolasyon + \
                                      8 * sva1_sarim_yukseklik_toplam + 8 * sva1_izolasyon + \
                                      8 * sva2_sarim_yukseklik_toplam + 8 * sva2_izolasyon + \
                                      8 * sva3_sarim_yukseklik_toplam + 8 * sva3_izolasyon + \
                                      8 * sva4_sarim_yukseklik_toplam + 8 * sva4_izolasyon

                            sva5_a1 = a_genel + 4 * gl[1]["tel_yuk"]
                            sva5_a2 = a_genel + 4 * gl[2]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"]
                            sva5_a3 = a_genel + 4 * gl[3]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * \
                                      gl[1]["tel_yuk"] * gl[1]["kat"]
                            sva5_a4 = a_genel + 4 * gl[4]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"]
                            sva5_a5 = a_genel + 4 * gl[5]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"]
                            sva5_a6 = a_genel + 4 * gl[6]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"]
                            sva5_a7 = a_genel + 4 * gl[7]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * \
                                      gl[5]["tel_yuk"] * gl[5]["kat"]
                            sva5_a8 = a_genel + 4 * gl[8]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * gl[5]["tel_yuk"] * gl[5]["kat"] + 8 * gl[6]["tel_yuk"] \
                                      * gl[6]["kat"]
                            sva5_a9 = a_genel + 4 * gl[9]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * gl[5]["tel_yuk"] * gl[5]["kat"] + 8 * gl[6]["tel_yuk"] \
                                      * gl[6]["kat"] + 8 * gl[7]["tel_yuk"] * gl[7]["kat"]

                            all_sva1_a = [0, sva5_a1, sva5_a2, sva5_a3, sva5_a4, sva5_a5, sva5_a6, sva5_a7, sva5_a8,
                                          sva5_a9]
                        if sarim == "sva6":
                            a_genel = a0 + 8 * primer_sarim_yukseklik_toplam + 8 * primer_izolasyon + \
                                      8 * sva1_sarim_yukseklik_toplam + 8 * sva1_izolasyon + \
                                      8 * sva2_sarim_yukseklik_toplam + 8 * sva2_izolasyon + \
                                      8 * sva3_sarim_yukseklik_toplam + 8 * sva3_izolasyon + \
                                      8 * sva4_sarim_yukseklik_toplam + 8 * sva4_izolasyon + \
                                      8 * sva5_sarim_yukseklik_toplam + 8 * sva5_izolasyon
                            sva6_a1 = a_genel + 4 * gl[1]["tel_yuk"]
                            sva6_a2 = a_genel + 4 * gl[2]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"]
                            sva6_a3 = a_genel + 4 * gl[3]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * \
                                      gl[1]["tel_yuk"] * gl[1]["kat"]
                            sva6_a4 = a_genel + 4 * gl[4]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"]
                            sva6_a5 = a_genel + 4 * gl[5]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"]
                            sva6_a6 = a_genel + 4 * gl[6]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"]
                            sva6_a7 = a_genel + 4 * gl[7]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * \
                                      gl[5]["tel_yuk"] * gl[5]["kat"]
                            sva6_a8 = a_genel + 4 * gl[8]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * gl[5]["tel_yuk"] * gl[5]["kat"] + 8 * gl[6]["tel_yuk"] \
                                      * gl[6]["kat"]
                            sva6_a9 = a_genel + 4 * gl[9]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * gl[5]["tel_yuk"] * gl[5]["kat"] + 8 * gl[6]["tel_yuk"] \
                                      * gl[6]["kat"] + 8 * gl[7]["tel_yuk"] * gl[7]["kat"]

                            all_sva1_a = [0, sva6_a1, sva6_a2, sva6_a3, sva6_a4, sva6_a5, sva6_a6, sva6_a7, sva6_a8,
                                          sva6_a9]
                        if sarim == "sva7":
                            a_genel = a0 + 8 * primer_sarim_yukseklik_toplam + 8 * primer_izolasyon + \
                                      8 * sva1_sarim_yukseklik_toplam + 8 * sva1_izolasyon + \
                                      8 * sva2_sarim_yukseklik_toplam + 8 * sva2_izolasyon + \
                                      8 * sva3_sarim_yukseklik_toplam + 8 * sva3_izolasyon + \
                                      8 * sva4_sarim_yukseklik_toplam + 8 * sva4_izolasyon + \
                                      8 * sva5_sarim_yukseklik_toplam + 8 * sva5_izolasyon + \
                                      8 * sva6_sarim_yukseklik_toplam + 8 * sva6_izolasyon
                            sva7_a1 = a_genel + 4 * gl[1]["tel_yuk"]
                            sva7_a2 = a_genel + 4 * gl[2]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"]
                            sva7_a3 = a_genel + 4 * gl[3]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * \
                                      gl[1]["tel_yuk"] * gl[1]["kat"]
                            sva7_a4 = a_genel + 4 * gl[4]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"]
                            sva7_a5 = a_genel + 4 * gl[5]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"]
                            sva7_a6 = a_genel + 4 * gl[6]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"]
                            sva7_a7 = a_genel + 4 * gl[7]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * \
                                      gl[5]["tel_yuk"] * gl[5]["kat"]
                            sva7_a8 = a_genel + 4 * gl[8]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * gl[5]["tel_yuk"] * gl[5]["kat"] + 8 * gl[6]["tel_yuk"] \
                                      * gl[6]["kat"]
                            sva7_a9 = a_genel + 4 * gl[9]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * gl[5]["tel_yuk"] * gl[5]["kat"] + 8 * gl[6]["tel_yuk"] \
                                      * gl[6]["kat"] + 8 * gl[7]["tel_yuk"] * gl[7]["kat"]

                            all_sva1_a = [0, sva7_a1, sva7_a2, sva7_a3, sva7_a4, sva7_a5, sva7_a6, sva7_a7, sva7_a8,
                                          sva7_a9]
                        if sarim == "sva8":
                            a_genel = a0 + 8 * primer_sarim_yukseklik_toplam + 8 * primer_izolasyon + \
                                      8 * sva1_sarim_yukseklik_toplam + 8 * sva1_izolasyon + \
                                      8 * sva2_sarim_yukseklik_toplam + 8 * sva2_izolasyon + \
                                      8 * sva3_sarim_yukseklik_toplam + 8 * sva3_izolasyon + \
                                      8 * sva4_sarim_yukseklik_toplam + 8 * sva4_izolasyon + \
                                      8 * sva5_sarim_yukseklik_toplam + 8 * sva5_izolasyon + \
                                      8 * sva6_sarim_yukseklik_toplam + 8 * sva6_izolasyon + \
                                      8 * sva7_sarim_yukseklik_toplam + 8 * sva7_izolasyon
                            sva8_a1 = a_genel + 4 * gl[1]["tel_yuk"]
                            sva8_a2 = a_genel + 4 * gl[2]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"]
                            sva8_a3 = a_genel + 4 * gl[3]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * \
                                      gl[1]["tel_yuk"] * gl[1]["kat"]
                            sva8_a4 = a_genel + 4 * gl[4]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"]
                            sva8_a5 = a_genel + 4 * gl[5]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"]
                            sva8_a6 = a_genel + 4 * gl[6]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"]
                            sva8_a7 = a_genel + 4 * gl[7]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * \
                                      gl[5]["tel_yuk"] * gl[5]["kat"]
                            sva8_a8 = a_genel + 4 * gl[8]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * gl[5]["tel_yuk"] * gl[5]["kat"] + 8 * gl[6]["tel_yuk"] \
                                      * gl[6]["kat"]
                            sva8_a9 = a_genel + 4 * gl[9]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * gl[5]["tel_yuk"] * gl[5]["kat"] + 8 * gl[6]["tel_yuk"] \
                                      * gl[6]["kat"] + 8 * gl[7]["tel_yuk"] * gl[7]["kat"]

                            all_sva1_a = [0, sva8_a1, sva8_a2, sva8_a3, sva8_a4, sva8_a5, sva8_a6, sva8_a7, sva8_a8,
                                          sva8_a9]
                        if sarim == "sva9":
                            a_genel = a0 + 8 * primer_sarim_yukseklik_toplam + 8 * primer_izolasyon + \
                                      8 * sva1_sarim_yukseklik_toplam + 8 * sva1_izolasyon + \
                                      8 * sva2_sarim_yukseklik_toplam + 8 * sva2_izolasyon + \
                                      8 * sva3_sarim_yukseklik_toplam + 8 * sva3_izolasyon + \
                                      8 * sva4_sarim_yukseklik_toplam + 8 * sva4_izolasyon + \
                                      8 * sva5_sarim_yukseklik_toplam + 8 * sva5_izolasyon + \
                                      8 * sva6_sarim_yukseklik_toplam + 8 * sva6_izolasyon + \
                                      8 * sva7_sarim_yukseklik_toplam + 8 * sva7_izolasyon + \
                                      8 * sva8_sarim_yukseklik_toplam + 8 * sva8_izolasyon
                            sva9_a1 = a_genel + 4 * gl[1]["tel_yuk"]
                            sva9_a2 = a_genel + 4 * gl[2]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"]
                            sva9_a3 = a_genel + 4 * gl[3]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * \
                                      gl[1]["tel_yuk"] * gl[1]["kat"]
                            sva9_a4 = a_genel + 4 * gl[4]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"]
                            sva9_a5 = a_genel + 4 * gl[5]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"]
                            sva9_a6 = a_genel + 4 * gl[6]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"]
                            sva9_a7 = a_genel + 4 * gl[7]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * \
                                      gl[5]["tel_yuk"] * gl[5]["kat"]
                            sva9_a8 = a_genel + 4 * gl[8]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                      gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * gl[5]["tel_yuk"] * gl[5]["kat"] + 8 * gl[6]["tel_yuk"] \
                                      * gl[6]["kat"]
                            sva9_a9 = a_genel + 4 * gl[9]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * gl[5]["tel_yuk"] * gl[5]["kat"] + 8 * gl[6]["tel_yuk"] \
                                      * gl[6]["kat"] + 8 * gl[7]["tel_yuk"] * gl[7]["kat"]

                            all_sva1_a = [0, sva9_a1, sva9_a2, sva9_a3, sva9_a4, sva9_a5, sva9_a6, sva9_a7, sva9_a8,
                                          sva9_a9]
                        if sarim == "sva10":
                            a_genel = a0 + 8 * primer_sarim_yukseklik_toplam + 8 * primer_izolasyon + \
                                      8 * sva1_sarim_yukseklik_toplam + 8 * sva1_izolasyon + \
                                      8 * sva2_sarim_yukseklik_toplam + 8 * sva2_izolasyon + \
                                      8 * sva3_sarim_yukseklik_toplam + 8 * sva3_izolasyon + \
                                      8 * sva4_sarim_yukseklik_toplam + 8 * sva4_izolasyon + \
                                      8 * sva5_sarim_yukseklik_toplam + 8 * sva5_izolasyon + \
                                      8 * sva6_sarim_yukseklik_toplam + 8 * sva6_izolasyon + \
                                      8 * sva7_sarim_yukseklik_toplam + 8 * sva7_izolasyon + \
                                      8 * sva8_sarim_yukseklik_toplam + 8 * sva8_izolasyon + \
                                      8 * sva9_sarim_yukseklik_toplam + 8 * sva9_izolasyon
                            sva10_a1 = a_genel + 4 * gl[1]["tel_yuk"]
                            sva10_a2 = a_genel + 4 * gl[2]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"]
                            sva10_a3 = a_genel + 4 * gl[3]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * \
                                       gl[1]["tel_yuk"] * gl[1]["kat"]
                            sva10_a4 = a_genel + 4 * gl[4]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"]
                            sva10_a5 = a_genel + 4 * gl[5]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                       gl[3]["tel_yuk"] * gl[3]["kat"]
                            sva10_a6 = a_genel + 4 * gl[6]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                       gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"]
                            sva10_a7 = a_genel + 4 * gl[7]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                       gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * \
                                       gl[5]["tel_yuk"] * gl[5]["kat"]
                            sva10_a8 = a_genel + 4 * gl[8]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                       gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * gl[5]["tel_yuk"] * gl[5]["kat"] + 8 * gl[6]["tel_yuk"] \
                                       * gl[6]["kat"]
                            sva10_a9 = a_genel + 4 * gl[9]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * gl[5]["tel_yuk"] * gl[5]["kat"] + 8 * gl[6]["tel_yuk"] \
                                       * gl[6]["kat"] + 8 * gl[7]["tel_yuk"] * gl[7]["kat"]

                            all_sva1_a = [0, sva10_a1, sva10_a2, sva10_a3, sva10_a4, sva10_a5, sva10_a6, sva10_a7,
                                          sva10_a8, sva10_a9]

                        if i == 0:
                            gl[i]["tel_uzunluk"]=(
                                        (gl[i]["kat"] - 1) * (
                                        a_genel + 4 * gl[i]["tel_yuk"])
                                        + 8 * gl[i]["tel_yuk"] * (gl[i]["kat"] - 1) * (
                                                gl[i]["kat"] - 2) / 2
                                ) / 1000 * gl[i]["spirkat"]+ (
                                        a_genel + 4 * gl[i]["tel_yuk"] + 8 * gl[i]["tel_yuk"] *
                                        (gl[i]["kat"] - 1)) / 1000 * gl[i]["sonkat_spir"]

                        elif i > 0:
                            if gl[i]["kat"] == 0:
                                gl[i]["tel_uzunluk"]=(all_sva1_a[i] + 8 * (gl[i - 1]["kat"] - 1) * gl[i - 1]["tel_yuk"]) *\
                                gl[i]["sonkat_spir"] / 1000
                            elif gl[i]["kat"] == 1:
                                gl[i]["tel_uzunluk"]=(all_sva1_a[i] + 8 * (gl[i - 1]["kat"] - 1) * gl[i - 1]["tel_yuk"]) *\
                                    math.floor(gl[i - 1]["katbosluk"] / gl[i]["tel_en"]) / 1000 + (\
                                            all_sva1_a[i] + 8 * (gl[i - 1]["kat"])\
                                            * gl[i - 1]["tel_yuk"]) * gl[i]["sonkat_spir"] / 1000

                            else:
                                gl[i]["tel_uzunluk"]=(all_sva1_a[i] + 8 * (gl[i - 1]["kat"] - 1) * gl[i - 1]["tel_yuk"]) *\
                                    math.floor(gl[i - 1]["katbosluk"] / gl[i]["tel_en"]) / 1000 + \
                                    ((gl[i]["kat"] - 1) * (all_sva1_a[i] + 8 * (gl[i - 1]["kat"]) * gl[i - 1]["tel_yuk"]) +\
                                     4 * (gl[i]["kat"] - 1) * (gl[i]["kat"] - 2) * gl[i]["tel_yuk"]) *\
                                    gl[i]["spirkat"] / 1000\
                                    + (all_sva1_a[i] + 8 * (gl[i - 1]["kat"]) * gl[i - 1]["tel_yuk"] + 8 * (\
                                            gl[i]["kat"] - 1) * gl[i]["tel_yuk"]) * gl[i]["sonkat_spir"] / 1000

                    # tel agirlik  ---------------------------
                    if gl[i]["tel_uzunluk"] != 0:
                        gl[i]["tel_agirlik"]=tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"], kesit_2=gl[i]["kesit2"],
                                                   tel_yogunluk=tel_yogunlugu_1(tel_turu=gl[i]["teltipi"]))

                        gl[i]["agr_tel_1"]=tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"], kesit_2=kesit_hesap_2(cap=gl[i]["mancap_1"]),
                                                   tel_yogunluk=tel_yogunlugu_1(tel_turu=gl[i]["teltipi"]))
                        gl[i]["agr_tel_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                 kesit_2=kesit_hesap_2(cap=gl[i]["mancap_2"]),
                                                                 tel_yogunluk=tel_yogunlugu_1(
                                                                     tel_turu=gl[i]["teltipi"]))
                        gl[i]["agr_tel_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                 kesit_2=kesit_hesap_2(cap=gl[i]["mancap_3"]),
                                                                 tel_yogunluk=tel_yogunlugu_1(
                                                                     tel_turu=gl[i]["teltipi"]))
                        gl[i]["agr_tel_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                 kesit_2=kesit_hesap_2(cap=gl[i]["mancap_4"]),
                                                                 tel_yogunluk=tel_yogunlugu_1(
                                                                     tel_turu=gl[i]["teltipi"]))
                        gl[i]["agr_karetel_1"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                 kesit_2=gl[i]["karetel11"] * gl[i]["karetel12"],
                                                                 tel_yogunluk=tel_yogunlugu_1(
                                                                     tel_turu=gl[i]["teltipi"]))
                        gl[i]["agr_karetel_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                     kesit_2=gl[i]["karetel21"] * gl[i]["karetel22"],
                                                                     tel_yogunluk=tel_yogunlugu_1(
                                                                         tel_turu=gl[i]["teltipi"]))
                        gl[i]["agr_karetel_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                     kesit_2=gl[i]["karetel31"] * gl[i]["karetel32"],
                                                                     tel_yogunluk=tel_yogunlugu_1(
                                                                         tel_turu=gl[i]["teltipi"]))
                        gl[i]["agr_karetel_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                     kesit_2=gl[i]["karetel41"] * gl[i]["karetel42"],
                                                                     tel_yogunluk=tel_yogunlugu_1(
                                                                         tel_turu=gl[i]["teltipi"]))
                        gl[i]["agr_folyo_1"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                     kesit_2=gl[i]["folyotel11"] * gl[i]["folyotel12"],
                                                                     tel_yogunluk=tel_yogunlugu_1(
                                                                         tel_turu=gl[i]["teltipi"]))
                        gl[i]["agr_folyo_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                   kesit_2=gl[i]["folyotel21"] * gl[i]["folyotel22"],
                                                                   tel_yogunluk=tel_yogunlugu_1(
                                                                       tel_turu=gl[i]["teltipi"]))
                        gl[i]["agr_folyo_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                   kesit_2=gl[i]["folyotel31"] * gl[i]["folyotel32"],
                                                                   tel_yogunluk=tel_yogunlugu_1(
                                                                       tel_turu=gl[i]["teltipi"]))
                        gl[i]["agr_folyo_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                   kesit_2=gl[i]["folyotel41"] * gl[i]["folyotel42"],
                                                                   tel_yogunluk=tel_yogunlugu_1(
                                                                       tel_turu=gl[i]["teltipi"]))
                        gl[i]["agr_kapton_1"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                   kesit_2=gl[i]["kapton1"],
                                                                   tel_yogunluk=1330)
                        gl[i]["agr_kapton_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                    kesit_2=gl[i]["kapton2"],
                                                                    tel_yogunluk=1330)
                        gl[i]["agr_kapton_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                    kesit_2=gl[i]["kapton3"],
                                                                    tel_yogunluk=1330)
                        gl[i]["agr_kapton_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                    kesit_2=gl[i]["kapton4"],
                                                                    tel_yogunluk=1330)
                    else:
                        gl[i]["tel_agirlik"]=0
                        gl[i]["agr_tel_1"] = 0
                        gl[i]["agr_tel_2"] = 0
                        gl[i]["agr_tel_3"] = 0
                        gl[i]["agr_tel_4"] = 0
                        gl[i]["agr_karetel_1"] = 0
                        gl[i]["agr_karetel_2"] = 0
                        gl[i]["agr_karetel_3"] = 0
                        gl[i]["agr_karetel_4"] = 0
                        gl[i]["agr_folyo_1"] = 0
                        gl[i]["agr_folyo_2"] = 0
                        gl[i]["agr_folyo_3"] = 0
                        gl[i]["agr_folyo_4"] = 0
                        gl[i]["agr_kapton_1"] = 0
                        gl[i]["agr_kapton_2"] = 0
                        gl[i]["agr_kapton_3"] = 0
                        gl[i]["agr_kapton_4"] = 0

            else:

                gl[i]["akim1"]=0
                gl[i]["kesit1"]=0
                gl[i]["cap1"]=0
                gl[i]["spir1"]=0
                gl[i]["cap2"]=0
                gl[i]["akim2"]=0
                gl[i]["spir2"]=0
                gl[i]["folyotel11"]=0
                gl[i]["folyotel12"]=0
                gl[i]["folyotel21"]=0
                gl[i]["folyotel22"]=0
                gl[i]["folyotel31"]=0
                gl[i]["folyotel32"]=0
                gl[i]["folyotel41"]=0
                gl[i]["folyotel42"]=0
                gl[i]["kapton1"]=0
                gl[i]["kapton2"]=0
                gl[i]["kapton3"]=0
                gl[i]["kapton4"]=0
                gl[i]["karetel11"]=0
                gl[i]["karetel12"]=0
                gl[i]["karetel21"]=0
                gl[i]["karetel22"]=0
                gl[i]["karetel31"]=0
                gl[i]["karetel32"]=0
                gl[i]["karetel41"]=0
                gl[i]["karetel42"]=0
                gl[i]["kesit2"]=0
                gl[i]["tel_en"]=0
                gl[i]["tel_yuk"]=0
                gl[i]["spirkat"]=0
                gl[i]["kat"]=0
                gl[i]["katbosluk"]=0
                gl[i]["tel_uzunluk"]=0
                gl[i]["tel_agirlik"]=0
                gl[i]["sarim_yukseklik"]=0
                gl[i]["sonkat_spir"]=0
                gl[i]["check_spir_man"] = False
                gl[i]["kesit_ok"]=False
                gl[i]["kesit_error"]=True
                gl[i]["akim_ok"]=False
                gl[i]["akim_error"]=True
                gl[i]["mancap_1"]=0
                gl[i]["mancap_2"]=0
                gl[i]["mancap_3"]=0
                gl[i]["mancap_4"]=0
                gl[i]["mlz_tel_1"] = ""
                gl[i]["mlz_tel_2"] = ""
                gl[i]["mlz_tel_3"] =  ""
                gl[i]["mlz_tel_4"] =  ""
                gl[i]["mlz_karetel_1"] =  ""
                gl[i]["mlz_karetel_2"] =  ""
                gl[i]["mlz_karetel_3"] =  ""
                gl[i]["mlz_karetel_4"] =  ""
                gl[i]["mlz_folyotel_1"] =  ""
                gl[i]["mlz_folyotel_2"] =  ""
                gl[i]["mlz_folyotel_3"] =  ""
                gl[i]["mlz_folyotel_4"] =  ""
                gl[i]["mlz_kapton_1"] =  ""
                gl[i]["mlz_kapton_2"] =  ""
                gl[i]["mlz_kapton_3"] =  ""
                gl[i]["mlz_kapton_4"] =  ""
                gl[i]["gb_check_tel_1"] =  False
                gl[i]["gb_check_tel_2"] =  False
                gl[i]["gb_check_tel_3"] =  False
                gl[i]["gb_check_tel_4"] =  False
                gl[i]["gb_check_karetel_1"]= False
                gl[i]["gb_check_karetel_2"]= False
                gl[i]["gb_check_karetel_3"]= False
                gl[i]["gb_check_karetel_4"]= False
                gl[i]["gb_check_folyotel_1"]= False
                gl[i]["gb_check_folyotel_2"]= False
                gl[i]["gb_check_folyotel_3"]= False
                gl[i]["gb_check_folyotel_4"]= False
                gl[i]["gb_check_kapton_1"]= False
                gl[i]["gb_check_kapton_2"]= False
                gl[i]["gb_check_kapton_3"]= False
                gl[i]["gb_check_kapton_4"]= False
                gl[i]["tel_agirlik"] = 0
                gl[i]["agr_tel_1"] = 0
                gl[i]["agr_tel_2"] = 0
                gl[i]["agr_tel_3"] = 0
                gl[i]["agr_tel_4"] = 0
                gl[i]["agr_karetel_1"] = 0
                gl[i]["agr_karetel_2"] = 0
                gl[i]["agr_karetel_3"] = 0
                gl[i]["agr_karetel_4"] = 0
                gl[i]["agr_folyo_1"] = 0
                gl[i]["agr_folyo_2"] = 0
                gl[i]["agr_folyo_3"] = 0
                gl[i]["agr_folyo_4"] = 0
                gl[i]["agr_kapton_1"] = 0
                gl[i]["agr_kapton_2"] = 0
                gl[i]["agr_kapton_3"] = 0
                gl[i]["agr_kapton_4"] = 0
        
def trafo_hesap_trifaz_izole( gl, guc, frekans, 
                   gauss, karkas_en, karkas_boy, 
                   karkas_yuk, verim, sarim, 
                   primer_sarim_yukseklik_toplam,
                   primer_izolasyon,
                   baglanti,
                   kademe=1):
        
        
        for i in range(0, 10):
            
            if gl[i]["voltaj"]> 0 :
                
                # Akım 1 Hesabı -------------------------
                if baglanti=="Yıldız":
                    
                    gl[i]["akim1"]=akim_hesap_3(
                            guc=guc,
                            gerilim=gl[i]["voltaj"])
                elif baglanti=="Üçgen":
                    gl[i]["akim1"]=akim_hesap_4(
                            guc=guc,
                            gerilim=gl[i]["voltaj"])
                else:
                    print("Akım hesaplanamadı . yanlıs Bağlanı Seçimi",baglanti," +")
                
                # Kesit 1 Hesabı -------------------------
                gl[i]["kesit1"]=kesit_hesap_1(
                    akim=gl[i]["akim1"],
                    akim_yogunlugu=akim_yogunlugu_1(
                        tel_turu=gl[i]["teltipi"]))
                # cap 1 Hesabı -------------------------
                gl[i]["cap1"]=cap_hesap_1(
                    kesit=gl[i]["kesit1"])
                # spir 1 Hesabı -------------------------
                if baglanti=="Yıldız":
                    gl[i]["spir1"]=spir_hesap_3(
                        gerilim=gl[i]["voltaj"],
                        frekans=frekans,
                        gauss=gauss,
                        karkas_en=karkas_en,
                        karkas_boy=karkas_boy,
                        verim=verim)
                elif baglanti=="Üçgen":
                    gl[i]["spir1"]=spir_hesap_4(
                        gerilim=gl[i]["voltaj"],
                        frekans=frekans,
                        gauss=gauss,
                        karkas_en=karkas_en,
                        karkas_boy=karkas_boy,
                        verim=verim)
                else:
                    print("Spir Hesaplanamadı . yanlıs Bağlanı Seçimi")    
                # spir 2 Hesabı -------------------------
                if gl[i]["check_spir_man"]==True:
                    pass
                else:
                    gl[i]["spir2"]=round(gl[i]["spir1"])
                # Kesit 2 Hesabı -------------------------
                gl[i]["kesit2"]= kesit_hesap_2(cap=gl[i]["mancap_1"]) + \
                    kesit_hesap_2(cap=gl[i]["mancap_2"]) +\
                    kesit_hesap_2(cap=gl[i]["mancap_3"]) +\
                    kesit_hesap_2(cap=gl[i]["mancap_4"]) +\
                    (gl[i]["folyotel11"] * gl[i]["folyotel12"]) +\
                    (gl[i]["folyotel21"] * gl[i]["folyotel22"]) +\
                    (gl[i]["folyotel31"] * gl[i]["folyotel32"]) +\
                    (gl[i]["folyotel41"] * gl[i]["folyotel42"]) +\
                    (gl[i]["karetel11"] * gl[i]["karetel12"]) +\
                    (gl[i]["karetel21"] * gl[i]["karetel22"]) +\
                    (gl[i]["karetel31"] * gl[i]["karetel32"]) +\
                    (gl[i]["karetel41"] * gl[i]["karetel42"])
                # Akım 2 Hesabı -------------------------
                gl[i]["akim2"]=akim_hesap_2(

                    kesit=gl[i]["kesit2"],
                    akim_yogunlugu=akim_yogunlugu_1(
                        tel_turu=gl[i]["teltipi"]))
                # cap 2 Hesabı -------------------------
                gl[i]["cap2"]= gl[i]["mancap_1"] + gl[i]["mancap_2"] + gl[i]["mancap_3"] + gl[i]["mancap_4"]
                # akım 2 ve kesit 2 kontrol -------------------------
                if gl[i]["kesit1"] <= gl[i]["kesit2"]:
                    gl[i]["kesit_ok"]=True
                    gl[i]["kesit_error"]=False
                else:
                    gl[i]["kesit_ok"]=False
                    gl[i]["kesit_error"]=True
                if gl[i]["akim1"] <= gl[i]["akim2"]:
                    gl[i]["akim_ok"]=True
                    gl[i]["akim_error"]=False
                else:
                    gl[i]["akim_ok"]=False
                    gl[i]["akim_error"]=True
                # -------------------------
                tel_cap = 0

                for tel_kademe in range(1, 5):

                    data = db.showfilter_tel_spir(filter_value=gl[i][f"mancap_{tel_kademe}"] , index=0)

                    if data == [] and gl[i][f"mancap_{tel_kademe}"] > 0:
                        tel_cap +=  (gl[i]["mancap_1"]) * 1.02
                    elif data != [] and gl[i][f"mancap_{tel_kademe}"] > 0:
                        tel_cap += data[0][4]
                
                # tel yüksekliği Hesabı -------------------------
                gl[i]["tel_yuk"]=tel_yukseklik_hesap_1(
                    tel_cap=tel_cap, karetel_yuk1=gl[i]["karetel12"],
                    karetel_yuk2=gl[i]["karetel22"],
                    karetel_yuk3=gl[i]["karetel32"], karetel_yuk4=gl[i]["karetel42"],
                    folyo_yuk1=gl[i]["folyotel12"], folyo_yuk2=gl[i]["folyotel22"],
                    folyo_yuk3=gl[i]["folyotel32"], folyo_yuk4=gl[i]["folyotel42"],
                    kapton1=gl[i]["kapton1"], kapton2=gl[i]["kapton2"],
                    kapton3=gl[i]["kapton3"], kapton4=gl[i]["kapton4"])
                # tel en Hesabı -------------------------
                gl[i]["tel_en"]= tel_en_hesap_1(
                    tel_cap=tel_cap,
                    karetel_en1=gl[i]["karetel11"],
                    karetel_en2=gl[i]["karetel21"],
                    karetel_en3=gl[i]["karetel31"], karetel_en4=gl[i]["karetel41"],
                    folyo_en1=gl[i]["folyotel11"], folyo_en2=gl[i]["folyotel21"],
                    folyo_en3=gl[i]["folyotel31"], folyo_en4=gl[i]["folyotel41"],
                    )

                if gl[i]["tel_en"] > 0:
                    # spir kat Hesabı -------------------------
                    gl[i]["spirkat"]=spir_kat_hesap_1(
                        karkas_yuk=karkas_yuk,
                        tel_en=gl[i]["tel_en"])

                    #  kat sayısı -------------------------------
                    if i == 0:
                        gl[i]["kat"]=kat_sayisi_hesap_1(
                            spir=gl[i]["spir2"],
                            spir_kat=gl[i]["spirkat"])

                    elif i > 0:
                        gl[i]["kat"]=kat_sayisi_hesap_2(
                            tel_spir_n=gl[i]["spir2"],
                            tel_spri_n_1=gl[i - 1]["spir2"],
                            kat_bosluk_n_1=gl[i - 1]["katbosluk"],
                            tel_en=gl[i]["tel_en"],
                            spir_kat=gl[i]["spirkat"]
                        )
                    # sarım yuksekliği  -------------------------
                    gl[i]["sarim_yukseklik"]=sarim_yüksekligi_hesap_1(
                        tel_yuk=gl[i]["tel_yuk"],
                        kat_sayisi=gl[i]["kat"])

                    # son kat
                    if i == 0:

                        try :
                            if math.fmod(gl[i]["spir2"], gl[i]["spirkat"]) == 0:
                                gl[i]["sonkat_spir"]=gl[i]["spirkat"]
                            else:
                                gl[i]["sonkat_spir"]=son_kat_hesap_1(
                                    spir_2=gl[i]["spir2"],
                                    spir_kat=gl[i]["spirkat"])
                        except Exception as err:
                            print(err)
                            # gl[i]["sonkat_spir"].setValue(math.fmod(gl[i]["spir2"].value(), gl[i]["spirkat"].value()))
                    elif i > 0:
                        if gl[i]["kat"] == 0:
                            gl[i]["sonkat_spir"]=son_kat_hesap_2(
                                spir_2=gl[i]["spir2"],
                                spir_2_n_1=gl[i - 1]["spir2"])
                            # gl[i]["sonkat_spir"].setValue(gl[i]["spir2"].value() - gl[i - 1]["spir2"])
                        else:
                            gl[i]["sonkat_spir"]=son_kat_hesap_3(
                                spir_2=gl[i]["spir2"],
                                spir_2_n_1=gl[i - 1]["spir2"],
                                kat_bosluk_n_1=gl[i - 1]["katbosluk"],
                                tel_en=gl[i]["tel_en"],
                                spir_kat=gl[i]["spirkat"])

                            # gl[i]["sonkat_spir"].setValue( math.fmod(gl[i]["spir2"].value()-gl[i-1]["spir2"] - math.floor(gl[i-1]["katbosluk"] / gl[i]["tel_en"].value()) ,gl[i]["spirkat"].value()))
                    # kattaki bosluk ---------------------------
                    if i == 0:
                        gl[i]["katbosluk"]=kattaki_bosluk_hesap_1(
                            karkas_yuk=karkas_yuk,
                            tel_en=gl[i]["tel_en"],
                            son_kat=gl[i]["sonkat_spir"]
                        )
                        # gl[i]["katbosluk"]setValue(self.ui.doubleSpinBox_karkas_yukseklik.value()-
                        #                                   (gl[i]["tel_en"].value()*gl[i]["sonkat_spir"]))
                    elif i > 0:
                        if gl[i]["kat"] == 0:
                            gl[i]["katbosluk"]=kattaki_bosluk_hesap_2(

                                kat_bosluk_n_1=gl[i - 1]["katbosluk"],
                                tel_en=gl[i]["tel_en"],
                                spir_2=gl[i]["spir2"],
                                spir_2_n_1=gl[i - 1]["spir2"]
                            )
                            # gl[i]["katbosluk"]setValue(gl[i-1]["katbosluk"]-(gl[i]["tel_en"].value()*(gl[i]["spir2"].value()-gl[i-1]["spir2"] )))
                        else:
                            gl[i]["katbosluk"]=kattaki_bosluk_hesap_3(
                                karkas_yuk=karkas_yuk,
                                spir_2=gl[i]["spir2"],
                                spir_2_n_1=gl[i - 1]["spir2"],
                                kat_bosluk_n_1=gl[i - 1]["katbosluk"],
                                tel_en=gl[i]["tel_en"],
                                spir_kat=gl[i]["spirkat"]

                            )
                            # gl[i]["katbosluk"]setValue(self.ui.doubleSpinBox_karkas_yukseklik.value()-
                            #                   math.fmod(gl[i]["spir2"].value()-gl[i-1]["spir2"] - math.floor(gl[i-1]["katbosluk"] /
                            #                                                                              gl[i]["tel_en"].value()) ,gl[i]["spirkat"].value())*gl[i]["tel_en"].value())
                    else:
                        pass

                    # tel uzunluk  ---------------------------
                    a0 = 2 * (karkas_en + karkas_boy) + 8 * 0.05 * karkas_en
                    a1 = a0 + 4 * gl[1]["tel_yuk"]
                    a2 = a0 + 4 * gl[2]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"]
                    a3 = a0 + 4 * gl[3]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"]
                    a4 = a0 + 4 * gl[4]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"]
                    a5 = a0 + 4 * gl[5]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * gl[3]["tel_yuk"] * gl[3]["kat"]
                    a6 = a0 + 4 * gl[6]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"]
                    a7 = a0 + 4 * gl[7]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * gl[5]["tel_yuk"] * gl[5]["kat"]
                    a8 = a0 + 4 * gl[8]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * gl[5]["tel_yuk"] * gl[5]["kat"] + 8 * gl[6]["tel_yuk"] * gl[6]["kat"]
                    a9 = a0 + 4 * gl[9]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * gl[5]["tel_yuk"] * gl[5]["kat"] + 8 * gl[6]["tel_yuk"] * gl[6]["kat"] + 8 * gl[7]["tel_yuk"] * gl[7]["kat"]
                    all_a = [0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
                    if i == 0:
                        gl[i]["tel_uzunluk"]=((gl[i]["kat"] - 1) * ((2 * (karkas_en + karkas_boy)) +
                                                        8 * karkas_en * 0.05 + 4 * gl[i]["tel_yuk"]) + \
                             (8 * gl[i]["tel_yuk"] * (gl[i]["kat"] - 1) * (gl[i]["kat"] - 2) / 2)) / 1000 *\
                            gl[i]["spirkat"] + \
                            ((2 * (karkas_en + karkas_boy)) + \
                             8 * karkas_en * 0.05 + 4 * gl[i]["tel_yuk"] + \
                             (8 * gl[i]["tel_yuk"] * (gl[i]["kat"] - 1))) / 1000 * gl[i]["sonkat_spir"]
                    elif i > 0:
                        if gl[i]["kat"] == 0:
                            gl[i]["tel_uzunluk"]=(all_a[i] + 8 * (gl[i - 1]["kat"] - 1) * gl[i - 1]["tel_yuk"]) * gl[i]["sonkat_spir"] / 1000
                        elif gl[i]["kat"] == 1:
                            gl[i]["tel_uzunluk"]=(all_a[i] + 8 * (gl[i - 1]["kat"] - 1) * gl[i - 1]["tel_yuk"]) *\
                                               math.floor(gl[i - 1]["katbosluk"] / gl[i]["tel_en"]) / 1000 + (
                                                       all_a[i] + 8 * (gl[i - 1]["kat"])
                                                       * gl[i - 1]["tel_yuk"]) * gl[i]["sonkat_spir"] / 1000

                        else:
                            gl[i]["tel_uzunluk"]=(all_a[i] + 8 * (gl[i - 1]["kat"] - 1) * gl[i - 1]["tel_yuk"]) *\
                                math.floor(gl[i - 1]["katbosluk"] / gl[i]["tel_en"]) / 1000 +\
                                ((gl[i]["kat"] - 1) * (
                                        all_a[i] + 8 * (gl[i - 1]["kat"]) * gl[i - 1]["tel_yuk"]) +
                                 4 * (gl[i]["kat"] - 1) * (gl[i]["kat"] - 2) * gl[i]["tel_yuk"]) * gl[i]["spirkat"] / 1000 + (all_a[i] + 8 * (gl[i - 1]["kat"]) * gl[i - 1]["tel_yuk"] + 8 * (
                                        gl[i]["kat"] - 1) *
                                   gl[i]["tel_yuk"]) * gl[i]["sonkat_spir"] / 1000


                    if sarim == "sekonder":

                        sek_a1 = a0 + 8 * primer_sarim_yukseklik_toplam + 8 * primer_izolasyon + 4 * gl[1]["tel_yuk"]
                        sek_a2 = a0 + 8 * primer_sarim_yukseklik_toplam + 4 * gl[2]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"]
                        sek_a3 = a0 + 8 * primer_sarim_yukseklik_toplam + 4 * gl[3]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"]
                        sek_a4 = a0 + 8 * primer_sarim_yukseklik_toplam + 4 * gl[4]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"]
                        sek_a5 = a0 + 8 * primer_sarim_yukseklik_toplam + 4 * gl[5]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                 gl[3]["tel_yuk"] * gl[3]["kat"]
                        sek_a6 = a0 + 8 * primer_sarim_yukseklik_toplam + 4 * gl[6]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                 gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"]
                        sek_a7 = a0 + 8 * primer_sarim_yukseklik_toplam + 4 * gl[7]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                 gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * \
                                 gl[5]["tel_yuk"] * gl[5]["kat"]
                        sek_a8 = a0 + 8 * primer_sarim_yukseklik_toplam + 4 * gl[8]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                 gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * \
                                 gl[5]["tel_yuk"] * gl[5]["kat"] + 8 * gl[6]["tel_yuk"] * gl[6]["kat"]
                        sek_a9 = a0 + 8 * primer_sarim_yukseklik_toplam + 4 * gl[9]["tel_yuk"] + 8 * gl[0]["tel_yuk"] * gl[0]["kat"] + 8 * gl[1]["tel_yuk"] * gl[1]["kat"] + 8 * gl[2]["tel_yuk"] * gl[2]["kat"] + 8 * \
                                 gl[3]["tel_yuk"] * gl[3]["kat"] + 8 * gl[4]["tel_yuk"] * gl[4]["kat"] + 8 * \
                                 gl[5]["tel_yuk"] * gl[5]["kat"] + 8 * gl[6]["tel_yuk"] * gl[6]["kat"] + 8 * \
                                 gl[7]["tel_yuk"] * gl[7]["kat"]

                        all_sek_a = [0, sek_a1, sek_a2, sek_a3, sek_a4, sek_a5, sek_a6, sek_a7, sek_a8, sek_a9]
                        if i == 0:
                            gl[i]["tel_uzunluk"]=(
                                        (gl[i]["kat"] - 1) * (
                                        a0 + 8 * primer_sarim_yukseklik_toplam + 8 * primer_izolasyon + 4 *
                                        gl[i]["tel_yuk"])
                                        + 8 * gl[i]["tel_yuk"] * (gl[i]["kat"] - 1) * (gl[i]["kat"] - 2) / 2
                                )/ 1000 * gl[i]["spirkat"] + (
                                        a0 + 8 * primer_sarim_yukseklik_toplam + 8 * primer_izolasyon + 4 *
                                        gl[i]["tel_yuk"] + 8 * gl[i]["tel_yuk"] *
                                        (gl[i]["kat"] - 1)) / 1000 * gl[i]["sonkat_spir"]

                        elif i > 0:
                            if gl[i]["kat"] == 0:
                                gl[i]["tel_uzunluk"]=(all_sek_a[i] + 8 * (gl[i - 1]["kat"] - 1) * gl[i - 1]["tel_yuk"]) * gl[i]["sonkat_spir"] / 1000
                            elif gl[i]["kat"] == 1:
                                gl[i]["tel_uzunluk"]=(all_sek_a[i] + 8 * (gl[i - 1]["kat"] - 1) * gl[i - 1]["tel_yuk"]) *\
                                    math.floor(gl[i - 1]["katbosluk"] / gl[i]["tel_en"]) / 1000 + (
                                            all_sek_a[i] + 8 * (gl[i - 1]["kat"])
                                            * gl[i - 1]["tel_yuk"]) * gl[i]["sonkat_spir"] / 1000

                            else:
                                gl[i]["tel_uzunluk"]=(all_sek_a[i] + 8 * (gl[i - 1]["kat"] - 1) * gl[i - 1]["tel_yuk"]) *\
                                    math.floor(gl[i - 1]["katbosluk"] / gl[i]["tel_en"]) / 1000 +\
                                    ((gl[i]["kat"] - 1) * (
                                            all_sek_a[i] + 8 * (gl[i - 1]["kat"]) * gl[i - 1]["tel_yuk"]) +
                                     4 * (gl[i]["kat"] - 1) * (gl[i]["kat"] - 2) * gl[i]["tel_yuk"]) * gl[i]["spirkat"] / 1000 + \
                                    (all_sek_a[i] + 8 * (gl[i - 1]["kat"]) * gl[i - 1]["tel_yuk"] + 8 * (
                                            gl[i]["kat"] - 1) *
                                       gl[i]["tel_yuk"]) * gl[i]["sonkat_spir"] / 1000
                    
                        
                    # tel agirlik  ---------------------------
                    if gl[i]["tel_uzunluk"] != 0:
                        gl[i]["tel_agirlik"]=tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"], kesit_2=gl[i]["kesit2"],
                                                   tel_yogunluk=tel_yogunlugu_1(tel_turu=gl[i]["teltipi"]))

                        gl[i]["agr_tel_1"]=tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"], kesit_2=kesit_hesap_2(cap=gl[i]["mancap_1"]),
                                                   tel_yogunluk=tel_yogunlugu_1(tel_turu=gl[i]["teltipi"]))
                        gl[i]["agr_tel_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                 kesit_2=kesit_hesap_2(cap=gl[i]["mancap_2"]),
                                                                 tel_yogunluk=tel_yogunlugu_1(
                                                                     tel_turu=gl[i]["teltipi"]))
                        gl[i]["agr_tel_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                 kesit_2=kesit_hesap_2(cap=gl[i]["mancap_3"]),
                                                                 tel_yogunluk=tel_yogunlugu_1(
                                                                     tel_turu=gl[i]["teltipi"]))
                        gl[i]["agr_tel_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                 kesit_2=kesit_hesap_2(cap=gl[i]["mancap_4"]),
                                                                 tel_yogunluk=tel_yogunlugu_1(
                                                                     tel_turu=gl[i]["teltipi"]))
                        gl[i]["agr_karetel_1"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                 kesit_2=gl[i]["karetel11"] * gl[i]["karetel12"],
                                                                 tel_yogunluk=tel_yogunlugu_1(
                                                                     tel_turu=gl[i]["teltipi"]))
                        gl[i]["agr_karetel_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                     kesit_2=gl[i]["karetel21"] * gl[i]["karetel22"],
                                                                     tel_yogunluk=tel_yogunlugu_1(
                                                                         tel_turu=gl[i]["teltipi"]))
                        gl[i]["agr_karetel_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                     kesit_2=gl[i]["karetel31"] * gl[i]["karetel32"],
                                                                     tel_yogunluk=tel_yogunlugu_1(
                                                                         tel_turu=gl[i]["teltipi"]))
                        gl[i]["agr_karetel_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                     kesit_2=gl[i]["karetel41"] * gl[i]["karetel42"],
                                                                     tel_yogunluk=tel_yogunlugu_1(
                                                                         tel_turu=gl[i]["teltipi"]))
                        gl[i]["agr_folyo_1"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                     kesit_2=gl[i]["folyotel11"] * gl[i]["folyotel12"],
                                                                     tel_yogunluk=tel_yogunlugu_1(
                                                                         tel_turu=gl[i]["teltipi"]))
                        gl[i]["agr_folyo_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                   kesit_2=gl[i]["folyotel21"] * gl[i]["folyotel22"],
                                                                   tel_yogunluk=tel_yogunlugu_1(
                                                                       tel_turu=gl[i]["teltipi"]))
                        gl[i]["agr_folyo_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                   kesit_2=gl[i]["folyotel31"] * gl[i]["folyotel32"],
                                                                   tel_yogunluk=tel_yogunlugu_1(
                                                                       tel_turu=gl[i]["teltipi"]))
                        gl[i]["agr_folyo_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                   kesit_2=gl[i]["folyotel41"] * gl[i]["folyotel42"],
                                                                   tel_yogunluk=tel_yogunlugu_1(
                                                                       tel_turu=gl[i]["teltipi"]))
                        gl[i]["agr_kapton_1"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                   kesit_2=gl[i]["kapton1"],
                                                                   tel_yogunluk=1330)
                        gl[i]["agr_kapton_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                    kesit_2=gl[i]["kapton2"],
                                                                    tel_yogunluk=1330)
                        gl[i]["agr_kapton_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                    kesit_2=gl[i]["kapton3"],
                                                                    tel_yogunluk=1330)
                        gl[i]["agr_kapton_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                    kesit_2=gl[i]["kapton4"],
                                                                    tel_yogunluk=1330)
                    else:
                        gl[i]["tel_agirlik"]=0
                        gl[i]["agr_tel_1"] = 0
                        gl[i]["agr_tel_2"] = 0
                        gl[i]["agr_tel_3"] = 0
                        gl[i]["agr_tel_4"] = 0
                        gl[i]["agr_karetel_1"] = 0
                        gl[i]["agr_karetel_2"] = 0
                        gl[i]["agr_karetel_3"] = 0
                        gl[i]["agr_karetel_4"] = 0
                        gl[i]["agr_folyo_1"] = 0
                        gl[i]["agr_folyo_2"] = 0
                        gl[i]["agr_folyo_3"] = 0
                        gl[i]["agr_folyo_4"] = 0
                        gl[i]["agr_kapton_1"] = 0
                        gl[i]["agr_kapton_2"] = 0
                        gl[i]["agr_kapton_3"] = 0
                        gl[i]["agr_kapton_4"] = 0

            else:

                gl[i]["akim1"]=0
                gl[i]["kesit1"]=0
                gl[i]["cap1"]=0
                gl[i]["spir1"]=0
                gl[i]["cap2"]=0
                gl[i]["akim2"]=0
                gl[i]["spir2"]=0
                gl[i]["folyotel11"]=0
                gl[i]["folyotel12"]=0
                gl[i]["folyotel21"]=0
                gl[i]["folyotel22"]=0
                gl[i]["folyotel31"]=0
                gl[i]["folyotel32"]=0
                gl[i]["folyotel41"]=0
                gl[i]["folyotel42"]=0
                gl[i]["kapton1"]=0
                gl[i]["kapton2"]=0
                gl[i]["kapton3"]=0
                gl[i]["kapton4"]=0
                gl[i]["karetel11"]=0
                gl[i]["karetel12"]=0
                gl[i]["karetel21"]=0
                gl[i]["karetel22"]=0
                gl[i]["karetel31"]=0
                gl[i]["karetel32"]=0
                gl[i]["karetel41"]=0
                gl[i]["karetel42"]=0
                gl[i]["kesit2"]=0
                gl[i]["tel_en"]=0
                gl[i]["tel_yuk"]=0
                gl[i]["spirkat"]=0
                gl[i]["kat"]=0
                gl[i]["katbosluk"]=0
                gl[i]["tel_uzunluk"]=0
                gl[i]["tel_agirlik"]=0
                gl[i]["sarim_yukseklik"]=0
                gl[i]["sonkat_spir"]=0
                gl[i]["check_spir_man"] = False
                gl[i]["kesit_ok"]=False
                gl[i]["kesit_error"]=True
                gl[i]["akim_ok"]=False
                gl[i]["akim_error"]=True
                gl[i]["mancap_1"]=0
                gl[i]["mancap_2"]=0
                gl[i]["mancap_3"]=0
                gl[i]["mancap_4"]=0
                gl[i]["mlz_tel_1"] = ""
                gl[i]["mlz_tel_2"] = ""
                gl[i]["mlz_tel_3"] =  ""
                gl[i]["mlz_tel_4"] =  ""
                gl[i]["mlz_karetel_1"] =  ""
                gl[i]["mlz_karetel_2"] =  ""
                gl[i]["mlz_karetel_3"] =  ""
                gl[i]["mlz_karetel_4"] =  ""
                gl[i]["mlz_folyotel_1"] =  ""
                gl[i]["mlz_folyotel_2"] =  ""
                gl[i]["mlz_folyotel_3"] =  ""
                gl[i]["mlz_folyotel_4"] =  ""
                gl[i]["mlz_kapton_1"] =  ""
                gl[i]["mlz_kapton_2"] =  ""
                gl[i]["mlz_kapton_3"] =  ""
                gl[i]["mlz_kapton_4"] =  ""
                gl[i]["gb_check_tel_1"] =  False
                gl[i]["gb_check_tel_2"] =  False
                gl[i]["gb_check_tel_3"] =  False
                gl[i]["gb_check_tel_4"] =  False
                gl[i]["gb_check_karetel_1"]= False
                gl[i]["gb_check_karetel_2"]= False
                gl[i]["gb_check_karetel_3"]= False
                gl[i]["gb_check_karetel_4"]= False
                gl[i]["gb_check_folyotel_1"]= False
                gl[i]["gb_check_folyotel_2"]= False
                gl[i]["gb_check_folyotel_3"]= False
                gl[i]["gb_check_folyotel_4"]= False
                gl[i]["gb_check_kapton_1"]= False
                gl[i]["gb_check_kapton_2"]= False
                gl[i]["gb_check_kapton_3"]= False
                gl[i]["gb_check_kapton_4"]= False
                gl[i]["tel_agirlik"] = 0
                gl[i]["agr_tel_1"] = 0
                gl[i]["agr_tel_2"] = 0
                gl[i]["agr_tel_3"] = 0
                gl[i]["agr_tel_4"] = 0
                gl[i]["agr_karetel_1"] = 0
                gl[i]["agr_karetel_2"] = 0
                gl[i]["agr_karetel_3"] = 0
                gl[i]["agr_karetel_4"] = 0
                gl[i]["agr_folyo_1"] = 0
                gl[i]["agr_folyo_2"] = 0
                gl[i]["agr_folyo_3"] = 0
                gl[i]["agr_folyo_4"] = 0
                gl[i]["agr_kapton_1"] = 0
                gl[i]["agr_kapton_2"] = 0
                gl[i]["agr_kapton_3"] = 0
                gl[i]["agr_kapton_4"] = 0
        
