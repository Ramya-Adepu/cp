# Write a class called Dog that has two properties: name and age. Write a constructor that takes three arguments self, name and age and set these to the object properties.
# Now write a function sayHI(dog) where dog is the dog class object that returns a Hi, my name is <dog’s name> and I am <age> years old!

# sayHi(d1) # Hi, my name is Dot and I am 4 years old!
# sayHi(d2) # Hi, my name is Elf and I am 3 years old!

class SayHi(object):
   def __init__(self, name, age):
       self.name = name
       self.age = age
  
   def sayHi1(details):
       print(f'Hi, my name is {details.name} and I am {details.age} years old!')
 
d1 = SayHi('Dolly', 4)
d2 = SayHi('pinky', 3)
 
d1.sayHi1()
d2.sayHi1()

