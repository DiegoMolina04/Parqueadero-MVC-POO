from model.Persona import Persona

class Administrador(Persona):

    arrayAdministradores = []

    def __init__(self, correo:str, contraseña:str, cedulaAdministrador:int, nombreAdministrador:str):
        super().__init__(cedulaAdministrador, nombreAdministrador)
        self.correo = correo
        self.contraseña = contraseña
        Administrador.arrayAdministradores.append([self.cedula, self.nombre, self.correo, self.contraseña])

    def iniciarSesion(correo, contraseña):
        
        repuesta = False
        
        for administradores in Administrador.arrayAdministradores:
            
            if correo == administradores[2] and contraseña == administradores[3]:

                repuesta = True
        
        return repuesta

    def registrarLlegada(self):
        pass

    def registrarSalida(self):
        pass

    def terminarSesion(self):
        pass