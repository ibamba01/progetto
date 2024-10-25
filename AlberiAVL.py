class Avl:
    def __init__(self, key=None, heightcluster=1, parent=None,root=None):
        self.key = key
        self.parent = parent
        self.height = heightcluster
        if root is None:  # serve a gestire il caso y = Arn(root=self), altrimenti y = Arn() imposterebbe sestesso come la radice
            if not parent:  # se non ha un padre e non è stata impostata una radice è la radice
                self.root = self
            else:  # altrimenti la radice è la radice del padre
                self.root = parent.root
        # imposta un nodo vuoto che ha la radice impostata
        self.left = None
        self.right = None

    def isempty(self):
        return self.key is None

    def notempty(self):
        return self.key is not None

    def isroot(self):
        return self.parent is None

    def isleaf(self):
        return self.left is None and self.right is None

        # commentato in alberirossonero
    def leftrotate(self):
        y = self.right
        self.right = y.left
        # # aggiorno l'altezza di X
        rheight = 0
        lheight = 0
        if self.right is not None:
            rheight = self.right.height
        if self.left is not None:
            lheight = self.left.height
        self.height = 1 + max(rheight, lheight)
        # codice ugale a quello di alberirossoneri
        if y.left is not None:
             y.left.parent = self
        y.parent = self.parent
        if self.isroot():
            self.root = y
        elif self == self.parent.left:
            self.parent.left = y
        else:
            self.parent.right = y
        y.left = self
        # aggiorno l'altezza di Y
        y.height = self.height
        rheight = 0
        lheight = 0
        if y.right is not None:
            rheight = y.right.height
        if y.left is not None:
            lheight = y.left.height
        y.height = 1 + max(rheight, lheight)
        self.parent = y
            # aggiorno la dimensione

    def rightrotate(self):
        y = self.left
        self.left = y.right
        rheight = 0
        lheight = 0
        if self.right is not None:
            rheight = self.right.height
        if self.left is not None:
            lheight = self.left.height
        self.height = 1 + max(rheight, lheight)
        if y.right is not None:
            y.right.parent = self
        y.parent = self.parent
        if self.isroot():
            self.root = y
        elif self == self.parent.right:
            self.parent.right = y
        else:
            self.parent.left = y
        y.right = self
        y.height = self.height
        rheight = 0
        lheight = 0
        if y.right is not None:
            rheight = y.right.height
        if y.left is not None:
            lheight = y.left.height
        y.height = 1 + max(rheight, lheight)
        self.parent = y


    def insert(self,value):
        current = self.root
        prev = None
        while current is not None:
            prev = current
            if value < current.key:
                current = current.left
            else:
                current = current.right
        newnode = Avl(value, parent=prev)
        if prev is None:
            self.root = newnode
        elif value < prev.key:
            prev.left = newnode
        else:
            prev.right = newnode
        newnode.left = None
        newnode.right = None
        newnode.height = 1
        self.insertfixup(newnode)


    def insertfixup(self, x):
        x = x.parent
        while x is not None:
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


