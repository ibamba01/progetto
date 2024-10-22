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
        if self.key:
            print("l'albero è stato creato con successo e {} è la sua radice".format(self.key))
            self.left = Abr(parent=self)
            self.right = Abr(parent=self)
        # se è vuoto non ha figli
        else:
            self.left = None
            self.right = None

    def isempty(self):
        return self.key is None

    def isroot(self):
        if self.root == self:
            return True
        else:
            return False

    def notempty(self):
        return self.key is not None

    def get_parent(self):
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
            print("il valore: {} è stato inserito con successo".format(self.key))
        else:
            padre = self
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
        current = self
        # controllo se il nodo a sinistra è vuoto
        while not current.left.isempty():
            current = current.left
        print("il valore minimo è: {}".format(current.key))


    def max(self):
        current = self
        # controllo se il nodo a destra è vuoto
        while not current.right.isempty():
            current = current.right
        print("il valore massimo è: {}".format(current.key))

    def min(self):
        current = self
        # controllo se il nodo a sinistra è vuoto
        while not current.left.isempty():
            current = current.left
        return current
    def minroot(root):
        x = root
        # controllo se il nodo a sinistra è vuoto
        while not x.left.isempty():
            x = x.left
        return x

    def successor(self):
        if self.right.isempty():
            return None
        next = self.right
        while not next.left.isempty():
            next = next.left
        return next

    def trasplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if  v.notempty():
            v.parent = u.parent

    def delete(self, value):
        current = self
        #trovo il nodo da eliminare
        while current.key != value:
            if current.isempty():  # il nodo non è presente
                print("il valore: {} non è presente nell'albero".format(value))
                return
            if value < current.key: # il valore è minore del nodo attuale cerco a sinistra
                current = current.left
            else:
                current = current.right # il valore è maggiore del nodo attuale cerco a destra
        z = current
        # Caso 1: il nodo da eliminare non ha figli o ha solo il figlio destro
        if z.left.isempty():
            self.trasplant(z, z.right)
        # Caso 2: il nodo da eliminare ha solo il figlio sinistro
        elif z.right.isempty():
             self.trasplant(z, z.left)
        # Caso 3: il nodo da eliminare ha entrambi i figli
        else:
            y = z.right.minroot()
            if y.parent != z:
                self.trasplant(y,y.right)
                y.right = z.right
                y.right.parent = y
            self.trasplant(z,y)
            y.left = z.left
            y.left.parent = y
        print("il valore: {} è stato eliminato con successo".format(value))

    def get_kesimo(root, k):
        stack = []
        current = root
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
                    print("il {}° nodo è: {}".format(k, current.key))
                    return current.key
                current = current.right
            else:
                break

        return None

    # calcola la deimensione dell'albero
    def size(root):
        size = 0
        stack = []
        current = root

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
        print("la dimensione dell'albero è: {}".format(size))
        return size

    def height(self):
        if (self.key is None):
            return 0
        else:
            return 1 + max(self.left.height(), self.right.height())