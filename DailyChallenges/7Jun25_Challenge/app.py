from inventory.functions import InventoryManagement

def main():
    inv = InventoryManagement('inventory.json')

    menu = """
    ===== Inventory Management =====
    1. Display Inventory
    2. Add Product
    3. Update Product Stock
    4. Search Product by Name
    5. Search Product by Price (with tolerance)
    6. Delete A Product
    7. Exit
    """

    actions = {
        '1': inv.display_inventory,
        '2': inv.add_product,
        '3': inv.update_product,
        '4': inv.search_product,
        '5': inv.search_by_price,
        '6': inv.delete_product,
    }

    while True:
        print(menu)
        choice = input("Select an option (1-6): ").strip()

        if choice == '7':
            print("Exiting. Goodbye!")
            break

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice, please enter a number between 1 and 7.")

        print()
        input("Press Enter to continue...")  # Pause for user to read output

if __name__ == "__main__":
    main()
