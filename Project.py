# Define a list to store the inventory
inventory = []


def add_item(name, price, quantity, category):
    """Add a new item to the inventory."""
    item = {
        'name': name,
        'price': price,
        'quantity': quantity,
        'category': category
    }
    inventory.append(item)
    print(f"Item '{name}' added to inventory.")


def update_item(name, price=None, quantity=None, category=None):
    """Update an existing item in the inventory."""
    for item in inventory:
        if item['name'].lower() == name.lower():
            if price is not None:
                item['price'] = price
            if quantity is not None:
                item['quantity'] = quantity
            if category is not None:
                item['category'] = category
            print(f"Item '{name}' updated.")
            return
    print(f"Item '{name}' not found.")


def view_inventory():
    """View all items in the inventory."""
    if not inventory:
        print("Inventory is empty.")
        return
    print("Current Inventory:")
    for item in inventory:
        print(
            f"Name: {item['name']}, Price: ${item['price']}, Quantity: {item['quantity']}, Category: {item['category']}")


def remove_item(name):
    """Remove an item from the inventory."""
    global inventory
    inventory = [item for item in inventory if item['name'].lower() != name.lower()]
    print(f"Item '{name}' removed from inventory.")


def search_by_category(category):
    """Search for items in the inventory by category."""
    found_items = [item for item in inventory if item['category'].lower() == category.lower()]
    if not found_items:
        print(f"No items found in category '{category}'.")
        return
    print(f"Items in category '{category}':")
    for item in found_items:
        print(f"Name: {item['name']}, Price: ${item['price']}, Quantity: {item['quantity']}")


def main():
    """Main loop to interact with the user."""
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Remove Item")
        print("5. Search by Category")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            category = input("Enter item category: ")
            add_item(name, price, quantity, category)

        elif choice == '2':
            name = input("Enter item name to update: ")
            price = input("Enter new price (leave blank if no change): ")
            quantity = input("Enter new quantity (leave blank if no change): ")
            category = input("Enter new category (leave blank if no change): ")
            price = float(price) if price else None
            quantity = int(quantity) if quantity else None
            update_item(name, price, quantity, category)

        elif choice == '3':
            view_inventory()

        elif choice == '4':
            name = input("Enter item name to remove: ")
            remove_item(name)

        elif choice == '5':
            category = input("Enter category to search: ")
            search_by_category(category)

        elif choice == '6':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()