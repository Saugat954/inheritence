
class Employee:
    def __init__(self, name,id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")

#using inheritance
class Programmar(Employee):
    def showLang(self):
        print("The default language is Python")

employee1 = Employee("saugat",101)
employee1.showDetails()

employee2 = Programmar("Saugat",200)
employee2.showDetails()
employee2.showLang()