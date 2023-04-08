from controller.MainController import MainController
from controller.LoginController import LoginController

MainController.iniciarDatos()

loginController = LoginController()
loginController.iniciarLogin()