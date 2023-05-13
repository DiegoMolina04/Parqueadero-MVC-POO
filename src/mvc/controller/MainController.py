from model.Main import Main

class MainController():

    def iniciarDatos():

        tamañoParqueadero = [2,5] #Para cambiar espacio parqueadero, 2 -> Niveles, 5 -> Espacios (No mayor a 24 por las letras del alfabeto)
        Main.iniciarModelo(tamañoParqueadero)