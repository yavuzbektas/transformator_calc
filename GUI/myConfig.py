import configparser,os
config = configparser.ConfigParser()
Local = "Yes"
def  read_config():

    config.read('MYPROJECT_CONF.ini')
    if Local == "Yes":
        config.set("PATHS", "BASE_PATH", os.getcwd())
    else:
        config.set("PATHS", "BASE_PATH", config.get("PATHS", "SERVER_DIR"))
    sections = config.sections()
    print(config.get("PATHS", "BASE_PATH"))
    return config

def write_config(sections,*arg,**kwargs):
    config = configparser.ConfigParser()
    with open('MYPROJECT_CONF.ini', 'w') as configfile:

        config.write(configfile)


