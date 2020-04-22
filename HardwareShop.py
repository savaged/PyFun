# HardwareShop.py
# Saskia Savage 20/04/2020

VAT_RATE = 0.15


class Product:

    discount = 0

    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    # b. Calculate Total (cost by quantity)
    def calcTotal(self, quantity):
        return self.cost * quantity

    # c. Calculate discount (per product type)
    def calcDiscount(self, quantity):
        total = self.calcTotal(quantity)
        return self.discount * total

    def calcDiscountedTotal(self, quantity):
        total = self.calcTotal(quantity)
        discountValue = self.calcDiscount(quantity)
        return total - discountValue

    # d. Calculate VAT (15% (total - discount))
    def calcVAT(self, quantity):
        discounted = self.calcDiscountedTotal(quantity)
        return discounted * VAT_RATE

    # e. Calculate payment due (total - discount + VAT)
    def calcPaymentDue(self, quantity):
        discounted = self.calcDiscountedTotal(quantity)
        vat = self.calcVAT(quantity)
        paymentDue = discounted + vat
        return round(paymentDue, 2)


class Gardening(Product):

    discount = 0.05


class Home(Product):

    discount = 0.08


class Building(Product):

    discount = 0.09


def outputProductPaymentDue(product, quantity):
    print(str(quantity) +
          " x " + product.description +
          " cost: " +
          str(product.calcPaymentDue(quantity)))


def getProductFromTypeSelection():
    while True:
        print("Select product type number from options below:")
        print("\t1) Home")
        print("\t2) Building")
        print("\t3) Gardening")
        productType = input("Type number: ")
        if productType == "1":
            return createHomeProduct()
        elif productType == "2":
            return createBuildingProduct()
        elif productType == "3":
            return createGardeningProduct()


def createHomeProduct():
    descriptionInput = input("Product description: ")
    priceInput = getPriceInput()
    product = Home(descriptionInput, priceInput)
    return product


def createBuildingProduct():
    descriptionInput = input("Product description: ")
    priceInput = getPriceInput()
    product = Building(descriptionInput, priceInput)
    return product


def createGardeningProduct():
    descriptionInput = input("Product description: ")
    priceInput = getPriceInput()
    product = Gardening(descriptionInput, priceInput) 
    return product


def getPriceInput():
    while True:
        priceInput = input("Product price: ")
        try:
            price = float(priceInput)
        except ValueError:
            print("A monetary value is required")
        if isinstance(price, float):
            break
    return price


def getProductQuantity():
    while True:
        quantityInput = input("Product quantity: ")
        try:
            quantity = int(quantityInput)
        except ValueError:
            print("An integer value is required")
        if isinstance(quantity, int):
            break
    return quantity


def main():
    # Test Data:
    #
    # product = Home("Taps", 12.99)
    # quantity = 3
    #
    # product = Building("Bricks", 1.89)
    # quantity = 300
    #
    # product = Gardening("Shovel", 11.20)
    # quantity = 2
    #
    # product = Home("Bath tubs", 120)
    # quantity = 2
    while True:
        product = getProductFromTypeSelection()
        quantity = getProductQuantity()
        outputProductPaymentDue(product, quantity)
        repeatInput = input("Repeat? (y/n):")
        if repeatInput != "y":
            break


if __name__ == "__main__":
    main()
