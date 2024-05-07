def main():
    """Starts the chatbot system for KJ Restaurant."""
    chatbot_system()


def chatbot_system():
    """Handles user interaction, order taking, and bill calculation."""
    name = input("Enter Your Name: ")
    print(f"Hello {name}, Welcome to KJ-Restaurant\n")
    print(f"What would you like to order, {name}?\n")

    menu_options = ["Rice-Plate", "Samosa", "Vada-Pava", "Chole-Bhature", "Pohe"]
    quantity_count = [0] * len(menu_options)  # Initialize with zeros

    while True:
        for i, option in enumerate(menu_options):
            print(f"Option {i+1}: {option}")
        print("\nI would like to have option: ", end="")

        try:
            choice = int(input()) - 1  # Subtract 1 to match index starting from 0
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice < 0 or choice >= len(menu_options):
            print("Invalid option. Please choose a valid option.")
            continue

        print(f"\nYou confirmed order: {menu_options[choice]}")
        quantity_count[choice] += 1  # Increment quantity for selected option

        if quantity_count[choice] >= 5:
            break

        order_again = input("Do you want anything else (yes/no): ").upper()
        if order_again != "YES":
            break

    your_order(menu_options, quantity_count)
    total_bill = calculate_bill(quantity_count)
    print(f"\nYour total bill is ₹{total_bill}")
    print("\nThanks for your order!")


def calculate_bill(quantity_count):
    """Calculates the total bill amount."""
    prices = [50, 25, 25, 55, 25]  # List of item prices
    total = 0
    for i, quantity in enumerate(quantity_count):
        total += quantity * prices[i]
    return total


def your_order(menu_options, quantity_count):
    """Prints the user's order details."""
    print("Your Order is:")
    for i, quantity in enumerate(quantity_count):
        if quantity > 0:
            print(f"{menu_options[i]} x {quantity}")


if __name__ == "__main__":
    main()


