class Abr:
    # costruttore
    def __init__(self, key=None, parent=None):
        # imposto il valore del nodo o crea un nodo vuoto
        self.key = key
        self.parent = parent
        # imposta la radice
        if not parent: # se non ha un padre è la radice
            self.root = self
        else: # altrimenti la radice è la radice del padre
            self.root = parent.root
        # se non è vuoto imposto i figli come nodi vuoti
        self.left = None
        self.right = None

    # check
    def isempty(self):
        return self.key is None

    def isroot(self):
        if self.root == self:
            return True
        else:
            return False

    def notempty(self):
        return self.key is not None

    # printparent
    def printparent(self):
        if self.parent:
            print("Il nodo padre di {} è {}".format(self.key, self.parent.key))
        else:
            print("Questo nodo non ha un padre (è la radice)")

    # inserisci valore
    def insert(self, value):
        # controllo se è il nodo root o se il nodo attuale è vuoto
        if self.isempty():
            self.key = value
            # imposto i figli come nodi vuoti
            self.right = Abr(parent=self)
            self.left = Abr(parent=self)
            # print("il valore: {} è stato inserito con successo".format(self.key))
        else:
            # controllo se il valore da inserire è < del nodo attuale
            if value < self.key:
                # è piu piccolo, inserisco a sinistra
                self.left.insert(value)
            else:
                # è più grande o uguale, inserisco a destra
                self.right.insert(value)

    # Attraversamento dell'albero
    def inorder(self):
        # controllo se il nodo è vuoto
        if self.isempty():
            return []  # termino e restituisco
        # esploro a sinistra fino a che non trovo un nodo vuoto
        else:
            return self.left.inorder() + [self.key] + self.right.inorder()

    # ricerca
    def search(self, value):
        current = self.root
        # controllo se il nodo è vuoto
        if current.isempty():
            # print("{} non è presente nell'albero".format(value))
            return False
        # controllo se il valore è uguale al nodo attuale
        if current.key == value:
            # print("{} è stato trovato".format(value))
            return True
        # controllo se il valore è minore del nodo attuale
        elif value < current.key:
            return current.left.search(value)
        # controllo se il valore è maggiore del nodo attuale
        else:
            return current.right.search(value)

    # print del minimo
    def minprint(self):
        current = self
        # controllo se il nodo a sinistra è vuoto
        while not current.left.isempty():
            current = current.left
        print("il valore minimo è: {}".format(current.key))

    # il massimo del sottoalbero
    def maxprint(self):
        current = self
        # controllo se il nodo a destra è vuoto
        while not current.right.isempty():
            current = current.right
        print("il valore massimo è: {}".format(current.key))

    # il minimo del sottoalbero
    def min(self):
        current = self
        # controllo se il nodo a sinistra è vuoto
        while not current.left.isempty():
            current = current.left
        return current

    # il minimo dell'albero
    def minroot(self):
        x = self.root
        # controllo se il nodo a sinistra è vuoto
        while not x.left.isempty():
            x = x.left
        return x

    # successor
    def successor(self):
        if self.right.isempty():
            return None
        next = self.right
        while not next.left.isempty():
            next = next.left
        return next

    # trasplant
    def trasplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if  v.notempty():
            v.parent = u.parent

    # ritorna il k-esimo elemento più piccolo
    def kesimo(self, k):
        stack = []
        current = self.root
        count = 0
        while True:
            # scendo a sinistra fino a trovare un nodo vuoto e metto i nodi visitati nello stack
            if current.left is not None:
                stack.append(current)
                current = current.left
            # prendo il nodo in cima allo stack e lo visito
            elif stack:
                current = stack.pop()
                count += 1
                if count == k:
                    # print("il {}° nodo è: {}".format(k, current.key))
                    return current.key
                current = current.right
            else:
                break

    # calcola la deimensione dell'albero
    def size(self):
        size = 0
        stack = []
        current = self.root

        while True:
            if current.left is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                size += 1
                current = current.right
            else:
                break
        # print("la dimensione dell'albero è: {}".format(size))
        return size

    # indica l'altezza del sottoalbero
    def height(self):
        if (self.key is None):
            return 0
        else:
            return 1 + max(self.left.height(), self.right.height())