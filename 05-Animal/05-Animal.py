class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        print "** walk"
        self.health -= 1
        return(self)
    def run(self):
        print "** run"
        self.health -= 5
        return(self)
    def display_health(self):
        print "** Display Health"
        print "{} is having {} health.".format(self.name, self.health)
        return(self)

class Dog(Animal):
    def __init__(self, name):
        self.name = name
        self.health = 150
    def pet(self):
        self.health += 5
        return self
    

class Dragon(Animal):
    def __init__(self, name):
        self.name = name
        self.health = 170
    def fly(self):
        self.health -=10
        return self
    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a Dragon"

print "--->"
dog0 = Animal("Sunspot",100)
dog0.walk().walk().walk().run().run().display_health()
print "--->"
dog1 = Dog("Max")
dog1.display_health()
dog1.pet().display_health()
print "--->"
dog2 = Dragon("buddy")
dog2.display_health()
dog2.fly().display_health()
print "--->"
dog3 = Animal("Duke",50)
dog3.display_health()
# dog3.pet().display_health()
# dog3.fly().display_health()
# dog1.fly()