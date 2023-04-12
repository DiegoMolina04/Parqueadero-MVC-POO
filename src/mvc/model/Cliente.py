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
        tiempoTranscurrido = horaSalida-horaLlegada
        valorCosto = 10
        valorPagar = round((tiempoTranscurrido.total_seconds()*valorCosto),3)

        return valorPagar

    def conducir(self):
        pass

# dt = datetime.now()
# now = dt.strftime('%H:%M:%S')