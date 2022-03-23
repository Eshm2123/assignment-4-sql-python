# Data transfer objects:

class Hat:
    def __init__(self, hat_list):
        self.id = int(hat_list[0])
        self.topping = hat_list[1]
        self.supplier = int(hat_list[2])
        self.quantity = int(hat_list[3])


class Supplier:
    def __init__(self, supplier_list):
        self.id = int(supplier_list[0])
        self.name = supplier_list[1]


class Order:
    def __init__(self, order_list):
        self.id = int(order_list[0])
        self.location = order_list[1]
        self.hat = int(order_list[2])