from model.Carro import Carro
from model.Cliente import Cliente
from model.Parqueadero import Parqueadero
import os, sys

actualPath = os.getcwd()+"/src/sources/db"
sys.path.append(actualPath)

import dbConnection

class Main():

    query = dbConnection.connection()

    def iniciarModelo(tamañoParqueadero:list):
        
        Parqueadero.query[1].execute('SELECT * FROM public."parqueadero" ORDER BY id ASC')
        datos = Parqueadero.query[1].fetchall() #Se busca si hay algo registrado en la tabla parqueadero

        niveles = tamañoParqueadero[0]
        espacios = tamañoParqueadero[1]

        if len(datos): #Si hay algo registrado en la tabla parqueadero
            
            for dato in datos:
                cedula = dato[3]
                nombre = dato[4]
                placa = dato[5]
                marca = dato[6]
                modelo = dato[7]
                color = dato[8]
                horaLlegada = dato[9]

                Carro(cedula, placa, marca, modelo, color) #Se inicia todos los carros guardados en bd dentro de arrayCarro
                Cliente(horaLlegada, cedula, nombre) #Se inicia todos los clientes guardados en bd dentro de arrayClientes
            
            Parqueadero(niveles,espacios) #Se inicia el parqueadero

        else: #Si no hay nada registrado en la tabla parqueadero
            Parqueadero(niveles,espacios) #Se inicia unicamente el parqueadero
