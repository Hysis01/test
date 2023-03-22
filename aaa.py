
class Person:
    def __init__(self, name, age, car, number):
        self.name = name
        self.age = age
        self.car = car
        self.number = number

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_car(self):
        return self.car

    def get_number(self):
        return self.number

    def change_age(self, chislo):
        self.age = self.age + chislo
        return self.age
# def main():
    a = Person('пидор', 23, 'Govno', '456')
    person_name = a.get_name()
    person_age = a.get_age()
    print(person_age)
    person_age = a.change_age(4)
    #person_age = a.get_age()
    print(person_age)
    print()
# main()