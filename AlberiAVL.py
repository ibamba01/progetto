class Avl:
    def __init__(self, key=None, sizecluster=1, parent=None,root=None):
        self.key = key
        self.parent = parent
        self.size = sizecluster
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

        # suppongo self.right non sia vuoto
    def leftrotate(self):
         # imposto y come figlio destro
        y = self.right
        # sposto il sottoalbero sinistro di y nel sottoalbero destro di self
        self.right = y.left
        # collego il padre di self a y
        if y.left is not None:  # il nodo esiste ma è vuoto, pertanto avrebbe y.left is None vero
             # aggiorno il parent del nodo a sinistra di y con self
             y.left.parent = self
        # faccio lo switch tra y e x
        y.parent = self.parent
        # se self è la radice
        if self.isroot():
            self.root = y
            # se self è il figlio sinistro
        elif self == self.parent.left:
            # imposto y come figlio sinistro
            self.parent.left = y
        else:
             # imposto y come figlio destro
            self.parent.right = y
        # imposto x come figlio sinistro di y concludendo lo switch
        y.left = self
        self.parent = y
        y.size = self.size
        self.size = 1
        if self.right is not None:
            self.size += self.right.size
        if self.left is not None:
            self.size += self.left.size

            # aggiorno la dimensione

    def rightrotate(self):
        y = self.left
        self.left = y.right
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
        self.parent = y
        self.size = 1
        if self.right is not None:
            self.size += self.right.size
        if self.left is not None:
            self.size += self.left.size