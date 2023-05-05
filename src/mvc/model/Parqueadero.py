import numpy, string, pandas, os, sys
actualPath = os.getcwd()+"/src/sources/db"
sys.path.append(actualPath)

import dbConnection

class Parqueadero():

    arrayEspacios = {}
    query = dbConnection.connection()
    idActual = None

    def __init__(self, niveles:int, espaciosAparcar:int):
        self.espaciosAparcar = espaciosAparcar
        self.niveles = niveles
        #self.arrayEspacios = numpy.full((niveles,espaciosAparcar), fill_value= {})
        Parqueadero.arrayEspacios = numpy.full((niveles,espaciosAparcar), fill_value= {})
        
        #print("Este es el array\n",self.arrayEspacios)
        #print("Este es el array\n",Parqueadero.arrayEspacios)

        
        Parqueadero.query[1].execute('SELECT * FROM public."tamano_parqueadero" ORDER BY id ASC')
        
        tamañoParqueadero = Parqueadero.query[1].fetchall() #Se busca si hay algo registrado en la tabla tamano_parqueadero

        #Parqueadero.query.close()

        if len(tamañoParqueadero): #Si hay algo en la tabla tamano_parqueadero

            print("Hay algo en parqueadero")

            registroEncontrado = False

            for espacioGuardado in tamañoParqueadero: #Se busca si dentro de la tabla tamano_parqueadero estan los datos con los que se inicializa el parqueadero

                if espacioGuardado[1] == self.niveles and espacioGuardado[2] == self.espaciosAparcar: #Se busca guardado el mismo tamaño ingresado
                    
                    Parqueadero.idActual = espacioGuardado[0]
                    print("Se encontro",espacioGuardado[1],espacioGuardado[2])
                    registroEncontrado = True

            if (registroEncontrado): #Si se encuentra el mismo valor dentro de la tabla tamano_parqueadero
                
                Parqueadero.query[1].execute(f'SELECT * FROM public.parqueadero WHERE tamano_parqueadero = {Parqueadero.idActual}')
                espaciosOcupados = Parqueadero.query[1].fetchall() #Se verifica la tabla parqueadero buscando esos mismos valores
                
                if len(espaciosOcupados): #Si se encuentran valores, se inicia el parqueadero con los espacios ocupados
                    #puestosOcupados = []
                    print("Estos son los puestos ocupados",espaciosOcupados)
                    # for espacio in espaciosOcupados:
                    #     puestosOcupados.append(espacio[2])

                    Parqueadero.iniciarParqueadero(self.niveles,self.espaciosAparcar, espaciosOcupados) #Se identifica que si hay espacios guardados, se pasa a comprobar si hay algun carro parqueado

                else: #Si no se encuentran valores, se inicia el parqueadero vacio.
                    
                    Parqueadero.idActual = Parqueadero.consultarID(self.niveles,self.espaciosAparcar)
                    Parqueadero.iniciarParqueaderoVacio(self.niveles,self.espaciosAparcar) #Se inicia el parqueadero con disponibilidad en todos
            
            else: #Si no se encuentra el mismo valor, se guardan los nuevos valores en la tabla tamano_parqueadero y se inicia el parqueadero vacio
                
                Parqueadero.insertarEspacioNuevo(self.niveles,self.espaciosAparcar)
                Parqueadero.idActual = Parqueadero.consultarID(self.niveles,self.espaciosAparcar)
                Parqueadero.iniciarParqueaderoVacio(self.niveles,self.espaciosAparcar) #Se identifica que no hay espacios guardados, se inicia el parqueadero con disponibilidad en todos
        
        else: #Si no, se guardan los nuevos valores en la tabla tamano_parqueadero y se inicia el parqueadero vacio
            print("Parqueadero vacio")
            Parqueadero.insertarEspacioNuevo(self.niveles,self.espaciosAparcar)
            Parqueadero.idActual = Parqueadero.consultarID(self.niveles,self.espaciosAparcar)
            Parqueadero.iniciarParqueaderoVacio(self.niveles,self.espaciosAparcar) #Se identifica que no hay espacios guardados, se inicia el parqueadero con disponibilidad en todos
            
        # letrasNiveles = list(string.ascii_uppercase)

        # for x in range(self.niveles):
        #     for y in range(self.espaciosAparcar):

        #         Parqueadero.arrayEspacios[x][y] = {"Disponibilidad":True, "Espacio":letrasNiveles[x]+str(y+1), "Cédula":"","Nombre":"", "Placa":"", "Marca":"", "Modelo":"", "Color":"", "Hora_Llegada":""}


    def iniciarParqueaderoVacio(niveles:int, espaciosAparcar:int):
        
        letrasNiveles = list(string.ascii_uppercase)

        for x in range(niveles):
            for y in range(espaciosAparcar):

                Parqueadero.arrayEspacios[x][y] = {"Disponibilidad":True, "Espacio":letrasNiveles[x]+str(y+1), "Cédula":"","Nombre":"", "Placa":"", "Marca":"", "Modelo":"", "Color":"", "Hora_Llegada":""}

    def iniciarParqueadero(niveles:int, espaciosAparcar:int, datosCliente:list):
        
        letrasNiveles = list(string.ascii_uppercase)

        for x in range(niveles):
            for y in range(espaciosAparcar):

                for espacio in datosCliente:
                    letra = letrasNiveles[x]+str(y+1)
                    if espacio[2] == letra: #Si se encuentra la letra, se coloca la disponibilidad en False y se rompe el ciclo para no sobre escribir
                        Parqueadero.arrayEspacios[x][y] = {"Disponibilidad":False, "Espacio":letra, "Cédula":espacio[3],"Nombre":espacio[4], "Placa":espacio[5], "Marca":espacio[6], "Modelo":espacio[7], "Color":espacio[8], "Hora_Llegada":espacio[9]}
                        break
                    else:
                        Parqueadero.arrayEspacios[x][y] = {"Disponibilidad":True, "Espacio":letra, "Cédula":"","Nombre":"", "Placa":"", "Marca":"", "Modelo":"", "Color":"", "Hora_Llegada":""}

    def obtenerEspacioDisponible():
        
        arrayRespuesta = []
        espaciosDisponibles = pandas.DataFrame(Parqueadero.arrayEspacios)

        for x in range(espaciosDisponibles.shape[0]):
            for y in range(espaciosDisponibles.shape[1]):
                
                if espaciosDisponibles[y][x].get('Disponibilidad') == True:
                    arrayRespuesta.append(espaciosDisponibles[y][x].get('Espacio'))
                
        if len(arrayRespuesta) == 0:
            arrayRespuesta = ["¡Parqueadero lleno!"]
        
        return arrayRespuesta
    
    def insertarEspacioNuevo(niveles:int, espaciosAparcar:int):
        Parqueadero.query[1].execute(f'INSERT INTO public."tamano_parqueadero" (niveles, espacios_aparcar) VALUES ({niveles}, {espaciosAparcar})')
        Parqueadero.query[0].commit()

    def consultarID(niveles:int, espaciosAparcar:int):
        Parqueadero.query[1].execute(f'SELECT * FROM public."tamano_parqueadero" WHERE niveles = {niveles} AND espacios_aparcar = {espaciosAparcar}')
        id = Parqueadero.query[1].fetchall()
        return id[0]
    # def verificar(self):
    #     print("Los espacios son\n", self.arrayEspacios)
    #     self.arrayEspacios[1][1] = False
    #     self.arrayEspacios[1][2] = False
    #     print("Los espacios son\n", self.arrayEspacios)
