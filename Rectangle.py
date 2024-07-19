class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def display_details(self):
        area = self.calculate_area()
        perimeter = self.calculate_perimeter()
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Area: {area}")
        print(f"Perimeter: {perimeter}")

# Main program
if __name__ == "__main__":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    rectangle = Rectangle(length, width)
    rectangle.display_details()