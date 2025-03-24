class Restaurant:
    def __init__(self):
        
        self.menu_items = []
        self.booked_tables = []
        self.orders = []

    def add_item_to_menu(self, item):
        
        self.menu_items.append(item)
        print(f"Added {item} to the menu.")

    def book_table(self, table_number):
       
        self.booked_tables.append(table_number)
        print(f"Table {table_number} has been booked.")

    def take_order(self, table_number, items):
       
        self.orders.append({'table_number': table_number, 'items': items})
        print(f"Order taken for Table {table_number}: {', '.join(items)}")

    def print_menu(self):
       
        print("\nMenu:")
        if not self.menu_items:
            print("Menu is empty.")
        else:
            for item in self.menu_items:
                print(f"- {item}")

    def print_table_reservations(self):
        
        print("\nTable Reservations:")
        if not self.booked_tables:
            print("No tables reserved.")
        else:
            for table in self.booked_tables:
                print(f"Table {table} is reserved.")

    def print_orders(self):
        
        print("\nCustomer Orders:")
        if not self.orders:
            print("No orders placed.")
        else:
            for order in self.orders:
                print(f"Table {order['table_number']} ordered: {', '.join(order['items'])}")


restaurant = Restaurant()

restaurant.add_item_to_menu("Burger")
restaurant.add_item_to_menu("Pizza")
restaurant.add_item_to_menu("Pasta")

restaurant.book_table(1)
restaurant.book_table(2)

restaurant.take_order(1, ["Burger", "Pizza"])
restaurant.take_order(2, ["Pasta"])

restaurant.print_menu()
restaurant.print_table_reservations()
restaurant.print_orders()
