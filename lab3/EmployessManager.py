from Employee import Employee

class EmployessManager:
    def __init__(self): # konstruktor bezparametrowy
        self.employess = []

    def add_Employess(self):
        print('Podaj dane pracownika: ')
        firstName = input("Podaj imie: ")
        lastName = input("Podaj nazwisko: ")
        age = input("Podaj wiek: ")
        salary = input("Podaj wynagrodzenie: ")
        self.employess.append(Employee(firstName, lastName, age, salary))

    def view_Employess(self):
        if len(self.employess) == 0:
            print("\n brak pracownikow w bazie")
            return
        else:
            for emp in self.employess:
                print(emp)

    def delete_Employess(self, age_from, age_to):
        for emp in self.employess:
            if age_from <= emp.age <= age_to:
                print(f"\y usunieto pracowniak: {emp.name}")
                self.employess.remove(emp)
                self.employess.remove(emp)

    def find_Employess(self, firstName, lastName):
        for emp in self.employess:
            if emp.firstName == firstName and emp.lastName == lastName:
                return emp
            return None
        
    def update_salary_Employess(self, firstName, lastName, salary):
        emp = self.find_Employess(firstName, lastName)
        if emp is None:
            print("blad: nie znaleziono pracownika")
        else:
            emp.salary = salary