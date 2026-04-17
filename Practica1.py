class Persona:
    def __init__(self,nombre,estatura,estudios, dia_cumpleanios,mes_cumpleanios):
        self.__nombre = nombre
        self.__estatura = estatura 
        self.__estudios = estudios
        self.__dia_cumpleanios = dia_cumpleanios
        self.__mes_cumpleanios = mes_cumpleanios

    def saludo(self):
        print(f"Hola, soy {self.__nombre}, mi estatura es: {self.__estatura} metros y tengo de Estudios {self.__estudios} ")

    