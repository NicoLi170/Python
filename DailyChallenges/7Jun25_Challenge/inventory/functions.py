import json
import os


class InventoryManagement:
    def __init__(self, filename):
        self.filename = filename
        self.inventory = self.load_inventory()

    def load_inventory(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                json.dump([], file)
        with open(self.filename) as file:
            return json.load(file)


    def save_inventory(self):
        with open(self.filename, 'w') as file:
            json.dump(self.inventory, file,indent = 4)


    def find_product(self, name):
        for product in self.inventory:
            if product['name'].lower() == name.lower():
                return product
        return None


    def search_by_price(self):
        try:
            price = float(input('Price of product ($): '))
        except ValueError:
            print('Invalid Input, price must be number')

        tolerance = 0.05
        matches = [p for p in self.inventory
                   if abs(p['price'] - price) <= tolerance
        ]

        if not matches:
            print(f'No products found with price ${price:.2f}.')
        else:
            print(f'Products priced around ${price:.2f}:')
            for product in matches:
                print(f"- {product['name']}: Price ${product['price']} Stock {product['stock']}")


    def display_inventory(self):
        if not self.inventory:
            print('Empty Inventory')
            return
        print('\n Current Inventory:')
        for product in self.inventory:
            print(f'- {product['name']}: ${product['price']:.2f}, Stock: {product['stock']}')


    def add_product(self):
        name = input('Please input the name of the new product: ')
        if self.find_product(name):
            print('Sorry, the product is already on the shelf.')
            return
        try:
            price = float(input('Enter price ($): '))
            stock = int(input('Enter stock quantity: '))
        except ValueError:
            print('Invalid Input. Price must be a number, stock must be an integer.')
            return
        self.inventory.append({"name":name, "price":price, "stock":stock})
        self.save_inventory()
        print('Product added.')

    def delete_product(self):
        name = input('Enter the name of the product to delete: ')
        product = self.find_product(name)
        if not product:
            print('Product not found.')
            return
        self.inventory.remove(product)
        self.save_inventory()
        print(f'Product log of {name} are deleted')


    def update_product(self):
        name = input('Enter product name to update: ')
        product = self.find_product(name)
        if not product:
            print('Sorry, the product is not existed')
            return
        try:
            product['stock']= int(input(f"Enter new stock for {product['name']}"))
            self.save_inventory()
            print('Stock updated.')
        except ValueError:
            print('Invalid input. Stocks must be integer.')


    def search_product(self):
        name = input('Search by product name: ')
        product = self.find_product(name)
        if not product:
            print('Sorry, the product is not existed')
        else:
            print(f'- {product['name']}: ${product['price']:.2f}, Stock: {product['stock']}')
