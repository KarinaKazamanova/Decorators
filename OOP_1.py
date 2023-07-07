# 📌Создайте класс окружность. 
# 📌Класс должен принимать радиус окружности при создании экземпляра. 
# 📌У класса должно быть два метода, возвращающие длину окружности и её площадь.



# 📌Создайте класс прямоугольник. 
# 📌Класс должен принимать длину и ширину при создании экземпляра. 
# 📌У класса должно быть два метода, возвращающие периметр и площадь. 
# 📌Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.



import random


class Square:

    

    def __init__(self, a, b=None):
        
        self.a = a
        if b:
            
            self.b = b
        else:
            
            self.b = a

    def square(self):
        return self.a * self.b
    
    def perimeter(self):
        return 2*(self.a + self.b)
    



# 📌Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор. 
# 📌У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор. 
# 📌Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.


class Person:

    def __init__(self, first_name, second_name, last_name, phone, age):
        self.first_name = first_name
        self.secondt_name = second_name
        self.last_name = last_name
        self._age = age
        self.phone = phone

    def birthday(self):
        self._age += 1

    def full_name(self):

        return f"{self.last_name} {self.first_name} {self.secondt_name}"
    
    def person_age(self):
        return self._age
    

p1 = Person("Илья", "Петрович", "Иванов", 12345, 32)

# print(p1.person_age())
# p1.birthday()
# print(p1.person_age())
# print(p1.full_name())



   


# 📌Создайте класс Сотрудник. 
# 📌Воспользуйтесь классом человека из прошлого задания. 
# 📌У сотрудника должен быть: ○шестизначный идентификационный номер ○уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
    

class Stuff(Person):

    def __init__(self, *args, **kwargs):
        self.id = random.randint(100000, 999999)
        super().__init__(*args, **kwargs)

    @property #Защищает от изменений, делает из метода атрибут, 
    def access_lvl(self):
        str_id = str(self.id)
        list_id_numbers = sum(list(map(int, str_id)))
        return  list_id_numbers % 7
        


s1 = Stuff("Илья", "Петрович", "Иванов", 12345, 32)

print(f"{s1.id = }, {s1.access_lvl = }")
# s1 = Square(3)
# s2 = Square(1,2)

# print(s1.a, s1.b)
# print(s2.a, s2.b)


class Animal:
    def __init__(self, name:str=None, breed:str='unknown', age: int = 0):
        self.name = name
        self.breed = breed
        self.age = age

    def print_specific(self):
        return f'Специфические данные'

class Dog(Animal):
    def __init__(self, name:str=None, breed:str='unknown', commands: list[str] = 'unknown'):
        super().__init__(name, breed)
        # self.name = name
        # self.breed = breed
        self.commands = commands

    def print_specific(self):
        return f'{self.commands}'

class Fish(Animal):
    def __init__(self, name: str = None, breed: str = 'unknown', count_fins: int = 0):
        super().__init__(name, breed)
        # self.name = name
        # self.breed = breed
        self.count_fins = count_fins

    def print_specific(self):
        return f'{self.count_fins}'

class Bird(Animal):
    def __init__(self, name: str = None, breed: str = 'unknown', count_flights: int = 0):
        super().__init__(name, breed)
        # self.name = name
        # self.breed = breed
        self.count_flights = count_flights

    def print_specific(self):
        return f'{self.count_flights}'




if __name__ == '__main__':
    dog = Dog('Kat', 'Husky', ['Голос', 'Сидеть'])
    fish = Fish('Nemo', 'Gold Fish', 3)
    bird = Bird('Kesha', 'Попугай', 2)
    animal = Animal('Lexa', 'Cat', 12)
    print(animal.print_specific())
    print(dog.print_specific())
    print(fish.print_specific())
    print(bird.print_specific())


    