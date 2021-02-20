
import configparser,os
config = configparser.ConfigParser()
import db_sql
def  read_config():

    config.read('MYPROJECT_CONF.ini')
    config.set("PATHS", "BASE_PATH", os.getcwd())
    sections = config.sections()

    return config

def write_config(sections,*arg,**kwargs):
    config = configparser.ConfigParser()
    with open('MYPROJECT_CONF.ini', 'w') as configfile:
        ...
        config.write(configfile)

config_file = read_config()


print(config_file.get("PATHS", "IMAGE_DIR"))
print(config_file.get("PATHS", "LOG_FILENAME"))
DB_NAME= config_file.get("PATHS", "DB_DIR") +"\\"+ config_file.get("DATABASE", "DB_NAME")
db=db_sql.mydb()