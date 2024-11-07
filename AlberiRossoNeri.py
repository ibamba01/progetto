class Color:
    Black = "black"
    Red = "red"
# nodo di un albero
class Node:
    def __init__(self, key, size=1, color=None):
        self.key = key
        self.size = size # dimensione del sottoalbero
        self.left = None
        self.right = None
        self.parent = None
        self.color = color  # colore del nodo


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

class Arn:
    def __init__(self):
        nil = Node(None, 0, Color.Black)
        self.Nil = nil
        self.root = nil

    def leftrotate(self, node):
        # imposto y come figlio destro
        y = node.right
        # sposto il sottoalbero di sinistra di y a destra di node (dove prima era y)
        node.right = y.left
        # controllo se y avesse figli
        if y.left != self.Nil:
            y.left.parent = node
        # switch dei parent
        y.parent = node.parent
        # check se è la radice
        if node.parent == self.Nil:
            self.root = y
        # check se è il figlio sinistro
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        # pongo x a sinistra
        y.left = node
        # lo imposto come figlio
        node.parent = y
        # aggiorno la dimensione del sottoalbero
        y.size = node.size
        node.size = node.left.size + node.right.size + 1

    def rightrotate(self, node):
        y = node.left
        node.left = y.right
        if y.right != self.Nil:
            y.right.parent = node
        y.parent = node.parent
        if node.parent == self.Nil:
            self.root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y
        y.right = node
        node.parent = y
        y.size = node.size
        node.size = node.left.size + node.right.size + 1


    def insert(self,value):
        # setup
        current = self.root # x
        previus = self.Nil # y
        newnode = Node(value,color=Color.Red) # z
        size = newnode.size
        # trova la posizione
        while current != self.Nil:
            previus = current
            if value < current.key:
                # aumento la grandezza che avrà il suo sottoalbero
                size += 1
                current = current.left
            else:
                size += 1
                current = current.right
        newnode.parent = previus
        newnode.size = size
        # check posizione del padre
        if previus == self.Nil:
            self.root = newnode
        elif newnode.key < previus.key:
            previus.left = newnode
        else:
            previus.right = newnode
        newnode.color = Color.Red
        newnode.right = self.Nil
        newnode.left = self.Nil
        self.insertfixup(newnode)

    def insertfixup(self, node):

        while node.parent.color == Color.Red and node.parent != self.Nil:
            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                if y.color == Color.Red:
                    node.parent.color = Color.Black
                    y.color = Color.Black
                    node.parent.parent.color = Color.Red
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.leftrotate(node)
                    node.parent.color = Color.Black
                    node.parent.parent.color = Color.Red
                    self.rightrotate(node.parent.parent)
            else:
                y = node.parent.parent.left
                if y.color == Color.Red:
                    node.parent.color = Color.Black
                    y.color = Color.Black
                    node.parent.parent.color = Color.Red
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rightrotate(node)
                    node.parent.color = Color.Black
                    node.parent.parent.color = Color.Red
                    self.leftrotate(node.parent.parent)
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
        while current != self.Nil and current.key != value:
            if value < current.key:
                current = current.left
            else:
                current = current.right
        if current.key == value:
            return True
        else: return False