class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    # check fun
    def isempty(self):
        return self.key is None

    def notempty(self):
        return self.key is not None

    def isroot(self):
        return self.parent is None

    def isleaf(self):
        return self.left is None and self.right is None

    #getter fun
    def getkey(self):
        return self.key

    def getfather(self):
        return self.parent

    # node fun

    # printparent node
    def printparent(self):
        if self.parent:
            print("Il nodo padre di {} è {}".format(self.key, self.parent.key))
        else:
            print("Questo nodo non ha un padre (è la radice)")

    # attraversamento del sottoalbero
    def inorder(self):
        # controllo se il nodo è vuoto
        if self.isempty():
            return []  # termino e restituisco
        # esploro a sinistra fino a che non trovo un nodo vuoto
        else:
            return self.left.inorder() + [self.key] + self.right.inorder()

    # ricerca nel sottoalbero
    def search(self, value):
        # controllo se il nodo è vuoto
        if self.isempty():
            # print("{} non è presente nell'albero".format(value))
            return False
        # controllo se il valore è uguale al nodo attuale
        if self.key == value:
            # print("{} è stato trovato".format(value))
            return True
        # controllo se il valore è minore del nodo attuale
        elif value < self.key:
            return self.left.search(value)
        # controllo se il valore è maggiore del nodo attuale
        else:
            return self.right.search(value)

    # minimo del sottoalbero
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

    # successor
    def successor(self):
        if self.right.isempty():
            return None
        next = self.right
        while not next.left.isempty():
            next = next.left
        return next

class Abr:
    # costruttore
    def __init__(self):
        self.root = None

    def insert(self, val):
        # set up
        current = self.root # parto dalla radice
        predecessor = None # inizia vuoto
        newnode = Node(val)
        # trova la posizione in cui posizionarlo
        while current is not None:
            predecessor = current
            if newnode.key < current.key:
                current = current.left
            else:
                current = current.right
        # imposta il padre
        newnode.parent = predecessor
        if predecessor is None: # caso radice
            self.root = newnode
        elif newnode.key < predecessor.key: # figlio sinistro
            predecessor.left = newnode
        else: # figlio destro
            predecessor.right = newnode

    # ritorna il k-esimo elemento più piccolo
    def kesimo(self, k):
        stack = []
        current = self.root
        count = 0
        while True:
            # scendo a sinistra fino a trovare un nodo vuoto e metto i nodi visitati nello stack
            if current is not None:
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

        # attraversaento

    def treetraversal(self):
        cur = self.root
        cur.inorder()

        # ricerca

    def search(self, value):
        cur = self.root
        cur.search(value)

        # print del minimo

    def treeminprint(self):
        cur = self.root
        cur.minprint()

    def treemaxprint(self):
        cur = self.root
        cur.maxprint()

        # minimo

    def treemin(self):
        cur = self.root
        cur.min()
