#User.py

class User:
    seq = 0
    obj= []

    def _init_(self, nome, idade):
        sel.id = None
        self.nome = None
        self.idade = None

    def save(self):
        self._class_.seq += 1
        self.id = self._class_.seq
        self._class_.obj.append(self)

    def _str_(self):
        return self.nome

    def __repr__(self):
        return '<{}: {} - {} - {}>\n'.format(self.__class__.__name__, self.id, self.nome, self.idade)

    @classmethod
    def all(cls):
        return cls.obj


