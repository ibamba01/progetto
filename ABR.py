class Abr:
    # costruttore
    def __init__(self, key=None):
        # imposto il valore del nodo o crea un nodo vuoto
        self.key = key
        self.parent = None
        # se non è vuoto imposto i figli come nodi vuoti
        if self.key:
            print("l'albero è stato creato con successo e {} è la sua radice".format(self.key))
            self.left = Abr()
            self.right = Abr()
            self.left.parent = self
            self.right.parent = self
        # se è vuoto non ha figli
        else:
            self.left = None
            self.right = None

    def isempty(self):
        return self.key is None

    def notempty(self):
        return self.key is not None

    # inserisci valore
    def insert(self, value):
        # controllo se è il nodo root o se il nodo attuale è vuoto
        if self.isempty():
            self.key = value
            # imposto i figli come nodi vuoti
            self.right = Abr()
            self.left = Abr()
            print("il valore: {} è stato inserito con successo".format(self.key))
        else:
            parent = self
            # controllo se il valore da inserire è < del nodo attuale
            if value < self.key:
                # è piu piccolo, inserisco a sinistra
                self.left.insert(value)
            else:
                # è più grande o uguale, inserisco a destra
                self.right.insert(value)
    # controllo se è vuoto
    # Attraversamento dell'albero

    def inorder(self):
        # controllo se il nodo è vuoto
        if self.isempty():
            return []  # termino e restituisco
        # esploro a sinistra fino a che non trovo un nodo vuoto
        else:
            return self.left.inorder() + [self.key] + self.right.inorder()


    def search(self, value):
        # controllo se il nodo è vuoto
        if self.isempty():
            print("{} non è presente nell'albero".format(value))
            return False
        # controllo se il valore è uguale al nodo attuale
        if self.key == value:
            print("{} è stato trovato".format(value))
            return True
        # controllo se il valore è minore del nodo attuale
        elif value < self.key:
            return self.left.search(value)
        # controllo se il valore è maggiore del nodo attuale
        else:
            return self.right.search(value)

    def minprint(self):
        # controllo se il nodo a sinistra è vuoto
        while not self.left.isempty():
            self = self.left
        print("il valore minimo è: {}".format(self.key))

    def min(self):
        # controllo se il nodo a sinistra è vuoto
        while not self.left.isempty():
            self = self.left
        return self

    def max(self):
        # controllo se il nodo a destra è vuoto
        while not self.right.isempty():
            self = self.right
        print("il valore massimo è: {}".format(self.key))

    def successor(value):
        if value.right.isempty():
            return None
        next = value.right
        while next is not None and next.left is not None:
            next = next.left
        return next

    def trasplant(self, u, v):
        if u.parent.isempty():
            self = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if  v.isnotempty():
            v.parent = u.parent

    def delete(self, value):
        root = self
        #trovo il nodo da eliminare
        while root.key != value:
            if root.isempty():  # il nodo non è presente
                print("il valore: {} non è presente nell'albero".format(value))
                return
            if value < root.key: # il valore è minore del nodo attuale cerco a sinistra
                root = root.left
            else:
                root = root.right # il valore è maggiore del nodo attuale cerco a destra
        # caso 1: il nodo da eliminare non ha figli o ha solo il figlio destro
        z = root
        if z.left.isempty():
            z.trasplant(z, z.right)
        # caso 2: il nodo da eliminare ha solo il figlio sinistro
        elif z.right.isempty():
             z.trasplant(z, z.left)
        # caso 3: il nodo da eliminare ha entrambi i figli
        else:
            y = z.right.min()
            if y.parent != value:
                z.trasplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            z.trasplant(z, y)
            y.left = z.left
            y.left.parent = y
        print("il valore: {} è stato eliminato con successo".format(value))
