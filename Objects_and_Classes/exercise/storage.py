class Storage:
    storage = []

    def __init__(self, capacity):
        self.capacity = capacity

    def add_product(self, product: str):
        if self.capacity > 0:
            self.capacity -= 1
            return Storage.storage.append(product)

    def get_products(self):
        return Storage.storage