from collections import deque
class Color:
    Black = "black"
    Red = "red"
class Arn:
    def __init__(self, key=None, parent=None):
        self.key = key
        self.parent = parent
        self.size = 1
        if not parent:  # se non ha un padre
            self.root = self
        else:  # altrimenti la radice è la radice del padre
            self.root = parent.root
        # imposta un nodo vuoto che ha la radice impostata
        self.left = None
        self.right = None
        if self.isempty():
            self.color = Color.Black

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

    # suppongo self.right non sia vuoto
    def leftrotate(self):
        # imposto y come figlio destro
        y = self.right
        # sposto il sottoalbero sinistro di y nel sottoalbero destro di self
        self.right = y.left
        # collego il padre di self a y
        if y.left is not None: # il nodo esiste ma è vuoto, pertanto avrebbe y.left is None vero
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

    def insert(self,value):
        current = self.root
        previus = None

        while current and current.notempty():
            previus = current
            if value < current.key:
                current = current.left
            else:
                current = current.right
        nuovo = Arn(key=value, parent=previus)
        if previus is None:
            self.root = nuovo
        elif nuovo.key < previus.key:
            previus.left = nuovo
        else:
            previus.right = nuovo
        nuovo.left = Arn(parent=nuovo)
        nuovo.right = Arn(parent=nuovo)
        nuovo.color = "red"
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
        # controllo se il nodo è vuoto
        if self.isempty():
            return []  # termino e restituisco
        # esploro a sinistra fino a che non trovo un nodo vuoto
        else:
            left_inorder = self.left.inorder() if self.left is not None else []
            right_inorder = self.right.inorder() if self.right is not None else []
            return left_inorder + [self.key, self.color] + right_inorder


    def print_by_level(self):
        if self.isempty():
            print("L'albero è vuoto.")
            return

        # Usa una coda per memorizzare i nodi da processare
        queue = deque([(self, 0)])  # (nodo, livello)
        current_level = 0
        print(f"Livello {current_level}: ", end="")

        while queue:
            node, level = queue.popleft()

            # Se cambia il livello, vai a capo e stampa il nuovo livello
            if level > current_level:
                current_level = level
                print(f"\nLivello {current_level}: ", end="")

            # Stampa il nodo e il suo colore
            if node.isempty():
                print("None", end=" ")  # Stampa None se il nodo è vuoto
            else:
                if node.parent is None:
                    print(f"{node.key}({node.color}) (Root)", end=" ")
                else:
                    print(f"{node.key}({node.color},{node.parent.key})", end=" ")

            # Aggiungi i figli alla coda con il livello incrementato
            if node.left is not None:
                queue.append((node.left, level + 1))
            if node.right is not None:
                queue.append((node.right, level + 1))

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
        # controllo se il nodo è vuoto
        if self.isempty():
            print("{} non è presente nell'albero".format(value))
            return False
        # controllo se il valore è uguale al nodo attuale
        if self.key == value:
            print("{} è stato trovato".format(value))
            return self
        # controllo se il valore è minore del nodo attuale
        elif value < self.key:
            return self.left.search(value)
        # controllo se il valore è maggiore del nodo attuale
        else:
            return self.right.search(value)