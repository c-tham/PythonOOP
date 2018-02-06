class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
        self.display_info()
    def sell(self):
        print "Item sold"
        self.tax(0.05)
        self.status = 'sold'
        self.display_info()
        return(self)
    def tax(self, tax):
        self.tax = tax
        print "Sale Tax: ", self.tax
        print "Tax Amount: ", self.price * self.tax
        if self.tax == 0:
            print "Tax cannot be zero!"
            return(self)
        self.price = self.price + (self.price * self.tax)
        return(self)
    def returnitem(self, reason):
        self.reason = reason
        print "Item return: ", self.reason
        if self.reason == 'defective':
            self.status = 'defective'
            self.price = 0
        elif self.reason == 'box':
            self.status = 'for sale'
        elif self.reason == 'opened':
            self.status = 'used'
            self.price = self.price * 0.8
        self.display_info()
        return(self)
    def display_info(self):
        print "Item Name: ", self.item_name
        print "Item Brand: ", self.brand
        print "Item Price: ", self.price
        print "Item Weight: ", self.weight
        print "Item status: ", self.status
        print "****************************"
        return(self)

# phone1 = Product(500,"Iphone7","5oz","Apple")
# phone1.sell().display_info()
# phone1.returnitem("opened").display_info()

phone1 = Product(500,"Iphone7","5oz","Apple")
phone1.sell()
phone1.returnitem("opened")
phone2 = Product(600,"Iphone8","5oz","Apple")
phone2.sell()
phone2.returnitem("box")
phone3 = Product(700,"IphoneX","5oz","Apple")
phone3.sell()
phone3.returnitem("defective")