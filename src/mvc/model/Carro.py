class Carro():
    
    arrayCarro = []

    def __init__(self, cedulaDueño:int, placa:str, marca:str, modelo:str, color:str):
        self.cedulaDueño = cedulaDueño
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.color = color
        Carro.arrayCarro.append([self.cedulaDueño, self.placa, self.marca, self.modelo, self.color])

    def arrancar():
        pass

    def estacionar():
        pass