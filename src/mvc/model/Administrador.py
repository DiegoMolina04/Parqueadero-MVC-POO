from Persona import Persona

class Administrador(Persona):

    def __init__(self, correo:str, contraseña:str, cedulaAdministrador:int, nombreAdministrador:str):
        super().__init__(cedulaAdministrador, nombreAdministrador)
        self.correo = correo
        self.contraseña = contraseña

    def iniciarSesion(self):
        print("El usuario", self.nombre, "contraseña", self.contraseña, "inicio sesión")

    def registrarLlegada(self):
        pass

    def registrarSalida(self):
        pass

    def terminarSesion(self):
        pass