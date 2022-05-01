


class Car:
    #feature
    # manufacturer = None
    # model = None
    # year = None
    # price = None
    # has_abc = None

    def __init__(self, manufacturer, model, year, price, has_abc):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.price = price
        self.has_abc = has_abc

    #methods

    def show_details(self):
        print("Manufacturer: " + self.manufacturer +
              "\nModel: " + self.model +
              "\nYear: " + str(self.year) +
              "\nPrice: " + str(self.price))

    def print_abs(self):
        if self.has_abc:
            print("Yes, I have abs")
        else:
            print("No, I don't have abs")