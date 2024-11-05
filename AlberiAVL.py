class Node:
    def __init__(self, key=0, parent=None, root = None):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None
        self.parent = parent
        if root is None:
            if not parent:  # se non ha un padre
                self.root = self
            else:  # altrimenti la radice è la radice del padre
                self.root = parent.root

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


class Avl:
    def __init__(self):
        self.left = None
        self.right = None
        self.Nil = Node()
        self.Nil.left = None
        self.Nil.right = None
        self.Nil.height = 0
        self.root = self.Nil

    def leftrotate(self, node):
        y = node.right
        node.right = y.left
        # # aggiorno l'altezza di X
        rheight = node.right.height
        lheight = node.left.height
        #if self.right is not None:
            #rheight = self.right.height
        #if self.left is not None:
            #lheight = self.left.height
        node.height = 1 + max(rheight, lheight)
        if y.left != self.Nil:
            y.left.parent = node
        y.parent = node.parent
        if node.isroot():
            node.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node

        rheight = y.right.height
        lheight = y.left.height
        #if y.right is not None:
         #   rheight = y.right.height
        #if y.left is not None:
         #   lheight = y.left.height
        y.height = 1 + max(rheight, lheight)

        node.parent = y


        # aggiorno la dimensione

    def rightrotate(self, node):
        y = node.left
        node.left = y.right
        rheight = 0
        lheight = 0
        if self.right is not None:
            rheight = self.right.height
        if self.left is not None:
            lheight = self.left.height
        node.height = 1 + max(rheight, lheight)
        if y.right != self.Nil:
            y.right.parent = node
        y.parent = node.parent
        if node.isroot():
            node.root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y
        y.right = node
        node.parent = y
        y.height = node.height
        rheight = 0
        lheight = 0
        if y.right is not None:
            rheight = y.right.height
        if y.left is not None:
           lheight = y.left.height
        y.height = 1 + max(rheight, lheight)


    def insert(self,value):
        current = self.root
        prev = None
        nuovo = Node(value, parent=prev, root=self.root)
        nuovo.parent = None
        nuovo.key = value
        nuovo.left = self.Nil
        nuovo.right = self.Nil

        while current != self.Nil:
            prev = current
            if value < current.key:
                current = current.left
            else:
                current = current.right

        if prev is None:
            self.root = nuovo
        elif value < prev.key:
            prev.left = nuovo
        else:
            prev.right = nuovo
        nuovo.height = 1
        self.insertfixup(nuovo)

    def insertfixup(self, x):
        x = x.parent
        while x is not None and x != self.Nil:
            rheight = 0
            lheight = 0
            if x.right is not None: # per evitare errori se z.right o z.left sono None e non hanno l'attributo height
                rheight = x.right.height
            if x.left is not None:
                lheight = x.left.height
            x.height = 1 + max(rheight, lheight)

            if (lheight - rheight) == 2:
                if (lheight - rheight) == -1:
                    x.left.leftrotate()
                x.rightrotate()
                x = x.parent
            # caso simmetrico
            elif (rheight - lheight) == 2:
                if (rheight - lheight) == -1:
                    x.right.rightrotate()
                x.leftrotate()
                x = x.parent
            x = x.parent

    def inorder(self):
        current = self.root
        # controllo se il nodo è vuoto
        if current.isempty():
            return []  # termino e restituisco
        # esploro a sinistra fino a che non trovo un nodo vuoto
        else:
            left_inorder = current.left.inorder() if current.left is not None else []
            right_inorder = current.right.inorder() if current.right is not None else []
            return left_inorder + [current.key] + right_inorder

    def search(self, value):
        current = self.root
        # controllo se il nodo è vuoto
        if current.isempty():
            print("{} non è presente nell'albero".format(value))
            return False
        # controllo se il valore è uguale al nodo attuale
        if current.key == value:
            print("{} è stato trovato".format(value))
            return current
        # controllo se il valore è minore del nodo attuale
        elif value < current.key:
            return current.left.search(value)
        # controllo se il valore è maggiore del nodo attuale
        else:
            return current.right.search(value)

    def min(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current.key

    def kesimo(self, k):
        stack = []
        current = self.root
        count = 0
        while True:
            # scendo a sinistra fino a trovare un nodo vuoto e metto i nodi visitati nello stack
            if current and current.left is not None:
                stack.append(current)
                current = current.left
            # prendo il nodo in cima allo stack e lo visito
            elif stack:
                current = stack.pop()
                count += 1
                if count == k:
                    #print("il {}° nodo è: {}".format(k, current.key))
                    return current.key
                current = current.right
            else:
                break