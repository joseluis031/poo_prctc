class Galleta:
    chocolate = False

    def __init__(self, sabor, color):
        self.sabor = sabor
        self.color = color
        print(f"Se acaba de crear una galleta {self.color} y {self.sabor}.")

galleta_1 = Galleta("marrón", "amarga")
galleta_2 = Galleta("blanca", "dulce")
#destructor
class Galleta:
    
    def __del__(self):
        print("La galleta se está borrando de la memoria")

galleta = Galleta()

del(galleta)


#Hay que tener en cuenta que este método debe devolver la cadena en lugar de mostrar 
# algo por pantalla, ese es el funcionamiento que se espera de él.

class Galleta:

    def __init__(self, sabor, color):
        self.sabor = sabor
        self.color = color

    def __str__(self):
       return f"Soy una galleta {self.color} y {self.sabor}."

galleta = Galleta("dulce", "blanca")

print(galleta)
print(str(galleta))
print(galleta.__str__())

