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
        if quantity < 1:
            return 0
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


def main():

    product = Home("Taps", 12.99)
    quantity = 3
    outputProductPaymentDue(product, quantity)

    product = Building("Bricks", 1.89)
    quantity = 300
    outputProductPaymentDue(product, quantity)

    product = Gardening("Shovel", 11.20)
    quantity = 2
    outputProductPaymentDue(product, quantity)

    product = Home("Bath tubs", 120)
    quantity = 2
    outputProductPaymentDue(product, quantity)


if __name__ == "__main__":

    main()
