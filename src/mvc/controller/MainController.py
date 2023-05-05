from model.Main import Main

class MainController():

    def iniciarDatos():
        #admin1 = Administrador("correo@correo","1234",123456798,"Marcos")
        #admin2 = Administrador("a","a",78945,"Viviana")
        #Parqueadero(2, 5)
        tamañoParqueadero = [2,5]
        Main.iniciarModelo(tamañoParqueadero)