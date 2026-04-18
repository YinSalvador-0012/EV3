class Persona:
    def __init__(self,nombre,estatura,estudios, dia_cumpleanios,mes_cumpleanios):
        self.__nombre = nombre
        self.__estatura = estatura 
        self.__estudios = estudios
        self.__dia_cumpleanios = dia_cumpleanios
        self.__mes_cumpleanios = mes_cumpleanios

    def saludo(self):
        print(f"Hola, soy {self.__nombre}, mi estatura es: {self.__estatura} metros y tengo de Estudios {self.__estudios} ")

    def calculadora_cumpleanios (self):

        meses = 4
        dia_hoy = 17

        total_hoy = meses * 30.4 + dia_hoy
        total_cumple = self.__mes_cumpleanios * 30.4 + self.__dia_cumpleanios

        if total_cumple < total_hoy:
            total_cumple += 360  

        faltan_dias = total_cumple - total_hoy
        opcion = 1

        if opcion == 1:
            print(f"Faltan {round(faltan_dias)} días.")
        else:
             print(f"Faltan {round(faltan_dias / 7)} semanas.")


    def info (self):
        self.saludo()
        print("")
        self.calculadora_cumpleanios()