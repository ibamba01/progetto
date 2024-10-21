class Abr:

    # costruttore
    def __init__(self, key=None):
        # imposto il valore del nodo o crea un nodo vuoto
        self.key = key
        print("l'albero è stato creato con successo")
        # se non è vuoto imposto i figli come nodi vuoti
        if self.key:
            self.left = Abr()
            self.right = Abr()
        # se è vuoto non ha figli
        else:
            self.left = None
            self.right = None

    # inserisci valore
    def insert(self, value):
        # controllo se è il nodo root o se il nodo attuale è vuoto
        if self.isempty:
            self.key = value

            self.right = Abr()
            self.left = Abr()
            print("il valore: {} è stato inserito con successo".format(self.key))

        else:
            # controllo se il valore da inserire è < del nodo attuale
            if self.key < value:
                # è piu piccolo, inserisco a sinistra
                self.left.insert(value)
            else:
                # è più grande o uguale, inserisco a destra
                self.right.insert(value)

    # controllo se è vuoto
    def isempty(self):
        return (self.key == None)


a = Abr(6)
a.insert(5)
a.insert(4)
a.insert(7)
b = Abr(4)
c = Abr(8)
