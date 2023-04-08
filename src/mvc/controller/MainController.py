from model.Administrador import Administrador

class MainController():

    def iniciarDatos():
        admin1 = Administrador("correo@correo","1234",123456798,"Marcos")
        admin2 = Administrador("gmail@correo","ejem",78945,"Viviana")
        print("Elementos inicializados")    