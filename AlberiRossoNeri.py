class Color:
    Black = "black"
    Red = "red"
# nodo di un albero
class Node:
    def __init__(self, key=0, parent=None, root = None):
        #self.size = 1
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent
        self.color = Color.Black
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

    def isblack(self):
        return self.color == Color.Black

    def isred(self):
        return self.color == Color.Red

    def isleaf(self):
        return self.left is None and self.right is None

    #getter fun
    def getkey(self):
        return self.key

    def getfather(self):
        return self.parent

    def getcolor(self):
        return self.color

    #
    def setkey(self, value):
        self.key = value

class Arn:
    def __init__(self):
        self.Nil = Node()
        self.Nil.color = Color.Black
        self.Nil.left = None
        self.Nil.right = None
        self.root = self.Nil


    # suppongo self.right non sia vuoto
    def leftrotate(self, node):
        # imposto y come figlio destro
        y = node.right
        # sposto il sottoalbero sinistro di y nel sottoalbero destro di self
        node.right = y.left
        # collego il padre di self a y
        if y.left != self.Nil: # il nodo esiste ma è vuoto, pertanto avrebbe y.left is None vero
            # aggiorno il parent del nodo a sinistra di y con self
            y.left.parent = node
        # faccio lo switch tra y e x
        y.parent = node.parent
        # se self è la radice
        if node.isroot():
            node.root = y
        # se self è il figlio sinistro
        elif node == node.parent.left:
            # imposto y come figlio sinistro
            node.parent.left = y
        else:
            # imposto y come figlio destro
            node.parent.right = y
        # imposto x come figlio sinistro di y concludendo lo switch
        y.left = node
        node.parent = y
        y.size = node.size
        node.size = 1
        #if node.right is not None:
            #node.size += node.right.size
        #if node.left is not None:
           # node.size += node.left.size


        # aggiorno la dimensione

    def rightrotate(self, node):
        y = node.left
        node.left = y.right
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
        node.size = 1
        #if node.right is not None:
            #node.size += node.right.size
        #if node.left is not None:
            #node.size += node.left.size

    def insert(self,value):
        # setup
        current = self.root
        previus = None
        nuovo = Node(value,parent=previus,root=self.root)
        nuovo.parent = None
        nuovo.key = value
        nuovo.left = self.Nil
        nuovo.right = self.Nil
        nuovo.color = Color.Black
        # trova la posizione
        while current != self.Nil:
            previus = current
            if value < current.key:
                current = current.left
            else:
                current = current.right
        # check posizione del padre
        if previus is None:
            self.root = nuovo
        elif nuovo.key < previus.key:
            previus.left = nuovo
        else:
            previus.right = nuovo
        nuovo.color = Color.Red
        self.insertfixup(nuovo)

    def insertfixup(self,z):
        while z.parent is not None and z.parent.isred():
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y is not None and y.isred():
                    z.parent.color = Color.Black
                    y.color = Color.Black
                    z.parent.parent.color = Color.Red
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        z.leftrotate()
                    z.parent.color = Color.Black
                    z.parent.parent.color = Color.Red
                    z.parent.parent.rightrotate()
            else:
                y = z.parent.parent.left
                if y is not None and y.isred():
                    z.parent.color = Color.Black
                    y.color = Color.Black
                    z.parent.parent.color = Color.Red
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        z.rightrotate()
                    z.parent.color = Color.Black
                    z.parent.parent.color = Color.Red
                    z.parent.parent.leftrotate()
        self.root.color = Color.Black

    def inorder(self):
        current = self.root
        # controllo se il nodo è vuoto
        if current.isempty():
            return []  # termino e restituisco
        # esploro a sinistra fino a che non trovo un nodo vuoto
        else:
            left_inorder = current.left.inorder() if current.left is not None else []
            right_inorder = current.right.inorder() if current.right is not None else []
            return left_inorder + [current.key, current.color] + right_inorder

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
                    #print("il {}° nodo è: {}".format(k, current.key))
                    return current.key
                current = current.right
            else:
                break

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