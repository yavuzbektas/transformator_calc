import math
import db_sql
import inspect
db=db_sql.mydb()
cu_par=3
cu_yog=8700
al_par=1.6 
al_yog=2700
dig_par=1
dig_yog=8700
# ======================  Formüller =========================


def spir_hesap_1(gerilim, frekans, gauss, karkas_en, karkas_boy, verim, Kf=4.44):
    # spir= gerilim * * (10 ** 8)) / (Kf * frekans * gauss *  (en * boy / 100))) / (verim / 100)
    try : 
        sonuc = ((gerilim * (10 ** 8)) / (Kf * frekans * gauss * (karkas_en * karkas_boy / 100))) / (verim / 100)
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc
def spir_hesap_2(gerilim, frekans, gauss, karkas_en, karkas_boy, verim, Kf=4.44):
    # spir= gerilim * * (10 ** 8)) / (Kf * frekans * gauss *  (en * boy / 100))) / (verim / 100)
    try : 
        sonuc =((gerilim * (10 ** 8)) / (Kf * frekans * gauss * (karkas_en * karkas_boy / 100)))
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc
def spir_hesap_3(gerilim, frekans, gauss, karkas_en, karkas_boy, verim, Kf=4.44):
    try : 
        sonuc =round(((gerilim * (10 ** 8)) / (Kf * frekans * gauss * (karkas_en * karkas_boy / 100)*math.sqrt(3)))/(verim/100) ,2)
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc 
def spir_hesap_4(gerilim, frekans, gauss, karkas_en, karkas_boy, verim, Kf=4.44):
    try : 
        sonuc =round(((gerilim * (10 ** 8)) / (Kf * frekans * gauss * (karkas_en * karkas_boy / 100))) / (verim / 100),2)
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc 
def spir_hesap_5(gerilim, frekans, gauss, karkas_en, karkas_boy, verim, Kf=4.44):
    try : 
        sonuc =round(((gerilim * (10 ** 8)) / (Kf * frekans * gauss * (karkas_en * karkas_boy / 100)*math.sqrt(3)))/ (verim / 100) ,0)
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc 
def spir_hesap_6(gerilim, frekans, gauss, karkas_en, karkas_boy, verim, Kf=4.44):
    try : 
        sonuc =round(((gerilim * (10 ** 8)) / (Kf * frekans * gauss * (karkas_en * karkas_boy / 100))) / (verim / 100),0)
    
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc 
def spir_hesap_7(gerilim, frekans, gauss, karkas_en, karkas_boy, verim, Kf=4.44):
    try : 
        sonuc =round(((gerilim/2 * (10 ** 8)) / (Kf * frekans * gauss * (karkas_en * karkas_boy / 100))) / (verim / 100),2)
    
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc 
def spir_hesap_8(Lg,enduktans,f_man,karkas_man):
    sonuc=0
    if f_man==0:
        return sonuc
    try:
       sonuc= math.sqrt(Lg * (enduktans /1000 ) * 10**8/ (0.4 * math.pi*karkas_man*f_man))
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc
def spir_hesap_9(spir):
    sonuc= math.round(spir)
    return sonuc
def spir_hesap_10(gerilim,gauss,frekans,karkas_man,Kf):
    try:
       sonuc= gerilim*10**8/(Kf*karkas_man*frekans*gauss)
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc
def spir_hesap_11(gerilim,gauss,frekans,karkas_man,Kf):
    try:
       sonuc= (gerilim/math.sqrt(3))*10**8/(Kf*karkas_man*frekans*gauss)
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc
def spir_hesap_12(Lg,enduktans,f_man,karkas_man,mpl,Um):
    sonuc=0
    if f_man==0:
        return sonuc
    try:
       sonuc= math.sqrt((Lg+ (mpl/Um))* (enduktans /1000 ) * 10**8/ (0.4 * math.pi*karkas_man*f_man))
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc
def akim_hesap_1(guc, gerilim):
    try : 
        sonuc =guc / gerilim
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc   
def akim_hesap_2(kesit, akim_yogunlugu):
    return kesit * akim_yogunlugu
def akim_hesap_3(guc, gerilim):
    try : 
        sonuc =guc / (gerilim*math.sqrt(3))
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc 
def akim_hesap_4(guc, gerilim):
    try : 
        sonuc =guc / (gerilim*3)
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc 
def akim_hesap_5(guc, gerilim):
    try : 
        sonuc =guc /gerilim/math.sqrt(3)
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc
def akim_hesap_6(guc, gerilim):
    try : 
        sonuc =guc / (gerilim*2)
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc    
def kesit_hesap_1(akim, akim_yogunlugu):  # akım yogunluguna göre
    try:
       sonuc= akim / akim_yogunlugu
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc  
def kesit_hesap_2(cap):  # çap değerine göre
    return cap ** 2 * math.pi / 4
def kesit_hesap_3(kenar1, kenar2):
    return kenar1 * kenar2
def cap_hesap_1(kesit):
    try:
       sonuc= math.sqrt(kesit * 4 / math.pi)
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc
def akim_yogunlugu_1(tel_turu, cu_par, cu_yog, al_par, al_yog, dig_par, dig_yog):
    
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
def tel_yogunlugu_1(tel_turu,  cu_yog, al_yog,  dig_yog):
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
def karkas_yuk_oto(karkas_en):
    return karkas_en * 1.5 - math.floor(karkas_en * 0.15)
def karkas_Ac_oto(c, guc, frekans):
    try : 
        sonuc =c * math.sqrt(guc / (2 * frekans))
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc
def karkas_Ac_oto_2(c, guc, frekans):
    try : 
        sonuc=  c * math.sqrt(guc / (3 * frekans))
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc
def karkas_Ac_oto_3(c, akim,gerilim, frekans):
    try : 
        sonuc =c * math.sqrt((akim*gerilim) / (2 * frekans))
    except Exception as error:
        print(error)
        sonuc=0
    return sonuc
def karkas_Ac_oto_4(c, akim,gerilim, frekans):
    try : 
        sonuc =c * math.sqrt((akim*gerilim*3/math.sqrt(3)) / (3 * frekans))
    except Exception as error:
        print(error)
        sonuc=0
    return sonuc
def karkas_izole_Ac_oto(akim,gerilim)  :
    try : 
        sonuc =(akim*gerilim*3/math.sqrt(3)) 
    except Exception as error:
        print(error)
        sonuc=0
    return sonuc  
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
    sonuc = math.floor(karkas_yuk / tel_en)
    return sonuc
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
def tel_agirlik_monoUI(sarim_agirlik):
    return sarim_agirlik * 2 # monoUI da  2 ile carpılıyor
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
def trafo_olcu_hesapla_3(sac_tipi,karkas_en,karkas_boy,karkas_yuk,nuve_bosluk,sarim_yukseklik_toplam,primer_izolasyon):
    if sac_tipi=="ei_sac":
        olcu_a=math.ceil(karkas_en*6 )+2
        olcu_c=math.ceil(3*karkas_en+2*karkas_en)+2
    elif sac_tipi=="kesme_sac":
        olcu_a=math.ceil(karkas_en*3+4*(karkas_en/2+nuve_bosluk)+2*(sarim_yukseklik_toplam +karkas_en*0.05+primer_izolasyon ))+2
        olcu_c=math.ceil(karkas_yuk+karkas_en*0.15+2*karkas_en)+2
    else:
        olcu_a=0
        olcu_c=0
    olcu_b = karkas_boy+2*karkas_en*0.7+2
    olcu_d=olcu_a-karkas_en
    olcu_e=karkas_boy+karkas_en*0.7+5+1
    olcu_f=0
    return (olcu_a,olcu_b,olcu_c,olcu_d,olcu_e,olcu_f)
def trafo_olcu_hesapla_4(sac_tipi,karkas_en,karkas_boy,karkas_yuk,nuve_bosluk):
    if sac_tipi=="ei_sac":
        olcu_a=math.ceil(karkas_en*3)
        olcu_c=math.ceil(karkas_en*0.5+2*karkas_en)+0  # +0 formülden geliyor.
    elif sac_tipi=="kesme_sac":
        olcu_a=math.ceil(karkas_en*2+2*(karkas_en/2+nuve_bosluk))
        olcu_c=math.ceil(karkas_yuk+karkas_en*0.15+karkas_en)
    else:
        olcu_a=0
        olcu_c=0
    olcu_b = karkas_en+karkas_boy
    olcu_d=olcu_a-karkas_en/2
    olcu_e=karkas_boy+karkas_en/2+2
    olcu_f=0
    return (olcu_a,olcu_b,olcu_c,olcu_d,olcu_e,olcu_f)
def trafo_olcu_hesapla_5(sac_tipi,karkas_en,karkas_boy,karkas_yuk,nuve_bosluk,sarim_yukseklik_toplam,primer_izolasyon):
    if sac_tipi=="ei_sac":
        olcu_a=math.ceil(karkas_en*4 )
        olcu_c=math.ceil(3*karkas_en+2*karkas_en)
    elif sac_tipi=="kesme_sac":
        olcu_a=math.ceil(2*(karkas_en+karkas_en/2+nuve_bosluk+sarim_yukseklik_toplam +karkas_en*0.05+primer_izolasyon ))
        olcu_c=math.ceil(karkas_yuk+karkas_en*0.15+2*karkas_en)
    else:
        olcu_a=0
        olcu_c=0
    olcu_b = 2*karkas_en+karkas_boy
    olcu_d=olcu_a-karkas_en
    olcu_e=karkas_boy+karkas_en+5
    olcu_f=0
    return (olcu_a,olcu_b,olcu_c,olcu_d,olcu_e,olcu_f)
def trafo_olcu_hesapla_6(karkas_en,karkas_boy):
    olcu_a=math.ceil(karkas_en*6 )
    olcu_c=math.ceil(3*karkas_en+2*karkas_en)
    
    olcu_b = karkas_boy+2*karkas_en
    olcu_d=olcu_a-karkas_en
    olcu_e=karkas_boy+karkas_en+5
    olcu_f=0
    return (olcu_a,olcu_b,olcu_c,olcu_d,olcu_e,olcu_f)
def nuve_olcu_hesapla(karkas_en,karkas_boy,klemens_a,klemens_b,ayak_a):
    nuve_olcu_a=karkas_en*3
    nuve_olcu_b=karkas_boy +klemens_a + ayak_a
    nuve_olcu_c=karkas_en*2.5 +klemens_b
    return (nuve_olcu_a,nuve_olcu_b,nuve_olcu_c)
def nuve_olcu_hesapla_2(sac_tipi,karkas_en,karkas_boy,klemens_a,klemens_b,ayak_a,sarim_yukseklik_toplam,nuve_bosluk):
    nuve_olcu_a=karkas_en*5 + (nuve_bosluk*6 if sac_tipi=="kesme_sac" else 0)
    nuve_olcu_b=karkas_boy +klemens_a + ayak_a+2*sarim_yukseklik_toplam
    nuve_olcu_c=karkas_en*5 +klemens_b
    return (nuve_olcu_a,nuve_olcu_b,nuve_olcu_c)
def nuve_olcu_hesapla_3(sac_tipi,karkas_en,karkas_boy,klemens_a,klemens_b,ayak_a,sarim_yukseklik_toplam,primer_izolasyon,nuve_bosluk):
    if sac_tipi=="ei_sac":
        nuve_olcu_a=karkas_en*3 + 2*sarim_yukseklik_toplam + 2* karkas_en * 0.05 
        
        
    elif sac_tipi=="kesme_sac": 
        nuve_olcu_a=karkas_en*2 + 4*sarim_yukseklik_toplam + karkas_en * 0.1 + 2*primer_izolasyon + 2*nuve_bosluk
        
    else:
        nuve_olcu_a=0
    nuve_olcu_b=karkas_boy +klemens_a + ayak_a
    nuve_olcu_c=karkas_en*5 +klemens_b
    return (nuve_olcu_a,nuve_olcu_b,nuve_olcu_c)
def nuve_olcu_hesapla_4(karkas_en,karkas_boy,klemens_a,klemens_b,ayak_a):
    nuve_olcu_a=karkas_en*6
    nuve_olcu_b=karkas_boy +klemens_a + ayak_a
    nuve_olcu_c=karkas_en*5 +klemens_b
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
def yanSacAgirlik_hesap_2(sac_tipi,karkas_en,toplam_sarim_Yukseklik,primer_izolasyon,nuveBosluk):
    yanSac=0
    if sac_tipi=="ei_sac":
        yanSac=0
    elif sac_tipi=="kesme_sac":    
        yanSac=math.ceil(2*karkas_en+(2*(toplam_sarim_Yukseklik+karkas_en*0.05+primer_izolasyon + nuveBosluk)))+9
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
def gobekSacAgirlik_hesap_2(sac_tipi,karkas_en):
    gobekSac=0
    if sac_tipi=="ei_sac":
        gobekSac=0
    elif sac_tipi=="kesme_sac":    
        gobekSac=karkas_en*3
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
def kesmeSacAgirlik_hesap_2(sac_tipi,karkas_en,karkas_boy,nuve_bosluk,gobek_sac,yan_sac,sac_yogunluk):
    kesmeSac=0

    if sac_tipi=="ei_sac":
        kesmeSac=0
    elif sac_tipi=="kesme_sac":    
        
        kesmeSac=(yan_sac*karkas_boy*karkas_en*2+2*gobek_sac*karkas_boy*karkas_en)/(10**9)*sac_yogunluk
    
    return kesmeSac  
def f_hesap_1(Lg,karkas_Ac,karkas_yuk):
    sonuc=0
    if Lg ==0 :
        return sonuc
    try : 
        sonuc = (1+(Lg/math.sqrt(karkas_Ac)*math.log(2*karkas_yuk/Lg,math.exp(1))))
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc 
def end_hesap_1(gerilim,frekans,akim):
    
    sonuc =0.0
    if akim<=0:
        sonuc=0
        return sonuc 
    try : 
        
        sonuc =  (gerilim / (2*math.pi * frekans* akim))*1000
        
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0.0
    return sonuc 
def end_hesap_2(gerilim,frekans,akim):
    sonuc =0.0
    if akim<=0:
        sonuc=0
        return sonuc 
    try : 
        
        sonuc =  (gerilim /math.sqrt(3)) / (2*math.pi * frekans* akim)*1000
        
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0.0
    return sonuc 
def end_hesap_3(gerilim,frekans,akim,enduktans_m):
    sonuc =0.0
    
    if akim<=0:
        sonuc=0
        return sonuc 
    if enduktans_m>0:
        sonuc=enduktans_m
        return sonuc
    else:
        try : 
            
            sonuc =  (gerilim / (2*math.pi * frekans* akim))*1000
            
        except Exception as error:
            print(error,inspect.currentframe().f_code.co_name)
            sonuc=0.0
        return sonuc 

def end_hesap_4(sp,karkas_man,f,Lg):
    sonuc =0.0
    
    if Lg<=0:
        return sonuc 
    
    try : 
        
        sonuc =  (sp**2*0.4*math.pi*karkas_man * f)/(Lg*10**8)*1000
        
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0.0
    return sonuc 
def end_hesap_5(sp,karkas_man,f,Lg,MPL,Um):
    sonuc =0.0
    
    if Lg<=0:
        return sonuc 
    
    try : 
        
        sonuc =  (sp**2*0.4*math.pi*karkas_man * f)/((Lg+(MPL/Um))*10**8)*1000
        
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0.0
    return sonuc 
def mpl_hesap_1(karkas_en,karkas_yuk):
    try : 
        sonuc =  (karkas_en*6+2*karkas_yuk)/10
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc 
def mpl_hesap_2(Ap):
    sonuc=0
    if Ap==None:
        return sonuc
    try : 
        data = db.show_nearest_MPLvalue_trifaz(filter_value=Ap)
        if data==[]:
            pass
        else: 
            sonuc=data[0][19]
        
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc
def mpl_hesap_3(Ap):
    sonuc=0
    try : 
        data = db.show_nearest_MPLvalue_tekfaz(filter_value=Ap)
        if data==[]:
            pass
        else: 
            sonuc=data[0][20]
        
        
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc
def Ap_hesap_1(guc,karkas_yuk,Kf,Ku,gauss,frekans,tel_turu,cu_par,cu_yog,al_par,al_yog,dig_par,dig_yog):
    tel_yogunluk=akim_yogunlugu_1(
                        tel_turu=tel_turu,
                        cu_par=cu_par,
                        cu_yog=cu_yog,
                        al_par=al_par,
                        al_yog=al_yog,
                        dig_par=dig_par,
                        dig_yog=dig_yog)
    try : 
        sonuc =guc*10**8/(Kf*Ku*gauss*frekans*tel_yogunluk*100)
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc
def ApSac_hesap_1(karkas_en,karkas_boy):
    try : 
        sonuc =  (karkas_en*karkas_boy)*(1.5*karkas_en-math.floor(0.15*karkas_en))*karkas_en/20000
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc 
def ApSac_hesap_2(karkas_en,karkas_boy):
    try : 
        sonuc = 3*karkas_en*karkas_en*karkas_en*karkas_boy/10000*1.5
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc 
def Lg_mpl_hesap_1(mpl,enduktans,karkas_man,sp1,karkas_en,karkas_boy,Um):
    if enduktans<=0:
        sonuc=0
        return sonuc 
    try : 
        sonuc = 0.4*math.pi*sp1**2*karkas_man/(10**8*(enduktans/1000))-(mpl/Um)
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc 
def Lg_oto_hesap_1(enduktans,karkas_man,sp1,karkas_en,karkas_boy):
    if enduktans <=0:
        sonuc=0
        return sonuc 
    try : 
        sonuc = 0.4*math.pi*sp1**2*karkas_man/(10**8*enduktans/1000)
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc 
 #  Trafa Formüllerininn hesaplanmasıı --
def voltaj_m_hesap_1(enduktans,enduktans_m,akim,frekans):
    if enduktans_m>0:
       end=  enduktans_m/1000
    else:
        end=enduktans/1000
    try : 
        sonuc = 2*math.pi*frekans*akim*end
    except Exception as error:
        print(error,inspect.currentframe().f_code.co_name)
        sonuc=0
    return sonuc 
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
                   kademe=1,
                   cu_par= 0,
                    cu_yog=0,
                    al_par= 0,
                    al_yog=0,
                    dig_par=0,
                    dig_yog=0):
        
    
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
                        tel_turu=gl[i]["teltipi"],
                        cu_par=cu_par,
                        cu_yog=cu_yog,
                        al_par=al_par,
                        al_yog=al_yog,
                        dig_par=dig_par,
                        dig_yog=dig_yog))
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
                        tel_turu=gl[i]["teltipi"],
                        cu_par=cu_par,
                        cu_yog=cu_yog,
                        al_par=al_par,
                        al_yog=al_yog,
                        dig_par=dig_par,
                        dig_yog=dig_yog))
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
                                                   tel_yogunluk=tel_yogunlugu_1(tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))

                        gl[i]["agr_tel_1"]=tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"], kesit_2=kesit_hesap_2(cap=gl[i]["mancap_1"]),
                                                   tel_yogunluk=tel_yogunlugu_1(tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_tel_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                 kesit_2=kesit_hesap_2(cap=gl[i]["mancap_2"]),
                                                                 tel_yogunluk=tel_yogunlugu_1(
                                                                     tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_tel_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                 kesit_2=kesit_hesap_2(cap=gl[i]["mancap_3"]),
                                                                 tel_yogunluk=tel_yogunlugu_1(
                                                                     tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_tel_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                 kesit_2=kesit_hesap_2(cap=gl[i]["mancap_4"]),
                                                                 tel_yogunluk=tel_yogunlugu_1(
                                                                     tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_karetel_1"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                 kesit_2=gl[i]["karetel11"] * gl[i]["karetel12"],
                                                                 tel_yogunluk=tel_yogunlugu_1(
                                                                     tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_karetel_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                     kesit_2=gl[i]["karetel21"] * gl[i]["karetel22"],
                                                                     tel_yogunluk=tel_yogunlugu_1(
                                                                         tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_karetel_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                     kesit_2=gl[i]["karetel31"] * gl[i]["karetel32"],
                                                                     tel_yogunluk=tel_yogunlugu_1(
                                                                         tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_karetel_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                     kesit_2=gl[i]["karetel41"] * gl[i]["karetel42"],
                                                                     tel_yogunluk=tel_yogunlugu_1(
                                                                         tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_folyo_1"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                     kesit_2=gl[i]["folyotel11"] * gl[i]["folyotel12"],
                                                                     tel_yogunluk=tel_yogunlugu_1(
                                                                         tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_folyo_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                   kesit_2=gl[i]["folyotel21"] * gl[i]["folyotel22"],
                                                                   tel_yogunluk=tel_yogunlugu_1(
                                                                       tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_folyo_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                   kesit_2=gl[i]["folyotel31"] * gl[i]["folyotel32"],
                                                                   tel_yogunluk=tel_yogunlugu_1(
                                                                       tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_folyo_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                   kesit_2=gl[i]["folyotel41"] * gl[i]["folyotel42"],
                                                                   tel_yogunluk=tel_yogunlugu_1(
                                                                       tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
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
                   kademe=1,
                   cu_par= 0,
                    cu_yog=0,
                    al_par= 0,
                    al_yog=0,
                    dig_par=0,
                    dig_yog=0):
        
        
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
                        tel_turu=gl[i]["teltipi"],
                        cu_par=cu_par,
                        cu_yog=cu_yog,
                        al_par=al_par,
                        al_yog=al_yog,
                        dig_par=dig_par,
                        dig_yog=dig_yog))
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
                        tel_turu=gl[i]["teltipi"],
                        cu_par=cu_par,
                        cu_yog=cu_yog,
                        al_par=al_par,
                        al_yog=al_yog,
                        dig_par=dig_par,
                        dig_yog=dig_yog))
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
                                        a0 + 8 * primer_sarim_yukseklik_toplam +  4 *
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
                                                   tel_yogunluk=tel_yogunlugu_1(tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))

                        gl[i]["agr_tel_1"]=tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"], kesit_2=kesit_hesap_2(cap=gl[i]["mancap_1"]),
                                                   tel_yogunluk=tel_yogunlugu_1(tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_tel_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                 kesit_2=kesit_hesap_2(cap=gl[i]["mancap_2"]),
                                                                 tel_yogunluk=tel_yogunlugu_1(
                                                                     tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_tel_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                 kesit_2=kesit_hesap_2(cap=gl[i]["mancap_3"]),
                                                                 tel_yogunluk=tel_yogunlugu_1(
                                                                     tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_tel_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                 kesit_2=kesit_hesap_2(cap=gl[i]["mancap_4"]),
                                                                 tel_yogunluk=tel_yogunlugu_1(
                                                                     tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_karetel_1"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                 kesit_2=gl[i]["karetel11"] * gl[i]["karetel12"],
                                                                 tel_yogunluk=tel_yogunlugu_1(
                                                                     tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_karetel_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                     kesit_2=gl[i]["karetel21"] * gl[i]["karetel22"],
                                                                     tel_yogunluk=tel_yogunlugu_1(
                                                                         tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_karetel_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                     kesit_2=gl[i]["karetel31"] * gl[i]["karetel32"],
                                                                     tel_yogunluk=tel_yogunlugu_1(
                                                                         tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_karetel_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                     kesit_2=gl[i]["karetel41"] * gl[i]["karetel42"],
                                                                     tel_yogunluk=tel_yogunlugu_1(
                                                                         tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_folyo_1"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                     kesit_2=gl[i]["folyotel11"] * gl[i]["folyotel12"],
                                                                     tel_yogunluk=tel_yogunlugu_1(
                                                                         tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_folyo_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                   kesit_2=gl[i]["folyotel21"] * gl[i]["folyotel22"],
                                                                   tel_yogunluk=tel_yogunlugu_1(
                                                                       tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_folyo_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                   kesit_2=gl[i]["folyotel31"] * gl[i]["folyotel32"],
                                                                   tel_yogunluk=tel_yogunlugu_1(
                                                                       tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_folyo_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                   kesit_2=gl[i]["folyotel41"] * gl[i]["folyotel42"],
                                                                   tel_yogunluk=tel_yogunlugu_1(
                                                                       tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
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
        
def trafo_hesap_trifaz_oto( gl, guc, frekans, 
                   gauss, karkas_en, karkas_boy, 
                   karkas_yuk, verim, sarim, 
                   primer_sarim_yukseklik_toplam,
                   primer_izolasyon,
                   baglanti,
                   kademe=1,
                   cu_par= 0,
                    cu_yog=0,
                    al_par= 0,
                    al_yog=0,
                    dig_par=0,
                    dig_yog=0):
        
        
        for i in range(0, 10):
            
            if gl[i]["voltaj"]> 0 :
                
                # Akım 1 Hesabı -------------------------
                if i == 0:
                    akim_2=0
                    
                    if gl[9]["voltaj"]>0:
                        akim_2=gl[9]["akim1"]
                    elif gl[8]["voltaj"]>0:
                        akim_2=gl[8]["akim1"]
                    elif gl[7]["voltaj"]>0:
                        akim_2=gl[7]["akim1"]
                    elif gl[6]["voltaj"]>0:
                        akim_2=gl[6]["akim1"]
                    elif gl[5]["voltaj"]>0:
                        akim_2=gl[5]["akim1"]
                    elif gl[4]["voltaj"]>0:
                        akim_2=gl[4]["akim1"]
                    elif gl[3]["voltaj"]>0:
                        akim_2=gl[3]["akim1"]
                    elif gl[2]["voltaj"]>0:
                        akim_2=gl[2]["akim1"]
                    elif gl[1]["voltaj"]>0:
                        akim_2=gl[1]["akim1"]
                    else :
                        akim_2=0
                    gl[0]["akim1"]=(akim_hesap_5(guc=guc,gerilim=gl[i]["voltaj"])-akim_2)
                elif i>0:
                    gl[i]["akim1"]=akim_hesap_5(
                                guc=guc,
                                gerilim=gl[i]["voltaj"])
                # Kesit 1 Hesabı -------------------------
                gl[i]["kesit1"]=kesit_hesap_1(
                    akim=gl[i]["akim1"],
                    akim_yogunlugu=akim_yogunlugu_1(
                        tel_turu=gl[i]["teltipi"],
                        cu_par=cu_par,
                        cu_yog=cu_yog,
                        al_par=al_par,
                        al_yog=al_yog,
                        dig_par=dig_par,
                        dig_yog=dig_yog))
                # cap 1 Hesabı -------------------------
                gl[i]["cap1"]=cap_hesap_1(
                    kesit=gl[i]["kesit1"])
                # spir 1 Hesabı -------------------------
                gl[i]["spir1"]=spir_hesap_3(
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
                        tel_turu=gl[i]["teltipi"],
                        cu_par=cu_par,
                        cu_yog=cu_yog,
                        al_par=al_par,
                        al_yog=al_yog,
                        dig_par=dig_par,
                        dig_yog=dig_yog))
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
                                        a0 + 8 * primer_sarim_yukseklik_toplam +  4 *
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
                                                   tel_yogunluk=tel_yogunlugu_1(tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))

                        gl[i]["agr_tel_1"]=tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"], kesit_2=kesit_hesap_2(cap=gl[i]["mancap_1"]),
                                                   tel_yogunluk=tel_yogunlugu_1(tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_tel_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                 kesit_2=kesit_hesap_2(cap=gl[i]["mancap_2"]),
                                                                 tel_yogunluk=tel_yogunlugu_1(
                                                                     tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_tel_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                 kesit_2=kesit_hesap_2(cap=gl[i]["mancap_3"]),
                                                                 tel_yogunluk=tel_yogunlugu_1(
                                                                     tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_tel_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                 kesit_2=kesit_hesap_2(cap=gl[i]["mancap_4"]),
                                                                 tel_yogunluk=tel_yogunlugu_1(
                                                                     tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_karetel_1"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                 kesit_2=gl[i]["karetel11"] * gl[i]["karetel12"],
                                                                 tel_yogunluk=tel_yogunlugu_1(
                                                                     tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_karetel_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                     kesit_2=gl[i]["karetel21"] * gl[i]["karetel22"],
                                                                     tel_yogunluk=tel_yogunlugu_1(
                                                                         tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_karetel_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                     kesit_2=gl[i]["karetel31"] * gl[i]["karetel32"],
                                                                     tel_yogunluk=tel_yogunlugu_1(
                                                                         tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_karetel_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                     kesit_2=gl[i]["karetel41"] * gl[i]["karetel42"],
                                                                     tel_yogunluk=tel_yogunlugu_1(
                                                                         tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_folyo_1"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                     kesit_2=gl[i]["folyotel11"] * gl[i]["folyotel12"],
                                                                     tel_yogunluk=tel_yogunlugu_1(
                                                                         tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_folyo_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                   kesit_2=gl[i]["folyotel21"] * gl[i]["folyotel22"],
                                                                   tel_yogunluk=tel_yogunlugu_1(
                                                                       tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_folyo_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                   kesit_2=gl[i]["folyotel31"] * gl[i]["folyotel32"],
                                                                   tel_yogunluk=tel_yogunlugu_1(
                                                                       tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_folyo_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                   kesit_2=gl[i]["folyotel41"] * gl[i]["folyotel42"],
                                                                   tel_yogunluk=tel_yogunlugu_1(
                                                                       tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
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
        
def trafo_hesap_monofaz_oto( gl, guc, frekans, 
                   gauss, karkas_en, karkas_boy, 
                   karkas_yuk, verim, sarim, 
                   primer_sarim_yukseklik_toplam,
                   primer_izolasyon,
                   baglanti,
                   kademe=1,
                   cu_par= 0,
                    cu_yog=0,
                    al_par= 0,
                    al_yog=0,
                    dig_par=0,
                    dig_yog=0):
        
        
        for i in range(0, 10):
            
            if gl[i]["voltaj"]> 0 :
                
                # Akım 1 Hesabı -------------------------
                if i == 0:
                    akim_2=0
                    
                    if gl[9]["voltaj"]>0:
                        akim_2=gl[9]["akim1"]
                    elif gl[8]["voltaj"]>0:
                        akim_2=gl[8]["akim1"]
                    elif gl[7]["voltaj"]>0:
                        akim_2=gl[7]["akim1"]
                    elif gl[6]["voltaj"]>0:
                        akim_2=gl[6]["akim1"]
                    elif gl[5]["voltaj"]>0:
                        akim_2=gl[5]["akim1"]
                    elif gl[4]["voltaj"]>0:
                        akim_2=gl[4]["akim1"]
                    elif gl[3]["voltaj"]>0:
                        akim_2=gl[3]["akim1"]
                    elif gl[2]["voltaj"]>0:
                        akim_2=gl[2]["akim1"]
                    elif gl[1]["voltaj"]>0:
                        akim_2=gl[1]["akim1"]
                    else :
                        akim_2=0
                             
                    gl[0]["akim1"]=(akim_hesap_1(guc=guc,gerilim=gl[0]["voltaj"])-akim_2)
                            
                    
                elif i>0:
                    
                        
                    gl[i]["akim1"]=akim_hesap_1(
                                guc=guc,
                                gerilim=gl[i]["voltaj"])
                   
                # Kesit 1 Hesabı -------------------------
                gl[i]["kesit1"]=kesit_hesap_1(
                    akim=gl[i]["akim1"],
                    akim_yogunlugu=akim_yogunlugu_1(
                        tel_turu=gl[i]["teltipi"],
                        cu_par=cu_par,
                        cu_yog=cu_yog,
                        al_par=al_par,
                        al_yog=al_yog,
                        dig_par=dig_par,
                        dig_yog=dig_yog))
                # cap 1 Hesabı -------------------------
                gl[i]["cap1"]=cap_hesap_1(
                    kesit=gl[i]["kesit1"])
                # spir 1 Hesabı -------------------------
                
                gl[i]["spir1"]=spir_hesap_1(
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
                        tel_turu=gl[i]["teltipi"],
                        cu_par=cu_par,
                        cu_yog=cu_yog,
                        al_par=al_par,
                        al_yog=al_yog,
                        dig_par=dig_par,
                        dig_yog=dig_yog))
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
                                        a0 + 8 * primer_sarim_yukseklik_toplam  + 4 *
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
                                                   tel_yogunluk=tel_yogunlugu_1(tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))

                        gl[i]["agr_tel_1"]=tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"], kesit_2=kesit_hesap_2(cap=gl[i]["mancap_1"]),
                                                   tel_yogunluk=tel_yogunlugu_1(tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_tel_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                 kesit_2=kesit_hesap_2(cap=gl[i]["mancap_2"]),
                                                                 tel_yogunluk=tel_yogunlugu_1(
                                                                     tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_tel_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                 kesit_2=kesit_hesap_2(cap=gl[i]["mancap_3"]),
                                                                 tel_yogunluk=tel_yogunlugu_1(
                                                                     tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_tel_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                 kesit_2=kesit_hesap_2(cap=gl[i]["mancap_4"]),
                                                                 tel_yogunluk=tel_yogunlugu_1(
                                                                     tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_karetel_1"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                 kesit_2=gl[i]["karetel11"] * gl[i]["karetel12"],
                                                                 tel_yogunluk=tel_yogunlugu_1(
                                                                     tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_karetel_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                     kesit_2=gl[i]["karetel21"] * gl[i]["karetel22"],
                                                                     tel_yogunluk=tel_yogunlugu_1(
                                                                         tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_karetel_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                     kesit_2=gl[i]["karetel31"] * gl[i]["karetel32"],
                                                                     tel_yogunluk=tel_yogunlugu_1(
                                                                         tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_karetel_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                     kesit_2=gl[i]["karetel41"] * gl[i]["karetel42"],
                                                                     tel_yogunluk=tel_yogunlugu_1(
                                                                         tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_folyo_1"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                     kesit_2=gl[i]["folyotel11"] * gl[i]["folyotel12"],
                                                                     tel_yogunluk=tel_yogunlugu_1(
                                                                         tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_folyo_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                   kesit_2=gl[i]["folyotel21"] * gl[i]["folyotel22"],
                                                                   tel_yogunluk=tel_yogunlugu_1(
                                                                       tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_folyo_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                   kesit_2=gl[i]["folyotel31"] * gl[i]["folyotel32"],
                                                                   tel_yogunluk=tel_yogunlugu_1(
                                                                       tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_folyo_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                   kesit_2=gl[i]["folyotel41"] * gl[i]["folyotel42"],
                                                                   tel_yogunluk=tel_yogunlugu_1(
                                                                       tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
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

def trafo_hesap_monoFazUI_izole( gl, guc, frekans, 
                   gauss, karkas_en, karkas_boy, 
                   karkas_yuk, verim, sarim, 
                   primer_sarim_yukseklik_toplam,
                   primer_izolasyon,
                   baglanti,
                   kademe=1,
                   cu_par= 0,
                    cu_yog=0,
                    al_par= 0,
                    al_yog=0,
                    dig_par=0,
                    dig_yog=0):
        
        
        for i in range(0, 10):
            
            if gl[i]["voltaj"]> 0 :
                
                # Akım 1 Hesabı -------------------------
                if baglanti=="Seri":
                    
                    gl[i]["akim1"]=akim_hesap_1(
                            guc=guc,
                            gerilim=gl[i]["voltaj"])
                elif baglanti=="Paralel":
                    gl[i]["akim1"]=akim_hesap_6(
                            guc=guc,
                            gerilim=gl[i]["voltaj"])
                else:
                    print("Akım hesaplanamadı . yanlıs Bağlanı Seçimi",baglanti," +")
                
                # Kesit 1 Hesabı -------------------------
                gl[i]["kesit1"]=kesit_hesap_1(
                    akim=gl[i]["akim1"],
                    akim_yogunlugu=akim_yogunlugu_1(
                        tel_turu=gl[i]["teltipi"],
                        cu_par=cu_par,
                        cu_yog=cu_yog,
                        al_par=al_par,
                        al_yog=al_yog,
                        dig_par=dig_par,
                        dig_yog=dig_yog))
                # cap 1 Hesabı -------------------------
                gl[i]["cap1"]=cap_hesap_1(
                    kesit=gl[i]["kesit1"])
                # spir 1 Hesabı -------------------------
                if baglanti=="Seri":
                    gl[i]["spir1"]=spir_hesap_7(
                        gerilim=gl[i]["voltaj"],
                        frekans=frekans,
                        gauss=gauss,
                        karkas_en=karkas_en,
                        karkas_boy=karkas_boy,
                        verim=verim)
                elif baglanti=="Paralel":
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
                        tel_turu=gl[i]["teltipi"],
                        cu_par=cu_par,
                        cu_yog=cu_yog,
                        al_par=al_par,
                        al_yog=al_yog,
                        dig_par=dig_par,
                        dig_yog=dig_yog))
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
                                        a0 + 8 * primer_sarim_yukseklik_toplam  + 4 *
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
                                                   tel_yogunluk=tel_yogunlugu_1(tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))

                        gl[i]["agr_tel_1"]=tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"], kesit_2=kesit_hesap_2(cap=gl[i]["mancap_1"]),
                                                   tel_yogunluk=tel_yogunlugu_1(tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_tel_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                 kesit_2=kesit_hesap_2(cap=gl[i]["mancap_2"]),
                                                                 tel_yogunluk=tel_yogunlugu_1(
                                                                     tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_tel_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                 kesit_2=kesit_hesap_2(cap=gl[i]["mancap_3"]),
                                                                 tel_yogunluk=tel_yogunlugu_1(
                                                                     tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_tel_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                 kesit_2=kesit_hesap_2(cap=gl[i]["mancap_4"]),
                                                                 tel_yogunluk=tel_yogunlugu_1(
                                                                     tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_karetel_1"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                 kesit_2=gl[i]["karetel11"] * gl[i]["karetel12"],
                                                                 tel_yogunluk=tel_yogunlugu_1(
                                                                     tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_karetel_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                     kesit_2=gl[i]["karetel21"] * gl[i]["karetel22"],
                                                                     tel_yogunluk=tel_yogunlugu_1(
                                                                         tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_karetel_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                     kesit_2=gl[i]["karetel31"] * gl[i]["karetel32"],
                                                                     tel_yogunluk=tel_yogunlugu_1(
                                                                         tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_karetel_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                     kesit_2=gl[i]["karetel41"] * gl[i]["karetel42"],
                                                                     tel_yogunluk=tel_yogunlugu_1(
                                                                         tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_folyo_1"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                     kesit_2=gl[i]["folyotel11"] * gl[i]["folyotel12"],
                                                                     tel_yogunluk=tel_yogunlugu_1(
                                                                         tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_folyo_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                   kesit_2=gl[i]["folyotel21"] * gl[i]["folyotel22"],
                                                                   tel_yogunluk=tel_yogunlugu_1(
                                                                       tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_folyo_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                   kesit_2=gl[i]["folyotel31"] * gl[i]["folyotel32"],
                                                                   tel_yogunluk=tel_yogunlugu_1(
                                                                       tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
                        gl[i]["agr_folyo_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[i]["tel_uzunluk"],
                                                                   kesit_2=gl[i]["folyotel41"] * gl[i]["folyotel42"],
                                                                   tel_yogunluk=tel_yogunlugu_1(
                                                                       tel_turu=gl[i]["teltipi"],
                        cu_yog=cu_yog,
                        al_yog=al_yog,
                        dig_yog=dig_yog))
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

def trafo_hesap_monofaz_sont( gl, guc, frekans, 
                   gauss, karkas_en, karkas_boy, 
                   karkas_yuk, verim, sarim, 
                   primer_sarim_yukseklik_toplam,
                   cu_par,
                    cu_yog,
                    al_par,
                    al_yog,
                    dig_par,
                    dig_yog,
                    Lg_man,
                    c,Kf,Ku,Um,
                    klemens_a, 
                    klemens_b, 
                    ayak_a):
        
        degerler = {}
        
           
        if gl[0]["voltaj"]> 0 :
            
            # Akım 1 Hesabı -------------------------
            
            gl[0]["akim1"]=akim_hesap_1(guc=guc,gerilim=gl[0]["voltaj"])
                    
            # Kesit 1 Hesabı -------------------------
            gl[0]["kesit1"]=kesit_hesap_1(
                akim=gl[0]["akim1"],
                akim_yogunlugu=akim_yogunlugu_1(
                    tel_turu=gl[0]["teltipi"],
                    cu_par=cu_par,
                    cu_yog=cu_yog,
                    al_par=al_par,
                    al_yog=al_yog,
                    dig_par=dig_par,
                    dig_yog=dig_yog))
            # cap 1 Hesabı -------------------------
            gl[0]["cap1"]=cap_hesap_1(
                kesit=gl[0]["kesit1"])
            # Karkas Man Hesabı -------------------------
            degerler["karkas_man"]=karkas_Ac(karkas_en=karkas_en,karkas_boy=karkas_boy)
            degerler["karkas_oto"]=karkas_Ac_oto(c=c, guc=guc, frekans=frekans)
            degerler["karkas_yuk_oto"]=karkas_yuk_oto(karkas_en=karkas_en)
            degerler["mpl"]=mpl_hesap_1(karkas_en=karkas_en,karkas_yuk=karkas_yuk)
            # Enduktans Hesabı -------------------------
            degerler["akim_t"]=gl[0]["akim1"]
            degerler["enduktans"]= end_hesap_1(
                gerilim=gl[0]["voltaj"],
                frekans=frekans, 
                akim=gl[0]["akim1"])
            # F man Hesabı -------------------------
            degerler["f_man"] = f_hesap_1(Lg=Lg_man, karkas_Ac=degerler["karkas_man"], karkas_yuk=karkas_yuk)
            degerler["Ap"] = Ap_hesap_1(
                guc=guc, 
                karkas_yuk=karkas_yuk, 
                Kf=Kf, 
                Ku=Ku, 
                gauss=gauss, 
                frekans=frekans, 
                tel_turu=gl[0]["teltipi"], 
                cu_par=cu_par, 
                cu_yog=cu_yog, 
                al_par=al_par, 
                al_yog=al_yog, 
                dig_par=dig_par, 
                dig_yog=dig_yog)
            degerler["ApSac"] = ApSac_hesap_1(karkas_en=karkas_en, karkas_boy=karkas_boy)
            degerler["sp1"] =spir_hesap_10(
                gerilim=gl[0]["voltaj"], 
                gauss=gauss, 
                frekans=frekans, 
                karkas_man=degerler["karkas_man"], 
                Kf=Kf)
            
            degerler["Lg_mpl"] = Lg_mpl_hesap_1(
                mpl=degerler["mpl"], 
                enduktans=degerler["enduktans"], 
                karkas_man=degerler["karkas_man"], 
                sp1=degerler["sp1"], 
                karkas_en=karkas_en, 
                karkas_boy=karkas_boy,
                Um=Um)
            degerler["Lg_oto"] = Lg_oto_hesap_1(
                enduktans=degerler["enduktans"], 
                karkas_man=degerler["karkas_man"], 
                sp1=degerler["sp1"], 
                karkas_en=karkas_en, 
                karkas_boy=karkas_boy)
            degerler["f_oto"]=f_hesap_1(Lg= degerler["Lg_oto"], karkas_Ac=degerler["karkas_man"], karkas_yuk=karkas_yuk)
            degerler["sp1_oto"]=spir_hesap_8(Lg=degerler["Lg_oto"],enduktans=degerler["enduktans"],f_man= degerler["f_oto"],karkas_man=degerler["karkas_man"])
            degerler["f_mpl"]=f_hesap_1(Lg=degerler["Lg_mpl"], karkas_Ac=degerler["karkas_man"], karkas_yuk=karkas_yuk)
            degerler["sp1_mpl"]=spir_hesap_8(Lg=degerler["Lg_mpl"],enduktans=degerler["enduktans"],f_man= degerler["f_mpl"],karkas_man=degerler["karkas_man"])
            degerler["nuveOlcu_a"],degerler["nuveOlcu_b"],degerler["nuveOlcu_c"]=nuve_olcu_hesapla(
                karkas_en=karkas_en, 
                karkas_boy=karkas_boy, 
                klemens_a=klemens_a, 
                klemens_b=klemens_b, 
                ayak_a=ayak_a)
            degerler["sac_agirlik"]=sac_agirlik(karkas_en=karkas_en,karkas_boy=karkas_boy)
            degerler["bosluk"]=0
            # spir 1 Hesabı -------------------------

            gl[0]["spir1"]=spir_hesap_8(Lg=Lg_man,enduktans=degerler["enduktans"],f_man= degerler["f_man"],karkas_man=degerler["karkas_man"])
            degerler["sp1_man"] =  gl[0]["spir1"]  
            # spir 2 Hesabı -------------------------
            if gl[0]["check_spir_man"]==True:
                pass
            else:
                gl[0]["spir2"]=round(gl[0]["spir1"])
            # Kesit 2 Hesabı -------------------------
            gl[0]["kesit2"]= kesit_hesap_2(cap=gl[0]["mancap_1"]) + \
                kesit_hesap_2(cap=gl[0]["mancap_2"]) +\
                kesit_hesap_2(cap=gl[0]["mancap_3"]) +\
                kesit_hesap_2(cap=gl[0]["mancap_4"]) +\
                (gl[0]["folyotel11"] * gl[0]["folyotel12"]) +\
                (gl[0]["folyotel21"] * gl[0]["folyotel22"]) +\
                (gl[0]["folyotel31"] * gl[0]["folyotel32"]) +\
                (gl[0]["folyotel41"] * gl[0]["folyotel42"]) +\
                (gl[0]["karetel11"] * gl[0]["karetel12"]) +\
                (gl[0]["karetel21"] * gl[0]["karetel22"]) +\
                (gl[0]["karetel31"] * gl[0]["karetel32"]) +\
                (gl[0]["karetel41"] * gl[0]["karetel42"])
            # Akım 2 Hesabı -------------------------
            gl[0]["akim2"]=akim_hesap_2(

                kesit=gl[0]["kesit2"],
                akim_yogunlugu=akim_yogunlugu_1(
                    tel_turu=gl[0]["teltipi"],
                    cu_par=cu_par,
                    cu_yog=cu_yog,
                    al_par=al_par,
                    al_yog=al_yog,
                    dig_par=dig_par,
                    dig_yog=dig_yog))
            # cap 2 Hesabı -------------------------
            gl[0]["cap2"]= gl[0]["mancap_1"] + gl[0]["mancap_2"] + gl[0]["mancap_3"] + gl[0]["mancap_4"]
            # akım 2 ve kesit 2 kontrol -------------------------
            if gl[0]["kesit1"] <= gl[0]["kesit2"]:
                gl[0]["kesit_ok"]=True
                gl[0]["kesit_error"]=False
            else:
                gl[0]["kesit_ok"]=False
                gl[0]["kesit_error"]=True
            if gl[0]["akim1"] <= gl[0]["akim2"]:
                gl[0]["akim_ok"]=True
                gl[0]["akim_error"]=False
            else:
                gl[0]["akim_ok"]=False
                gl[0]["akim_error"]=True
            # -------------------------
            tel_cap = 0

            for tel_kademe in range(1, 5):

                data = db.showfilter_tel_spir(filter_value=gl[0][f"mancap_{tel_kademe}"] , index=0)

                if data == [] and gl[0][f"mancap_{tel_kademe}"] > 0:
                    tel_cap +=  (gl[0]["mancap_1"]) * 1.02
                elif data != [] and gl[0][f"mancap_{tel_kademe}"] > 0:
                    tel_cap += data[0][4]
            
            # tel yüksekliği Hesabı -------------------------
            gl[0]["tel_yuk"]=tel_yukseklik_hesap_1(
                tel_cap=tel_cap, karetel_yuk1=gl[0]["karetel12"],
                karetel_yuk2=gl[0]["karetel22"],
                karetel_yuk3=gl[0]["karetel32"], karetel_yuk4=gl[0]["karetel42"],
                folyo_yuk1=gl[0]["folyotel12"], folyo_yuk2=gl[0]["folyotel22"],
                folyo_yuk3=gl[0]["folyotel32"], folyo_yuk4=gl[0]["folyotel42"],
                kapton1=gl[0]["kapton1"], kapton2=gl[0]["kapton2"],
                kapton3=gl[0]["kapton3"], kapton4=gl[0]["kapton4"])
            # tel en Hesabı -------------------------
            gl[0]["tel_en"]= tel_en_hesap_1(
                tel_cap=tel_cap,
                karetel_en1=gl[0]["karetel11"],
                karetel_en2=gl[0]["karetel21"],
                karetel_en3=gl[0]["karetel31"], karetel_en4=gl[0]["karetel41"],
                folyo_en1=gl[0]["folyotel11"], folyo_en2=gl[0]["folyotel21"],
                folyo_en3=gl[0]["folyotel31"], folyo_en4=gl[0]["folyotel41"],
                )

            if gl[0]["tel_en"] > 0:
                # spir kat Hesabı -------------------------
                gl[0]["spirkat"]=spir_kat_hesap_1(
                    karkas_yuk=karkas_yuk,
                    tel_en=gl[0]["tel_en"])

                #  kat sayısı -------------------------------
                
                gl[0]["kat"]=kat_sayisi_hesap_1(
                    spir=gl[0]["spir2"],
                    spir_kat=gl[0]["spirkat"])

                
                # sarım yuksekliği  -------------------------
                gl[0]["sarim_yukseklik"]=sarim_yüksekligi_hesap_1(
                    tel_yuk=gl[0]["tel_yuk"],
                    kat_sayisi=gl[0]["kat"])
                
                # bosluk   -------------------------
                degerler["bosluk"]=bosluk_hesap_1(karkas_en=karkas_en,
                primer_top_yuk=gl[0]["sarim_yukseklik"],sekonder_top_yuk =0 ,primer_izolasyon=0)
                
                # son kat
                

                try :
                    if math.fmod(gl[0]["spir2"], gl[0]["spirkat"]) == 0:
                        gl[0]["sonkat_spir"]=gl[0]["spirkat"]
                    else:
                        gl[0]["sonkat_spir"]=son_kat_hesap_1(
                            spir_2=gl[0]["spir2"],
                            spir_kat=gl[0]["spirkat"])
                except Exception as err:
                    print(err)
                
                    # kattaki bosluk ---------------------------
                
                gl[0]["katbosluk"]=kattaki_bosluk_hesap_1(
                    karkas_yuk=karkas_yuk,
                    tel_en=gl[0]["tel_en"],
                    son_kat=gl[0]["sonkat_spir"]
                )
                
                

                # tel uzunluk  ---------------------------
                a0 = 2 * (karkas_en + karkas_boy) + 8 * 0.05 * karkas_en
                
                
                
                gl[0]["tel_uzunluk"]=((gl[0]["kat"] - 1) * ((2 * (karkas_en + karkas_boy)) +
                                                    8 * karkas_en * 0.05 + 4 * gl[0]["tel_yuk"]) + \
                            (8 * gl[0]["tel_yuk"] * (gl[0]["kat"] - 1) * (gl[0]["kat"] - 2) / 2)) / 1000 *\
                        gl[0]["spirkat"] + \
                        ((2 * (karkas_en + karkas_boy)) + \
                            8 * karkas_en * 0.05 + 4 * gl[0]["tel_yuk"] + \
                            (8 * gl[0]["tel_yuk"] * (gl[0]["kat"] - 1))) / 1000 * gl[0]["sonkat_spir"]
                

                # tel agirlik  ---------------------------
                if gl[0]["tel_uzunluk"] != 0:
                    gl[0]["tel_agirlik"]=tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"], kesit_2=gl[0]["kesit2"],
                                                tel_yogunluk=tel_yogunlugu_1(tel_turu=gl[0]["teltipi"],
                    cu_yog=cu_yog,
                    al_yog=al_yog,
                    dig_yog=dig_yog))
                    
                    gl[0]["agr_tel_1"]=tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"], kesit_2=kesit_hesap_2(cap=gl[0]["mancap_1"]),
                                                tel_yogunluk=tel_yogunlugu_1(tel_turu=gl[0]["teltipi"],
                    cu_yog=cu_yog,
                    al_yog=al_yog,
                    dig_yog=dig_yog))
                    gl[0]["agr_tel_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=kesit_hesap_2(cap=gl[0]["mancap_2"]),
                                                                tel_yogunluk=tel_yogunlugu_1(
                                                                    tel_turu=gl[0]["teltipi"],
                    cu_yog=cu_yog,
                    al_yog=al_yog,
                    dig_yog=dig_yog))
                    gl[0]["agr_tel_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=kesit_hesap_2(cap=gl[0]["mancap_3"]),
                                                                tel_yogunluk=tel_yogunlugu_1(
                                                                    tel_turu=gl[0]["teltipi"],
                    cu_yog=cu_yog,
                    al_yog=al_yog,
                    dig_yog=dig_yog))
                    gl[0]["agr_tel_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=kesit_hesap_2(cap=gl[0]["mancap_4"]),
                                                                tel_yogunluk=tel_yogunlugu_1(
                                                                    tel_turu=gl[0]["teltipi"],
                    cu_yog=cu_yog,
                    al_yog=al_yog,
                    dig_yog=dig_yog))
                    gl[0]["agr_karetel_1"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=gl[0]["karetel11"] * gl[0]["karetel12"],
                                                                tel_yogunluk=tel_yogunlugu_1(
                                                                    tel_turu=gl[0]["teltipi"],
                    cu_yog=cu_yog,
                    al_yog=al_yog,
                    dig_yog=dig_yog))
                    gl[0]["agr_karetel_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                    kesit_2=gl[0]["karetel21"] * gl[0]["karetel22"],
                                                                    tel_yogunluk=tel_yogunlugu_1(
                                                                        tel_turu=gl[0]["teltipi"],
                    cu_yog=cu_yog,
                    al_yog=al_yog,
                    dig_yog=dig_yog))
                    gl[0]["agr_karetel_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                    kesit_2=gl[0]["karetel31"] * gl[0]["karetel32"],
                                                                    tel_yogunluk=tel_yogunlugu_1(
                                                                        tel_turu=gl[0]["teltipi"],
                    cu_yog=cu_yog,
                    al_yog=al_yog,
                    dig_yog=dig_yog))
                    gl[0]["agr_karetel_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                    kesit_2=gl[0]["karetel41"] * gl[0]["karetel42"],
                                                                    tel_yogunluk=tel_yogunlugu_1(
                                                                        tel_turu=gl[0]["teltipi"],
                    cu_yog=cu_yog,
                    al_yog=al_yog,
                    dig_yog=dig_yog))
                    gl[0]["agr_folyo_1"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                    kesit_2=gl[0]["folyotel11"] * gl[0]["folyotel12"],
                                                                    tel_yogunluk=tel_yogunlugu_1(
                                                                        tel_turu=gl[0]["teltipi"],
                    cu_yog=cu_yog,
                    al_yog=al_yog,
                    dig_yog=dig_yog))
                    gl[0]["agr_folyo_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=gl[0]["folyotel21"] * gl[0]["folyotel22"],
                                                                tel_yogunluk=tel_yogunlugu_1(
                                                                    tel_turu=gl[0]["teltipi"],
                    cu_yog=cu_yog,
                    al_yog=al_yog,
                    dig_yog=dig_yog))
                    gl[0]["agr_folyo_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=gl[0]["folyotel31"] * gl[0]["folyotel32"],
                                                                tel_yogunluk=tel_yogunlugu_1(
                                                                    tel_turu=gl[0]["teltipi"],
                    cu_yog=cu_yog,
                    al_yog=al_yog,
                    dig_yog=dig_yog))
                    gl[0]["agr_folyo_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=gl[0]["folyotel41"] * gl[0]["folyotel42"],
                                                                tel_yogunluk=tel_yogunlugu_1(
                                                                    tel_turu=gl[0]["teltipi"],
                    cu_yog=cu_yog,
                    al_yog=al_yog,
                    dig_yog=dig_yog))
                    gl[0]["agr_kapton_1"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=gl[0]["kapton1"],
                                                                tel_yogunluk=1330)
                    gl[0]["agr_kapton_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=gl[0]["kapton2"],
                                                                tel_yogunluk=1330)
                    gl[0]["agr_kapton_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=gl[0]["kapton3"],
                                                                tel_yogunluk=1330)
                    gl[0]["agr_kapton_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=gl[0]["kapton4"],
                                                                tel_yogunluk=1330)
                else:
                    
                    gl[0]["tel_agirlik"]=0
                    gl[0]["agr_tel_1"] = 0
                    gl[0]["agr_tel_2"] = 0
                    gl[0]["agr_tel_3"] = 0
                    gl[0]["agr_tel_4"] = 0
                    gl[0]["agr_karetel_1"] = 0
                    gl[0]["agr_karetel_2"] = 0
                    gl[0]["agr_karetel_3"] = 0
                    gl[0]["agr_karetel_4"] = 0
                    gl[0]["agr_folyo_1"] = 0
                    gl[0]["agr_folyo_2"] = 0
                    gl[0]["agr_folyo_3"] = 0
                    gl[0]["agr_folyo_4"] = 0
                    gl[0]["agr_kapton_1"] = 0
                    gl[0]["agr_kapton_2"] = 0
                    gl[0]["agr_kapton_3"] = 0
                    gl[0]["agr_kapton_4"] = 0

        else:
            degerler.clear()
            gl[0]["akim1"]=0
            gl[0]["kesit1"]=0
            gl[0]["cap1"]=0
            gl[0]["spir1"]=0
            gl[0]["cap2"]=0
            gl[0]["akim2"]=0
            gl[0]["spir2"]=0
            gl[0]["folyotel11"]=0
            gl[0]["folyotel12"]=0
            gl[0]["folyotel21"]=0
            gl[0]["folyotel22"]=0
            gl[0]["folyotel31"]=0
            gl[0]["folyotel32"]=0
            gl[0]["folyotel41"]=0
            gl[0]["folyotel42"]=0
            gl[0]["kapton1"]=0
            gl[0]["kapton2"]=0
            gl[0]["kapton3"]=0
            gl[0]["kapton4"]=0
            gl[0]["karetel11"]=0
            gl[0]["karetel12"]=0
            gl[0]["karetel21"]=0
            gl[0]["karetel22"]=0
            gl[0]["karetel31"]=0
            gl[0]["karetel32"]=0
            gl[0]["karetel41"]=0
            gl[0]["karetel42"]=0
            gl[0]["kesit2"]=0
            gl[0]["tel_en"]=0
            gl[0]["tel_yuk"]=0
            gl[0]["spirkat"]=0
            gl[0]["kat"]=0
            gl[0]["katbosluk"]=0
            gl[0]["tel_uzunluk"]=0
            gl[0]["tel_agirlik"]=0
            gl[0]["sarim_yukseklik"]=0
            gl[0]["sonkat_spir"]=0
            gl[0]["check_spir_man"] = False
            gl[0]["kesit_ok"]=False
            gl[0]["kesit_error"]=True
            gl[0]["akim_ok"]=False
            gl[0]["akim_error"]=True
            gl[0]["mancap_1"]=0
            gl[0]["mancap_2"]=0
            gl[0]["mancap_3"]=0
            gl[0]["mancap_4"]=0
            gl[0]["mlz_tel_1"] = ""
            gl[0]["mlz_tel_2"] = ""
            gl[0]["mlz_tel_3"] =  ""
            gl[0]["mlz_tel_4"] =  ""
            gl[0]["mlz_karetel_1"] =  ""
            gl[0]["mlz_karetel_2"] =  ""
            gl[0]["mlz_karetel_3"] =  ""
            gl[0]["mlz_karetel_4"] =  ""
            gl[0]["mlz_folyotel_1"] =  ""
            gl[0]["mlz_folyotel_2"] =  ""
            gl[0]["mlz_folyotel_3"] =  ""
            gl[0]["mlz_folyotel_4"] =  ""
            gl[0]["mlz_kapton_1"] =  ""
            gl[0]["mlz_kapton_2"] =  ""
            gl[0]["mlz_kapton_3"] =  ""
            gl[0]["mlz_kapton_4"] =  ""
            gl[0]["gb_check_tel_1"] =  False
            gl[0]["gb_check_tel_2"] =  False
            gl[0]["gb_check_tel_3"] =  False
            gl[0]["gb_check_tel_4"] =  False
            gl[0]["gb_check_karetel_1"]= False
            gl[0]["gb_check_karetel_2"]= False
            gl[0]["gb_check_karetel_3"]= False
            gl[0]["gb_check_karetel_4"]= False
            gl[0]["gb_check_folyotel_1"]= False
            gl[0]["gb_check_folyotel_2"]= False
            gl[0]["gb_check_folyotel_3"]= False
            gl[0]["gb_check_folyotel_4"]= False
            gl[0]["gb_check_kapton_1"]= False
            gl[0]["gb_check_kapton_2"]= False
            gl[0]["gb_check_kapton_3"]= False
            gl[0]["gb_check_kapton_4"]= False
            gl[0]["tel_agirlik"] = 0
            gl[0]["agr_tel_1"] = 0
            gl[0]["agr_tel_2"] = 0
            gl[0]["agr_tel_3"] = 0
            gl[0]["agr_tel_4"] = 0
            gl[0]["agr_karetel_1"] = 0
            gl[0]["agr_karetel_2"] = 0
            gl[0]["agr_karetel_3"] = 0
            gl[0]["agr_karetel_4"] = 0
            gl[0]["agr_folyo_1"] = 0
            gl[0]["agr_folyo_2"] = 0
            gl[0]["agr_folyo_3"] = 0
            gl[0]["agr_folyo_4"] = 0
            gl[0]["agr_kapton_1"] = 0
            gl[0]["agr_kapton_2"] = 0
            gl[0]["agr_kapton_3"] = 0
            gl[0]["agr_kapton_4"] = 0
        return dict(degerler)      

def trafo_hesap_trifaz_sont( gl, guc, frekans, 
                   gauss, karkas_en, karkas_boy, 
                   karkas_yuk, verim, sarim, 
                   primer_sarim_yukseklik_toplam,
                   cu_par,
                    cu_yog,
                    al_par,
                    al_yog,
                    dig_par,
                    dig_yog,
                    Lg_man,
                    c,Kf,Ku,Um,
                    klemens_a, 
                    klemens_b, 
                    ayak_a):
        
        degerler = {}
        
           
        if gl[0]["voltaj"]> 0 :
            
            # Akım 1 Hesabı -------------------------
            
            gl[0]["akim1"]=akim_hesap_3(guc=guc,gerilim=gl[0]["voltaj"])
                    
            # Kesit 1 Hesabı -------------------------
            gl[0]["kesit1"]=kesit_hesap_1(
                akim=gl[0]["akim1"],
                akim_yogunlugu=akim_yogunlugu_1(
                    tel_turu=gl[0]["teltipi"],
                    cu_par=cu_par,
                    cu_yog=cu_yog,
                    al_par=al_par,
                    al_yog=al_yog,
                    dig_par=dig_par,
                    dig_yog=dig_yog))
            # cap 1 Hesabı -------------------------
            gl[0]["cap1"]=cap_hesap_1(
                kesit=gl[0]["kesit1"])
            # Karkas Man Hesabı -------------------------
            degerler["karkas_man"]=karkas_Ac(karkas_en=karkas_en,karkas_boy=karkas_boy)
            degerler["karkas_oto"]=karkas_Ac_oto_2(c=c, guc=guc, frekans=frekans)
            degerler["karkas_yuk_oto"]=karkas_yuk_2(karkas_en=karkas_en)
            
            # Enduktans Hesabı -------------------------
            degerler["akim_t"]=gl[0]["akim1"]
            degerler["enduktans"]= end_hesap_2(
                gerilim=gl[0]["voltaj"],
                frekans=frekans, 
                akim=gl[0]["akim1"])
            # F man Hesabı -------------------------
            degerler["f_man"] = f_hesap_1(Lg=Lg_man, karkas_Ac=degerler["karkas_man"], karkas_yuk=karkas_yuk)
            degerler["Ap"] = Ap_hesap_1(
                guc=guc, 
                karkas_yuk=karkas_yuk, 
                Kf=Kf, 
                Ku=Ku, 
                gauss=gauss, 
                frekans=frekans, 
                tel_turu=gl[0]["teltipi"], 
                cu_par=cu_par, 
                cu_yog=cu_yog, 
                al_par=al_par, 
                al_yog=al_yog, 
                dig_par=dig_par, 
                dig_yog=dig_yog)
            degerler["mpl"]=mpl_hesap_2(Ap=degerler["Ap"])
            degerler["ApSac"] = ApSac_hesap_2(karkas_en=karkas_en, karkas_boy=karkas_boy)
            degerler["sp1"] =spir_hesap_11(
                gerilim=gl[0]["voltaj"], 
                gauss=gauss, 
                frekans=frekans, 
                karkas_man=degerler["karkas_man"], 
                Kf=Kf)
            
            degerler["Lg_mpl"] = Lg_mpl_hesap_1(
                mpl=degerler["mpl"], 
                enduktans=degerler["enduktans"], 
                karkas_man=degerler["karkas_man"], 
                sp1=degerler["sp1"], 
                karkas_en=karkas_en, 
                karkas_boy=karkas_boy,
                Um=Um)
            degerler["Lg_oto"] = Lg_oto_hesap_1(
                enduktans=degerler["enduktans"], 
                karkas_man=degerler["karkas_man"], 
                sp1=degerler["sp1"], 
                karkas_en=karkas_en, 
                karkas_boy=karkas_boy)
            degerler["f_oto"]=f_hesap_1(Lg= degerler["Lg_oto"], karkas_Ac=degerler["karkas_man"], karkas_yuk=karkas_yuk)
            degerler["sp1_oto"]=spir_hesap_8(Lg=degerler["Lg_oto"],enduktans=degerler["enduktans"],f_man= degerler["f_oto"],karkas_man=degerler["karkas_man"])
            degerler["f_mpl"]=f_hesap_1(Lg=degerler["Lg_mpl"], karkas_Ac=degerler["karkas_man"], karkas_yuk=karkas_yuk)
            degerler["sp1_mpl"]=spir_hesap_8(Lg=degerler["Lg_mpl"],enduktans=degerler["enduktans"],f_man= degerler["f_mpl"],karkas_man=degerler["karkas_man"])
            degerler["nuveOlcu_a"],degerler["nuveOlcu_b"],degerler["nuveOlcu_c"]=nuve_olcu_hesapla_4(
                karkas_en=karkas_en, 
                karkas_boy=karkas_boy, 
                klemens_a=klemens_a, 
                klemens_b=klemens_b, 
                ayak_a=ayak_a)
            degerler["trafoOlcu_a"],degerler["trafoOlcu_b"],degerler["trafoOlcu_c"],degerler["trafoOlcu_d"],degerler["trafoOlcu_e"],degerler["trafoOlcu_f"]=trafo_olcu_hesapla_6(karkas_en=karkas_en, karkas_boy=karkas_boy)
            degerler["sac_agirlik"]=sac_agirlik_trifaz(karkas_en=karkas_en,karkas_boy=karkas_boy)
            degerler["bosluk"]=0
            # spir 1 Hesabı -------------------------

            gl[0]["spir1"]=spir_hesap_8(Lg=Lg_man,enduktans=degerler["enduktans"],f_man= degerler["f_man"],karkas_man=degerler["karkas_man"])
            degerler["sp1_man"] =  gl[0]["spir1"]  
            # spir 2 Hesabı -------------------------
            if gl[0]["check_spir_man"]==True:
                pass
            else:
                gl[0]["spir2"]=round(gl[0]["spir1"])
            # Kesit 2 Hesabı -------------------------
            gl[0]["kesit2"]= kesit_hesap_2(cap=gl[0]["mancap_1"]) + \
                kesit_hesap_2(cap=gl[0]["mancap_2"]) +\
                kesit_hesap_2(cap=gl[0]["mancap_3"]) +\
                kesit_hesap_2(cap=gl[0]["mancap_4"]) +\
                (gl[0]["folyotel11"] * gl[0]["folyotel12"]) +\
                (gl[0]["folyotel21"] * gl[0]["folyotel22"]) +\
                (gl[0]["folyotel31"] * gl[0]["folyotel32"]) +\
                (gl[0]["folyotel41"] * gl[0]["folyotel42"]) +\
                (gl[0]["karetel11"] * gl[0]["karetel12"]) +\
                (gl[0]["karetel21"] * gl[0]["karetel22"]) +\
                (gl[0]["karetel31"] * gl[0]["karetel32"]) +\
                (gl[0]["karetel41"] * gl[0]["karetel42"])
            # Akım 2 Hesabı -------------------------
            gl[0]["akim2"]=akim_hesap_2(

                kesit=gl[0]["kesit2"],
                akim_yogunlugu=akim_yogunlugu_1(
                    tel_turu=gl[0]["teltipi"],
                    cu_par=cu_par,
                    cu_yog=cu_yog,
                    al_par=al_par,
                    al_yog=al_yog,
                    dig_par=dig_par,
                    dig_yog=dig_yog))
            # cap 2 Hesabı -------------------------
            gl[0]["cap2"]= gl[0]["mancap_1"] + gl[0]["mancap_2"] + gl[0]["mancap_3"] + gl[0]["mancap_4"]
            # akım 2 ve kesit 2 kontrol -------------------------
            if gl[0]["kesit1"] <= gl[0]["kesit2"]:
                gl[0]["kesit_ok"]=True
                gl[0]["kesit_error"]=False
            else:
                gl[0]["kesit_ok"]=False
                gl[0]["kesit_error"]=True
            if gl[0]["akim1"] <= gl[0]["akim2"]:
                gl[0]["akim_ok"]=True
                gl[0]["akim_error"]=False
            else:
                gl[0]["akim_ok"]=False
                gl[0]["akim_error"]=True
            # -------------------------
            tel_cap = 0

            for tel_kademe in range(1, 5):

                data = db.showfilter_tel_spir(filter_value=gl[0][f"mancap_{tel_kademe}"] , index=0)

                if data == [] and gl[0][f"mancap_{tel_kademe}"] > 0:
                    tel_cap +=  (gl[0]["mancap_1"]) * 1.02
                elif data != [] and gl[0][f"mancap_{tel_kademe}"] > 0:
                    tel_cap += data[0][4]
            
            # tel yüksekliği Hesabı -------------------------
            gl[0]["tel_yuk"]=tel_yukseklik_hesap_1(
                tel_cap=tel_cap, karetel_yuk1=gl[0]["karetel12"],
                karetel_yuk2=gl[0]["karetel22"],
                karetel_yuk3=gl[0]["karetel32"], karetel_yuk4=gl[0]["karetel42"],
                folyo_yuk1=gl[0]["folyotel12"], folyo_yuk2=gl[0]["folyotel22"],
                folyo_yuk3=gl[0]["folyotel32"], folyo_yuk4=gl[0]["folyotel42"],
                kapton1=gl[0]["kapton1"], kapton2=gl[0]["kapton2"],
                kapton3=gl[0]["kapton3"], kapton4=gl[0]["kapton4"])
            # tel en Hesabı -------------------------
            gl[0]["tel_en"]= tel_en_hesap_1(
                tel_cap=tel_cap,
                karetel_en1=gl[0]["karetel11"],
                karetel_en2=gl[0]["karetel21"],
                karetel_en3=gl[0]["karetel31"], karetel_en4=gl[0]["karetel41"],
                folyo_en1=gl[0]["folyotel11"], folyo_en2=gl[0]["folyotel21"],
                folyo_en3=gl[0]["folyotel31"], folyo_en4=gl[0]["folyotel41"],
                )

            if gl[0]["tel_en"] > 0:
                # spir kat Hesabı -------------------------
                gl[0]["spirkat"]=spir_kat_hesap_1(
                    karkas_yuk=karkas_yuk,
                    tel_en=gl[0]["tel_en"])

                #  kat sayısı -------------------------------
                
                gl[0]["kat"]=kat_sayisi_hesap_1(
                    spir=gl[0]["spir2"],
                    spir_kat=gl[0]["spirkat"])

                
                # sarım yuksekliği  -------------------------
                gl[0]["sarim_yukseklik"]=sarim_yüksekligi_hesap_1(
                    tel_yuk=gl[0]["tel_yuk"],
                    kat_sayisi=gl[0]["kat"])
                
                # bosluk   -------------------------
                degerler["bosluk"]=bosluk_hesap_1(karkas_en=karkas_en,
                primer_top_yuk=gl[0]["sarim_yukseklik"],sekonder_top_yuk =0 ,primer_izolasyon=0)
                
                # son kat
                

                try :
                    if math.fmod(gl[0]["spir2"], gl[0]["spirkat"]) == 0:
                        gl[0]["sonkat_spir"]=gl[0]["spirkat"]
                    else:
                        gl[0]["sonkat_spir"]=son_kat_hesap_1(
                            spir_2=gl[0]["spir2"],
                            spir_kat=gl[0]["spirkat"])
                except Exception as err:
                    print(err)
                
                    # kattaki bosluk ---------------------------
                
                gl[0]["katbosluk"]=kattaki_bosluk_hesap_1(
                    karkas_yuk=karkas_yuk,
                    tel_en=gl[0]["tel_en"],
                    son_kat=gl[0]["sonkat_spir"]
                )
                
                

                # tel uzunluk  ---------------------------
                a0 = 2 * (karkas_en + karkas_boy) + 8 * 0.05 * karkas_en
                
                
                
                gl[0]["tel_uzunluk"]=((gl[0]["kat"] - 1) * ((2 * (karkas_en + karkas_boy)) +
                                                    8 * karkas_en * 0.05 + 4 * gl[0]["tel_yuk"]) + \
                            (8 * gl[0]["tel_yuk"] * (gl[0]["kat"] - 1) * (gl[0]["kat"] - 2) / 2)) / 1000 *\
                        gl[0]["spirkat"] + \
                        ((2 * (karkas_en + karkas_boy)) + \
                            8 * karkas_en * 0.05 + 4 * gl[0]["tel_yuk"] + \
                            (8 * gl[0]["tel_yuk"] * (gl[0]["kat"] - 1))) / 1000 * gl[0]["sonkat_spir"]
                

                # tel agirlik  ---------------------------
                if gl[0]["tel_uzunluk"] != 0:
                    gl[0]["tel_agirlik"]=tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"], kesit_2=gl[0]["kesit2"],
                                                tel_yogunluk=tel_yogunlugu_1(tel_turu=gl[0]["teltipi"],
                    cu_yog=cu_yog,
                    al_yog=al_yog,
                    dig_yog=dig_yog))
                    
                    gl[0]["agr_tel_1"]=tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"], kesit_2=kesit_hesap_2(cap=gl[0]["mancap_1"]),
                                                tel_yogunluk=tel_yogunlugu_1(tel_turu=gl[0]["teltipi"],
                    cu_yog=cu_yog,
                    al_yog=al_yog,
                    dig_yog=dig_yog))
                    gl[0]["agr_tel_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=kesit_hesap_2(cap=gl[0]["mancap_2"]),
                                                                tel_yogunluk=tel_yogunlugu_1(
                                                                    tel_turu=gl[0]["teltipi"],
                    cu_yog=cu_yog,
                    al_yog=al_yog,
                    dig_yog=dig_yog))
                    gl[0]["agr_tel_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=kesit_hesap_2(cap=gl[0]["mancap_3"]),
                                                                tel_yogunluk=tel_yogunlugu_1(
                                                                    tel_turu=gl[0]["teltipi"],
                    cu_yog=cu_yog,
                    al_yog=al_yog,
                    dig_yog=dig_yog))
                    gl[0]["agr_tel_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=kesit_hesap_2(cap=gl[0]["mancap_4"]),
                                                                tel_yogunluk=tel_yogunlugu_1(
                                                                    tel_turu=gl[0]["teltipi"],
                    cu_yog=cu_yog,
                    al_yog=al_yog,
                    dig_yog=dig_yog))
                    gl[0]["agr_karetel_1"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=gl[0]["karetel11"] * gl[0]["karetel12"],
                                                                tel_yogunluk=tel_yogunlugu_1(
                                                                    tel_turu=gl[0]["teltipi"],
                    cu_yog=cu_yog,
                    al_yog=al_yog,
                    dig_yog=dig_yog))
                    gl[0]["agr_karetel_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                    kesit_2=gl[0]["karetel21"] * gl[0]["karetel22"],
                                                                    tel_yogunluk=tel_yogunlugu_1(
                                                                        tel_turu=gl[0]["teltipi"],
                    cu_yog=cu_yog,
                    al_yog=al_yog,
                    dig_yog=dig_yog))
                    gl[0]["agr_karetel_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                    kesit_2=gl[0]["karetel31"] * gl[0]["karetel32"],
                                                                    tel_yogunluk=tel_yogunlugu_1(
                                                                        tel_turu=gl[0]["teltipi"],
                    cu_yog=cu_yog,
                    al_yog=al_yog,
                    dig_yog=dig_yog))
                    gl[0]["agr_karetel_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                    kesit_2=gl[0]["karetel41"] * gl[0]["karetel42"],
                                                                    tel_yogunluk=tel_yogunlugu_1(
                                                                        tel_turu=gl[0]["teltipi"],
                    cu_yog=cu_yog,
                    al_yog=al_yog,
                    dig_yog=dig_yog))
                    gl[0]["agr_folyo_1"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                    kesit_2=gl[0]["folyotel11"] * gl[0]["folyotel12"],
                                                                    tel_yogunluk=tel_yogunlugu_1(
                                                                        tel_turu=gl[0]["teltipi"],
                    cu_yog=cu_yog,
                    al_yog=al_yog,
                    dig_yog=dig_yog))
                    gl[0]["agr_folyo_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=gl[0]["folyotel21"] * gl[0]["folyotel22"],
                                                                tel_yogunluk=tel_yogunlugu_1(
                                                                    tel_turu=gl[0]["teltipi"],
                    cu_yog=cu_yog,
                    al_yog=al_yog,
                    dig_yog=dig_yog))
                    gl[0]["agr_folyo_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=gl[0]["folyotel31"] * gl[0]["folyotel32"],
                                                                tel_yogunluk=tel_yogunlugu_1(
                                                                    tel_turu=gl[0]["teltipi"],
                    cu_yog=cu_yog,
                    al_yog=al_yog,
                    dig_yog=dig_yog))
                    gl[0]["agr_folyo_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=gl[0]["folyotel41"] * gl[0]["folyotel42"],
                                                                tel_yogunluk=tel_yogunlugu_1(
                                                                    tel_turu=gl[0]["teltipi"],
                    cu_yog=cu_yog,
                    al_yog=al_yog,
                    dig_yog=dig_yog))
                    gl[0]["agr_kapton_1"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=gl[0]["kapton1"],
                                                                tel_yogunluk=1330)
                    gl[0]["agr_kapton_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=gl[0]["kapton2"],
                                                                tel_yogunluk=1330)
                    gl[0]["agr_kapton_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=gl[0]["kapton3"],
                                                                tel_yogunluk=1330)
                    gl[0]["agr_kapton_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=gl[0]["kapton4"],
                                                                tel_yogunluk=1330)
                else:
                    gl[0]["tel_agirlik"]=0
                    gl[0]["agr_tel_1"] = 0
                    gl[0]["agr_tel_2"] = 0
                    gl[0]["agr_tel_3"] = 0
                    gl[0]["agr_tel_4"] = 0
                    gl[0]["agr_karetel_1"] = 0
                    gl[0]["agr_karetel_2"] = 0
                    gl[0]["agr_karetel_3"] = 0
                    gl[0]["agr_karetel_4"] = 0
                    gl[0]["agr_folyo_1"] = 0
                    gl[0]["agr_folyo_2"] = 0
                    gl[0]["agr_folyo_3"] = 0
                    gl[0]["agr_folyo_4"] = 0
                    gl[0]["agr_kapton_1"] = 0
                    gl[0]["agr_kapton_2"] = 0
                    gl[0]["agr_kapton_3"] = 0
                    gl[0]["agr_kapton_4"] = 0

        else:
            degerler.clear()
            gl[0]["akim1"]=0
            gl[0]["kesit1"]=0
            gl[0]["cap1"]=0
            gl[0]["spir1"]=0
            gl[0]["cap2"]=0
            gl[0]["akim2"]=0
            gl[0]["spir2"]=0
            gl[0]["folyotel11"]=0
            gl[0]["folyotel12"]=0
            gl[0]["folyotel21"]=0
            gl[0]["folyotel22"]=0
            gl[0]["folyotel31"]=0
            gl[0]["folyotel32"]=0
            gl[0]["folyotel41"]=0
            gl[0]["folyotel42"]=0
            gl[0]["kapton1"]=0
            gl[0]["kapton2"]=0
            gl[0]["kapton3"]=0
            gl[0]["kapton4"]=0
            gl[0]["karetel11"]=0
            gl[0]["karetel12"]=0
            gl[0]["karetel21"]=0
            gl[0]["karetel22"]=0
            gl[0]["karetel31"]=0
            gl[0]["karetel32"]=0
            gl[0]["karetel41"]=0
            gl[0]["karetel42"]=0
            gl[0]["kesit2"]=0
            gl[0]["tel_en"]=0
            gl[0]["tel_yuk"]=0
            gl[0]["spirkat"]=0
            gl[0]["kat"]=0
            gl[0]["katbosluk"]=0
            gl[0]["tel_uzunluk"]=0
            gl[0]["tel_agirlik"]=0
            gl[0]["sarim_yukseklik"]=0
            gl[0]["sonkat_spir"]=0
            gl[0]["check_spir_man"] = False
            gl[0]["kesit_ok"]=False
            gl[0]["kesit_error"]=True
            gl[0]["akim_ok"]=False
            gl[0]["akim_error"]=True
            gl[0]["mancap_1"]=0
            gl[0]["mancap_2"]=0
            gl[0]["mancap_3"]=0
            gl[0]["mancap_4"]=0
            gl[0]["mlz_tel_1"] = ""
            gl[0]["mlz_tel_2"] = ""
            gl[0]["mlz_tel_3"] =  ""
            gl[0]["mlz_tel_4"] =  ""
            gl[0]["mlz_karetel_1"] =  ""
            gl[0]["mlz_karetel_2"] =  ""
            gl[0]["mlz_karetel_3"] =  ""
            gl[0]["mlz_karetel_4"] =  ""
            gl[0]["mlz_folyotel_1"] =  ""
            gl[0]["mlz_folyotel_2"] =  ""
            gl[0]["mlz_folyotel_3"] =  ""
            gl[0]["mlz_folyotel_4"] =  ""
            gl[0]["mlz_kapton_1"] =  ""
            gl[0]["mlz_kapton_2"] =  ""
            gl[0]["mlz_kapton_3"] =  ""
            gl[0]["mlz_kapton_4"] =  ""
            gl[0]["gb_check_tel_1"] =  False
            gl[0]["gb_check_tel_2"] =  False
            gl[0]["gb_check_tel_3"] =  False
            gl[0]["gb_check_tel_4"] =  False
            gl[0]["gb_check_karetel_1"]= False
            gl[0]["gb_check_karetel_2"]= False
            gl[0]["gb_check_karetel_3"]= False
            gl[0]["gb_check_karetel_4"]= False
            gl[0]["gb_check_folyotel_1"]= False
            gl[0]["gb_check_folyotel_2"]= False
            gl[0]["gb_check_folyotel_3"]= False
            gl[0]["gb_check_folyotel_4"]= False
            gl[0]["gb_check_kapton_1"]= False
            gl[0]["gb_check_kapton_2"]= False
            gl[0]["gb_check_kapton_3"]= False
            gl[0]["gb_check_kapton_4"]= False
            gl[0]["tel_agirlik"] = 0
            gl[0]["agr_tel_1"] = 0
            gl[0]["agr_tel_2"] = 0
            gl[0]["agr_tel_3"] = 0
            gl[0]["agr_tel_4"] = 0
            gl[0]["agr_karetel_1"] = 0
            gl[0]["agr_karetel_2"] = 0
            gl[0]["agr_karetel_3"] = 0
            gl[0]["agr_karetel_4"] = 0
            gl[0]["agr_folyo_1"] = 0
            gl[0]["agr_folyo_2"] = 0
            gl[0]["agr_folyo_3"] = 0
            gl[0]["agr_folyo_4"] = 0
            gl[0]["agr_kapton_1"] = 0
            gl[0]["agr_kapton_2"] = 0
            gl[0]["agr_kapton_3"] = 0
            gl[0]["agr_kapton_4"] = 0
        return dict(degerler)     

def trafo_hesap_monofaz_sok( gl, guc, frekans, 
                   gauss, karkas_en, karkas_boy, 
                   karkas_yuk, verim, sarim, 
                   primer_sarim_yukseklik_toplam,
                   cu_par,
                    cu_yog,
                    al_par,
                    al_yog,
                    dig_par,
                    dig_yog,
                    Lg_man,
                    c,Kf,Ku,Um,
                    klemens_a, 
                    klemens_b, 
                    ayak_a,
                    akim_m,
                    enduktans_m):
        
        degerler = {}
        degerler["volt_m"]=0.0
        if akim_m > 0.0 :
            
            degerler["volt_m"]=float(voltaj_m_hesap_1(enduktans=0, enduktans_m=enduktans_m, akim=akim_m, frekans=frekans))
            
        degerler["guc_m"]=0.0   
        if gl[0]["voltaj"]== 0 and degerler["volt_m"]>0:
            gl[0]["voltaj"]=float(degerler["volt_m"])
        elif gl[0]["voltaj"]> 0 :
            degerler["guc_m"]  =  akim_m * gl[0]["voltaj"]
            
        # Akım 1 Hesabı -------------------------
        
        gl[0]["akim1"]=round(akim_m)
                
        # Kesit 1 Hesabı -------------------------
        gl[0]["kesit1"]=kesit_hesap_1(
            akim=gl[0]["akim1"],
            akim_yogunlugu=akim_yogunlugu_1(
                tel_turu=gl[0]["teltipi"],
                cu_par=cu_par,
                cu_yog=cu_yog,
                al_par=al_par,
                al_yog=al_yog,
                dig_par=dig_par,
                dig_yog=dig_yog))
        # cap 1 Hesabı -------------------------
        gl[0]["cap1"]=cap_hesap_1(
            kesit=gl[0]["kesit1"])
        # Karkas Man Hesabı -------------------------
        degerler["karkas_man"]=karkas_Ac(karkas_en=karkas_en,karkas_boy=karkas_boy)
        degerler["karkas_oto"]=karkas_Ac_oto(c=c, guc=degerler["guc_m"], frekans=frekans)
        degerler["karkas_yuk_oto"]=karkas_yuk_oto(karkas_en=karkas_en)
        degerler["Ap"] = Ap_hesap_1(
            guc=degerler["guc_m"], 
            karkas_yuk=karkas_yuk, 
            Kf=Kf, 
            Ku=Ku, 
            gauss=gauss, 
            frekans=frekans, 
            tel_turu=gl[0]["teltipi"], 
            cu_par=cu_par, 
            cu_yog=cu_yog, 
            al_par=al_par, 
            al_yog=al_yog, 
            dig_par=dig_par, 
            dig_yog=dig_yog)
        degerler["mpl"]=mpl_hesap_3(Ap=degerler["Ap"])
       
        degerler["akim_t"]=gl[0]["akim1"]
        # F man Hesabı -------------------------
        degerler["f_man"] = f_hesap_1(Lg=Lg_man, karkas_Ac=degerler["karkas_man"], karkas_yuk=karkas_yuk)
        degerler["ApSac"] = ApSac_hesap_1(karkas_en=karkas_en, karkas_boy=karkas_boy)
        degerler["sp1"] =spir_hesap_10(
            gerilim=gl[0]["voltaj"], 
            gauss=gauss, 
            frekans=frekans, 
            karkas_man=degerler["karkas_man"], 
            Kf=Kf)
        # Enduktans Hesabı -------------------------
        if gl[0]["check_spir_man"]==True:
                degerler["enduktans"]= end_hesap_4(
                sp= gl[0]["spir2"],
                karkas_man=degerler["karkas_man"], 
                f=degerler["f_man"], 
                Lg=Lg_man
                )
        else:
            degerler["enduktans"]= end_hesap_1(
                gerilim=gl[0]["voltaj"],
                frekans=frekans, 
                akim=gl[0]["akim1"])
        degerler["volt_m"]=float(voltaj_m_hesap_1(enduktans= degerler["enduktans"], enduktans_m=enduktans_m, akim=akim_m, frekans=frekans))
        
        
        degerler["Lg_mpl"] = Lg_mpl_hesap_1(
            mpl=degerler["mpl"], 
            enduktans=degerler["enduktans"], 
            karkas_man=degerler["karkas_man"], 
            sp1=degerler["sp1"], 
            karkas_en=karkas_en, 
            karkas_boy=karkas_boy,
            Um=Um)
        degerler["Lg_oto"] = Lg_oto_hesap_1(
            enduktans=degerler["enduktans"], 
            karkas_man=degerler["karkas_man"], 
            sp1=degerler["sp1"], 
            karkas_en=karkas_en, 
            karkas_boy=karkas_boy)
        degerler["f_oto"]=f_hesap_1(Lg= degerler["Lg_oto"], karkas_Ac=degerler["karkas_man"], karkas_yuk=karkas_yuk)
        degerler["sp1_oto"]=spir_hesap_8(Lg=degerler["Lg_oto"],enduktans=degerler["enduktans"],f_man= degerler["f_oto"],karkas_man=degerler["karkas_man"])
        degerler["f_mpl"]=f_hesap_1(Lg=degerler["Lg_mpl"], karkas_Ac=degerler["karkas_man"], karkas_yuk=karkas_yuk)
        degerler["sp1_mpl"]=spir_hesap_8(Lg=degerler["Lg_mpl"],enduktans=degerler["enduktans"],f_man= degerler["f_mpl"],karkas_man=degerler["karkas_man"])
        degerler["nuveOlcu_a"],degerler["nuveOlcu_b"],degerler["nuveOlcu_c"]=nuve_olcu_hesapla(
            karkas_en=karkas_en, 
            karkas_boy=karkas_boy, 
            klemens_a=klemens_a, 
            klemens_b=klemens_b, 
            ayak_a=ayak_a)
        degerler["sac_agirlik"]=sac_agirlik(karkas_en=karkas_en,karkas_boy=karkas_boy)
        degerler["bosluk"]=0
        # spir 1 Hesabı -------------------------

        gl[0]["spir1"]=spir_hesap_8(Lg=Lg_man,enduktans=degerler["enduktans"],f_man= degerler["f_man"],karkas_man=degerler["karkas_man"])
        degerler["sp1_man"] =  gl[0]["spir1"]  
        # spir 2 Hesabı -------------------------
        if gl[0]["check_spir_man"]==True:
            pass
        else:
            gl[0]["spir2"]=round(gl[0]["spir1"])
        # Kesit 2 Hesabı -------------------------
        gl[0]["kesit2"]= kesit_hesap_2(cap=gl[0]["mancap_1"]) + \
            kesit_hesap_2(cap=gl[0]["mancap_2"]) +\
            kesit_hesap_2(cap=gl[0]["mancap_3"]) +\
            kesit_hesap_2(cap=gl[0]["mancap_4"]) +\
            (gl[0]["folyotel11"] * gl[0]["folyotel12"]) +\
            (gl[0]["folyotel21"] * gl[0]["folyotel22"]) +\
            (gl[0]["folyotel31"] * gl[0]["folyotel32"]) +\
            (gl[0]["folyotel41"] * gl[0]["folyotel42"]) +\
            (gl[0]["karetel11"] * gl[0]["karetel12"]) +\
            (gl[0]["karetel21"] * gl[0]["karetel22"]) +\
            (gl[0]["karetel31"] * gl[0]["karetel32"]) +\
            (gl[0]["karetel41"] * gl[0]["karetel42"])
        # Akım 2 Hesabı -------------------------
        gl[0]["akim2"]=akim_hesap_2(

            kesit=gl[0]["kesit2"],
            akim_yogunlugu=akim_yogunlugu_1(
                tel_turu=gl[0]["teltipi"],
                cu_par=cu_par,
                cu_yog=cu_yog,
                al_par=al_par,
                al_yog=al_yog,
                dig_par=dig_par,
                dig_yog=dig_yog))
        # cap 2 Hesabı -------------------------
        gl[0]["cap2"]= gl[0]["mancap_1"] + gl[0]["mancap_2"] + gl[0]["mancap_3"] + gl[0]["mancap_4"]
        # akım 2 ve kesit 2 kontrol -------------------------
        if gl[0]["kesit1"] <= gl[0]["kesit2"]:
            gl[0]["kesit_ok"]=True
            gl[0]["kesit_error"]=False
        else:
            gl[0]["kesit_ok"]=False
            gl[0]["kesit_error"]=True
        if gl[0]["akim1"] <= gl[0]["akim2"]:
            gl[0]["akim_ok"]=True
            gl[0]["akim_error"]=False
        else:
            gl[0]["akim_ok"]=False
            gl[0]["akim_error"]=True
        # -------------------------
        tel_cap = 0

        for tel_kademe in range(1, 5):

            data = db.showfilter_tel_spir(filter_value=gl[0][f"mancap_{tel_kademe}"] , index=0)

            if data == [] and gl[0][f"mancap_{tel_kademe}"] > 0:
                tel_cap +=  (gl[0]["mancap_1"]) * 1.02
            elif data != [] and gl[0][f"mancap_{tel_kademe}"] > 0:
                tel_cap += data[0][4]
        
        # tel yüksekliği Hesabı -------------------------
        gl[0]["tel_yuk"]=tel_yukseklik_hesap_1(
            tel_cap=tel_cap, karetel_yuk1=gl[0]["karetel12"],
            karetel_yuk2=gl[0]["karetel22"],
            karetel_yuk3=gl[0]["karetel32"], karetel_yuk4=gl[0]["karetel42"],
            folyo_yuk1=gl[0]["folyotel12"], folyo_yuk2=gl[0]["folyotel22"],
            folyo_yuk3=gl[0]["folyotel32"], folyo_yuk4=gl[0]["folyotel42"],
            kapton1=gl[0]["kapton1"], kapton2=gl[0]["kapton2"],
            kapton3=gl[0]["kapton3"], kapton4=gl[0]["kapton4"])
        # tel en Hesabı -------------------------
        gl[0]["tel_en"]= tel_en_hesap_1(
            tel_cap=tel_cap,
            karetel_en1=gl[0]["karetel11"],
            karetel_en2=gl[0]["karetel21"],
            karetel_en3=gl[0]["karetel31"], karetel_en4=gl[0]["karetel41"],
            folyo_en1=gl[0]["folyotel11"], folyo_en2=gl[0]["folyotel21"],
            folyo_en3=gl[0]["folyotel31"], folyo_en4=gl[0]["folyotel41"],
            )

        if gl[0]["tel_en"] > 0:
            # spir kat Hesabı -------------------------
            gl[0]["spirkat"]=spir_kat_hesap_1(
                karkas_yuk=karkas_yuk,
                tel_en=gl[0]["tel_en"])

            #  kat sayısı -------------------------------
            
            gl[0]["kat"]=kat_sayisi_hesap_1(
                spir=gl[0]["spir2"],
                spir_kat=gl[0]["spirkat"])

            
            # sarım yuksekliği  -------------------------
            gl[0]["sarim_yukseklik"]=sarim_yüksekligi_hesap_1(
                tel_yuk=gl[0]["tel_yuk"],
                kat_sayisi=gl[0]["kat"])
            
            # bosluk   -------------------------
            degerler["bosluk"]=bosluk_hesap_1(karkas_en=karkas_en,
            primer_top_yuk=gl[0]["sarim_yukseklik"],sekonder_top_yuk =0 ,primer_izolasyon=0)
            
            # son kat
            

            try :
                if math.fmod(gl[0]["spir2"], gl[0]["spirkat"]) == 0:
                    gl[0]["sonkat_spir"]=gl[0]["spirkat"]
                else:
                    gl[0]["sonkat_spir"]=son_kat_hesap_1(
                        spir_2=gl[0]["spir2"],
                        spir_kat=gl[0]["spirkat"])
            except Exception as err:
                print(err)
            
                # kattaki bosluk ---------------------------
            
            gl[0]["katbosluk"]=kattaki_bosluk_hesap_1(
                karkas_yuk=karkas_yuk,
                tel_en=gl[0]["tel_en"],
                son_kat=gl[0]["sonkat_spir"]
            )
            
            

            # tel uzunluk  ---------------------------
            a0 = 2 * (karkas_en + karkas_boy) + 8 * 0.05 * karkas_en
            
            
            
            gl[0]["tel_uzunluk"]=((gl[0]["kat"] - 1) * ((2 * (karkas_en + karkas_boy)) +
                                                8 * karkas_en * 0.05 + 4 * gl[0]["tel_yuk"]) + \
                        (8 * gl[0]["tel_yuk"] * (gl[0]["kat"] - 1) * (gl[0]["kat"] - 2) / 2)) / 1000 *\
                    gl[0]["spirkat"] + \
                    ((2 * (karkas_en + karkas_boy)) + \
                        8 * karkas_en * 0.05 + 4 * gl[0]["tel_yuk"] + \
                        (8 * gl[0]["tel_yuk"] * (gl[0]["kat"] - 1))) / 1000 * gl[0]["sonkat_spir"]
            

            # tel agirlik  ---------------------------
            if gl[0]["tel_uzunluk"] != 0:
                gl[0]["tel_agirlik"]=tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"], kesit_2=gl[0]["kesit2"],
                                            tel_yogunluk=tel_yogunlugu_1(tel_turu=gl[0]["teltipi"],
                cu_yog=cu_yog,
                al_yog=al_yog,
                dig_yog=dig_yog))
                
                gl[0]["agr_tel_1"]=tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"], kesit_2=kesit_hesap_2(cap=gl[0]["mancap_1"]),
                                            tel_yogunluk=tel_yogunlugu_1(tel_turu=gl[0]["teltipi"],
                cu_yog=cu_yog,
                al_yog=al_yog,
                dig_yog=dig_yog))
                gl[0]["agr_tel_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                            kesit_2=kesit_hesap_2(cap=gl[0]["mancap_2"]),
                                                            tel_yogunluk=tel_yogunlugu_1(
                                                                tel_turu=gl[0]["teltipi"],
                cu_yog=cu_yog,
                al_yog=al_yog,
                dig_yog=dig_yog))
                gl[0]["agr_tel_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                            kesit_2=kesit_hesap_2(cap=gl[0]["mancap_3"]),
                                                            tel_yogunluk=tel_yogunlugu_1(
                                                                tel_turu=gl[0]["teltipi"],
                cu_yog=cu_yog,
                al_yog=al_yog,
                dig_yog=dig_yog))
                gl[0]["agr_tel_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                            kesit_2=kesit_hesap_2(cap=gl[0]["mancap_4"]),
                                                            tel_yogunluk=tel_yogunlugu_1(
                                                                tel_turu=gl[0]["teltipi"],
                cu_yog=cu_yog,
                al_yog=al_yog,
                dig_yog=dig_yog))
                gl[0]["agr_karetel_1"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                            kesit_2=gl[0]["karetel11"] * gl[0]["karetel12"],
                                                            tel_yogunluk=tel_yogunlugu_1(
                                                                tel_turu=gl[0]["teltipi"],
                cu_yog=cu_yog,
                al_yog=al_yog,
                dig_yog=dig_yog))
                gl[0]["agr_karetel_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=gl[0]["karetel21"] * gl[0]["karetel22"],
                                                                tel_yogunluk=tel_yogunlugu_1(
                                                                    tel_turu=gl[0]["teltipi"],
                cu_yog=cu_yog,
                al_yog=al_yog,
                dig_yog=dig_yog))
                gl[0]["agr_karetel_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=gl[0]["karetel31"] * gl[0]["karetel32"],
                                                                tel_yogunluk=tel_yogunlugu_1(
                                                                    tel_turu=gl[0]["teltipi"],
                cu_yog=cu_yog,
                al_yog=al_yog,
                dig_yog=dig_yog))
                gl[0]["agr_karetel_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=gl[0]["karetel41"] * gl[0]["karetel42"],
                                                                tel_yogunluk=tel_yogunlugu_1(
                                                                    tel_turu=gl[0]["teltipi"],
                cu_yog=cu_yog,
                al_yog=al_yog,
                dig_yog=dig_yog))
                gl[0]["agr_folyo_1"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=gl[0]["folyotel11"] * gl[0]["folyotel12"],
                                                                tel_yogunluk=tel_yogunlugu_1(
                                                                    tel_turu=gl[0]["teltipi"],
                cu_yog=cu_yog,
                al_yog=al_yog,
                dig_yog=dig_yog))
                gl[0]["agr_folyo_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                            kesit_2=gl[0]["folyotel21"] * gl[0]["folyotel22"],
                                                            tel_yogunluk=tel_yogunlugu_1(
                                                                tel_turu=gl[0]["teltipi"],
                cu_yog=cu_yog,
                al_yog=al_yog,
                dig_yog=dig_yog))
                gl[0]["agr_folyo_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                            kesit_2=gl[0]["folyotel31"] * gl[0]["folyotel32"],
                                                            tel_yogunluk=tel_yogunlugu_1(
                                                                tel_turu=gl[0]["teltipi"],
                cu_yog=cu_yog,
                al_yog=al_yog,
                dig_yog=dig_yog))
                gl[0]["agr_folyo_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                            kesit_2=gl[0]["folyotel41"] * gl[0]["folyotel42"],
                                                            tel_yogunluk=tel_yogunlugu_1(
                                                                tel_turu=gl[0]["teltipi"],
                cu_yog=cu_yog,
                al_yog=al_yog,
                dig_yog=dig_yog))
                gl[0]["agr_kapton_1"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                            kesit_2=gl[0]["kapton1"],
                                                            tel_yogunluk=1330)
                gl[0]["agr_kapton_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                            kesit_2=gl[0]["kapton2"],
                                                            tel_yogunluk=1330)
                gl[0]["agr_kapton_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                            kesit_2=gl[0]["kapton3"],
                                                            tel_yogunluk=1330)
                gl[0]["agr_kapton_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                            kesit_2=gl[0]["kapton4"],
                                                            tel_yogunluk=1330)
            else:
                
                gl[0]["tel_agirlik"]=0
                gl[0]["agr_tel_1"] = 0
                gl[0]["agr_tel_2"] = 0
                gl[0]["agr_tel_3"] = 0
                gl[0]["agr_tel_4"] = 0
                gl[0]["agr_karetel_1"] = 0
                gl[0]["agr_karetel_2"] = 0
                gl[0]["agr_karetel_3"] = 0
                gl[0]["agr_karetel_4"] = 0
                gl[0]["agr_folyo_1"] = 0
                gl[0]["agr_folyo_2"] = 0
                gl[0]["agr_folyo_3"] = 0
                gl[0]["agr_folyo_4"] = 0
                gl[0]["agr_kapton_1"] = 0
                gl[0]["agr_kapton_2"] = 0
                gl[0]["agr_kapton_3"] = 0
                gl[0]["agr_kapton_4"] = 0

        # else:
        #     degerler.clear()
        #     gl[0]["akim1"]=0
        #     gl[0]["kesit1"]=0
        #     gl[0]["cap1"]=0
        #     gl[0]["spir1"]=0
        #     gl[0]["cap2"]=0
        #     gl[0]["akim2"]=0
        #     gl[0]["spir2"]=0
        #     gl[0]["folyotel11"]=0
        #     gl[0]["folyotel12"]=0
        #     gl[0]["folyotel21"]=0
        #     gl[0]["folyotel22"]=0
        #     gl[0]["folyotel31"]=0
        #     gl[0]["folyotel32"]=0
        #     gl[0]["folyotel41"]=0
        #     gl[0]["folyotel42"]=0
        #     gl[0]["kapton1"]=0
        #     gl[0]["kapton2"]=0
        #     gl[0]["kapton3"]=0
        #     gl[0]["kapton4"]=0
        #     gl[0]["karetel11"]=0
        #     gl[0]["karetel12"]=0
        #     gl[0]["karetel21"]=0
        #     gl[0]["karetel22"]=0
        #     gl[0]["karetel31"]=0
        #     gl[0]["karetel32"]=0
        #     gl[0]["karetel41"]=0
        #     gl[0]["karetel42"]=0
        #     gl[0]["kesit2"]=0
        #     gl[0]["tel_en"]=0
        #     gl[0]["tel_yuk"]=0
        #     gl[0]["spirkat"]=0
        #     gl[0]["kat"]=0
        #     gl[0]["katbosluk"]=0
        #     gl[0]["tel_uzunluk"]=0
        #     gl[0]["tel_agirlik"]=0
        #     gl[0]["sarim_yukseklik"]=0
        #     gl[0]["sonkat_spir"]=0
        #     gl[0]["check_spir_man"] = False
        #     gl[0]["kesit_ok"]=False
        #     gl[0]["kesit_error"]=True
        #     gl[0]["akim_ok"]=False
        #     gl[0]["akim_error"]=True
        #     gl[0]["mancap_1"]=0
        #     gl[0]["mancap_2"]=0
        #     gl[0]["mancap_3"]=0
        #     gl[0]["mancap_4"]=0
        #     gl[0]["mlz_tel_1"] = ""
        #     gl[0]["mlz_tel_2"] = ""
        #     gl[0]["mlz_tel_3"] =  ""
        #     gl[0]["mlz_tel_4"] =  ""
        #     gl[0]["mlz_karetel_1"] =  ""
        #     gl[0]["mlz_karetel_2"] =  ""
        #     gl[0]["mlz_karetel_3"] =  ""
        #     gl[0]["mlz_karetel_4"] =  ""
        #     gl[0]["mlz_folyotel_1"] =  ""
        #     gl[0]["mlz_folyotel_2"] =  ""
        #     gl[0]["mlz_folyotel_3"] =  ""
        #     gl[0]["mlz_folyotel_4"] =  ""
        #     gl[0]["mlz_kapton_1"] =  ""
        #     gl[0]["mlz_kapton_2"] =  ""
        #     gl[0]["mlz_kapton_3"] =  ""
        #     gl[0]["mlz_kapton_4"] =  ""
        #     gl[0]["gb_check_tel_1"] =  False
        #     gl[0]["gb_check_tel_2"] =  False
        #     gl[0]["gb_check_tel_3"] =  False
        #     gl[0]["gb_check_tel_4"] =  False
        #     gl[0]["gb_check_karetel_1"]= False
        #     gl[0]["gb_check_karetel_2"]= False
        #     gl[0]["gb_check_karetel_3"]= False
        #     gl[0]["gb_check_karetel_4"]= False
        #     gl[0]["gb_check_folyotel_1"]= False
        #     gl[0]["gb_check_folyotel_2"]= False
        #     gl[0]["gb_check_folyotel_3"]= False
        #     gl[0]["gb_check_folyotel_4"]= False
        #     gl[0]["gb_check_kapton_1"]= False
        #     gl[0]["gb_check_kapton_2"]= False
        #     gl[0]["gb_check_kapton_3"]= False
        #     gl[0]["gb_check_kapton_4"]= False
        #     gl[0]["tel_agirlik"] = 0
        #     gl[0]["agr_tel_1"] = 0
        #     gl[0]["agr_tel_2"] = 0
        #     gl[0]["agr_tel_3"] = 0
        #     gl[0]["agr_tel_4"] = 0
        #     gl[0]["agr_karetel_1"] = 0
        #     gl[0]["agr_karetel_2"] = 0
        #     gl[0]["agr_karetel_3"] = 0
        #     gl[0]["agr_karetel_4"] = 0
        #     gl[0]["agr_folyo_1"] = 0
        #     gl[0]["agr_folyo_2"] = 0
        #     gl[0]["agr_folyo_3"] = 0
        #     gl[0]["agr_folyo_4"] = 0
        #     gl[0]["agr_kapton_1"] = 0
        #     gl[0]["agr_kapton_2"] = 0
        #     gl[0]["agr_kapton_3"] = 0
        #     gl[0]["agr_kapton_4"] = 0
        return dict(degerler)  


def trafo_hesap_trifaz_sok( gl, guc, frekans, 
                   gauss, karkas_en, karkas_boy, 
                   karkas_yuk, verim, sarim, 
                   primer_sarim_yukseklik_toplam,
                   cu_par,
                    cu_yog,
                    al_par,
                    al_yog,
                    dig_par,
                    dig_yog,
                    Lg_man,
                    c,Kf,Ku,Um,
                    klemens_a, 
                    klemens_b, 
                    ayak_a,
                    akim_m,
                    enduktans_m):
        
        degerler = {}
        degerler["volt_m"]=0.0
        if akim_m > 0.0 :
            
            degerler["volt_m"]=float(voltaj_m_hesap_1(enduktans=0, enduktans_m=enduktans_m, akim=akim_m, frekans=frekans))
            
        degerler["guc_m"]=0.0   
        if gl[0]["voltaj"]== 0 and degerler["volt_m"]>0:
            gl[0]["voltaj"]=float(degerler["volt_m"])
        elif gl[0]["voltaj"]> 0 :
            degerler["guc_m"]  =  akim_m * gl[0]["voltaj"]*3
            
        # Akım 1 Hesabı -------------------------
        
        gl[0]["akim1"]=round(akim_m)
                
        # Kesit 1 Hesabı -------------------------
        gl[0]["kesit1"]=kesit_hesap_1(
            akim=gl[0]["akim1"],
            akim_yogunlugu=akim_yogunlugu_1(
                tel_turu=gl[0]["teltipi"],
                cu_par=cu_par,
                cu_yog=cu_yog,
                al_par=al_par,
                al_yog=al_yog,
                dig_par=dig_par,
                dig_yog=dig_yog))
        # cap 1 Hesabı -------------------------
        gl[0]["cap1"]=cap_hesap_1(
            kesit=gl[0]["kesit1"])
        # Karkas Man Hesabı -------------------------
        degerler["karkas_man"]=karkas_Ac(karkas_en=karkas_en,karkas_boy=karkas_boy)
        degerler["karkas_oto"]=karkas_Ac_oto_2(c=c, guc=degerler["guc_m"], frekans=frekans)
        degerler["karkas_yuk_oto"]=karkas_yuk_2(karkas_en=karkas_en)
        degerler["Ap"] = Ap_hesap_1(
            guc=degerler["guc_m"], 
            karkas_yuk=karkas_yuk, 
            Kf=Kf, 
            Ku=Ku, 
            gauss=gauss, 
            frekans=frekans, 
            tel_turu=gl[0]["teltipi"], 
            cu_par=cu_par, 
            cu_yog=cu_yog, 
            al_par=al_par, 
            al_yog=al_yog, 
            dig_par=dig_par, 
            dig_yog=dig_yog)
        degerler["mpl"]=mpl_hesap_2(Ap=degerler["Ap"])
        
        degerler["akim_t"]=gl[0]["akim1"]
        # F man Hesabı -------------------------
        degerler["f_man"] = f_hesap_1(Lg=Lg_man, karkas_Ac=degerler["karkas_man"], karkas_yuk=karkas_yuk)
        degerler["ApSac"] = ApSac_hesap_2(karkas_en=karkas_en, karkas_boy=karkas_boy)
        degerler["sp1"] =spir_hesap_11(
            gerilim=gl[0]["voltaj"], 
            gauss=gauss, 
            frekans=frekans, 
            karkas_man=degerler["karkas_man"], 
            Kf=Kf)
        # Enduktans Hesabı -------------------------
        if gl[0]["check_spir_man"]==True:
                degerler["enduktans"]= end_hesap_5(
                sp= gl[0]["spir2"],
                karkas_man=degerler["karkas_man"], 
                f=degerler["f_man"], 
                Lg=Lg_man,
                MPL=degerler["mpl"],
                Um=Um
                )
        else:
            degerler["enduktans"]= end_hesap_3(
                gerilim=gl[0]["voltaj"],
                frekans=frekans, 
                akim=gl[0]["akim1"],
                enduktans_m=enduktans_m)
            
        
        
        degerler["volt_m"]=float(voltaj_m_hesap_1(enduktans= degerler["enduktans"], enduktans_m=enduktans_m, akim=akim_m, frekans=frekans))
        
        
        
        degerler["Lg_mpl"] = Lg_mpl_hesap_1(
            mpl=degerler["mpl"], 
            enduktans=degerler["enduktans"], 
            karkas_man=degerler["karkas_man"], 
            sp1=degerler["sp1"], 
            karkas_en=karkas_en, 
            karkas_boy=karkas_boy,
            Um=Um)
        degerler["Lg_oto"] = Lg_oto_hesap_1(
            enduktans=degerler["enduktans"], 
            karkas_man=degerler["karkas_man"], 
            sp1=degerler["sp1"], 
            karkas_en=karkas_en, 
            karkas_boy=karkas_boy)
        degerler["f_oto"]=f_hesap_1(Lg= degerler["Lg_oto"], karkas_Ac=degerler["karkas_man"], karkas_yuk=karkas_yuk)
        degerler["sp1_oto"]=spir_hesap_8(Lg=degerler["Lg_oto"],enduktans=degerler["enduktans"],f_man= degerler["f_oto"],karkas_man=degerler["karkas_man"])
        degerler["f_mpl"]=f_hesap_1(Lg=degerler["Lg_mpl"], karkas_Ac=degerler["karkas_man"], karkas_yuk=karkas_yuk)
        degerler["sp1_mpl"]=spir_hesap_8(Lg=degerler["Lg_mpl"],enduktans=degerler["enduktans"],f_man= degerler["f_mpl"],karkas_man=degerler["karkas_man"])
        degerler["nuveOlcu_a"],degerler["nuveOlcu_b"],degerler["nuveOlcu_c"]=nuve_olcu_hesapla_4(
            karkas_en=karkas_en, 
            karkas_boy=karkas_boy, 
            klemens_a=klemens_a, 
            klemens_b=klemens_b, 
            ayak_a=ayak_a)
        degerler["sac_agirlik"]=sac_agirlik_trifaz(karkas_en=karkas_en,karkas_boy=karkas_boy)
        degerler["bosluk"]=0
        # spir 1 Hesabı -------------------------

        gl[0]["spir1"]=spir_hesap_12(
            Lg=Lg_man,
            enduktans=degerler["enduktans"],
            f_man= degerler["f_man"],
            karkas_man=degerler["karkas_man"],
            mpl=degerler["mpl"],
            Um=Um)
        degerler["sp1_man"] =  gl[0]["spir1"]  
        # spir 2 Hesabı -------------------------
        if gl[0]["check_spir_man"]==True:
            pass
        else:
            gl[0]["spir2"]=round(gl[0]["spir1"])
        # Kesit 2 Hesabı -------------------------
        gl[0]["kesit2"]= kesit_hesap_2(cap=gl[0]["mancap_1"]) + \
            kesit_hesap_2(cap=gl[0]["mancap_2"]) +\
            kesit_hesap_2(cap=gl[0]["mancap_3"]) +\
            kesit_hesap_2(cap=gl[0]["mancap_4"]) +\
            (gl[0]["folyotel11"] * gl[0]["folyotel12"]) +\
            (gl[0]["folyotel21"] * gl[0]["folyotel22"]) +\
            (gl[0]["folyotel31"] * gl[0]["folyotel32"]) +\
            (gl[0]["folyotel41"] * gl[0]["folyotel42"]) +\
            (gl[0]["karetel11"] * gl[0]["karetel12"]) +\
            (gl[0]["karetel21"] * gl[0]["karetel22"]) +\
            (gl[0]["karetel31"] * gl[0]["karetel32"]) +\
            (gl[0]["karetel41"] * gl[0]["karetel42"])
        # Akım 2 Hesabı -------------------------
        gl[0]["akim2"]=akim_hesap_2(

            kesit=gl[0]["kesit2"],
            akim_yogunlugu=akim_yogunlugu_1(
                tel_turu=gl[0]["teltipi"],
                cu_par=cu_par,
                cu_yog=cu_yog,
                al_par=al_par,
                al_yog=al_yog,
                dig_par=dig_par,
                dig_yog=dig_yog))
        # cap 2 Hesabı -------------------------
        gl[0]["cap2"]= gl[0]["mancap_1"] + gl[0]["mancap_2"] + gl[0]["mancap_3"] + gl[0]["mancap_4"]
        # akım 2 ve kesit 2 kontrol -------------------------
        if gl[0]["kesit1"] <= gl[0]["kesit2"]:
            gl[0]["kesit_ok"]=True
            gl[0]["kesit_error"]=False
        else:
            gl[0]["kesit_ok"]=False
            gl[0]["kesit_error"]=True
        if gl[0]["akim1"] <= gl[0]["akim2"]:
            gl[0]["akim_ok"]=True
            gl[0]["akim_error"]=False
        else:
            gl[0]["akim_ok"]=False
            gl[0]["akim_error"]=True
        # -------------------------
        tel_cap = 0

        for tel_kademe in range(1, 5):

            data = db.showfilter_tel_spir(filter_value=gl[0][f"mancap_{tel_kademe}"] , index=0)

            if data == [] and gl[0][f"mancap_{tel_kademe}"] > 0:
                tel_cap +=  (gl[0]["mancap_1"]) * 1.02
            elif data != [] and gl[0][f"mancap_{tel_kademe}"] > 0:
                tel_cap += data[0][4]
        
        # tel yüksekliği Hesabı -------------------------
        gl[0]["tel_yuk"]=tel_yukseklik_hesap_1(
            tel_cap=tel_cap, karetel_yuk1=gl[0]["karetel12"],
            karetel_yuk2=gl[0]["karetel22"],
            karetel_yuk3=gl[0]["karetel32"], karetel_yuk4=gl[0]["karetel42"],
            folyo_yuk1=gl[0]["folyotel12"], folyo_yuk2=gl[0]["folyotel22"],
            folyo_yuk3=gl[0]["folyotel32"], folyo_yuk4=gl[0]["folyotel42"],
            kapton1=gl[0]["kapton1"], kapton2=gl[0]["kapton2"],
            kapton3=gl[0]["kapton3"], kapton4=gl[0]["kapton4"])
        # tel en Hesabı -------------------------
        gl[0]["tel_en"]= tel_en_hesap_1(
            tel_cap=tel_cap,
            karetel_en1=gl[0]["karetel11"],
            karetel_en2=gl[0]["karetel21"],
            karetel_en3=gl[0]["karetel31"], karetel_en4=gl[0]["karetel41"],
            folyo_en1=gl[0]["folyotel11"], folyo_en2=gl[0]["folyotel21"],
            folyo_en3=gl[0]["folyotel31"], folyo_en4=gl[0]["folyotel41"],
            )

        if gl[0]["tel_en"] > 0:
            # spir kat Hesabı -------------------------
            gl[0]["spirkat"]=spir_kat_hesap_1(
                karkas_yuk=karkas_yuk,
                tel_en=gl[0]["tel_en"])

            #  kat sayısı -------------------------------
            
            gl[0]["kat"]=kat_sayisi_hesap_1(
                spir=gl[0]["spir2"],
                spir_kat=gl[0]["spirkat"])

            
            # sarım yuksekliği  -------------------------
            gl[0]["sarim_yukseklik"]=sarim_yüksekligi_hesap_1(
                tel_yuk=gl[0]["tel_yuk"],
                kat_sayisi=gl[0]["kat"])
            
            # bosluk   -------------------------
            degerler["bosluk"]=bosluk_hesap_1(karkas_en=karkas_en,
            primer_top_yuk=gl[0]["sarim_yukseklik"],sekonder_top_yuk =0 ,primer_izolasyon=0)
            
            # son kat
            

            try :
                if math.fmod(gl[0]["spir2"], gl[0]["spirkat"]) == 0:
                    gl[0]["sonkat_spir"]=gl[0]["spirkat"]
                else:
                    gl[0]["sonkat_spir"]=son_kat_hesap_1(
                        spir_2=gl[0]["spir2"],
                        spir_kat=gl[0]["spirkat"])
            except Exception as err:
                print(err)
            
                # kattaki bosluk ---------------------------
            
            gl[0]["katbosluk"]=kattaki_bosluk_hesap_1(
                karkas_yuk=karkas_yuk,
                tel_en=gl[0]["tel_en"],
                son_kat=gl[0]["sonkat_spir"]
            )
            
            

            # tel uzunluk  ---------------------------
            a0 = 2 * (karkas_en + karkas_boy) + 8 * 0.05 * karkas_en
            
            
            
            gl[0]["tel_uzunluk"]=((gl[0]["kat"] - 1) * ((2 * (karkas_en + karkas_boy)) +
                                                8 * karkas_en * 0.05 + 4 * gl[0]["tel_yuk"]) + \
                        (8 * gl[0]["tel_yuk"] * (gl[0]["kat"] - 1) * (gl[0]["kat"] - 2) / 2)) / 1000 *\
                    gl[0]["spirkat"] + \
                    ((2 * (karkas_en + karkas_boy)) + \
                        8 * karkas_en * 0.05 + 4 * gl[0]["tel_yuk"] + \
                        (8 * gl[0]["tel_yuk"] * (gl[0]["kat"] - 1))) / 1000 * gl[0]["sonkat_spir"]
            

            # tel agirlik  ---------------------------
            if gl[0]["tel_uzunluk"] != 0:
                gl[0]["tel_agirlik"]=tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"], kesit_2=gl[0]["kesit2"],
                                            tel_yogunluk=tel_yogunlugu_1(tel_turu=gl[0]["teltipi"],
                cu_yog=cu_yog,
                al_yog=al_yog,
                dig_yog=dig_yog))
                
                gl[0]["agr_tel_1"]=tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"], kesit_2=kesit_hesap_2(cap=gl[0]["mancap_1"]),
                                            tel_yogunluk=tel_yogunlugu_1(tel_turu=gl[0]["teltipi"],
                cu_yog=cu_yog,
                al_yog=al_yog,
                dig_yog=dig_yog))
                gl[0]["agr_tel_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                            kesit_2=kesit_hesap_2(cap=gl[0]["mancap_2"]),
                                                            tel_yogunluk=tel_yogunlugu_1(
                                                                tel_turu=gl[0]["teltipi"],
                cu_yog=cu_yog,
                al_yog=al_yog,
                dig_yog=dig_yog))
                gl[0]["agr_tel_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                            kesit_2=kesit_hesap_2(cap=gl[0]["mancap_3"]),
                                                            tel_yogunluk=tel_yogunlugu_1(
                                                                tel_turu=gl[0]["teltipi"],
                cu_yog=cu_yog,
                al_yog=al_yog,
                dig_yog=dig_yog))
                gl[0]["agr_tel_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                            kesit_2=kesit_hesap_2(cap=gl[0]["mancap_4"]),
                                                            tel_yogunluk=tel_yogunlugu_1(
                                                                tel_turu=gl[0]["teltipi"],
                cu_yog=cu_yog,
                al_yog=al_yog,
                dig_yog=dig_yog))
                gl[0]["agr_karetel_1"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                            kesit_2=gl[0]["karetel11"] * gl[0]["karetel12"],
                                                            tel_yogunluk=tel_yogunlugu_1(
                                                                tel_turu=gl[0]["teltipi"],
                cu_yog=cu_yog,
                al_yog=al_yog,
                dig_yog=dig_yog))
                gl[0]["agr_karetel_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=gl[0]["karetel21"] * gl[0]["karetel22"],
                                                                tel_yogunluk=tel_yogunlugu_1(
                                                                    tel_turu=gl[0]["teltipi"],
                cu_yog=cu_yog,
                al_yog=al_yog,
                dig_yog=dig_yog))
                gl[0]["agr_karetel_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=gl[0]["karetel31"] * gl[0]["karetel32"],
                                                                tel_yogunluk=tel_yogunlugu_1(
                                                                    tel_turu=gl[0]["teltipi"],
                cu_yog=cu_yog,
                al_yog=al_yog,
                dig_yog=dig_yog))
                gl[0]["agr_karetel_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=gl[0]["karetel41"] * gl[0]["karetel42"],
                                                                tel_yogunluk=tel_yogunlugu_1(
                                                                    tel_turu=gl[0]["teltipi"],
                cu_yog=cu_yog,
                al_yog=al_yog,
                dig_yog=dig_yog))
                gl[0]["agr_folyo_1"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                                kesit_2=gl[0]["folyotel11"] * gl[0]["folyotel12"],
                                                                tel_yogunluk=tel_yogunlugu_1(
                                                                    tel_turu=gl[0]["teltipi"],
                cu_yog=cu_yog,
                al_yog=al_yog,
                dig_yog=dig_yog))
                gl[0]["agr_folyo_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                            kesit_2=gl[0]["folyotel21"] * gl[0]["folyotel22"],
                                                            tel_yogunluk=tel_yogunlugu_1(
                                                                tel_turu=gl[0]["teltipi"],
                cu_yog=cu_yog,
                al_yog=al_yog,
                dig_yog=dig_yog))
                gl[0]["agr_folyo_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                            kesit_2=gl[0]["folyotel31"] * gl[0]["folyotel32"],
                                                            tel_yogunluk=tel_yogunlugu_1(
                                                                tel_turu=gl[0]["teltipi"],
                cu_yog=cu_yog,
                al_yog=al_yog,
                dig_yog=dig_yog))
                gl[0]["agr_folyo_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                            kesit_2=gl[0]["folyotel41"] * gl[0]["folyotel42"],
                                                            tel_yogunluk=tel_yogunlugu_1(
                                                                tel_turu=gl[0]["teltipi"],
                cu_yog=cu_yog,
                al_yog=al_yog,
                dig_yog=dig_yog))
                gl[0]["agr_kapton_1"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                            kesit_2=gl[0]["kapton1"],
                                                            tel_yogunluk=1330)
                gl[0]["agr_kapton_2"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                            kesit_2=gl[0]["kapton2"],
                                                            tel_yogunluk=1330)
                gl[0]["agr_kapton_3"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                            kesit_2=gl[0]["kapton3"],
                                                            tel_yogunluk=1330)
                gl[0]["agr_kapton_4"] = tel_agirlik_hesap_1(tel_uzunluk=gl[0]["tel_uzunluk"],
                                                            kesit_2=gl[0]["kapton4"],
                                                            tel_yogunluk=1330)
            else:
                
                gl[0]["tel_agirlik"]=0
                gl[0]["agr_tel_1"] = 0
                gl[0]["agr_tel_2"] = 0
                gl[0]["agr_tel_3"] = 0
                gl[0]["agr_tel_4"] = 0
                gl[0]["agr_karetel_1"] = 0
                gl[0]["agr_karetel_2"] = 0
                gl[0]["agr_karetel_3"] = 0
                gl[0]["agr_karetel_4"] = 0
                gl[0]["agr_folyo_1"] = 0
                gl[0]["agr_folyo_2"] = 0
                gl[0]["agr_folyo_3"] = 0
                gl[0]["agr_folyo_4"] = 0
                gl[0]["agr_kapton_1"] = 0
                gl[0]["agr_kapton_2"] = 0
                gl[0]["agr_kapton_3"] = 0
                gl[0]["agr_kapton_4"] = 0

        # else:
        #     degerler.clear()
        #     gl[0]["akim1"]=0
        #     gl[0]["kesit1"]=0
        #     gl[0]["cap1"]=0
        #     gl[0]["spir1"]=0
        #     gl[0]["cap2"]=0
        #     gl[0]["akim2"]=0
        #     gl[0]["spir2"]=0
        #     gl[0]["folyotel11"]=0
        #     gl[0]["folyotel12"]=0
        #     gl[0]["folyotel21"]=0
        #     gl[0]["folyotel22"]=0
        #     gl[0]["folyotel31"]=0
        #     gl[0]["folyotel32"]=0
        #     gl[0]["folyotel41"]=0
        #     gl[0]["folyotel42"]=0
        #     gl[0]["kapton1"]=0
        #     gl[0]["kapton2"]=0
        #     gl[0]["kapton3"]=0
        #     gl[0]["kapton4"]=0
        #     gl[0]["karetel11"]=0
        #     gl[0]["karetel12"]=0
        #     gl[0]["karetel21"]=0
        #     gl[0]["karetel22"]=0
        #     gl[0]["karetel31"]=0
        #     gl[0]["karetel32"]=0
        #     gl[0]["karetel41"]=0
        #     gl[0]["karetel42"]=0
        #     gl[0]["kesit2"]=0
        #     gl[0]["tel_en"]=0
        #     gl[0]["tel_yuk"]=0
        #     gl[0]["spirkat"]=0
        #     gl[0]["kat"]=0
        #     gl[0]["katbosluk"]=0
        #     gl[0]["tel_uzunluk"]=0
        #     gl[0]["tel_agirlik"]=0
        #     gl[0]["sarim_yukseklik"]=0
        #     gl[0]["sonkat_spir"]=0
        #     gl[0]["check_spir_man"] = False
        #     gl[0]["kesit_ok"]=False
        #     gl[0]["kesit_error"]=True
        #     gl[0]["akim_ok"]=False
        #     gl[0]["akim_error"]=True
        #     gl[0]["mancap_1"]=0
        #     gl[0]["mancap_2"]=0
        #     gl[0]["mancap_3"]=0
        #     gl[0]["mancap_4"]=0
        #     gl[0]["mlz_tel_1"] = ""
        #     gl[0]["mlz_tel_2"] = ""
        #     gl[0]["mlz_tel_3"] =  ""
        #     gl[0]["mlz_tel_4"] =  ""
        #     gl[0]["mlz_karetel_1"] =  ""
        #     gl[0]["mlz_karetel_2"] =  ""
        #     gl[0]["mlz_karetel_3"] =  ""
        #     gl[0]["mlz_karetel_4"] =  ""
        #     gl[0]["mlz_folyotel_1"] =  ""
        #     gl[0]["mlz_folyotel_2"] =  ""
        #     gl[0]["mlz_folyotel_3"] =  ""
        #     gl[0]["mlz_folyotel_4"] =  ""
        #     gl[0]["mlz_kapton_1"] =  ""
        #     gl[0]["mlz_kapton_2"] =  ""
        #     gl[0]["mlz_kapton_3"] =  ""
        #     gl[0]["mlz_kapton_4"] =  ""
        #     gl[0]["gb_check_tel_1"] =  False
        #     gl[0]["gb_check_tel_2"] =  False
        #     gl[0]["gb_check_tel_3"] =  False
        #     gl[0]["gb_check_tel_4"] =  False
        #     gl[0]["gb_check_karetel_1"]= False
        #     gl[0]["gb_check_karetel_2"]= False
        #     gl[0]["gb_check_karetel_3"]= False
        #     gl[0]["gb_check_karetel_4"]= False
        #     gl[0]["gb_check_folyotel_1"]= False
        #     gl[0]["gb_check_folyotel_2"]= False
        #     gl[0]["gb_check_folyotel_3"]= False
        #     gl[0]["gb_check_folyotel_4"]= False
        #     gl[0]["gb_check_kapton_1"]= False
        #     gl[0]["gb_check_kapton_2"]= False
        #     gl[0]["gb_check_kapton_3"]= False
        #     gl[0]["gb_check_kapton_4"]= False
        #     gl[0]["tel_agirlik"] = 0
        #     gl[0]["agr_tel_1"] = 0
        #     gl[0]["agr_tel_2"] = 0
        #     gl[0]["agr_tel_3"] = 0
        #     gl[0]["agr_tel_4"] = 0
        #     gl[0]["agr_karetel_1"] = 0
        #     gl[0]["agr_karetel_2"] = 0
        #     gl[0]["agr_karetel_3"] = 0
        #     gl[0]["agr_karetel_4"] = 0
        #     gl[0]["agr_folyo_1"] = 0
        #     gl[0]["agr_folyo_2"] = 0
        #     gl[0]["agr_folyo_3"] = 0
        #     gl[0]["agr_folyo_4"] = 0
        #     gl[0]["agr_kapton_1"] = 0
        #     gl[0]["agr_kapton_2"] = 0
        #     gl[0]["agr_kapton_3"] = 0
        #     gl[0]["agr_kapton_4"] = 0
        return dict(degerler)  
