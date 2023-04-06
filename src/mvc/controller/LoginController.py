from model.Administrador import Administrador

class LoginController():

    def controller(self, correo:str, contraseña:str):
        
        respuesta:bool = False

        if len(correo and contraseña):
            #respuesta = True
            respuesta = Administrador.iniciarSesion(correo,contraseña)
            #admin = Administrador()
            #admin.iniciarSesion(correo,contraseña)
            
        
        return respuesta
        
        #pass