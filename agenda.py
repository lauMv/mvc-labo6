import shelve


class Agenda:

    def __init__(self, archivo='estante.db', wb=False):
        try:
            self.dic = shelve.open(archivo, writeback=wb)
        except: 
            self.dic = {}

    def __repr__(self):
        return repr(self.dic)

    def __getitem__(self, clave):
        return self.dic.get(clave, None)

    def __setitem__(self, clave, valor):
        self.dic[clave] = valor

    def __delitem__(self, clave):
        del self.dic[clave]

    def __iter__(self):
        return iter(self.dic.keys())


    def __del__(self):
        try:
            self.dic.close()
        except AttributeError:
            pass

    def keys(self):
        return list(self.dic.keys())

    def esarchivo(self):
        return isinstance(self.dic, shelve.DbfilenameShelf)

