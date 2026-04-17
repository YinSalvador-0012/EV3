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
        dia_hoy = int(input("Dime el numero del dia de hoy: "))
        meses = int(input("Dime el numero del mes en el que estas: "))

        total_hoy = meses * 30.4 + dia_hoy
        total_cumple = self.__mes_cumple * 30.4 + self.__dia_cumple

        if total_cumple < total_hoy:
            total_cumple += 360  

        faltan_dias = total_cumple - total_hoy
        opcion = input("¿Quieres saberlo en (dias), (semanas) o (meses)?: ").lower()

        if opcion == "dias":
            print(f"Faltan {round(faltan_dias)} días.")
        elif opcion == "semanas":
            print(f"Faltan {round(faltan_dias / 7)} semanas.")
        elif opcion == "meses":
            print(f"Faltan {round(faltan_dias / 30.4, 1)} meses.")
        else:
            print("Opción no válida.")