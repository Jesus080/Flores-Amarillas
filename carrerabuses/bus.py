class Bus:
    def __init__(self):
        self.posicion = 0
    @staticmethod
    def dibujar_inicio_pista():
        print("---------------------------------------------------------------------------------------------------------------------------")

    def dibujar_bus(self, desface, nombre):
        self.posicion += desface
        print("                                                                                                                           ") 
        print(" " * self.posicion + nombre)
        print(" " * self.posicion + "---------------")
        print(" " * self.posicion + "|__|__|__|__|__|__")
        print(" " * self.posicion + "|                 |)")
        print(" " * self.posicion + "|----@----------@-|")       

    @staticmethod
    def dibujar_final_pista():
        print("---------------------------------------------------------------------------------------------------------------------------")
    