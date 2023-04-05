from model.Administrador import Administrador

class LoginController():

    def controlador(self, correo:str, contraseña:str):

        #print("Entre al controlador")
        #ejemplo = Administrador("correo@corre","contrAA",123456798,"Marcos")
        #Administrador.iniciarSesion()
        if len(correo):
            print("El correo es", correo," y contraseña es",contraseña)
            Administrador.iniciarSesion()
        else:
            pass
        
        #pass