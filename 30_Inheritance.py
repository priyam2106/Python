class Animal:
    location="Australia"
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("Generic animal sound" )

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Awwww")


# a = Animal("Dog")
# a.speak() 
d = Dog("Bruno")
d.speak()
print(d.location)
