import sys
from traceback import format_exc
from collections.abc import Iterable
try:
    from readline import set_completer
    from readline import parse_and_bind
except ImportError:
    pass


def out(cadena="", final="\n"):
    sys.stdout.write(str(cadena) + final)
    sys.stdout.flush()


def strip(cadena):
    if cadena:
        return "\n".join(linea.strip()
                         for linea in cadena.split('\n') if linea).strip()
    else:
        return cadena


def esiterable(objeto):
    return isinstance(objeto, Iterable) and not isinstance(objeto, str)


def iterable(objeto):
    return iter([objeto]) if not esiterable(objeto) else objeto


def salir(estado=0):
    out()
    sys.exit(estado)


class REPL:

    def __init__(self, comandos, introduccion="Bienvenido", indicador="> "):
        self.comandos = comandos
        self.introduccion = introduccion
        self.indicador = indicador
        

    def ciclo(self):
        print (" agregar \n borrar nombre \n mostrar \n listar \n salir \n")
        while True:
            try:
                comando, *parametros = input(self.indicador).split()
                salida = self.comandos[comando](*parametros)
                if salida:
                    for linea in iterable(salida):
                        out(linea)
            except ValueError:
                pass
            except (KeyboardInterrupt, EOFError):
                salir()
            except KeyError:
                out("{}: Comando desconocido.".format(comando))
            except TypeError:
                out(strip(self.comandos[comando].__doc__))
            except Exception as excepcion:
                out("Error inesperado:\n" +
                    str(type(excepcion)) + str(excepcion) + "\n" +
                    format_exc().strip())
