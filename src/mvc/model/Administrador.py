from model.Persona import Persona
from model.Parqueadero import Parqueadero
from datetime import datetime
#from controller.LoginController import LoginController
import pandas

class Administrador(Persona):

    arrayAdministradores = []

    def __init__(self, correo:str, contraseña:str, cedulaAdministrador:int, nombreAdministrador:str):
        super().__init__(cedulaAdministrador, nombreAdministrador)
        self.correo = correo
        self.contraseña = contraseña
        Administrador.arrayAdministradores.append([self.cedula, self.nombre, self.correo, self.contraseña])

    def iniciarSesion(correo:str, contraseña:str):
        
        repuesta = [False, None]
        
        for administradores in Administrador.arrayAdministradores:
            
            if correo == administradores[2] and contraseña == administradores[3]:

                repuesta = [True, administradores]
        
        return repuesta

    def registrarLlegada(cedulaEntrada:int,nombre:str,placa:str,marca:str,modelo:str,color:str,espacioSeleccionado:str,horaLlegada:datetime):

        espaciosDisponibles = pandas.DataFrame(Parqueadero.arrayEspacios)

        for x in range(espaciosDisponibles.shape[0]):
            for y in range(espaciosDisponibles.shape[1]):
                
                if espaciosDisponibles[y][x].get('Espacio') == espacioSeleccionado:
                    #print("Este es el array de datos",espaciosDisponibles[y][x])
                    Parqueadero.arrayEspacios[x][y] = {"Disponibilidad":False, "Espacio":espacioSeleccionado, "Cédula":cedulaEntrada,"Nombre":nombre, "Placa":placa, "Marca":marca, "Modelo":modelo, "Color":color, "Hora_Llegada":horaLlegada}
                    print("Este es el array actualizado\n",Parqueadero.arrayEspacios)
                    return True
        
        
        return False
        #return arrayRespuesta
        
        #Parqueadero.actualizarEspacio()       

    def registrarSalida(cedulaSalida:int):
        
        arrayRespuesta =[False, None, None]
        espaciosDisponibles = pandas.DataFrame(Parqueadero.arrayEspacios)

        for x in range(espaciosDisponibles.shape[0]):
            for y in range(espaciosDisponibles.shape[1]):
                
                if espaciosDisponibles[y][x].get('Cédula') == cedulaSalida:

                    nombre = espaciosDisponibles[y][x].get('Nombre')
                    hora = espaciosDisponibles[y][x].get('Hora_Llegada')
                    espacio = espaciosDisponibles[y][x].get('Espacio')

                    Parqueadero.arrayEspacios[x][y] = {"Disponibilidad":True, "Espacio":espacio, "Cédula":"","Nombre":"", "Placa":"", "Marca":"", "Modelo":"", "Color":"", "Hora_Llegada":""}

                    arrayRespuesta = [True, nombre, hora]
                    print("Este es el array salida\n",Parqueadero.arrayEspacios)
                    return arrayRespuesta
        
        return arrayRespuesta

    def terminarSesion():
        from controller.LoginController import LoginController
        loginController = LoginController()
        loginController.iniciarLogin()