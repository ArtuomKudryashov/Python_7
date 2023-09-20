class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname= surname

    def hello(self):
        return f'Hello, my name is {self.name} {self.surname}'


    def walk(self):
        return 'I can walk'

    def set_name(self, new_name):
         self.name = new_name


person_1= Person('Alex', 'Baker')
print(person_1.name)
print(person_1.surname)
print(person_1.hello())
print(person_1.walk())





person_2=Person('Anna', 'Smith')
print(person_2.name)
print(person_2.surname)
print(person_2.hello())
print(person_2.walk())

class Tester(Person):

    def __init__(self, name, surname, framework):
        super(). __init__(name,surname)
        self.framework = framework

    def test(self):
        return 'I love testing'

tester_1 =Tester('Max', 'Popov','pytest')


print(tester_1.name)
print(tester_1.framework)
print(tester_1.hello())
print("Examp")
print(person_1.__dict__)

people = [person_1, person_2, tester_1]
print(person_1.surname)
print("<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>")

for person in people:
    print(person.name)
    if isinstance(person, Tester):
        print(person.name)
    # print(person.hello())
    if isinstance(person, person_1):
        print(person_1.name)

    # print()
    # if person == person_1:
    #     print(person_1.name)


# person_1.set_name("Anna")
# print(person_1.hello())
