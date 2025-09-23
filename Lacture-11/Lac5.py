class Animal:
    def __init__(self,name):
        self.name = name
        
    def speak(self, sound):
        return 'Some Sound'
    
class Dog(Animal):
    def speak(self):
        return f'{self.name} say woof'
class Cat(Animal):
    def speak(self):
        return f'{self.name} say meow'
    
dog = Dog('Black')
cat = Cat('Wiskey')

print(dog.speak())
print(cat.speak())