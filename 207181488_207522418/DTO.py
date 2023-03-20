class Hat:
    def __init__(self,id,topping,supplier,quantity):
        self.id=id
        self.topping=topping
        self.supplier=supplier
        self.quantity=quantity


class Supplier:
    def __init__(self,id,name):
        self.id=id
        self.name=name

class Order:
    def __init__(self,id,location,hatid):
        self.id=id
        self.location=location
        self.hatid=hatid
