class circulo:
    def __init__(self, radio):
        self.radio = radio
        self.pi = 3.1416
        self.diametro = 0
        self.area1 = 0
        self.circunferencia1 = 0
    def area(self):
        self.area1 = (self.pi*(self.radio**2))
    
    def circunferencia(self):
        self.circunferencia1 = (self.pi*(2*self.radio))

circulo1 = circulo(6)
circulo1.area()
print(circulo1.area1)