import products
import store  # ✅ Fix: Correct import


def start(best_buy):
    while True:
        print("\nWelcome to Best Buy Store!")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            for product in best_buy.get_all_products():
                product.show()

        elif choice == "2":
            print(f"Total quantity in store: {best_buy.get_total_quantity()}")

        elif choice == "3":
            shopping_list = []
            while True:
                product_name = input("Enter product name to order (or 'done' to finish): ").strip()
                if product_name.lower() == "done":
                    break

                found_product = next((p for p in best_buy.get_all_products() if p.name.lower() == product_name.lower()), None)

                if not found_product:
                    print("Product not found. Please try again.")
                    continue

                while True:
                    try:
                        quantity = int(input(f"Enter quantity for {found_product.name} (Available: {found_product.quantity}): "))
                        if quantity > found_product.quantity:
                            print(f"Only {found_product.quantity} available. Please enter a lower quantity.")
                        else:
                            shopping_list.append((found_product, quantity))
                            break  # Move to next product
                    except ValueError:
                        print("Invalid quantity. Please enter a valid number.")

            if shopping_list:
                total_cost = best_buy.order(shopping_list)
                print(f"Total cost of your order: ${total_cost}")
            else:
                print("No valid products selected for order.")

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
    best_buy = store.Store(product_list)  # ✅ Fix: Correct reference to Store class

    start(best_buy)


if __name__ == "__main__":
    main()
