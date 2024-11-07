class Node:
    def __init__(self, key, height=1):
        self.key = key
        self.height = height
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


class Avl:
    def __init__(self):
        nil = Node(None, 0)
        self.Nil = nil
        self.root = nil

    def leftrotate(self, node):
        y = node.right
        node.right = y.left
        # aggiorno l'altezza del nodo ruotante
        node.height = 1 + max(node.right.height, node.left.height)
        if y.left != self.Nil:
           y.left.parent = node
        y.parent = node.parent
        if node.parent == self.Nil:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else: node.parent.right = y
        y.left = node
        y.height = 1 + max(y.right.height, y.left.height)
        node.parent = y



    def rightrotate(self, node):
        y = node.left
        node.left = y.right
        node.height = 1 + max(node.right.height, node.left.height)
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
        y.height = 1 + max(y.right.height, y.left.height)
        node.parent = y


    def insert(self,value):
        # set up
        current = self.root
        prev = self.Nil
        newnode = Node(value,1)
        while current != self.Nil:
            prev = current
            if newnode.key < current.key:
                current = current.left
            else:
                current = current.right
        newnode.parent = prev
        if prev == self.Nil:
            self.root = newnode
        elif newnode.key < prev.key:
            prev.left = newnode
        else:
            prev.right = newnode
        newnode.right = self.Nil
        newnode.left = self.Nil
        self.insertfixup(newnode)

    def insertfixup(self, x):
        x = x.parent
        while x != self.Nil:

            x.height = 1 + max(x.right.height, x.left.height)

            if (x.left.height - x.right.height) == 2:
                if (x.left.left.height - x.left.right.height) == -1:
                    self.leftrotate(x.left)
                self.rightrotate(x)
                x = x.parent
            # caso simmetrico
            elif (x.left.height - x.right.height) == -2:
                if (x.right.left.height - x.right.right.height) == 1:
                    self.rightrotate(x.right)
                self.leftrotate(x)
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
        while current != self.Nil and current.key != value:
            if value < current.key:
                current = current.left
            else:
                current = current.right
        if current.key == value:
            return True
        else: return False

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

