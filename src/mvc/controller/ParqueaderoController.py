from model.Parqueadero import Parqueadero
from model.Administrador import Administrador
from model.Cliente import Cliente
from model.Carro import Carro
from PyQt5 import QtWidgets, QtGui, uic
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime
#from controller.LoginController import LoginController
import os, sys

from time import sleep

actualPath = os.getcwd()+"/src/sources/QT Design/qrc"
sys.path.append(actualPath)
import imgs_qrc_rc

class ParqueaderoController():

    app = QtWidgets.QApplication([])
    actualPath = os.getcwd()+"/src/mvc/view/parqueadero.ui"
    parqueadero = uic.loadUi(actualPath)

    def iniciarParqueadero(self):
        
        ParqueaderoController.parqueadero.setWindowIcon(QtGui.QIcon(":/images/icon.png"))
        ParqueaderoController.parqueadero.buttonLimpiar.clicked.connect(ParqueaderoController.limpiarCamposLlegada)
        ParqueaderoController.parqueadero.buttonRegistrarLlegada.clicked.connect(ParqueaderoController.registrarLlegada)

        espaciosDisponibles = Parqueadero.obtenerEspacioDisponible()
        ParqueaderoController.parqueadero.comboEspacios.addItems(espaciosDisponibles)

        ParqueaderoController.parqueadero.buttonLimpiarCampo.clicked.connect(ParqueaderoController.limpiarCampoSalida)
        ParqueaderoController.parqueadero.buttonRegistrarSalida.clicked.connect(ParqueaderoController.registrarSalida)

        #ParqueaderoController.parqueadero.buttonSalir.clicked.connect(ParqueaderoController.terminarSesion)
        ParqueaderoController.parqueadero.buttonSalir.clicked.connect(ParqueaderoController.terminarSesion)

        ParqueaderoController.parqueadero.show()
        ParqueaderoController.app.exec()

    def limpiarCamposLlegada():
        ParqueaderoController.parqueadero.inputCedulaEntrada.setText("")
        ParqueaderoController.parqueadero.inputNombre.setText("")
        ParqueaderoController.parqueadero.inputPlaca.setText("")
        ParqueaderoController.parqueadero.inputMarca.setText("")
        ParqueaderoController.parqueadero.inputModelo.setText("")
        ParqueaderoController.parqueadero.inputColor.setText("")

    def limpiarCampoSalida():
        ParqueaderoController.parqueadero.inputCedulaSalida.setText("")
    
    def registrarLlegada(self):
        
        cedulaEntrada = ParqueaderoController.parqueadero.inputCedulaEntrada.text()
        nombre = ParqueaderoController.parqueadero.inputNombre.text()
        placa = ParqueaderoController.parqueadero.inputPlaca.text()
        marca = ParqueaderoController.parqueadero.inputMarca.text()
        modelo = ParqueaderoController.parqueadero.inputModelo.text()
        color = ParqueaderoController.parqueadero.inputColor.text()
        
        espacioSeleccionado = ParqueaderoController.parqueadero.comboEspacios.itemText(ParqueaderoController.parqueadero.comboEspacios.currentIndex())

        if len(cedulaEntrada and nombre and placa and marca and modelo and color):

            if espacioSeleccionado != "¡Parqueadero lleno!":

                try:
                    cedulaEntrada = int(cedulaEntrada)
                    horaLlegada = datetime.now()
                    #now = dt.strftime('%H:%M:%S')
                    nuevoCliente = Cliente(horaLlegada,cedulaEntrada,nombre)
                    nuevoCarro = Carro(nuevoCliente.cedula,placa,marca,modelo,color)

                    # sleep(10)
                    # ejemplo = datetime.now()
                    # now_2 = ejemplo.strftime('%H:%M:%S')

                    # resultado = (ejemplo-dt)

                    # print("La diferencia de hora es",resultado.total_seconds())

                    respuesta = Administrador.registrarLlegada(nuevoCliente.cedula,nuevoCliente.nombre,nuevoCarro.placa,nuevoCarro.marca,nuevoCarro.modelo,nuevoCarro.color,espacioSeleccionado,nuevoCliente.hora)

                    if respuesta == True:
                        mensaje = [f"Se a registrado llegada correctamente de {nuevoCliente.nombre}", QMessageBox.Information]
                        ParqueaderoController.limpiarCamposLlegada()
                        espaciosDisponibles = Parqueadero.obtenerEspacioDisponible()
                        ParqueaderoController.parqueadero.comboEspacios.clear()
                        ParqueaderoController.parqueadero.comboEspacios.addItems(espaciosDisponibles)
                    
                    else:
                        mensaje = [f"No se a podido registrar llegada de {nuevoCliente.nombre}", QMessageBox.Warning]

                except ValueError:
                    mensaje = ["El valor de cédula debe ser un número", QMessageBox.Warning]
            
            else:
                mensaje = ["El parqueadero esta lleno, no se puede registrar más llegadas", QMessageBox.Warning]

        else:
            mensaje = ["Complete todos los campos", QMessageBox.Warning]
            
        ParqueaderoController.generarCuadroDialogo(mensaje)

    def generarCuadroDialogo(respuesta):
        
        ventana = QMessageBox()
        ventana.setText(respuesta[0])
        ventana.setIcon(respuesta[1])
        ventana.setWindowIcon(QtGui.QIcon(":/images/icon.png"))
        ventana.setWindowTitle("Parqueadero")
        ventana.exec_()

    def registrarSalida():
        
        cedulaSalida = ParqueaderoController.parqueadero.inputCedulaSalida.text()

        if len(cedulaSalida):
            
            try:
                cedulaSalida = int(cedulaSalida)
                respuesta = Administrador.registrarSalida(cedulaSalida)
                
                if respuesta[0] == True:
                    
                    valorPagar = ParqueaderoController.calcularPago(respuesta[2])
                    
                    #Se borra información del array Clientes
                    iteradorCliente = 0
                    for datos in Cliente.arrayClientes:
                        if datos[0] == cedulaSalida:
                            Cliente.arrayClientes.pop(iteradorCliente)
                        
                        iteradorCliente = iteradorCliente+1

                    #Se borra información del array Carro
                    iteradorCarro = 0
                    
                    for datos in Carro.arrayCarro:
                        #print("Estos son los valores del array antes\n",datos)
                        if datos[0] == cedulaSalida:
                            mensaje = [f"Se retira el cliente {respuesta[1]} con el auto marca {datos[2]} {datos[3]}, color {datos[4]}, placa {datos[1]} y paga ${valorPagar}", QMessageBox.Information]
                            Carro.arrayCarro.pop(iteradorCarro)
                        
                        iteradorCarro = iteradorCarro+1
        
                    #mensaje = [f"Se retira el cliente {respuesta[1]}", QMessageBox.Information]
                    ParqueaderoController.limpiarCampoSalida()
                    espaciosDisponibles = Parqueadero.obtenerEspacioDisponible()
                    ParqueaderoController.parqueadero.comboEspacios.clear()
                    ParqueaderoController.parqueadero.comboEspacios.addItems(espaciosDisponibles)

                else:
                    mensaje = ["La cédula introducida no esta registrada", QMessageBox.Warning]

            except ValueError:
                mensaje = ["El valor de cédula debe ser un número", QMessageBox.Warning]

        else:
            mensaje = ["Debe completar el campo", QMessageBox.Warning]

        ParqueaderoController.generarCuadroDialogo(mensaje)

    def terminarSesion():

        ParqueaderoController.parqueadero.close()
        print("Entre al terminar sesion")
        Administrador.terminarSesion()


    def calcularPago(horaLlegada:datetime):
        
        # horaSalida = datetime.now()
        # tiempoTranscurrido = horaSalida-horaLlegada
        # valorCosto = 10
        # valorPagar = round((tiempoTranscurrido.total_seconds()*valorCosto),3)

        valorPagar = Cliente.realizarPago(horaLlegada)

        return valorPagar
