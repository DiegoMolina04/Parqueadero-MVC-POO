import numpy, string, pandas

class Parqueadero():

    arrayEspacios = {}

    def __init__(self, niveles:int, espaciosAparcar:int):
        self.espaciosAparcar = espaciosAparcar
        self.niveles = niveles
        #self.arrayEspacios = numpy.full((niveles,espaciosAparcar), fill_value= {})
        Parqueadero.arrayEspacios = numpy.full((niveles,espaciosAparcar), fill_value= {})
        
        #print("Este es el array\n",self.arrayEspacios)
        #print("Este es el array\n",Parqueadero.arrayEspacios)

        letrasNiveles = list(string.ascii_uppercase)

        for x in range(self.niveles):
            for y in range(self.espaciosAparcar):
                #self.arrayEspacios[x][y] = {"Disponibilidad":True, "Espacio":espaciosNiveles[x]+str(y+1), "Cédula":"","Nombre":"", "Placa":"", "Marca":"", "Modelo":"", "Color":""}
                Parqueadero.arrayEspacios[x][y] = {"Disponibilidad":True, "Espacio":letrasNiveles[x]+str(y+1), "Cédula":"","Nombre":"", "Placa":"", "Marca":"", "Modelo":"", "Color":"", "Hora_Llegada":""}

        #print("Este es el array\n",self.arrayEspacios)
        #print("Este es el array\n",Parqueadero.arrayEspacios)

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

        #Parqueadero.verificar(self)
        
    # def verificar(self):
    #     print("Los espacios son\n", self.arrayEspacios)
    #     self.arrayEspacios[1][1] = False
    #     self.arrayEspacios[1][2] = False
    #     print("Los espacios son\n", self.arrayEspacios)
