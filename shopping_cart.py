import csv
import os

CART_FILE = "cart.csv"

class ShoppingCart:
    def __init__(self):
        self.cart = []
        self.load_cart()

    def load_cart(self):
        """Load cart items from CSV file if it exists."""
        if os.path.exists(CART_FILE):
            with open(CART_FILE, mode='r', newline='') as file:
                reader = csv.reader(file)
                self.cart = [row[0] for row in reader]
        print(f"Current cart items: {self.cart}")

    def save_cart(self):
        """Save cart items to CSV file."""
        with open(CART_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            for  item in self.cart:
                writer.writerow([item])

    def add_item(self, item):
        self.cart.append(item)
        self.save_cart()
        print(f"Added '{item}' to cart. Current cart: {self.cart}")

    def remove_item(self, item):
        if item in self.cart:
            self.cart.remove(item)
            self.save_cart()
            print(f"Removed '{item}' from cart. Current cart: {self.cart}")
        else:
            print(f"Item '{item}' not found in cart.")

    def empty_cart(self):
        self.cart.clear()
        self.save_cart()
        print("Cart emptied.")

# Example Usage
if __name__ == "__main__":
    cart = ShoppingCart()

    while True:
        print("\n--- Shopping Cart Menu ---")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Empty Cart")
        print("4. View Cart")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            item = input("Enter item to add: ")
            cart.add_item(item)
        elif choice == '2':
            item = input("Enter item to remove: ")
            cart.remove_item(item)
        elif choice == '3':
            cart.empty_cart()
        elif choice == '4':
            print(f"Current cart items: {cart.cart}")
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select 1-5.")
