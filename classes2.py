class perro():
    def __init__(self):
        self.nombre = "pipo"
        self.color = "negro"
        self.raza = "border collie"
        self.vida =  100
        self.energia = 100

    def walk(self):
        print(f"{self.nombre} comienza a caminar")
        self.energia -= 5
        
    def run(self):
        print(f"{self.nombre} comienza a correr")
        self.energia -= 10

    def eat(self):
        print(f"{self.nombre} comienza a comer")
        if self.vida < 90:
            self.vida += 10

    def rage(self):
        print(f"{self.nombre} comienza a enojarse")
        self.energia -= 10

    def attack(self):
        print(f"{self.nombre} comienza a atacar")
        self.energia -= 10


dog = perro()


print(dog.energia)