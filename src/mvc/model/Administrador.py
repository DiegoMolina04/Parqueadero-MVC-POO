from model.Persona import Persona
from model.Parqueadero import Parqueadero
from datetime import datetime
import pandas, os, sys
actualPath = os.getcwd()+"/src/sources/db"
sys.path.append(actualPath)

import dbConnection

class Administrador(Persona):

    arrayAdministradores = []
    query = dbConnection.connection()

    def __init__(self, correo:str, contraseña:str, cedulaAdministrador:int, nombreAdministrador:str):
        super().__init__(cedulaAdministrador, nombreAdministrador)
        self.correo = correo
        self.contraseña = contraseña

    def iniciarSesion(correo:str, contraseña:str):
        
        repuesta = [False, None]
        
        Administrador.query[1].execute("SELECT * FROM public.administrador ORDER BY id ASC ")

        administradores = Administrador.query[1].fetchall()

        if len(administradores):
            for persona in administradores:
            
                if correo == persona[1] and contraseña == persona[2]:

                    repuesta = [True, persona]
        
        return repuesta

    def registrarLlegada(cedulaEntrada:int,nombre:str,placa:str,marca:str,modelo:str,color:str,espacioSeleccionado:str,horaLlegada:datetime):
        
        hora = horaLlegada.strftime('%Y-%m-%d/%I+%M+%S')

        queryInsertar = """INSERT INTO public."parqueadero" (disponibilidad, espacio, cedula, nombre, placa, marca, modelo, color, hora_llegada, tamano_parqueadero) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        data = ('False', espacioSeleccionado, cedulaEntrada, nombre, placa, marca, modelo, color, hora, Parqueadero.idActual)
        Administrador.query[1].execute(queryInsertar, data)
        Administrador.query[0].commit()

        espaciosDisponibles = pandas.DataFrame(Parqueadero.arrayEspacios)

        for x in range(espaciosDisponibles.shape[0]):
            for y in range(espaciosDisponibles.shape[1]):
                
                if espaciosDisponibles[y][x].get('Espacio') == espacioSeleccionado:
                    
                    Parqueadero.arrayEspacios[x][y] = {"Disponibilidad":False, "Espacio":espacioSeleccionado, "Cédula":cedulaEntrada,"Nombre":nombre, "Placa":placa, "Marca":marca, "Modelo":modelo, "Color":color, "Hora_Llegada":hora}
                    
                    return True
        
        
        return False

    def registrarSalida(cedulaSalida:int):
        
        arrayRespuesta =[False, None, None]
        espaciosDisponibles = pandas.DataFrame(Parqueadero.arrayEspacios)

        for x in range(espaciosDisponibles.shape[0]):
            for y in range(espaciosDisponibles.shape[1]):
                
                if espaciosDisponibles[y][x].get('Cédula') == cedulaSalida:
                    
                    queryEliminar = """DELETE FROM public."parqueadero" WHERE cedula = %s"""
                    data = (cedulaSalida,)

                    Administrador.query[1].execute(queryEliminar, data)
                    Administrador.query[0].commit()

                    nombre = espaciosDisponibles[y][x].get('Nombre')
                    hora = espaciosDisponibles[y][x].get('Hora_Llegada')
                    espacio = espaciosDisponibles[y][x].get('Espacio')

                    Parqueadero.arrayEspacios[x][y] = {"Disponibilidad":True, "Espacio":espacio, "Cédula":"","Nombre":"", "Placa":"", "Marca":"", "Modelo":"", "Color":"", "Hora_Llegada":""}

                    arrayRespuesta = [True, nombre, hora]

                    return arrayRespuesta
        
        return arrayRespuesta

    def terminarSesion():

        sys.exit()