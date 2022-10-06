class Galleta:
    pass

galleta = Galleta()
galleta.sabor = "salado"
galleta.color = "marrón"

print(f"El sabor de esta galleta es {galleta.sabor} "
      f"y el color {galleta.color}") #sin la f no me lee el sabor

class Galleta:
    chocolate = False #atributo de clase

Galleta.chocolate = True

galleta = Galleta()

if galleta.chocolate:
    print("La galleta tiene chocolate")
else:
    print("La galleta no tiene chocolate")


