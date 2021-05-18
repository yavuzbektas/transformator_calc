# #######################################
__name__ = "db_sql.py"
__author__ = "Yavuz Bektaş & "
__version__ = "1.0"
__email__ = "yavuzbektas@gmail.com"
__linkedin__ = "https://www.linkedin.com/in/yavuz-bekta%C5%9F-28659642/"
__release_date__ = "2020.05.01"
__github__ = ""
# #######################################
db_type ="sqlite"

import sqlite3,myConfig

TABLES = {}
TABLES['users'] = ("CREATE TABLE `users` "
                   "(`id` INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,"
                   "`username` VARCHAR(30) NOT NULL,"
                   "`password` VARCHAR(30) NOT NULL,"
                   "`usertype` VARCHAR(30) NOT NULL,"
                   "`record_date` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP )")
TABLES['logs'] = ("CREATE TABLE `logs` ("
                           "`id` INTEGER NOT NULL UNIQUE PRIMARY KEY  AUTOINCREMENT,"
                           "`stock_ID` INT NOT NULL,"
                           "`used_quantity` INT,"
                           "`reason` TEXT,"
                           "`yourname` TEXT,"
                           "`userID` TEXT NOT NULL,"
                           "`record_date` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP)")
TABLES['karkas'] = ("CREATE TABLE `karkas` ("
                           "`id` INTEGER NOT NULL UNIQUE PRIMARY KEY  AUTOINCREMENT,"
                           "`karkas_name` TEXT,"
                           "`en` INT NOT NULL,"
                           "`boy` INT NOT NULL,"
                           "`ozellik_1` TEXT ,"
                           "`ozellik_2` TEXT ,"
                           "`record_date` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP)")
TABLES['teller'] = ("CREATE TABLE `teller` ("
                           "`id` INTEGER NOT NULL UNIQUE PRIMARY KEY  AUTOINCREMENT,"
                           "`tel_name` TEXT,"
                           "`cap` REAL NOT NULL,"
                            "`ozellik_1` INT ,"
                           "`ozellik_2` TEXT ,"
                           "`record_date` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP)")
TABLES['kare_tel'] = ("CREATE TABLE `kare_tel` ("
                           "`id` INTEGER NOT NULL UNIQUE PRIMARY KEY  AUTOINCREMENT,"
                           "`tel_name` TEXT,"
                           "`cap1` REAL NOT NULL,"
                            "`cap2` REAL NOT NULL,"
                           "`ozellik_1` TEXT ,"
                           "`ozellik_2` TEXT ,"
                           "`record_date` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP)")
TABLES['folyo_tel'] = ("CREATE TABLE `folyo_tel` ("
                           "`id` INTEGER NOT NULL UNIQUE PRIMARY KEY  AUTOINCREMENT,"
                           "`tel_name` TEXT,"
                           "`cap1` REAL NOT NULL,"
                            "`cap2` REAL NOT NULL,"
                           "`ozellik_1` TEXT ,"
                           "`record_date` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP)")
TABLES['kapton'] = ("CREATE TABLE `kapton` ("
                           "`id` INTEGER NOT NULL UNIQUE PRIMARY KEY  AUTOINCREMENT,"
                           "`kapton_name` TEXT,"
                           "`cap` REAL NOT NULL,"
                            "`ozellik_1` INT ,"
                           "`record_date` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP)")
TABLES['tel_spir'] = ("CREATE TABLE `tel_spir` ("
                           "`id` INTEGER NOT NULL UNIQUE PRIMARY KEY  AUTOINCREMENT,"
                           "`tel_cap` REAL NOT NULL,"
                           "`a_deg` REAL NOT NULL,"
                            "`b_deg` REAL NOT NULL,"
                           "`c_deg` REAL ,"
                           "`cu_deg` REAL ,"
                           "`al_deg` REAL ,"
                           "`record_date` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP)")
TABLES['klemens'] = ("CREATE TABLE `klemens` ("
                           "`id` INTEGER NOT NULL UNIQUE PRIMARY KEY  AUTOINCREMENT,"
                           "`klemens_name` TEXT,"
                           "`a_deg` INT ,"
                            "`b_deg` INT ,"
                            "`akim` REAL ,"
                           "`record_date` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP)")
TABLES['ayak'] = ("CREATE TABLE `ayak` ("
                           "`id` INTEGER NOT NULL UNIQUE PRIMARY KEY  AUTOINCREMENT,"
                           "`ayak_name` TEXT,"
                           "`a_deg` INT ,"
                           
                           "`record_date` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP)")
TABLES['sac_tekfaz'] = ("CREATE TABLE `sac_tekfaz` ("
                           "`id` INTEGER NOT NULL UNIQUE PRIMARY KEY  AUTOINCREMENT,"
                           "`sac_olcu` REAL NOT NULL UNIQUE,"
                           "`a_deg` REAL ,"
                           "`b_deg` REAL ,"
                           "`c_deg` REAL ,"
                           "`d_deg` REAL ,"
                           "`e_deg` REAL ,"
                           "`f_deg` REAL ,"
                           "`h_deg` REAL ,"
                           "`i_deg` REAL ,"
                           "`k1_deg` REAL ,"
                           "`k2_deg` REAL ,"
                           "`ag1_deg` REAL ,"
                           "`ag2_deg` REAL ,"
                           "`Ac_deg` REAL ,"
                           "`Wa_deg` REAL ,"
                           "`Ap_deg` REAL ,"
                           "`Kg_deg` REAL ,"
                           "`At_deg` REAL ,"
                           "`MPL_deg` REAL ,"
                           "`MLT_deg` REAL ,"

                           "`record_date` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP)")
TABLES['sac_trifaz'] = ("CREATE TABLE `sac_trifaz` ("
                           "`id` INTEGER NOT NULL UNIQUE PRIMARY KEY  AUTOINCREMENT,"
                           "`sac_olcu` REAL NOT NULL UNIQUE,"
                           "`a_deg` REAL ,"
                           "`b_deg` REAL ,"
                           "`c_deg` REAL ,"
                           "`d_deg` REAL ,"
                           "`e_deg` REAL ,"
                           "`f_deg` REAL ,"
                           "`h_deg` REAL ,"
                           "`i_deg` REAL ,"
                           "`k1_deg` REAL ,"
                           "`k2_deg` REAL ,"
                           "`ag1_deg` REAL ,"
                           "`ag2_deg` REAL ,"
                           "`Ac_deg` REAL ,"
                           "`Wa_deg` REAL ,"
                           "`Ap_deg` REAL ,"
                           "`Kg_deg` REAL ,"
                           "`At_deg` REAL ,"
                           "`MPL_deg` REAL ,"
                           "`MLT_deg` REAL ,"

                           "`record_date` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP)")
TABLES['recete'] = ("CREATE TABLE `recete` "
                   "(`id` INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,"
                   "`musteri_kodu` TEXT," 
                   "`musteri_adi` TEXT,"
                   "`siparis_kodu` TEXT," 
                   "`kademeli` VARCHAR(30),"
                    "`primer_kademe` VARCHAR(30),"
                    "`sekonder_kademe` VARCHAR(30),"
                    "`va_kademe` VARCHAR(30),"
                   "`guc` REAL,"
                   "`karkas_en` REAL ,"
                   "`karkas_boy` REAL ,"
                    "`karkas_yukseklik` REAL ,"
                    "`karkas_verim` REAL ,"
                    "`sac_tipi` VARCHAR(30),"
                    "`sac` REAL ,"
                    "`frekans` REAL ,"
                    "`gauss` REAL ,"
                    "`c_deg` REAL ,"
                    "`nuve_bosluk` REAL ,"
                    "`primer_izo_deg` REAL ,"
                    "`primer_izo_tur` REAL ,"
                    "`sekonder_izo_deg` REAL ,"
                    "`sekonder_izo_tur` REAL ,"
                    "`pri_sek_izo_deg` REAL ,"
                    "`pri_sek_izo_tur` REAL ,"
                    "`ekran_sec` VARCHAR(10) ,"
                    "`ekran_izo_deg` REAL ,"
                    "`ekstra` VARCHAR(10) ,"
                    "`ekstra_izo_deg` REAL ,"
                    "`klemens_adi` VARCHAR(30) ,"
                    "`klemens_a_deg` REAL ,"
                    "`klemens_b_deg` REAL ,"
                    "`ayak_adi` VARCHAR(30) ,"
                    "`ayak_a_deg` REAL ,"
                    "`ayak_b_deg` REAL ,"
                    "`primer_1` TEXT ,"
                    "`primer_2` TEXT ,"
                    "`primer_3` TEXT ,"
                    "`primer_4` TEXT ,"
                    "`primer_5` TEXT ,"
                    "`primer_6` TEXT ,"
                    "`primer_7` TEXT ,"
                    "`primer_8` TEXT ,"
                    "`primer_9` TEXT ,"
                    "`primer_10` TEXT ,"
                    "`sekonder_1` TEXT ,"
                    "`sekonder_2` TEXT ,"
                    "`sekonder_3` TEXT ,"
                    "`sekonder_4` TEXT ,"
                    "`sekonder_5` TEXT ,"
                    "`sekonder_6` TEXT ,"
                    "`sekonder_7` TEXT ,"
                    "`sekonder_8` TEXT ,"
                    "`sekonder_9` TEXT ,"
                    "`sekonder_10` TEXT ,"
                    "`sva1_1` TEXT ,"
                    "`sva1_2` TEXT ,"
                    "`sva1_3` TEXT ,"
                    "`sva1_4` TEXT ,"
                    "`sva1_5` TEXT ,"
                    "`sva1_6` TEXT ,"
                    "`sva1_7` TEXT ,"
                    "`sva1_8` TEXT ,"
                    "`sva1_9` TEXT ,"
                    "`sva1_10` TEXT ,"
                    "`sva2_1` TEXT ,"
                    "`sva2_2` TEXT ,"
                    "`sva2_3` TEXT ,"
                    "`sva2_4` TEXT ,"
                    "`sva2_5` TEXT ,"
                    "`sva2_6` TEXT ,"
                    "`sva2_7` TEXT ,"
                    "`sva2_8` TEXT ,"
                    "`sva2_9` TEXT ,"
                    "`sva2_10` TEXT ,"
                    "`sva3_1` TEXT ,"
                    "`sva3_2` TEXT ,"
                    "`sva3_3` TEXT ,"
                    "`sva3_4` TEXT ,"
                    "`sva3_5` TEXT ,"
                    "`sva3_6` TEXT ,"
                    "`sva3_7` TEXT ,"
                    "`sva3_8` TEXT ,"
                    "`sva3_9` TEXT ,"
                    "`sva3_10` TEXT ,"
                    "`sva4_1` TEXT ,"
                    "`sva4_2` TEXT ,"
                    "`sva4_3` TEXT ,"
                    "`sva4_4` TEXT ,"
                    "`sva4_5` TEXT ,"
                    "`sva4_6` TEXT ,"
                    "`sva4_7` TEXT ,"
                    "`sva4_8` TEXT ,"
                    "`sva4_9` TEXT ,"
                    "`sva4_10` TEXT ,"
                    "`sva5_1` TEXT ,"
                    "`sva5_2` TEXT ,"
                    "`sva5_3` TEXT ,"
                    "`sva5_4` TEXT ,"
                    "`sva5_5` TEXT ,"
                    "`sva5_6` TEXT ,"
                    "`sva5_7` TEXT ,"
                    "`sva5_8` TEXT ,"
                    "`sva5_9` TEXT ,"
                    "`sva5_10` TEXT ,"
                    "`sva6_1` TEXT ,"
                    "`sva6_2` TEXT ,"
                    "`sva6_3` TEXT ,"
                    "`sva6_4` TEXT ,"
                    "`sva6_5` TEXT ,"
                    "`sva6_6` TEXT ,"
                    "`sva6_7` TEXT ,"
                    "`sva6_8` TEXT ,"
                    "`sva6_9` TEXT ,"
                    "`sva6_10` TEXT ,"
                    "`sva7_1` TEXT ,"
                    "`sva7_2` TEXT ,"
                    "`sva7_3` TEXT ,"
                    "`sva7_4` TEXT ,"
                    "`sva7_5` TEXT ,"
                    "`sva7_6` TEXT ,"
                    "`sva7_7` TEXT ,"
                    "`sva7_8` TEXT ,"
                    "`sva7_9` TEXT ,"
                    "`sva7_10` TEXT ,"
                    "`sva8_1` TEXT ,"
                    "`sva8_2` TEXT ,"
                    "`sva8_3` TEXT ,"
                    "`sva8_4` TEXT ,"
                    "`sva8_5` TEXT ,"
                    "`sva8_6` TEXT ,"
                    "`sva8_7` TEXT ,"
                    "`sva8_8` TEXT ,"
                    "`sva8_9` TEXT ,"
                    "`sva8_10` TEXT ,"
                    "`sva9_1` TEXT ,"
                    "`sva9_2` TEXT ,"
                    "`sva9_3` TEXT ,"
                    "`sva9_4` TEXT ,"
                    "`sva9_5` TEXT ,"
                    "`sva9_6` TEXT ,"
                    "`sva9_7` TEXT ,"
                    "`sva9_8` TEXT ,"
                    "`sva9_9` TEXT ,"
                    "`sva9_10` TEXT ,"
                    "`sva10_1` TEXT ,"
                    "`sva10_2` TEXT ,"
                    "`sva10_3` TEXT ,"
                    "`sva10_4` TEXT ,"
                    "`sva10_5` TEXT ,"
                    "`sva10_6` TEXT ,"
                    "`sva10_7` TEXT ,"
                    "`sva10_8` TEXT ,"
                    "`sva10_9` TEXT ,"
                    "`sva10_10` TEXT ,"
                    "`sva1_kad` INT ,"
                    "`sva2_kad` INT ,"
                    "`sva3_kad` INT ,"
                    "`sva4_kad` INT ,"
                    "`sva5_kad` INT ,"
                    "`sva6_kad` INT ,"
                    "`sva7_kad` INT ,"
                    "`sva8_kad` INT ,"
                    "`sva9_kad` INT ,"
                    "`sva10_kad` INT ,"
                    "`sva1_guc` INT ,"
                    "`sva2_guc` INT ,"
                    "`sva3_guc` INT ,"
                    "`sva4_guc` INT ,"
                    "`sva5_guc` INT ,"
                    "`sva6_guc` INT ,"
                    "`sva7_guc` INT ,"
                    "`sva8_guc` INT ,"
                    "`sva9_guc` INT ,"
                    "`sva10_guc` INT ,"
                    "`p_tel` TEXT ,"
                    "`sk_tel` TEXT ,"
                    "`sva1_tel` TEXT ,"
                    "`sva2_tel` TEXT ,"
                    "`sva3_tel` TEXT ,"
                    "`sva4_tel` TEXT ,"
                    "`sva5_tel` TEXT ,"
                    "`sva6_tel` TEXT ,"
                    "`sva7_tel` TEXT ,"
                    "`sva8_tel` TEXT ,"
                    "`sva9_tel` TEXT ,"
                    "`sva10_tel` TEXT ,"
                   "`record_date` TIMESTAMP  DEFAULT CURRENT_TIMESTAMP )")

import myConfig
config_file = myConfig.read_config()
DB_NAME= config_file.get("PATHS", "DB_DIR") +"\\"+ config_file.get("DATABASE", "DB_NAME")
HOST= config_file.get("DATABASE", "HOST")
USERNAME=config_file.get("DATABASE", "USERNAME")
PASSWORD= config_file.get("DATABASE", "PASSWORD")
class mydb(): 
    def __init__(self,host=HOST,username=USERNAME,password=PASSWORD,DB_NAME=DB_NAME):
        self.host=host
        self.username=username
        self.password=password
        self.db_name=DB_NAME
        self.connect_db()
        #self.create_tables()
    def connect_db(self):
        try:

            self.db = sqlite3.connect(database=self.db_name)

        except Exception as error:
            print("DataBase'e ulasılamadı bu nedenle  Server Ayarlarını lutfen kontrol edin. İlgili hata : ",error)

        self.cursor = self.db.cursor()

    def create_db(self,cursor):
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT COLLATE 'utf8_turkish_ci'".format(self.db_name))
            self.create_tables()
        except Exception as err:
            print("Veri Tabanı yaratılırken Su hata Meydana Geldi: {}".format(err))
            exit(1)
    def create_tables(self):

        for table_name in TABLES:
            table_description = TABLES[table_name]
            try:

                self.cursor.execute(table_description)
                print("Tablo Yaratılıyor {}: ".format(table_name), end='')
            except Exception as err:
                    print("Bilgi   : ", err)

        self.cursor.close()
        self.db.close()
    def search_data(self,query,values):
        self.connect_db()
        self.cursor.execute(query,(values))
        data = self.cursor.fetchall()
        self.cursor.close()
        self.db.close()
        return data
    def fetchall(self,query):
        self.connect_db()
        self.cursor.execute(query)
        try:
            data = self.cursor.fetchall()
        except Exception as err:
            print(err)
        finally:
            self.cursor.close()
            self.db.close()
        if data == None:
            return None
        else:
            return data
    def fetchone(self,query):
        self.connect_db()
        self.cursor.execute(query)
        try:
            data = self.cursor.fetchone()

        except Exception as err:
            print(err)
        finally:
            self.cursor.close()
            self.db.close()
        if data == None:
            return None
        else:
            return data
    def commit_db(self,query):
        self.connect_db()
        try:
            self.cursor.execute(query)
            self.db.commit()
        except Exception as err:
            print(err)
            return err
        finally:
            self.cursor.close()
            self.db.close()
    # =========== USER ==========================
    def check_user(self,values):
        self.connect_db()
        query = "SELECT id,username,password,usertype FROM users WHERE username='%s' AND password='%s'" % (values)
        data = self.fetchone(query)
        return data
    def check_username(self,values):
        query = "SELECT id,username,password,usertype FROM users WHERE username='%s'" % values
        data = self.fetchone(query)
        return data
    def insert_user(self,values):
        query = "INSERT INTO users (username,password,usertype ) VALUES ( '%s','%s','%s')" % values
        data = self.commit_db(query)
        return data
    def calldata_with_id_user(self,id):
        query =  "SELECT id,username,password,usertype,record_date FROM users WHERE users.id = '%s'" % (id,)
        data = self.fetchone(query)
        return data
    def delete_user(self,value):
        query = "DELETE FROM users WHERE id='%s'" % (value,)
        data = self.commit_db(query)
        return data
    def update_user(self,value):
        query = "UPDATE  users SET " \
                "username='%s',password='%s',usertype='%s' " \
                "WHERE id='%s'" % (value)
        data = self.commit_db(query)
        return data
    def showall_user(self):
        query = "SELECT id,username,usertype,record_date,password  FROM users "
        data = self.fetchall(query)
        return data
    def showfilter_user(self,filter_value):
        query = "SELECT id,username,usertype,record_date,password  FROM users WHERE username LIKE '{}%'".format(filter_value)
        data = self.fetchall(query)
        return data

    # =========== recete  ==========================
    def check_recete(self,values):

        query = "SELECT id,kullanici,musteri_adi,siparis_kodu, \
                 guc,primer_list,sekonder_list,sva_list,rec_veriler,trafo_tipi" \
        " FROM recete WHERE siparis_kodu = '%s'" % values

        data = self.fetchone(query)
        return data
    def insert_recete(self,values):
        query = "INSERT INTO recete (kullanici,musteri_adi,siparis_kodu, \
                 guc,primer_list,sekonder_list,sva_list,rec_veriler,trafo_tipi) VALUES ( " \
                "'%s','%s','%s','%f','%s','%s','%s','%s','%s' )" % values
        try:
            data = self.commit_db(query)
        except Exception as err:
            print("SQL Error : ",err)
            return None
        return True
    def calldata_with_id_recete(self,id):
        query = "SELECT recete.id,kullanici,musteri_adi,siparis_kodu, \
                 guc,primer_list,sekonder_list,sva_list,recete.record_date, rec_veriler,trafo_tipi " \
                "FROM recete  WHERE recete.id = '%d'" % (id,)
        data = self.fetchone(query)
        return data
    def delete_recete(self,value):
        query = "DELETE FROM recete WHERE id='%d'" % (value,)
        data = self.commit_db(query)
        return data
    def update_recete(self,value):
        query = "UPDATE  recete SET " \
                "kullanici='%s',musteri_adi='%s',siparis_kodu='%s',guc='%f',primer_list='%s',sekonder_list='%s',sva_list='%s',rec_veriler='%s' ,trafo_tipi='%s' " \
                "WHERE id='%d'" % (value)
        data = self.commit_db(query)
        return data
    def showall_recete(self):
        query = "SELECT recete.id,kullanici,musteri_adi,siparis_kodu ,guc,primer_list,sekonder_list,sva_list,recete.record_date,rec_veriler,trafo_tipi " \
                " FROM recete "
        data = self.fetchall(query)
        return data
    def showfilter_recete(self, filter_value, index=0):
        index1,index2=index
        filter1,filter2,trafo_tipi=filter_value
        if index1 == 1:
            criteria1 = "recete.kullanici"
        elif index1 == 2:
            criteria1 = "recete.guc"
        elif index1 == 3:
            criteria1 = "recete.musteri_adi"
        elif index1 == 4:
            criteria1 = "recete.siparis_kodu"
        elif index1 == 5:
            criteria1 = "recete.record_date"
        else:
            criteria1 = ""
        if index2 == 1:
            criteria2 = "recete.kullanici"
        elif index2 == 2:
            criteria2 = "recete.musteri_adi"
        elif index2 == 3:
            criteria2 = "recete.siparis_kodu"
        elif index2 == 4:
            criteria2 = "recete.record_date"
        else:
            criteria2 = ""
        if index1 >0 and index2 >0:
            query = "SELECT id,kullanici,musteri_adi,siparis_kodu, \
                 guc,primer_list,sekonder_list,sva_list,record_date " \
                " FROM recete WHERE {} LIKE '{}%' AND {} LIKE '{}%' AND recete.trafo_tipi = '{}'".format(criteria1,filter1,criteria2,filter2,trafo_tipi)
        elif index1 >0 and index2 ==0:
            query = "SELECT id,kullanici,musteri_adi,siparis_kodu, \
                             guc,primer_list,sekonder_list,sva_list,record_date " \
                    " FROM recete WHERE {} LIKE '{}%' AND recete.trafo_tipi = '{}'".format(criteria1, filter1,trafo_tipi)
        else: 
            query = "SELECT id,kullanici,musteri_adi,siparis_kodu, \
                             guc,primer_list,sekonder_list,sva_list,record_date " \
                    " FROM recete WHERE  recete.trafo_tipi = '{}'".format(trafo_tipi)
        data = self.fetchall(query)
        return data
    # =========== logs  ==========================

    # =========== karkas==========================

    def check_karkas(self,values):
        query = "SELECT id,karkas_name,en,boy,ozellik_1,ozellik_2 FROM karkas WHERE karkas_name='%s'" % values
        data = self.fetchone(query)
        return data
    def insert_karkas(self,values):
        query = "INSERT INTO karkas (karkas_name,en,boy,ozellik_1,ozellik_2 ) VALUES ( '%s','%f','%f','%s','%s')" % (values)
        data = self.commit_db(query)
        return data
    def calldata_with_id_karkas(self,id):
        query =  "SELECT id,karkas_name,en,boy,ozellik_1,ozellik_2,record_date FROM karkas WHERE karkas.id = '%s'" % (id,)
        data = self.fetchone(query)
        return data
    def delete_karkas(self,value):
        query = "DELETE FROM karkas WHERE id='%s'" % (value,)
        data = self.commit_db(query)
        return data
    def update_karkas(self,value):
        query = "UPDATE  karkas SET " \
                "karkas_name='%s',en='%f',boy='%f',ozellik_1='%s' ,ozellik_2='%s'" \
                "WHERE id='%d'" % (value)
        data = self.commit_db(query)
        return data
    def showall_karkas(self):
        query = "SELECT id,karkas_name,en,boy,ozellik_1,ozellik_2,record_date  FROM karkas ORDER BY en DESC "
        data = self.fetchall(query)
        return data

    def showfilter_karkas(self, filter_value, index=0):
        if index == 0:
            criteria = "karkas.en = " + filter_value.split("x")[0] + " AND " + "karkas.boy  = " + filter_value.split("x")[1]

        elif index == 1:
            criteria = "karkas.karkas_name LIKE '{}%'".format(filter_value)
        elif index == 2:
            criteria = "karkas.en LIKE '{}%'".format(filter_value)
        elif index == 3:
            criteria = "karkas.boy LIKE '{}%'".format(filter_value)

        else:
            criteria = ""

        query = "SELECT id,karkas_name,en,boy,ozellik_1,ozellik_2,record_date  FROM karkas WHERE {} ".format(criteria)
        data = self.fetchall(query)
        return data

    # =========== TELLER ==========================
    # tel secimi
    def check_teller(self,values):
        query = "SELECT id,tel_name,cap,ozellik_1,ozellik_2 FROM teller WHERE tel_name='%s'" % values
        data = self.fetchone(query)
        return data
    def insert_teller(self,values):
        query = "INSERT INTO teller (tel_name,cap,ozellik_1 ,ozellik_2 ) VALUES ( '%s','%f','%s','%s')" % values
        data = self.commit_db(query)
        return data
    def calldata_with_id_teller(self,id):
        query =  "SELECT id,tel_name,cap,ozellik_1,ozellik_2,record_date FROM teller WHERE teller.id = '%d'" % (id,)
        data = self.fetchone(query)
        return data
    def delete_teller(self,value):
        query = "DELETE FROM teller WHERE id='%d'" % (value,)
        data = self.commit_db(query)
        return data
    def update_teller(self,value):
        query = "UPDATE  teller SET " \
                "tel_name='%s',cap='%f',ozellik_1='%s' ,ozellik_2='%s'" \
                "WHERE id='%d'" % (value)
        data = self.commit_db(query)
        return data
    def showall_teller(self):
        query = "SELECT id,tel_name,cap,ozellik_1,ozellik_2,record_date  FROM teller "
        data = self.fetchall(query)
        return data
    def showfilter_teller(self, filter_value, index=0):
        if index == 0:
            criteria = "teller.tel_name"
        elif index == 1:
            criteria = "teller.cap"
        elif index == 2:
            criteria = "teller.ozellik_1"

        else:
            criteria = ""

        query = "SELECT id,tel_name,cap,ozellik_1,ozellik_2,record_date  FROM teller WHERE {} LIKE '{}%'".format(criteria, filter_value)
        data = self.fetchall(query)
        return data
    def get_tell_byname(self, filter_value):
        query = f"SELECT cap  FROM teller WHERE tel_name = '{filter_value}'"
        data = self.fetchone(query)
        return data
    # folyoteel secimi
    def check_folyotel(self,values):
        query = "SELECT id,tel_name,cap1,cap2,ozellik_1 FROM folyo_tel WHERE tel_name='%s'" % values
        data = self.fetchone(query)
        return data
    def insert_folyotel(self,values):
        query = "INSERT INTO folyo_tel (tel_name,cap1,cap2,ozellik_1 ,ozellik_2) VALUES ( '%s','%f','%f','%s','%s')" % values
        data = self.commit_db(query)
        return data
    def calldata_with_id_folyotel(self,id):
        query =  "SELECT id,tel_name,cap1,cap2,ozellik_1,ozellik_2,record_date FROM folyo_tel WHERE folyo_tel.id = '%d'" % (id,)
        data = self.fetchone(query)
        return data
    def delete_folyotel(self,value):
        query = "DELETE FROM folyo_tel WHERE id='%d'" % (value,)
        data = self.commit_db(query)
        return data
    def update_folyotel(self,value):
        query = "UPDATE  folyo_tel SET " \
                "tel_name='%s',cap1='%f',cap2='%f',ozellik_1='%s' ,ozellik_2='%s' " \
                "WHERE id='%s'" % (value)
        data = self.commit_db(query)
        return data
    def showall_folyotel(self):
        query = "SELECT id,tel_name,cap1,cap2,ozellik_1,ozellik_2,record_date  FROM folyo_tel "
        data = self.fetchall(query)
        return data
    def showfilter_folyotel(self, filter_value, index=0):
        if index == 0:
            criteria = "folyo_tel.tel_name"
        elif index == 1:
            criteria = "folyo_tel.cap1"
        elif index == 2:
            criteria = "folyo_tel.cap2"
        elif index == 3:
            criteria = "folyo_tel.ozellik_1"
        else:
            criteria = ""

        query = "SELECT id,tel_name,cap1,cap2,ozellik_1,ozellik_2,record_date  FROM folyo_tel WHERE {} LIKE '{}%'".format(criteria, filter_value)
        data = self.fetchall(query)
        return data
    def get_folyotell_byname(self, filter_value):
        query = f"SELECT cap1,cap2  FROM folyo_tel WHERE tel_name = '{filter_value}'"
        data = self.fetchone(query)
        return data
    # karetel secimi
    def check_karetel(self, values):
        query = "SELECT id,tel_name,cap1,cap2,ozellik_1,ozellik_2 FROM kare_tel WHERE tel_name='%s'" % values
        data = self.fetchone(query)
        return data
    def insert_karetel(self, values):
        query = "INSERT INTO kare_tel (tel_name,cap1,cap2,ozellik_1,ozellik_2 ) VALUES ( '%s','%f','%f','%s','%s')" % values
        data = self.commit_db(query)
        return data
    def calldata_with_id_karetel(self, id):
        query = "SELECT id,tel_name,cap1,cap2,ozellik_1,ozellik_2,record_date FROM kare_tel WHERE kare_tel.id = '%d'" % (id,)
        data = self.fetchone(query)
        return data
    def delete_karetel(self, value):
        query = "DELETE FROM kare_tel WHERE id='%d'" % (value,)
        data = self.commit_db(query)
        return data
    def update_karetel(self, value):
        query = "UPDATE  kare_tel SET " \
                "tel_name='%s',cap1='%f',cap2='%f',ozellik_1='%s',ozellik_2='%s' " \
                "WHERE id='%d'" % (value)
        data = self.commit_db(query)
        return data
    def showall_karetel(self):
        query = "SELECT id,tel_name,cap1,cap2,ozellik_1,ozellik_2,record_date  FROM kare_tel "
        data = self.fetchall(query)
        return data
    def showfilter_karetel(self, filter_value, index=0):
        if index == 0:
            criteria = "kare_tel.tel_name"
        elif index == 1:
            criteria = "kare_tel.cap1"
        elif index == 2:
            criteria = "kare_tel.cap2"
        elif index == 3:
            criteria = "kare_tel.ozellik_1"
        else:
            criteria = ""

        query = "SELECT id,tel_name,cap1,cap2,ozellik_1,ozellik_2,record_date  FROM kare_tel WHERE {} LIKE '{}%'".format(
            criteria, filter_value)
        data = self.fetchall(query)
        return data
    def get_karetell_byname(self, filter_value):
        query = f"SELECT cap1,cap2  FROM kare_tel WHERE tel_name = '{filter_value}'"
        data = self.fetchone(query)
        return data
    # kapton secimi
    def check_kapton(self,values):
        query = "SELECT id,kapton_name,cap,ozellik_1 FROM kapton WHERE kapton_name='%s'" % values
        data = self.fetchone(query)
        return data
    def insert_kapton(self,values):
        query = "INSERT INTO kapton (kapton_name,cap,ozellik_1 ) VALUES ( '%s','%f','%s')" % values
        data = self.commit_db(query)
        return data
    def calldata_with_id_kapton(self,id):
        query =  "SELECT id,kapton_name,cap,ozellik_1,record_date FROM kapton WHERE kapton.id = '%d'" % (id,)
        data = self.fetchone(query)
        return data
    def delete_kapton(self,value):
        query = "DELETE FROM kapton WHERE id='%d'" % (value,)
        data = self.commit_db(query)
        return data
    def update_kapton(self,value):
        query = "UPDATE  kapton SET " \
                "kapton_name='%s',cap='%f',ozellik_1='%s' " \
                "WHERE id='%d'" % (value)
        data = self.commit_db(query)
        return data
    def showall_kapton(self):
        query = "SELECT id,kapton_name,cap,ozellik_1,record_date  FROM kapton "
        data = self.fetchall(query)
        return data
    def showfilter_kapton(self, filter_value, index=0):
        if index == 0:
            criteria = "kapton.kapton_name"
        elif index == 1:"kapton.cap"
        elif index == 2:
            criteria = "kapton.ozellik_1"

        else:
            criteria = ""

        query = "SELECT id,kapton_name,cap,ozellik_1,record_date  FROM kapton WHERE {} LIKE '{}%'".format(criteria, filter_value)
        data = self.fetchall(query)
        return data
    def get_kapton_byname(self, filter_value):
        query = f"SELECT cap  FROM kapton WHERE kapton_name = '{filter_value}'"
        data = self.fetchone(query)
        return data
    # tel_spir secimi
    def check_tel_spir(self,values):
        query = "SELECT id,tel_cap,a_deg,b_deg,c_deg,cu_deg,al_deg FROM tel_spir WHERE tel_cap='%s'" % values
        data = self.fetchone(query)
        return data
    def insert_tel_spir(self,values):
        query = "INSERT INTO tel_spir (tel_cap,a_deg,b_deg,c_deg,cu_deg,al_deg ) VALUES ( '%s','%s','%s','%s','%s','%s')" % values
        data = self.commit_db(query)
        return data
    def calldata_with_id_tel_spir(self,id):
        query =  "SELECT id,tel_cap,a_deg,b_deg,c_deg,cu_deg,al_deg,record_date FROM tel_spir WHERE tel_spir.id = '%s'" % (id,)
        data = self.fetchone(query)
        return data
    def delete_tel_spir(self,value):
        query = "DELETE FROM tel_spir WHERE id='%s'" % (value,)
        data = self.commit_db(query)
        return data
    def update_tel_spir(self,value):
        query = "UPDATE  tel_spir SET " \
                "tel_cap='%s',a_deg='%s',b_deg='%s',c_deg='%s',cu_deg='%s',al_deg='%s' " \
                "WHERE id='%s'" % (value)
        data = self.commit_db(query)
        return data
    def showall_tel_spir(self):
        query = "SELECT id,tel_cap,a_deg,b_deg,c_deg,cu_deg,al_deg,record_date  FROM tel_spir "
        data = self.fetchall(query)
        return data
    def showfilter_tel_spir(self, filter_value, index=0):
        if index == 0:
            criteria = "tel_spir.tel_cap"
        elif index == 1:
            criteria = "tel_spir.a_deg"
        elif index == 2:
            criteria = "tel_spir.b_deg"
        elif index == 3:
            criteria = "tel_spir.c_deg"
        elif index == 4:
            criteria = "tel_spir.cu_deg"
        elif index == 5:
            criteria = "tel_spir.al_deg"
        else:
            criteria = ""

        query = "SELECT id,tel_cap,a_deg,b_deg,c_deg,cu_deg,al_deg,record_date  FROM tel_spir WHERE {} LIKE '{}'".format(criteria, filter_value)
        data = self.fetchall(query)
        return data
    # klemens secimi   
    def check_klemens(self,values):
        query = "SELECT id,klemens_name,en,boy,yuk,akim FROM klemens WHERE klemens_name='%s'" % values
        data = self.fetchone(query)
        return data
    def insert_klemens(self,values):
        query = "INSERT INTO klemens (klemens_name,en,boy,yuk,akim ) VALUES ( '%s','%f','%f','%f','%f')" % values
        data = self.commit_db(query)
        return data
    def calldata_with_id_klemens(self,id):
        query =  "SELECT id,klemens_name,en,boy,yuk,akim,record_date FROM klemens WHERE klemens.id = '%d'" % (id,)
        data = self.fetchone(query)
        return data
    def delete_klemens(self,value):
        query = "DELETE FROM klemens WHERE id='%d'" % (value,)
        data = self.commit_db(query)
        return data
    def update_klemens(self,value):
        query = "UPDATE  klemens SET " \
                "klemens_name='%s',en='%f',boy='%f' ,yuk='%f' ,akim='%f' " \
                "WHERE id='%d'" % (value)
        data = self.commit_db(query)
        return data
    def showall_klemens(self):
        query = "SELECT id,klemens_name,en,boy,yuk,akim,record_date  FROM klemens "
        data = self.fetchall(query)
        return data
    def showfilter_klemens(self, filter_value, index=0):
        if index == 0:
            criteria = "klemens.klemens_name"
        elif index == 1: criteria ="klemens.en"
        elif index == 2:  criteria = "klemens.boy"
        elif index == 3:
            criteria = "klemens.yuk"
        elif index == 4:
            criteria = "klemens.akim"
        else:
            criteria = ""

        query = "SELECT id,klemens_name,en,boy,yuk,akim,record_date  FROM klemens WHERE {} LIKE '{}%'".format(criteria, filter_value)
        data = self.fetchall(query)
        return data

    # ayak secimi   
    def check_ayak(self,values):
        query = "SELECT id,ayak_name,en,boy,yuk FROM ayak WHERE ayak_name='%s'" % values
        data = self.fetchone(query)
        return data
    def insert_ayak(self,values):
        query = "INSERT INTO ayak (ayak_name,en,boy,yuk) VALUES ( '%s','%f','%f','%f')" % values
        data = self.commit_db(query)
        return data
    def calldata_with_id_ayak(self,id):
        query =  "SELECT id,ayak_name,en,boy,yuk,record_date FROM ayak WHERE ayak.id = '%d'" % (id,)
        data = self.fetchone(query)
        return data
    def delete_ayak(self,value):
        query = "DELETE FROM ayak WHERE id='%d'" % (value,)
        data = self.commit_db(query)
        return data
    def update_ayak(self,value):
        query = "UPDATE  ayak SET " \
                "ayak_name='%s',en='%f' ,boy='%f',yuk='%f'" \
                "WHERE id='%d'" % (value)
        data = self.commit_db(query)
        return data
    def showall_ayak(self):
        query = "SELECT id,ayak_name,en,boy,yuk,record_date  FROM ayak "
        data = self.fetchall(query)
        return data
    def showfilter_ayak(self, filter_value, index=0):
        if index == 0:
            criteria = "ayak.ayak_name"
        elif index == 1: criteria ="ayak.en"
        elif index == 2:  criteria = "ayak.boy"
        elif index == 3:
            criteria = "ayak.yuk"
        else:
            criteria = ""

        query = "SELECT id,ayak_name,en,boy,yuk,record_date  FROM ayak WHERE {} LIKE '{}%'".format(criteria, filter_value)
        data = self.fetchall(query)
        return data

    # sac_tekfaz secimi   
    def check_sac_tekfaz(self,values):
        query = "SELECT id,sac_olcu,a_deg,b_deg,c_deg,d_deg,e_deg,f_deg,h_deg,i_deg,k1_deg,k2_deg,ag1_deg,ag2_deg,Ac_deg,Wa_deg,Ap_deg,Kg_deg,At_deg,MPL_deg,MLT_deg FROM sac_tekfaz WHERE sac_olcu='%s'" % values
        data = self.fetchone(query)
        return data
    def insert_sac_tekfaz(self,values):
        query = "INSERT INTO sac_tekfaz (sac_olcu,a_deg,b_deg,c_deg,d_deg,e_deg,f_deg,h_deg,i_deg,k1_deg,k2_deg,ag1_deg,ag2_deg,Ac_deg,Wa_deg,Ap_deg,Kg_deg,At_deg,MPL_deg,MLT_deg ) VALUES ( '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % values
        data = self.commit_db(query)
        return data
    def calldata_with_id_sac_tekfaz(self,id):
        query =  "SELECT id,sac_olcu,a_deg,b_deg,c_deg,d_deg,e_deg,f_deg,h_deg,i_deg,k1_deg,k2_deg,ag1_deg,ag2_deg,Ac_deg,Wa_deg,Ap_deg,Kg_deg,At_deg,MPL_deg,MLT_deg,record_date FROM sac_tekfaz WHERE sac_tekfaz.id = '%s'" % (id,)
        data = self.fetchone(query)
        return data
    def delete_sac_tekfaz(self,value):
        query = "DELETE FROM sac_tekfaz WHERE id='%s'" % (value,)
        data = self.commit_db(query)
        return data
    def update_sac_tekfaz(self,value):
        query = "UPDATE  sac_tekfaz SET sac_olcu='%s',a_deg='%s',b_deg='%s',c_deg='%s',d_deg='%s',e_deg='%s',f_deg='%s',h_deg='%s',i_deg='%s',k1_deg='%s',k2_deg='%s',ag1_deg='%s',ag2_deg='%s',Ac_deg='%s',Wa_deg='%s',Ap_deg='%s',Kg_deg='%s',At_deg='%s',MPL_deg='%s',MLT_deg='%s'"\
                "WHERE id='%s'" % (value)
        data = self.commit_db(query)
        return data
    def showall_sac_tekfaz(self):
        query = "SELECT id,sac_olcu,a_deg,b_deg,c_deg,d_deg,e_deg,f_deg,h_deg,i_deg,k1_deg,k2_deg,ag1_deg,ag2_deg,Ac_deg,Wa_deg,Ap_deg,Kg_deg,At_deg,MPL_deg,MLT_deg,record_date  FROM sac_tekfaz "
        data = self.fetchall(query)
        return data
    def showfiltersac_tekfaz(self, filter_value, index=0):
        if index == 0:
            criteria = "sac_tekfaz.sac_olcu"
        elif index == 1: criteria ="sac_tekfaz.a_deg"
        elif index == 2:  criteria = "sac_tekfaz.b_deg"

        else:
            criteria = ""

        query = "SELECT *  FROM sac_tekfaz  WHERE {} LIKE {}%) LIMIT 1 ".format(criteria, filter_value)
        data = self.fetchall(query)
        return data
    def show_nearest_value_tekfaz(self, filter_value):
        query = "SELECT *  FROM sac_tekfaz  WHERE sac_tekfaz.sac_olcu ORDER BY ABS(sac_tekfaz.sac_olcu - {}) LIMIT 1 ".format( filter_value)
        data = self.fetchall(query)
        return data
    def show_nearest_MPLvalue_tekfaz(self, filter_value):
        query = "SELECT *  FROM sac_tekfaz  WHERE sac_tekfaz.At_deg ORDER BY ABS(sac_tekfaz.At_deg - {}) LIMIT 1 ".format( filter_value)
        data = self.fetchall(query)
        return data
    # sac_trifaz secimi   
    def check_sac_trifaz(self,values):
        query = "SELECT id,sac_olcu,a_deg,b_deg,c_deg,d_deg,e_deg,f_deg,h_deg,i_deg,k1_deg,k2_deg,ag1_deg,ag2_deg,Ac_deg,Wa_deg,Ap_deg,Kg_deg,At_deg,MPL_deg,MLT_deg FROM sac_trifaz WHERE sac_olcu='%s'" % values
        data = self.fetchone(query)
        return data
    def insert_sac_trifaz(self,values):
        query = "INSERT INTO sac_trifaz (sac_olcu,a_deg,b_deg,c_deg,d_deg,e_deg,f_deg,h_deg,i_deg,k1_deg,k2_deg,ag1_deg,ag2_deg,Ac_deg,Wa_deg,Ap_deg,Kg_deg,At_deg,MPL_deg,MLT_deg ) VALUES ( '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % values
        data = self.commit_db(query)
        return data
    def calldata_with_id_sac_trifaz(self,id):
        query =  "SELECT id,sac_olcu,a_deg,b_deg,c_deg,d_deg,e_deg,f_deg,h_deg,i_deg,k1_deg,k2_deg,ag1_deg,ag2_deg,Ac_deg,Wa_deg,Ap_deg,Kg_deg,At_deg,MPL_deg,MLT_deg,record_date FROM sac_trifaz WHERE sac_trifaz.id = '%s'" % (id,)
        data = self.fetchone(query)
        return data
    def delete_sac_trifaz(self,value):
        query = "DELETE FROM sac_trifaz WHERE id='%s'" % (value,)
        data = self.commit_db(query)
        return data
    def update_sac_trifaz(self,value):
        query = "UPDATE  sac_trifaz SET sac_olcu='%s',a_deg='%s',b_deg='%s',c_deg='%s',d_deg='%s',e_deg='%s',f_deg='%s',h_deg='%s',i_deg='%s',k1_deg='%s',k2_deg='%s',ag1_deg='%s',ag2_deg='%s',Ac_deg='%s',Wa_deg='%s',Ap_deg='%s',Kg_deg='%s',At_deg='%s',MPL_deg='%s',MLT_deg='%s'"\
                "WHERE id='%s'" % (value)
        data = self.commit_db(query)
        return data
    def showall_sac_trifaz(self):
        query = "SELECT id,sac_olcu,a_deg,b_deg,c_deg,d_deg,e_deg,f_deg,h_deg,i_deg,k1_deg,k2_deg,ag1_deg,ag2_deg,Ac_deg,Wa_deg,Ap_deg,Kg_deg,At_deg,MPL_deg,MLT_deg,record_date  FROM sac_trifaz "
        data = self.fetchall(query)
        return data
    def showfiltersac_trifaz(self, filter_value, index=0):
        if index == 0:
            criteria = "sac_trifaz.sac_olcu"
        elif index == 1: criteria ="sac_trifaz.a_deg"
        elif index == 2:  criteria = "sac_trifaz.b_deg"

        else:
            criteria = ""

        query = "SELECT *  FROM sac_trifaz  WHERE {} LIKE {}%) LIMIT 1 ".format(criteria, filter_value)
        data = self.fetchall(query)
        return data
    def show_nearest_value_trifaz(self, filter_value):
        query = "SELECT *  FROM sac_trifaz  WHERE sac_trifaz.sac_olcu ORDER BY ABS(sac_trifaz.sac_olcu - {}) LIMIT 1 ".format( filter_value)
        data = self.fetchall(query)
        return data
    def show_nearest_MPLvalue_trifaz(self, filter_value):
        query = "SELECT *  FROM sac_trifaz  WHERE sac_trifaz.Ap_deg ORDER BY ABS(sac_trifaz.Ap_deg - {}) LIMIT 1 ".format( filter_value)
        data = self.fetchall(query)
        return data