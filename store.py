from typing import List
from products import Product


class Store:
    def __init__(self, products: List[Product]):
        self.products = products

    def add_product(self, product: Product):
        """Adds a product to the store."""
        self.products.append(product)

    def remove_product(self, product: Product):
        """Removes a product if it exists in the store."""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns the total quantity of all products in the store."""
        return sum(product.quantity for product in self.products)

    def get_all_products(self) -> List[Product]:
        """Returns a list of active products (quantity > 0)."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[tuple]) -> float:
        """
        Processes an order based on a shopping list of (Product, quantity) tuples.
        Returns the total cost of the order.
        """
        total_cost = 0
        for product, quantity in shopping_list:
            if product not in self.products:
                print(f"Product {product.name} is not available in the store.")
                continue

            if product.quantity < quantity:
                print(f"Not enough stock for {product.name} (Available: {product.quantity}, Requested: {quantity})")
                continue

            total_cost += product.price * quantity
            product.buy(quantity)  # Reduces the stock

        return total_cost


def main():
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
