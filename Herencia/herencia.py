class Producto:
    def __init__(self,referencia,nombre,pvp,descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion

    def __str__(self):   #para q me sirve este str
        return f"REFERENCIA\t {self.referencia}\n" \
               f"NOMBRE\t\t {self.nombre}\n" \
               f"PVP\t\t {self.pvp}\n" \
               f"DESCRIPCIÓN\t {self.descripcion}\n"

class Alimento(Producto):
    productor = ""
    distribuidor = ""

    def __str__(self):
        return f"REFERENCIA\t {self.referencia}\n" \
               f"NOMBRE\t\t {self.nombre}\n" \
               f"PVP\t\t {self.pvp}\n" \
               f"DESCRIPCIÓN\t {self.descripcion}\n" \
               f"PRODUCTOR\t\t {self.productor}\n" \
               f"DISTRIBUIDOR\t\t {self.distribuidor}\n"
               
               
class Libro(Producto):
    isbn = ""
    autor = ""

    def __str__(self):
        return f"REFERENCIA\t {self.referencia}\n" \
               f"NOMBRE\t\t {self.nombre}\n" \
               f"PVP\t\t {self.pvp}\n" \
               f"DESCRIPCIÓN\t {self.descripcion}\n" \
               f"ISBN\t\t {self.isbn}\n" \
               f"AUTOR\t\t {self.autor}\n"


alimento = Alimento(2035, "Botella de Aceite de Oliva", 5, "250 ML")
alimento.productor = "La Aceitera"
alimento.distribuidor = "Distribuciones SA"

libro = Libro(2036, "Cocina Mediterránea",9, "Recetas sanas y buenas")
libro.isbn = "0-123456-78-9"
libro.autor = "Doña Juana"


productos = [alimento]
productos.append(libro)

for produc in productos:
    print(produc, "\n")    #llamo a las 3 filas de cada uno y por eso me printea


###INSISTANCE(printea aquellos atributos q tiene)

for producto in productos:

    if( isinstance(producto, Alimento) ):
        print(producto.referencia, producto.nombre, producto.productor)
    elif( isinstance(producto, Libro) ):
        print(producto.referencia, producto.nombre, producto.isbn)   

###POLIMORFISMO

def rebajar_producto(producto, rebaja):
    producto.pvp = producto.pvp - (producto.pvp/100 * rebaja)
rebajar_producto(alimento, 10)
print(alimento)   #printea todo pero el precio lo cambia

#herencia multiple

class A:
    def __init__(self):
        print("Soy de clase A")
    def a(self):
        print("Este método lo heredo de A")

class B:
    def __init__(self):
        print("Soy de clase B")
    def b(self):
        print("Este método lo heredo de B")

class C(A,B):
    def c(self):
        print("Este método es de C")
c = C()
c.a()
c.b()
c.c()

