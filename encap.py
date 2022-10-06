#sea como sea para acceder a esos datos se deberían 
# crear métodos públicos que hagan de interfaz. 
# En otros lenguajes les llamaríamos GETTERS y SETTERS y 
# es lo que da lugar a las PROPIEDADES, que no son más que atributos 
# protegidos con interfaces de acceso:
class Ejemplo:
    __atributo_privado = "Soy un atributo inalcanzable desde fuera."

    def __metodo_privado(self):
        print("Soy un método inalcanzable desde fuera.")

    def atributo_publico(self):
        return self.__atributo_privado

    def metodo_publico(self):
        return self.__metodo_privado()

e = Ejemplo()
print(e.atributo_publico())
e.metodo_publico() ##si no se hace asi no se vera nada pq los "print" estan encapsulados(por las 2 __)
