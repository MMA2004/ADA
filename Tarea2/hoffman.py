from heapq import heappop, heappush

class Arbol:
    def __init__(self, label, left=None, right=None):
        self.__label = label
        self.__left = left
        self.__right = right

    def isLeaf(self):
        return self.__left is None and self.__right is None

    def getLabel(self):
        return self.__label

    def getLeft(self):
        return self.__left

    def getRight(self):
        return self.__right

    def to_dict(self):
        return {
            "label": self.getLabel(),
            "left": self.getLeft().to_dict() if self.getLeft() else None,
            "right": self.getRight().to_dict() if self.getRight() else None
        }

    def __inOrderAux(self, s):
        if self.isLeaf(): print("".join(s)+self.__label)
        else:
            s.append("0")
            self.getLeft().__inOrderAux(s)
            s.pop()
            s.append("1")
            self.getRight().__inOrderAux(s)
            s.pop()

    def inOrder(self):
        s = []
        self.__inOrderAux(s)





def solve(f):
    forest = []

    for k in f:
        heappush(forest, (f[k], Arbol(k)))
    print(forest)

    while len(forest) != 1:
        fl, l = heappop(forest)
        fr, r = heappop(forest)

        label_nueva = l.getLabel() + r.getLabel()
        arbol = Arbol(label_nueva, l, r)
        heappush(forest, (fl + fr , arbol))

    return heappop(forest)






freq = dict()
freq["a"] = 45
freq["b"] = 13
freq["c"] = 12
freq["d"] = 16
freq["e"] = 9
freq["f"] = 5


f, a = solve(freq)

print(f)
a.inOrder()
