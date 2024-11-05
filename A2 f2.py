# Importing necessary classes from the main system file
from A2 import Ebook, Customer, ShoppingCart, Order, Discount, LoyaltyDiscount, BulkDiscount, Invoice
# Creating a list of 10 e-books for the e-bookstore across different categories
books = [
    Ebook("To Kill a Mockingbird", "Harper Lee", "1960-07-11", "Fiction", 10.0),
    Ebook("A Brief History of Time", "Stephen Hawking", "1988-04-01", "Science", 15.0),
    Ebook("The Art of War", "Sun Tzu", "500 BC", "Philosophy", 8.0),
    Ebook("Pride and Prejudice", "Jane Austen", "1813-01-28", "Romance", 12.0),
    Ebook("The Great Gatsby", "F. Scott Fitzgerald", "1925-04-10", "Classic", 10.0),
    Ebook("The Catcher in the Rye", "J.D. Salinger", "1951-07-16", "Classic", 10.0),
    Ebook("Thinking, Fast and Slow", "Daniel Kahneman", "2011-10-25", "Psychology", 18.0),
    Ebook("The Lean Startup", "Eric Ries", "2011-09-13", "Business", 20.0),
    Ebook("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", "2011-09-04", "History", 22.0),
    Ebook("Becoming", "Michelle Obama", "2018-11-13", "Biography", 18.0)
]

# Display the list of e-books
print("Available e-books in the store:")
for book in books:
    print(book)

# Creating a Customer Manager instance for managing customers
customer_manager = Customer("", "", "", "manager")  # Placeholder instance as a manager

# Adding 3 customers to the system (Add customer account)
customer1 = Customer("Maryam Fahad", "MaryamFahad@gmail.com", "971509827735", "Ac001", is_loyalty_member=True)
customer2 = Customer("Mohammed Saif", "MohammedSaif@gmail.com", "971559988765", "Ac002", is_loyalty_member=False)
customer3 = Customer("Sara Ali", "SaraAli@gmail.com", "971554332211", "Ac003", is_loyalty_member=True)

# Aggregation relationship: CustomerManager aggregates multiple Customer instances.
customer_manager.add_customer(customer1)
customer_manager.add_customer(customer2)
customer_manager.add_customer(customer3)

# Display the list of customers
print("\nCustomers in the system:")
customer_manager.list_customers()

# Maryam Fahad (Customer1) - Add/Modify/Remove Books in ShoppingCart, Apply Discounts, and Generate Invoice
# Setting up a shopping cart for Customer1
cart1 = ShoppingCart()
customer1.set_shopping_cart(cart1)  # Binary association between Customer and ShoppingCart (one-to-one)

# Adding books to Maryam's cart
print("\nCustomer 1: Maryam Fahad is adding books to the shopping cart:")
cart1.add_ebook(books[0])  # To Kill a Mockingbird
print("Added:", books[0].get_title())
cart1.add_ebook(books[1])  # A Brief History of Time
print("Added:", books[1].get_title())
cart1.add_ebook(books[2])  # The Art of War
print("Added:", books[2].get_title())

# Composition relationship: ShoppingCart is composed of specific Ebook instances.
# If the cart is removed, the specific books are removed from the cart, but they remain in the store catalog.
print("\nMaryam's Shopping Cart:", cart1)
print("Total price in Maryam's shopping cart:", cart1.calculate_total())

# Maryam decides to remove a book
print("\nMaryam is removing a book from the cart:")
cart1.remove_ebook(books[1])  # Removing A Brief History of Time
print("Removed:", books[1].get_title())
print("Maryam's Shopping Cart after removal:", cart1)
print("Total price in Maryam's shopping cart after removal:", cart1.calculate_total())

# Maryam places an order
order1 = Order(customer1, cart1.get_ebooks(), "2023-11-05")
# Aggregation relationship: Order aggregates Ebook instances but does not own them permanently.
# The Ebooks are referenced in the order but exist independently in the catalog.

# Applying discounts: Loyalty discount applies for Maryam
loyalty_discount = LoyaltyDiscount()  # Inheritance: LoyaltyDiscount inherits from Discount
original_price = order1.get_final_price()
order1.apply_discount(loyalty_discount)
discount_applied = original_price - order1.get_final_price()
print("\nDiscount applied for Maryam's Order:")
print("Original Price:", original_price)
print("Loyalty Discount Applied:", discount_applied)
print("Price After Discount:", order1.get_final_price())

# Generating an invoice for Maryam's order
invoice1 = Invoice(order1)
# Composition relationship: Invoice is composed of an Order.
# If the order is removed, the invoice is also removed.
print("\nInvoice for Maryam's Order:")
print("Customer:", customer1.get_name())
print(invoice1.generate_invoice_details())

# Mohammed Saif (Customer2) - Bulk Purchase Scenario
cart2 = ShoppingCart()
customer2.set_shopping_cart(cart2)  # Binary association between Customer and ShoppingCart

# Adding multiple books to qualify for bulk discount
print("\nCustomer 2: Mohammed Saif is adding books to the shopping cart:")
for i in range(5):  # Adding first 5 books
    cart2.add_ebook(books[i])
    print("Added:", books[i].get_title())

# Display the shopping cart contents and total price
print("\nMohammed's Shopping Cart:", cart2)
print("Total price in Mohammed's shopping cart:", cart2.calculate_total())

# Mohammed places an order
order2 = Order(customer2, cart2.get_ebooks(), "2023-11-06")

# Applying discounts: Bulk discount applies for Mohammed
bulk_discount = BulkDiscount()  # Inheritance from Discount class
original_price = order2.get_final_price()
order2.apply_discount(bulk_discount)
discount_applied = original_price - order2.get_final_price()
print("\nDiscount applied for Mohammed's Order:")
print("Original Price:", original_price)
print("Bulk Discount Applied:", discount_applied)
print("Price After Discount:", order2.get_final_price())

# Generating an invoice for Mohammed's order
invoice2 = Invoice(order2)
print("\nInvoice for Mohammed's Order:")
print("Customer:", customer2.get_name())
print(invoice2.generate_invoice_details())

# Sara Ali (Customer3) - Loyalty and Bulk Discount Combined
cart3 = ShoppingCart()
customer3.set_shopping_cart(cart3)  # Binary association between Customer and ShoppingCart

# Adding books to qualify for both loyalty and bulk discount
print("\nCustomer 3: Sara Ali is adding books to the shopping cart:")
for i in range(7):  # Adding first 7 books
    cart3.add_ebook(books[i])
    print("Added:", books[i].get_title())

# Display the shopping cart contents and total price
print("\nSara's Shopping Cart:", cart3)
print("Total price in Sara's shopping cart:", cart3.calculate_total())

# Sara places an order
order3 = Order(customer3, cart3.get_ebooks(), "2023-11-07")

# Applying discounts: Both Loyalty and Bulk discounts apply
original_price = order3.get_final_price()
order3.apply_discount(loyalty_discount, bulk_discount)
discount_applied = original_price - order3.get_final_price()
print("\nDiscounts applied for Sara's Order:")
print("Original Price:", original_price)
print("Total Discount Applied:", discount_applied)
print("Price After Discounts:", order3.get_final_price())

# Generating an invoice for Sara's order
invoice3 = Invoice(order3)
print("\nInvoice for Sara's Order:")
print("Customer:", customer3.get_name())
print(invoice3.generate_invoice_details())

# Modifying Customer Information for Maryam
print("\nModifying Maryam's information...")
customer1.set_email("MaryamUpdated@gmail.com")
print("Maryam's updated email:", customer1.get_email())

# Removing a Customer Account (Mohammed Saif)
print("\nRemoving Mohammed Saif from the system...")
customer_manager.remove_customer("Ac002")  # Aggregation: CustomerManager can manage (aggregate) multiple customers