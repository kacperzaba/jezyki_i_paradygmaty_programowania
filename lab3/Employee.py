class Employee:
    def __init__(self, firstName, lastName, age, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.salary = salary

    def getInfo(self):
        return f"Pracownik: {self.firstName} {self.lastName} \t wiek: {self.age} \t wynagroedzenie: {self.salary}"
    
pracownik = Employee("jan", "nowak", 21, 3500)
print(pracownik.getInfo)