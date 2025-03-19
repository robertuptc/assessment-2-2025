from classes.customer import Customer
from classes.inventory import Inventory


class Store:
    def __init__(self):
        self.all_customers = Customer.all_customers()
        self.inventory = Inventory.all_inventory()