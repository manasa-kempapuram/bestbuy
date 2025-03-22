class Store:

        def __init__(self,price : float,name : str,quantity : int):
            self.name = name
            self.price = price
            self.quantity = quantity
            self.active = True

            if not name:
                raise ValueError("Name cannot be empty.")
            if price < 0:
                 raise ValueError("Price cannot be negative.")
            if quantity < 0:
                raise ValueError("Quantity cannot be negative.")

        def get_quantity(self):
            return self.quantity

        def set_quantity(self,quantity : int):
            if quantity < 0:
                raise ValueError("Quantity cannot be negative.")
            self.quantity = quantity
            if self.quantity == 0:
                self.deactivate()

        def is_active(self) -> bool:
            """Returns True if the product is active, otherwise False."""
            return self.active

        def activate(self):
            """Activates the product."""
            self.active = True

        def deactivate(self):
            """Deactivates the product."""
            self.active = False

        def show(self) -> str:
            """Returns a string representation of the product."""
            return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

        def buy(self, quantity: int) -> float:
            """
            Buys a given quantity of the product.
            Updates the quantity and returns the total price.
            Raises an exception if there is not enough stock.
            """
            if quantity <= 0:
                raise ValueError("Quantity to buy must be greater than zero.")
            if quantity > self.quantity:
                raise ValueError("Not enough stock available.")

            total_price = quantity * self.price
            self.set_quantity(self.quantity - quantity)
            return total_price








