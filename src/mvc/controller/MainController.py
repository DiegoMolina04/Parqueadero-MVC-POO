from model.Administrador import Administrador

class MainController():

    def initElements():
        admin1 = Administrador("correo@corre","contrAA",123456798,"Marcos")
        admin2 = Administrador("gmail@correo","UNEJEMPLO",78945,"Viviana")
        print("Elementos inicializados")