##Classes inheritance##
#definition

class Person:
    def __init__(self, firstname="Luchito", lastname="Montero", age="250", country="Israel", city="Jerusalem"):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f'{self.firstname} {self.lastname} tiene {self.age} años. El vive en {self.city}, {self.country}.'

    def add_skill(self, skill):
        self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('Html')
p1.add_skill('JavaScript')
p1.add_skill('CSS')
print(p1.skills)

class Student(Person): #Sobre escribiendo el metodo padre
    def __init__(self, firstname="Maria", lastname="Vallejo", age="25", country="Ecuador", city="Guayaquil", gender="Femenino"):
        self.gender = gender
        super().__init__(firstname, lastname, age, country, city)

    def person_info(self):
        gender = "Ella " if self.gender == 'Femenino' else 'El'
        return f"{self.firstname} {self.lastname} tiene {self.age} años. {gender} vive en {self.city}, {self.country}"

s1 = Student('David', 'Diamond', '68', 'Bolivia', 'Sucre', 'Masculino')
print(s1.person_info())
s1.add_skill('Periodista')
s1.add_skill('Conferencista')
print(s1.skills)