from datetime import datetime
from Persona import Persona

class Cliente(Persona):
    
    def __init__(self, hora:datetime, cedulaCliente: int, nombreCliente: str):
        super().__init__(cedulaCliente, nombreCliente)
        self.hora = hora

    def realizarPago(self):
        pass

    def conducir(self):
        pass

# dt = datetime.now()
# now = dt.strftime('%H:%M:%S')