from datetime import datetime
from model.Persona import Persona

class Cliente(Persona):
    
    arrayClientes = []

    def __init__(self, hora:datetime, cedulaCliente: int, nombreCliente: str):
        super().__init__(cedulaCliente, nombreCliente)
        self.hora = hora
        Cliente.arrayClientes.append([self.cedula, self.nombre, self.hora])

    def realizarPago(horaLlegada:datetime):
        
        horaSalida = datetime.now()
        horaSalida = horaSalida.strftime('%Y-%m-%d %I:%M:%S') #Se toma la hora y se le da un formato en especifico como string
        
        horaLlegada = horaLlegada.replace('/', ' ') 
        horaLlegada = horaLlegada.replace('+', ':') #Se modifica los signos de la horaLLegada para ser legible como hora

        llegadaDt = datetime.strptime(horaLlegada, '%Y-%m-%d %I:%M:%S') #Se modifica hora llegada como tipo datetime
        salidaDt = datetime.strptime(horaSalida, '%Y-%m-%d %I:%M:%S') #Se modifica hora salida como tipo datetime

        tiempoTranscurrido = salidaDt-llegadaDt #Se saca la diferencia de tiempo
        valorCosto = 10
        
        valorPagar = round((tiempoTranscurrido.total_seconds()*valorCosto),3) #Se multiplica la diferencia de tiempo por valorCosto y redondea el valor a 3 decimales

        # locale.setlocale(locale.LC_MONETARY, 'es-CO') #Se indica cual es la moneda local -> Colombia
        # valorPagar = locale.currency(valorPagar) #Se da formato de moneda al valorPagar

        return valorPagar

    def conducir(self):
        pass