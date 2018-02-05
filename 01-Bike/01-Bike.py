class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def display_info(self):
        print "Price: ", self.price
        print "Max Speed: ", self.max_speed
        print "Total Miles: ", self.miles
        return(self)
    def ride(self):
        self.miles += 10
        print "Riding... and your new total mileage: ", self.miles
        return(self)
    def reverse(self):
        if self.miles <= 5:
            print "Stop, you can't reverse anymore!"
            return(self)
        self.miles -= 5
        print "Reversing... and your new total mileage: ", self.miles
        return(self)


# print "*****"
# bike0 = Bike(200,"25mph")
# print "*****"
# print bike0.price
# print bike0.max_speed
# print bike0.miles
# print "*****"
# bike0.display_info()
# print "*****"
# bike0.ride()
# bike0.display_info()
# bike0.reverse()
# bike0.display_info()
print "*****"
bike1 = Bike(200,"25mph")
bike1.ride().ride().ride().reverse().display_info()
print "*****"
bike2 = Bike(200,"25mph")
bike2.ride().ride().reverse().reverse().display_info()
print "*****"
bike3 = Bike(200,"25mph")
bike3.reverse().reverse().reverse().display_info()


