import configparser,os,sys
config = configparser.ConfigParser()
Local = "No"

def  read_config():
    try:
        config.read("MYPROJECT_CONF.ini")
    except Exception as err:
        print(err) 
  
    if Local == "Yes":
           
        config.set("PATHS", "BASE_PATH", os.getcwd())
   
    else:
        config.set("PATHS", "BASE_PATH", config.get("PATHS", "SERVER_DIR"))
           
            #config.read('O:\\ODEV\\Ybektas\\trafo\\MYPROJECT_CONF.ini')
       
        
    sections = config.sections()
    
    print(config.get("PATHS", "BASE_PATH"))
    return config

def write_config(config,sections,serverpath,*arg,**kwargs):
    
    if Local == "Yes":
        with open('MYPROJECT_CONF.ini', 'w') as configfile:

            config.write(configfile)
    else:
        with open(serverpath + "\\"+ "MYPROJECT_CONF.ini", 'w') as configfile:

            config.write(configfile)





