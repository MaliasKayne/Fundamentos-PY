## Classes #
#Definition
class MyEmptyPerson:
    pass #Para poder dejar la clase vacia

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias="Sin alias"): #self= representacion de la instancia u objeto a partir de la clase
        self.full_name = f"{name} {surname} ({alias})" #propiedad publica
        self.__name = name #__ = propiedad privada, Name Mangling (ocultamiento de nombres)

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} esta caminando")

my_person = Person("Jossie", "Diaz")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Jossie", "Diaz", "JossieDev")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Hector de Leon (El loco de los perros)"
print(my_other_person.full_name)