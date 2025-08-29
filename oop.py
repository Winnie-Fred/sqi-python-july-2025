# OOP - Object Oriented Programming


# Programming paradigm
# A paradigm is a way of doing things

# Functional Programming Paradigm
# Modular


# Classes and Instances/Objects
# uppercase camel-casing
# class BankAccount:
#     # dunder init - double underscore
#     def __init__(self, account_holder, account_balance, bank_name, is_savings):
#         self.account_holder_full_name = account_holder
#         self.account_balance = account_balance
#         self.bank_name = bank_name
#         self.is_savings = is_savings

#     def account_details(self):
#         print(f"Account holder: {self.account_holder_full_name}")
#         print(f"Account balance: {self.account_balance}")
#         print(f"Bank name: {self.bank_name}")
#         print("Savings" if self.is_savings else "Current", "Account")


# olaitan_bank_acct = BankAccount("Oladipupo Olaitan", 70_000_000, "Opay", True)
# dan_bank_acct = BankAccount("Adesanya Daniel", 100_000_000, "Access", False)

# olaitan_bank_acct.account_details()
# dan_bank_acct.account_details()


# print(olaitan_bank_acct.bank_name)

# olaitan_bank_acct.bank_name = "First Bank"

# olaitan_bank_acct.account_holder_full_name

# print(olaitan_bank_acct.bank_name)
# print(type(olaitan_bank_acct))
# print(type(dan_bank_acct))


# num = 4
# print(type(num))


# num = int("4")


# class Book:
#     def __init__(self, author, title, no_of_pages, isbn, cost, year_published, is_available, genre):
#         self.year_published = year_published
#         self.author = author
#         self.title = title
#         self.genre = genre
#         self.isbn = isbn
#         self.cost = cost
#         self.no_of_pages = no_of_pages
#         self.is_book_available = is_available


#     def check_book_pages(self):
#         return f"{self.title} has {self.no_of_pages} pages"
    
#     def apply_discount(self, percentage):
#         discount = (percentage / 100) * self.cost
#         return self.cost - discount
    



# holy_bible = Book("Jehovah's Witnesses", "Holy Bible", 2000, "789-678-568-567", 1000, 1501, True, "Spirituality")
# and_then_there_were_none = Book("Agatha Christie", "And then there were None", 400, "987-778-233-789", 29.99, 1976, False, "Fiction")

# print(holy_bible.check_book_pages())
# print(and_then_there_were_none.check_book_pages())

# print("Original cost:", and_then_there_were_none.cost)
# print("New Discounted cost:", and_then_there_were_none.apply_discount(20))



# class Person:
#     def __init__(self, age):
#         self._age = age


#     # getter
#     @property
#     def age(self):
#         return self._age

#     # setter
#     @age.setter
#     def age(self, value):
#         if value < 1:
#             raise ValueError("Age must be positive")
    
#         self._age = value

    
# olaitan = Person(12)
# print(olaitan.age)
# olaitan.age = 100
# print(olaitan.age)
# olaitan.age = -6
# print(olaitan.age)



# ==============================
# EXERCISE 1: MOVIE CLASS
# ==============================
# CLASS NAME: Movie
#
# ATTRIBUTES:
#   - title
#   - director
#   - duration (in minutes)
#   - year_released
#   - rating (out of 10)
#
# METHODS:
#   1. movie_summary() 
#        -> returns a string summary of the movie
#
#   2. update_rating(new_rating)
#        -> updates the movie rating to new_rating
#
#   3. is_long_movie()
#        -> returns True if duration > 150 minutes, else False
#


# class Movie:
#     def __init__(self, title, director, duration, year_released, rating):
#         self.title = title
#         self.director = director
#         self.duration = duration
#         self.year_released = year_released
#         self.rating = rating

#     def movie_summary(self):
#         return f"{self.title} ({self.year_released}), directed by {self.director}, rated {self.rating}/10"

#     def update_rating(self, new_rating):
#         self.rating = new_rating
#         return "Rating updated successfully"

#     def is_long_movie(self):
#         return self.duration > 150

# # ------------------------------
# # SAMPLE EXECUTION:
# #
# avengers = Movie("Avengers: Endgame", "Anthony & Joe Russo", 181, 2019, 8.4)
# movie_2 = Movie("Koto aye", "Alhaji Yekini Ajileye", 200, 2001, 10.0)
# #
# print(avengers.movie_summary())
# # # EXPECTED: "Avengers: Endgame (2019), directed by Anthony & Joe Russo, rated 8.4/10."
# #
# print(avengers.is_long_movie())
# # # EXPECTED: True
# #
# print(avengers.update_rating(9.0))
# print(avengers.rating)


# print(movie_2.movie_summary())
# print(movie_2.is_long_movie())
# print(movie_2.update_rating(9.0))
# print(movie_2.rating)
# ------------------------------


# ==============================
# EXERCISE 2: STUDENT CLASS
# ==============================
# CLASS NAME: Student
#
# ATTRIBUTES:
#   - name
#   - age
#   - student_id
#   - grades (a list of numbers)
#
# METHODS:
#   1. add_grade(grade)
#        -> adds a new grade to the grades list
#
#   2. calculate_average()
#        -> returns the average of all grades, or "No grades yet" if empty
#
#   3. student_summary()
#        -> returns a string with the student's name, age, ID, and current average grade


# class Student:
#     def __init__(self, name: str, age: int, student_id: str, grades: list[int]):
#         self.name = name
#         self.age = age
#         self.student_id = student_id
#         self.grades = grades

#     def add_grade(self, grade):
#         self.grades.append(grade)

#     def calculate_average(self):
#         if not self.grades:
#             return "No grades yet"
#         return sum(self.grades) / len(self.grades)
    
#     def student_summary(self):
#         return f"{self.name} ({self.age} years old, ID: {self.student_id}) has an average grade of {self.calculate_average()}."

    

# # ------------------------------
# # SAMPLE EXECUTION:
# #
# john = Student("John Doe", 16, "S12345")

# john.add_grade(85)
# john.add_grade(90)
# john.add_grade(78)

# print(john.calculate_average())
# # # EXPECTED: 84.333... (depending on rounding)
# #
# print(john.student_summary())
# # # EXPECTED: "John Doe (16 years old, ID: S12345) has an average grade of 84.33."
# #
# empty_student = Student("Alice", 15, "S54321", [])
# print(empty_student.calculate_average())
# # EXPECTED: "No grades yet"
# ------------------------------


# OOP vs Primitive Data Types

# john = {
#     "name": "John Doe",
#     "age": 16,
#     "student_id": "S12345",
#     "grades": []
# }

# fatima = {
#     "name": "Fatima Bello",
#     "age": 15,
#     "student_id": "S67890",
#     "grades": []
# }

# def add_grade(student, grade):
#     student["grades"].append(grade)

# def calculate_average(student):
#     if not student["grades"]:
#         return "No grdes yet"
#     return sum(student["grades"]) / len(student["grades"])

# def student_summary(student):
#     return f"{student["name"]} ({student["age"]} years old, ID: {student["student_id"]}) has an average grade of {calculate_average(student)}."



# add_grade(john, 85)
# add_grade(john, 90)
# add_grade(john, 78)

# print(calculate_average(john))
# # # EXPECTED: 84.333... (depending on rounding)
# #
# print(student_summary(john))
# # # EXPECTED: "John Doe (16 years old, ID: S12345) has an average grade of 84.33."
# #
# print(calculate_average(fatima))
# EXPECTED: "No grades yet"


# class Book:
#     def __init__(self, author, title, no_of_pages, isbn, cost, year_published, is_available, genre):
#         self.year_published = year_published
#         self.author = author
#         self.title = title
#         self.genre = genre
#         self.isbn = isbn
#         self.cost = cost
#         self.no_of_pages = no_of_pages
#         self.is_book_available = is_available


#     def check_book_pages(self):
#         return f"{self.title} has {self.no_of_pages} pages"
    
#     def apply_discount(self, percentage):
#         discount = (percentage / 100) * self.cost
#         return self.cost - discount
    

# class Library:
#     def __init__(self, books: list[Book]):
#         self.books = books



# holy_bible = Book("Jehovah's Witnesses", "Holy Bible", 2000, "789-678-568-567", 1000, 1501, True, "Spirituality")
# and_then_there_were_none = Book("Agatha Christie", "And then there were None", 400, "987-778-233-789", 29.99, 1976, False, "Fiction")
# community_library = Library([holy_bible, and_then_there_were_none])



# ==============================
# EXERCISE 4: TEACHER & CLASSROOM
# ==============================
# CLASS NAME: Teacher
#
# ATTRIBUTES:
#   - name
#   - subject
#
# METHODS:
#   1. introduce()
#        -> returns a string introducing the teacher with their subject

# class Teacher:
#     def __init__(self, name, subject):
#         self.name = name
#         self.subject = subject


#     def introduce(self):
#         return f"Hello, I am {self.name} and I teach {self.subject}."        


# ------------------------------
# CLASS NAME: Classroom
#
# ATTRIBUTES:
#   - teacher (a Teacher object)
#   - students (a list of student names)
#
# METHODS:
#   1. add_student(student_name)
#        -> adds a student to the classroom
#
#   2. classroom_summary()
#        -> returns a string with the teacher's name, subject, and number of students

# class Classroom:
#     def __init__(self, teacher: Teacher, students: list[str]):
#         self.teacher = teacher
#         self.students = students

#     def add_student(self, student_name):
#         self.students.append(student_name)

#     def classroom_summary(self):
#         # print(self.teacher)
#         return f"Classroom taught by {self.teacher.name} ({self.teacher.subject}) has {len(self.students)} students."

# # ------------------------------
# # SAMPLE EXECUTION:
# #
# mr_smith = Teacher("Mr. Smith", "Mathematics")
# math_class = Classroom(mr_smith, [])
# #
# math_class.add_student("Alice")
# math_class.add_student("Bob")
# #
# print(mr_smith.introduce())
# # # EXPECTED: "Hello, I am Mr. Smith and I teach Mathematics."
# #
# print(math_class.classroom_summary())
# # # EXPECTED: "Classroom taught by Mr. Smith (Mathematics) has 2 students."
# # ------------------------------


# ==============================
# EXERCISE 5: CUSTOMER & ORDER
# ==============================
# CLASS NAME: Customer
#
# ATTRIBUTES:
#   - name
#   - email
#
# METHODS:
#   1. customer_info()
#        -> returns a string with the customer's name and email

# class Customer:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email

#     def customer_info(self):
#         return f"Customer: {self.name}, Email: {self.email}"        


# # ------------------------------
# # CLASS NAME: Order
# #
# # ATTRIBUTES:
# #   - customer (a Customer object)
# #   - items (a list of item names)
# #
# # METHODS:
# #   1. add_item(item_name)
# #        -> adds an item to the order
# #
# #   2. order_summary()
# #        -> returns a string with the customer's name and how many items they ordered

# class Order:
#     def __init__(self, customer: Customer, items: list[str]):
#         self.customer = customer
#         self.items = items

#     def add_item(self, item_name):
#         self.items.append(item_name)

#     def order_summary(self):
#         return f"Order for {self.customer.name} has {len(self.items)} items."



# # ------------------------------
# # SAMPLE EXECUTION:
# #
# john = Customer("John Doe", "john@example.com")
# order1 = Order(john, [])

# order1.add_item("Laptop")
# order1.add_item("Mouse")

# print(john.customer_info())
# # EXPECTED: "Customer: John Doe, Email: john@example.com"

# print(order1.order_summary())
# # EXPECTED: "Order for John Doe has 2 items."
# # ------------------------------



# class Teacher:

#     is_wicked = True

#     def __init__(self, name, subject):
#         self.name = name
#         self.subject = subject


#     def introduce(self):
#         return f"Hello, I am {self.name} and I teach {self.subject}."   


# mr_smith = Teacher("Mr. Smith", "Mathematics")
# miss_winnie = Teacher("Miss Winnie", "Python")

# print(mr_smith.name)
# print(miss_winnie.name)

# print(mr_smith.is_wicked)
# Teacher.is_wicked = False
# print(mr_smith.is_wicked)

# print(miss_winnie.is_wicked)


# class Circle:

#     PI = 22/7

#     def __init__(self, radius):
#         self.radius = radius
#         # self.circumeference = 2 * self.PI * self.radius
#         # self.circumeference = 2 * Circle.PI * self.radius

#     @property
#     def circumference(self):
#         return 2 * Circle.PI * self.radius


# circle_one = Circle(5)
# print(circle_one.PI)
# print(circle_one.radius)
# print(circle_one.circumference)




# You are building a simple simulation of a fantasy battle. Create different types of game 
# characters.

# 1. Create a base class
# Create a class called GameCharacter that has:
# Attributes:
# name (string)
# health (integer)
# attack_power (integer)

# Methods:
# A method attack(target) that reduces the target's health by self.attack_power.

# 2. Create subclasses
# Warrior
# Has an extra attribute: armor (integer)
# Override attack(target) so that it deals extra 10 damage.

# Mage
# Has an extra attribute: mana (integer)
# Override attack(target) so that it uses 5 mana each time it attacks. 
# If mana is less than 5, print "Not enough mana to attack".

# 3. Handle cases where the target is the same as the attacker.



# SAMPLE EXECUTION 1
# warrior = Warrior(name="Thor", health=100, attack_power=10, armor=20)
# mage = Mage(name="Merlin", health=100, attack_power=10, mana=10)
# warrior.attack(mage)
# # Output:
# # Thor attacks Merlin!
# # Merlin's health is now 80
# mage.attack(warrior)
# # Output:
# # Merlin attacks Thor!
# # Thor's health is now 90
# mage.attack(warrior)
# # Output:
# # Merlin attacks Thor!
# # Thor's health is now 80
# mage.attack(warrior)
# # Output:
# # Not enough mana to attack
# print(warrior.health)  # 80
# print(mage.health)  # 80
# print(mage.mana)  # 0



# # SAMPLE EXECUTION 2
# merlin = Mage(name="Merlin", health=100, attack_power=20, mana=10)
# gaius = Mage(name="Gaius", health=100, attack_power=10, mana=30)

# merlin.attack(gaius)
# # Output:
# # Merlin attacks Gaius
# # Gaius’s health is now 80
# gaius.attack(merlin)
# # Output:
# # Gaius attacks Merlin
# # Merlin’s health is now 90
# gaius.attack(gaius)
# # Output:
# # Gaius cannot attack themself
# gaius.attack(merlin)
# # Output:
# # Gaius attacks Merlin
# # Merlin’s health is now 80
# merlin.attack(gaius)
# # Output:
# # Merlin attacks Gaius
# # Gaius’s health is now 60
# merlin.attack(gaius)
# # Output:
# # Not enough mana to attack




# Create a class called CartItem.
# A CartItem has a name, a price, and a quantity
# Also create a class called Cart
# A cart is a list of CartItems
# A cart can print the total price of CartItems in it



# cart_item1 = CartItem("eggs", 250, 4)
# cart_item2 = CartItem("bread", 1200, 6)
# print(cart_item1.total_price()) # -> 1000
# print(cart_item2.total_price()) # -> 7200
# cart = Cart([cart_item1, cart_item2])
# print(cart.total()) # -> 8200

# instance attribute outside __init__()
# class Customer:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email

#     def customer_info(self):
#         self.new_var = "new variable"
#         return f"Customer: {self.name}, Email: {self.email}"
    
#     def some_method(self):
#         return f"Value of new_var: {self.new_var}"
    
# customer = Customer("Winnie", "winnie@gmail.com")
# print(customer.some_method())  # AttributeError
# print(customer.customer_info())


# class Customer:
#     def __init__(self, name, email):
#         print("inside", self)
#         self.name = name
#         self.email = email
#         self.new_var = "new variable"

#     def customer_info(self):
#         return f"Customer: {self.name}, Email: {self.email}"
    
#     def some_method(self):
#         return f"Value of new_var: {self.new_var}"


# customer = Customer("Winnie", "winnie@gmail.com")
# print("Outside", customer)
# print(customer.customer_info())


# class Animal:
#     def __init__(self, name: str, type: str, color: str, is_mammal: bool):
#         self.name = name
#         self.type = type
#         self.color = color
#         self.is_mammal = is_mammal

#     def describe_yourself(self):
#         article = "an" if self.type.startswith(("a", "e", "i", "o", "u")) else "a"
#         animal_is_mammal = "" if self.is_mammal else "not "
#         return f"I am {self.name}, {article} {self.type}. My color is {self.color} and I am {animal_is_mammal}a mammal"
    

# from datetime import datetime

# now = datetime.now().year

# class Dog(Animal):
#     # def __init__(self, name, color):
#     #     super().__init__(name, "dog", color, True)
    
    
#     # def __init__(self, breed, age):
#     #     self.breed = breed
#     #     self.age = age

#     def __init__(self, name, color, breed, age):
#         self.color = "black and white"
#         self.breed = breed
#         self.age = age
#         super().__init__(name, "dog", color, True)

#     def get_birth_year(self):
#         return now - self.age
    
#     def describe_yourself(self):
#         return f"I am {self.name}, a {self.type}. My color is {self.color} and I am a mammal. Breed: {self.breed}, I was born in {self.get_birth_year()} "

# lion = Animal("Simba", "lion", "brown", True)
# chicken = Animal("Clucky", "chicken", "white", False)
# print(lion.describe_yourself())
# # print(chicken.describe_yourself())

# dog = Dog("Bingo", "black", "German Shepherd", 2)
# # print(dog.name)
# # print(dog.type)
# print(dog.describe_yourself())
# # print(dog.get_birth_year())
# # print(lion.get_birth_year())  # AttributeError





# ==============================
# EXERCISE 7: VEHICLE & CAR
# ==============================
# CLASS NAME: Vehicle
#
# ATTRIBUTES:
#   - brand
#   - model
#   - year
#
# METHODS:
#   1. vehicle_info()
#        -> returns a string like: "<year> <brand> <model>"
#
#   2. start_engine()
#        -> returns a string like: "The vehicle's engine is starting..."
#
# ------------------------------
# CLASS NAME: Car (inherits from Vehicle)
#
# ATTRIBUTES (overrides init):
#   - brand (inherited)
#   - model (inherited)
#   - year (inherited)
#   - doors (new attribute, number of doors)
#
# METHODS (override):
#   1. start_engine()  (override)
#        -> returns a string like: "The car <brand> <model> engine roars to life!"
#
#   2. vehicle_info()  (override)
#        -> returns a string with the vehicle details PLUS number of doors
#
# ------------------------------
# SAMPLE EXECUTION:
#
# generic_vehicle = Vehicle("GenericBrand", "ModelX", 2000)
# print(generic_vehicle.vehicle_info())
# # EXPECTED: "2000 GenericBrand ModelX"
#
# print(generic_vehicle.start_engine())
# # EXPECTED: "The vehicle's engine is starting..."
#
# my_car = Car("Toyota", "Corolla", 2022, 4)
# print(my_car.vehicle_info())
# # EXPECTED: "2022 Toyota Corolla with 4 doors"
#
# print(my_car.start_engine())
# # EXPECTED: "The car Toyota Corolla engine roars to life!"
# ------------------------------


# You are building a simple simulation of a fantasy battle. Create different types of game 
# characters.

# 1. Create a base class
# Create a class called GameCharacter that has:
# Attributes:
# name (string)
# health (integer)
# attack_power (integer)

# Methods:
# A method attack(target) that reduces the target's health by self.attack_power.

# class GameCharacter:
#     def __init__(self, name, health, attack_power):
#         self.name = name
#         self.health = health
#         self.attack_power = attack_power

#     def attack(self, target):
#         if self == target:
#             print(f"{self.name} cannot attack themself")
#             return
#         print(f"{self.name} attacks {target.name}!")
#         target.health -= self.attack_power
#         print(f"{target.name}'s health is now {target.health}")


# # 2. Create subclasses
# # Warrior
# # Has an extra attribute: armor (integer)
# # Override attack(target) so that it deals extra 10 damage.

# class Warrior(GameCharacter):
#     def __init__(self, name, health, attack_power, armor):
#         super().__init__(name, health, attack_power)
#         self.armor = armor

#     def attack(self, target):
#         target.health -= 10
#         super().attack(target)

# # Mage
# # Has an extra attribute: mana (integer)
# # Override attack(target) so that it uses 5 mana each time it attacks. 
# # If mana is less than 5, print "Not enough mana to attack".

# class Mage(GameCharacter):
#     def __init__(self, name: str, health: int, attack_power: int, mana: int):
#         super().__init__(name, health, attack_power)
#         self.mana = mana

#     def attack(self, target):
#         if self.mana < 5:
#             print("Not enough mana to attack")
#             return
#         super().attack(target)
#         self.mana -= 5



# # 3. Handle cases where the target is the same as the attacker.
# # SAMPLE EXECUTION 1
# warrior = Warrior(name="Thor", health=100, attack_power=10, armor=20)
# mage = Mage(name="Merlin", health=100, attack_power=10, mana=10)
# warrior.attack(mage)
# # Output:
# # Thor attacks Merlin!
# # Merlin's health is now 80
# mage.attack(warrior)
# # Output:
# # Merlin attacks Thor!
# # Thor's health is now 90
# mage.attack(warrior)
# # Output:
# # Merlin attacks Thor!
# # Thor's health is now 80
# mage.attack(warrior)
# # Output:
# # Not enough mana to attack
# print(warrior.health)  # 80
# print(mage.health)  # 80
# print(mage.mana)  # 0



# # SAMPLE EXECUTION 2
# merlin = Mage(name="Merlin", health=100, attack_power=20, mana=10)
# gaius = Mage(name="Gaius", health=100, attack_power=10, mana=30)

# merlin.attack(gaius)
# # Output:
# # Merlin attacks Gaius
# # Gaius’s health is now 80
# gaius.attack(merlin)
# # Output:
# # Gaius attacks Merlin
# # Merlin’s health is now 90
# gaius.attack(gaius)
# # Output:
# # Gaius cannot attack themself
# gaius.attack(merlin)
# # Output:
# # Gaius attacks Merlin
# # Merlin’s health is now 80
# merlin.attack(gaius)
# # Output:
# # Merlin attacks Gaius
# # Gaius’s health is now 60
# merlin.attack(gaius)
# # Output:
# # Not enough mana to attack



# class GameCharacter:
#     def __init__(self, name, health, attack_power):
#         self.name = name
#         self.health = health
#         self.attack_power = attack_power

#     def attack(self, target):
#         if self == target:
#             print(f"{self.name} cannot attack themself")
#             return
#         print(f"{self.name} attacks {target.name}!")
#         target.health -= self.attack_power
#         print(f"{target.name}'s health is now {target.health}")

# class Warrior(GameCharacter):
#     def __init__(self, name, health, attack_power, armor):
#         super().__init__(name, health, attack_power)
#         self.armor = armor

#     def attack(self, target):
#         target.health -= 10
#         super().attack(target)

# class Mage(GameCharacter):
#     def __init__(self, name: str, health: int, attack_power: int, mana: int):
#         super().__init__(name, health, attack_power)
#         self.mana = mana

#     def attack(self, target):
#         if self.mana < 5:
#             print("Not enough mana to attack")
#             return
#         super().attack(target)
#         self.mana -= 5


# # print(7 + 4)  # 11
# # print("7" + "4")  # 74
# # print(7 + 4.9)  # 11.9

# # print(len("hello"))  # 5
# # print(len([1, 89, 6789, 62, 672])) # 5


# warrior = Warrior(name="Thor", health=100, attack_power=10, armor=20)
# mage = Mage(name="Merlin", health=100, attack_power=10, mana=10)
# game_character = GameCharacter("Game Character", 50, 67)

# print(isinstance(warrior, GameCharacter))
# print(isinstance(warrior, GameCharacter))
# print(isinstance(game_character, Warrior))
# print(issubclass(Warrior, GameCharacter))

# game_characters = [warrior, mage]

# for game_character in game_characters:
#     print(f"Game character's Name: {game_character.name}")
#     print(f"Game character's health: {game_character.health}")
#     print(f"Game character's attack power: {game_character.attack_power}")



# class Device:
#     def operate(self):
#         return "Operating the device"
    
# class Phone:
#     def operate(self):
#         return "Operating the phone"
    
# class Laptop:
#     def operate(self):
#         return "Operating the laptop"
    

# device = Device()
# phone = Phone()
# laptop = Laptop()

# # print(device.operate())
# # print(phone.operate())
# # print(laptop.operate())

# print(isinstance(device, Device))
# print(isinstance(phone, Device))



# Magic Dunder Methods in Python

# class Book:
#     def __init__(self, author, title, no_of_pages, isbn, cost, year_published, is_available, genre):
#         self.year_published = year_published
#         self.author = author
#         self.title = title
#         self.genre = genre
#         self.isbn = isbn
#         self.cost = cost
#         self.no_of_pages = no_of_pages
#         self.is_book_available = is_available


#     def __str__(self):
#         return f"Book {self.title} by {self.author}."
    
#     def __repr__(self):
#         return f'Book(title="{self.title}", author="{self.author}", no_of_pages={self.no_of_pages}, isbn="{self.isbn}", cost={self.cost}, year_published={self.year_published}, is_available={self.is_book_available}, genre="{self.genre}")'
    
#     def __len__(self):
#         return self.no_of_pages

#     def check_book_pages(self):
#         return f"{self.title} has {self.no_of_pages} pages"
    
#     def apply_discount(self, percentage):
#         discount = (percentage / 100) * self.cost
#         return self.cost - discount
    

# holy_bible = Book("Jehovah's Witnesses", "Holy Bible", 2000, "789-678-568-567", 1000, 1501, True, "Spirituality")
# and_then_there_were_none = Book("Agatha Christie", "And then there were None", 400, "987-778-233-789", 29.99, 1976, False, "Fiction")

# print(repr(holy_bible))
# print(holy_bible)
# print(len(holy_bible))
# print(len(and_then_there_were_none))

# print(holy_bible.check_book_pages())
# print(and_then_there_were_none.check_book_pages())

# print("Original cost:", and_then_there_were_none.cost)
# print("New Discounted cost:", and_then_there_were_none.apply_discount(20))




# class FixedSizeList(list):
#     def __init__(self, max_size):
#         self.max_size = max_size

#     def append(self, item):
#         if len(self) > self.max_size - 1:
#             print('greater')
#             raise ValueError(f"List length cannot exceed {self.max_size}")
#         super().append(item)


# my_list = FixedSizeList(6)
# my_list.append(7)
# my_list.append(2)
# my_list.append(2)
# my_list.append(2)
# my_list.append(2)
# my_list.append(2)
# my_list.append(2)
# print(my_list)