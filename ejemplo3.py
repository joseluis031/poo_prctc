class Galleta:
    chocolate = False

    def chocolatear(self):
        chocolate = True

galleta = Galleta()
galleta.chocolatear()
print(galleta.chocolate)

class Galleta:#Da la sensación como os decía antes de que las instancias tienen que saber quienes son porque sino no 
                #pueden acceder sus atributos internos y por eso tienen que enviarse asimismas a los métodos.
                #Sea como sea con este ejemplo podemos entender que por defecto el valor de un atributo se busca en la clase, 
                #pero para modificarlo en la instancia es necesario hacer referencia al objeto.

    chocolate = False

    def chocolatear(self):
        self.chocolate = True

galleta = Galleta()
galleta.chocolatear()
print(galleta.chocolate)
