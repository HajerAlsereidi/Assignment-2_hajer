from typing import List

# Ebook Class - Represents each e-book in the store
class Ebook:
    def __init__(self, title, author, publication_date, genre, price):
        # Private attributes for encapsulation
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price

    # Getters and setters for each attribute
    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_publication_date(self):
        return self.__publication_date

    def set_publication_date(self, publication_date):
        self.__publication_date = publication_date

    def get_genre(self):
        return self.__genre

    def set_genre(self, genre):
        self.__genre = genre

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return "Ebook: " + self.__title + " by " + self.__author + ", Genre: " + self.__genre + ", Price: " + str(self.__price)


class Customer:
    # Class-level dictionary to store all customers by account ID
    customers = {}

    def __init__(self, name, email, phone_number, account_id, is_loyalty_member=False):
        # Instance attributes for each customer
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number
        self.__account_id = account_id
        self.__is_loyalty_member = is_loyalty_member
        self.__purchase_history = []  # List to store orders
        self.__shopping_cart = None   # Shopping cart associated with the customer

    # Instance methods (getters and setters)
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_account_id(self):
        return self.__account_id

    def get_is_loyalty_member(self):
        return self.__is_loyalty_member

    def set_is_loyalty_member(self, status):
        self.__is_loyalty_member = status

    # Shopping cart getter and setter
    def set_shopping_cart(self, cart):
        """Assigns a shopping cart to the customer."""
        self.__shopping_cart = cart

    def get_shopping_cart(self):
        """Returns the customer's shopping cart."""
        return self.__shopping_cart

    # Methods for managing customer accounts
    def add_customer(self, customer):
        """Add a new customer to the system."""
        account_id = customer.get_account_id()
        if account_id in Customer.customers:
            print("A customer with this account ID already exists.")
        else:
            Customer.customers[account_id] = customer
            print("Customer added:", customer.get_name())

    def modify_customer(self, account_id, name=None, email=None, phone_number=None, is_loyalty_member=None):
        """Modify an existing customer's details."""
        if account_id in Customer.customers:
            customer = Customer.customers[account_id]
            if name is not None:
                customer.set_name(name)
            if email is not None:
                customer.set_email(email)
            if phone_number is not None:
                customer.set_phone_number(phone_number)
            if is_loyalty_member is not None:
                customer.set_is_loyalty_member(is_loyalty_member)
            print("Customer modified:", account_id)
        else:
            print("No customer found with this account ID.")

    def remove_customer(self, account_id):
        """Remove a customer from the system."""
        if account_id in Customer.customers:
            del Customer.customers[account_id]
            print("Customer removed:", account_id)
        else:
            print("No customer found with this account ID.")

    def list_customers(self):
        """List all customers in the system."""
        if not Customer.customers:
            print("No customers in the system.")
        else:
            for account_id, customer in Customer.customers.items():
                print("Account ID:", account_id, "Name:", customer.get_name(), "Email:", customer.get_email())

# ShoppingCart Class - Contains e-books the customer wants to buy
class ShoppingCart:
    def __init__(self):
        # Private attributes for cart items and total quantity
        self.__ebooks = []  # Composition relationship with Ebook
        self.__total_quantity = 0

    # Getters and setters for each attribute
    def get_ebooks(self):
        return self.__ebooks

    def set_ebooks(self, ebooks):
        self.__ebooks = ebooks
        self.__total_quantity = len(ebooks)  # Update total quantity based on the new list

    def get_total_quantity(self):
        return self.__total_quantity

    def set_total_quantity(self, quantity):
        self.__total_quantity = quantity

    # Adds an e-book to the cart
    def add_ebook(self, ebook):
        self.__ebooks.append(ebook)
        self.__total_quantity += 1

    # Removes an e-book from the cart
    def remove_ebook(self, ebook):
        if ebook in self.__ebooks:
            self.__ebooks.remove(ebook)
            self.__total_quantity -= 1

    # Empties the cart
    def clear_cart(self):
        self.__ebooks.clear()
        self.__total_quantity = 0

    def calculate_total(self):
        # Calculates total cost of items in the cart
        return sum(ebook.get_price() for ebook in self.__ebooks)

    def __str__(self):
        return "Shopping Cart with " + str(len(self.__ebooks)) + " e-books, Total Quantity: " + str(self.__total_quantity)


# Base Discount Class
class Discount:
    def apply(self, order):
        # Base method to be overridden by subclasses
        return 0.0

# LoyaltyDiscount subclass that inherits from Discount
class LoyaltyDiscount(Discount):
    def __init__(self, discount_rate=0.10):
        self.__discount_rate = discount_rate

    def apply(self, order):
        # Applies loyalty discount if the customer is a loyalty member
        if order.get_customer().get_is_loyalty_member():
            return order.get_final_price() * self.__discount_rate
        return 0.0

# BulkDiscount subclass that inherits from Discount
class BulkDiscount(Discount):
    def __init__(self, discount_rate=0.20):
        self.__discount_rate = discount_rate

    def apply(self, order):
        # Applies bulk discount if the order has 5 or more e-books
        if len(order.get_ebooks()) >= 5:
            return order.get_final_price() * self.__discount_rate
        return 0.0


class Order:
    def __init__(self, customer, ebooks, order_date):
        # Private attributes for customer, e-books, order date, and final price
        self.__customer = customer
        self.__ebooks = ebooks  # Aggregation relationship with Ebook
        self.__order_date = order_date
        self.__final_price = self.calculate_total()
        self.__discount_applied = 0.0

    # Getters and setters for each attribute
    def get_customer(self):
        return self.__customer

    def set_customer(self, customer):
        self.__customer = customer

    def get_ebooks(self):
        return self.__ebooks

    def set_ebooks(self, ebooks):
        self.__ebooks = ebooks
        self.__final_price = self.calculate_total()  # Recalculate total with new ebooks

    def get_order_date(self):
        return self.__order_date

    def set_order_date(self, order_date):
        self.__order_date = order_date

    def get_final_price(self):
        return self.__final_price

    def set_final_price(self, price):
        self.__final_price = price

    def get_discount_applied(self):
        return self.__discount_applied

    def set_discount_applied(self, discount):
        self.__discount_applied = discount

    # Applies discounts to the order
    def apply_discount(self, *discounts):
        """Apply multiple discounts to the order."""
        for discount in discounts:
            self.__discount_applied += discount.apply(self)
        self.__final_price -= self.__discount_applied

    def calculate_total(self):
        # Calculates total cost of the order
        return sum(ebook.get_price() for ebook in self.__ebooks)

    def __str__(self):
        return "Order Date: " + self.__order_date + ", Total: " + str(self.__final_price) + ", Discount Applied: " + str(self.__discount_applied)


# Invoice Class - Generates an itemized invoice for an order
class Invoice:
    def __init__(self, order, VAT_rate=0.08):
        # Private attributes for order, VAT rate, and total amount
        self.__order = order  # Composition with Order
        self.__VAT_rate = VAT_rate
        self.__total_amount = self.calculate_total()

    # Getters and setters for each attribute
    def get_order(self):
        return self.__order

    def set_order(self, order):
        self.__order = order

    def get_VAT_rate(self):
        return self.__VAT_rate

    def set_VAT_rate(self, rate):
        self.__VAT_rate = rate

    def get_total_amount(self):
        return self.__total_amount

    def set_total_amount(self, amount):
        self.__total_amount = amount

    def calculate_total(self):
        # Calculates the total amount including VAT
        base_total = self.__order.get_final_price()
        VAT_amount = base_total * self.__VAT_rate
        return base_total + VAT_amount

    def generate_invoice_details(self):
        # Generates itemized details of the invoice
        invoice_details = "Invoice for Order on " + self.__order.get_order_date() + ": "
        for ebook in self.__order.get_ebooks():
            invoice_details += ebook.get_title() + " - " + str(ebook.get_price()) + " "
        invoice_details += "Subtotal: " + str(self.__order.get_final_price()) + " "
        invoice_details += "VAT (" + str(self.__VAT_rate * 100) + "%): " + str(self.__total_amount - self.__order.get_final_price()) + " "
        invoice_details += "Total: " + str(self.__total_amount)
        return invoice_details

    def __str__(self):
        return "Invoice Total: " + str(self.__total_amount) + ", VAT Rate: " + str(self.__VAT_rate * 100) + "%"
