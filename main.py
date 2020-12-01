from contacto import Contacto
from agenda import Agenda
from vista import REPL
from vista import strip
from vista import salir


class Main:

    def __init__(self):
        self.comandos = {
            "agregar": self.agregar,
            "borrar": self.borrar,
            "mostrar": self.mostrar,
            "listar": self.listar,
            "salir": self.salir
        }
        archivo = "agenda.db"
        introduccion = strip(__doc__)
        self.contacto = Agenda(archivo)
        if not self.contacto.esarchivo():
            introduccion += '\nError: No se pudo abrir "{}"'.format(archivo)
        REPL(self.comandos, introduccion).ciclo()

    def agregar(self, nombre, telefono):
        self.contacto[nombre] = Contacto(nombre, telefono)

    def borrar(self, nombre):
        del self.contacto[nombre]

    def mostrar(self, nombre):
       return self.contacto[nombre]

    def listar(self):
        return (self.contacto[nombre]
                for nombre in sorted(self.contacto))

    def salir(self):
        salir()


if __name__ == "__main__":
    Main()