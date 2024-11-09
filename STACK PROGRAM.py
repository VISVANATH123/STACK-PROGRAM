# Define the Stack ADT class
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print(f"Shipment '{item}' added to the supply stack.")

    def pop(self):
        if self.is_empty():
            print("No shipments left to distribute.")
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def display(self):
        if self.is_empty():
            print("The stack is empty. No shipments in stock.")
        else:
            print("Current supply stack (top to bottom):")
            for item in reversed(self.items):
                print(item)

# Main function to interact with the user
def main():
    food_stack = Stack()

    while True:
        print("\n--- Food Supply Chain Management ---")
        print("1. Add a new shipment")
        print("2. Distribute latest shipment")
        print("3. View current shipments")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            shipment = input("Enter the shipment details: ")
            food_stack.push(shipment)
        elif choice == '2':
            distributed_shipment = food_stack.pop()
            if distributed_shipment:
                print(f"Distributed shipment: {distributed_shipment}")
        elif choice == '3':
            food_stack.display()
        elif choice == '4':
            print("Exiting the Food Supply Chain Management system.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Run the main function
if __name__ == "__main__":
    main()
