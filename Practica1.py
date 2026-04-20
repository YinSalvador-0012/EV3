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

        mes_actual = 4
        dia_actual = 20

        total_hoy = mes_actual * 30.4 + dia_actual
        total_cumple = self.__mes_cumpleanios * 30.4 + self.__dia_cumpleanios

        if total_cumple < total_hoy:
            total_cumple += 360  

        faltan_dias = total_cumple - total_hoy
        print(f"Faltan {round(faltan_dias)} días que convertidos en semanas faltantes serian {round(faltan_dias / 7)} semanas aproximadamente para mi cumpleaños.")
        
        
    def info (self):
        self.saludo()
        self.calculadora_cumpleanios()

    def get_nombre(self):
        return self.__nombre
    
    def get_estatura(self):
        return self.__estatura
    
    def get_estudios(self):
        return self.__estudios
    
    def get_dia_cumpleanios(self):
        return self.__dia_cumpleanios

    def get_mes_cumpleanios(self):
        return self.__mes_cumpleanios
    
    def set_nombre(self,nombreNuevo):
        self.__nombre = nombreNuevo

    def set_estatura(self,estaturaNueva):
        self.__estatura = estaturaNueva
    
    def set_estudios(self,estudiosNuevos):
        self.__estudios = estudiosNuevos

    def set_dia_cumpleanios(self,dia_cumpleaniosNuevo):
        self.__dia_cumpleanios = dia_cumpleaniosNuevo

    def set_mes_cumpleanios(self,mes_cumpleaniosNuevo):
        self.__mes_cumpleanios = mes_cumpleaniosNuevo


#USO DE CLASE
objeto_persona = Persona("X", 1.59,"LIC",7,10)

objeto_persona.info()

