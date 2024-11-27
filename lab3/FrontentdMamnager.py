from EmployessManager import *
from utility import *

class FrontedManager:
    def __init__(self):
        self.EmployessManager = EmployessManager()

    def print_menu(self):
        print("\n zarzadzanie pracownikami: \n")
        message = [
            '1. Dodaj pracownika',
            '2. Wyswietl pracownikow',
            '3. Usun pracowinika',
            '4. Akutalizacja wynagrodzen',
            '5. Wyjescie'
        ]

        print('\n'.join(message))
        msg = f"Wybierz opcje 1 - {len(message)}: "
        return inputValue(msg, 1, len(message))
    
    def run(self):
        while True:
            choice = self.print_menu()

            if choice == 1:
                self.EmployessManager.add_Employess()
            elif choice == 2:
                self.EmployessManager.view_Employess()
            elif choice == 3:
                age_from = int(input("Podaj poczatek przedzialu wieku pracownika: "))
                age_to = int(input("podaj koniec przedzialu wieku pracowniak: "))
                self.EmployessManager.delete_Employess(age_from, age_to)
            elif choice == 4:
                firstName = input("Podaj imie pracownika: ")
                lastName = input("Podaj nazwisko pracownika: ")
                salary = int(input("Podaj nowe wynagrodzienie pracownika: "))
                self.EmployessManager.update_salary_Employess(firstName, lastName, salary)
            elif choice == 5:
                break
            else:
                continue
