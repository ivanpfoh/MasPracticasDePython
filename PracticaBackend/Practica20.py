class Libro:
    
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año
    
    def consulta(self):
        print("Libro: {} \nAutor: {} \nAño de publicacion: {}".format(self.titulo, self.autor, self.año))
        
    

libro1 = Libro("Analisis de sistemas", "Steve Jobs", 1978)
libro1.consulta()