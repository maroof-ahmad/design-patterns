import copy

class Product:
    """
    Concrete class for Product.
    """
    def __init__(self,members):
        self.members = members
    def clone(self):
        members = []
        for member in self.members:
            members.append(member)
        return Product(members)

if __name__ == '__main__':
    a = Product(['maroof','karan'])
    print a.members
    b = a.clone()
    b.members.append('rahul')
    print a.members
    print b.members
