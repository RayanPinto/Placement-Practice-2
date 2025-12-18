class tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

a=tree("A")
b=tree("B")
c=tree("C")
d=tree("D")
e=tree("E")
a.left=b
a.right=c
b.left=d
b.right=e
print(a.left.left.data)