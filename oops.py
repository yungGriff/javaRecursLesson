class Animal():
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    
    def makesound(self):
        print(f"{self.name} makes {self.sound}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof")
        self.breed = breed
        
        
        
    def makesound(self):
        print(f"{self.name} makes {self.sound}")
        
    def fetch(self):
        print(f"{self.name} is fetching a ball!")
            
            
            
        
    
    
    
    
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Meow")
        self.color = color
        
    def makesound(self):
        print(f"{self.name} makes {self.sound}")


if __name__ == "__main__":
    my_dog = Dog("Buddy", "Golden Retriever")
    
    my_cat = Cat("Peaches", "Orange")

    # my_dog.makesound()
    
    # my_cat.makesound()
    
    
    
    
    my_dog.fetch()
    
    animals = [my_dog, my_cat]
        
    for animal in animals:
        animal.makesound()
