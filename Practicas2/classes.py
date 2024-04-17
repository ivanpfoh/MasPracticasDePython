class My_first_class:
    def __init__(self, numeroTel, codigoPostal, nombre, apellido, documento):
        self.numeroTel = numeroTel
        self.codigoPostal = codigoPostal
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento

yo = My_first_class(245678987, 8777, "ivan", "pfoh", 444444444)

print("Mi nombre es: ",yo.nombre, yo.apellido)
print("Mi numero de documento es: ", yo.documento)
print("Mi numero de telefono es: ", yo.numeroTel)

print(f"mi nombre es: {yo.nombre} {yo.apellido}")