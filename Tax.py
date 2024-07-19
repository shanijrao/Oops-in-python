class Company:
    def __init__(self, name, cost_price, selling_price, tax_rate):
        self.name = name
        self.cost_price = cost_price
        self.selling_price = selling_price
        self.tax_rate = tax_rate

    def calculate_profit_or_loss(self):
        if self.selling_price > self.cost_price:
            return self.selling_price - self.cost_price, "Profit"
        elif self.selling_price < self.cost_price:
            return self.cost_price - self.selling_price, "Loss"
        else:
            return 0, "No Profit No Loss"

    def calculate_tax(self, amount):
        return amount * self.tax_rate / 100

    def display_details(self):
        amount, status = self.calculate_profit_or_loss()
        tax = self.calculate_tax(amount)
        print(f"Company Name: {self.name}")
        print(f"Cost Price: {self.cost_price}")
        print(f"Selling Price: {self.selling_price}")
        print(f"Status: {status}")
        print(f"Amount: {amount}")
        print(f"Tax: {tax}")

# Taking inputs from the user
name = input("Enter the company name: ")
cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))
tax_rate = float(input("Enter the tax rate (%): "))

# Creating an instance of the Company class
company = Company(name, cost_price, selling_price, tax_rate)

# Displaying the details
company.display_details()
