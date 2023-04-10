from model.Administrador import Administrador
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets, QtGui, uic
import os, sys
actualPath = os.getcwd()+"/src/sources/QT Design/qrc"
sys.path.append(actualPath)
import imgs_qrc_rc

class LoginController():

    app = QtWidgets.QApplication([])
    actualPath = os.getcwd()+"/src/mvc/view/login.ui"
    login = uic.loadUi(actualPath)

    def iniciarLogin(self):

        LoginController.login.buttonEnviar.clicked.connect(LoginController.generarCuadroDialogo)
        LoginController.login.show()
        LoginController.app.exec()

    def generarCuadroDialogo(self):

        correo = LoginController.login.inputCorreo.text()
        contraseña = LoginController.login.inputContrasena.text()
        respuesta = LoginController.verificarDatos(correo, contraseña)
        
        ventana = QMessageBox()
        ventana.setText(respuesta[1])
        ventana.setIcon(respuesta[2])
        ventana.setWindowIcon(QtGui.QIcon(":/images/icon.png"))
        ventana.setWindowTitle("Parqueadero")
        ventana.exec_()

        if respuesta[0] == True:
            LoginController.cerrarLogin()

    def verificarDatos(correo:str, contraseña:str):
        
        respuesta = [False, ""]
        mensaje = []

        if len(correo and contraseña):

            respuesta = Administrador.iniciarSesion(correo,contraseña)

        if respuesta[0] != False and respuesta[1] != None:
            
            mensaje = [True, f"¡Bienvenido al sistema {respuesta[1][1]}!", QMessageBox.Information]

        elif respuesta[0] == False and respuesta[1] == "":

            mensaje = [False, "Complete todos los campos", QMessageBox.Warning]

        else:

            mensaje = [False, "Verifique los datos ingresados", QMessageBox.Warning]

        return mensaje

    def cerrarLogin():
        LoginController.login.close()
