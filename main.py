import products
import Store


def start(best_buy):
    while True:
        print("\nWelcome to Best Buy Store!")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            for product in best_buy.get_all_products():
                product.show()

        elif choice == "2":
            print(f"Total quantity in store: {best_buy.get_total_quantity()}")

        elif choice == "3":
            shopping_list = []
            while True:
                product_name = input("Enter product name to order (or 'done' to finish): ")
                if product_name.lower() == "done":
                    break
                quantity = int(input("Enter quantity: "))

                found_product = next((p for p in best_buy.get_all_products() if p.name == product_name), None)

                if found_product:
                    shopping_list.append((found_product, quantity))
                else:
                    print("Product not found.")

            total_cost = best_buy.order(shopping_list)
            print(f"Total cost of your order: ${total_cost}")

        elif choice == "4":
            print("Thank you for visiting Best Buy Store!")
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    # Setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = store.Store(product_list)

    start(best_buy)


if __name__ == "__main__":
    main()
