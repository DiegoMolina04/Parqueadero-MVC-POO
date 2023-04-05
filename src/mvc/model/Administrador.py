from model.Persona import Persona

class Administrador(Persona):

    arrayAdministradores = []

    def __init__(self, correo:str, contraseña:str, cedulaAdministrador:int, nombreAdministrador:str):
        super().__init__(cedulaAdministrador, nombreAdministrador)
        self.correo = correo
        self.contraseña = contraseña
        Administrador.arrayAdministradores.append([self.cedula, self.nombre, self.correo, self.contraseña])

    def iniciarSesion():
        #print("El usuario", self.nombre, "contraseña", self.contraseña, "inicio sesión")
        print(Administrador.arrayAdministradores)

    def registrarLlegada(self):
        pass

    def registrarSalida(self):
        pass

    def terminarSesion(self):
        pass