# mamy firme, ktora posiada pracownikow, chcemy miec rozne typy pracownikow
# kazdy bedzie miala w inny sposob obliczane wynagrodzenie(stawka godzinowa, miesięczna)

# pracownik - imie, nazwisko
# Stanowiska godzinowe  - EmployeeHourly
# Stanowska Inne - EmployeeSalary

class Employee:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name


class EmployeeHourly(Employee):
    def __init__(self,hour,stawka):
        self.hour = hour
        self.stawka = stawka

    def count_salary(self):
        hour = input("Podaj liczbę przepracowanych godzin:")
        stawka = 7.50
        salary  = int(hour)* stawka
        return salary

class EmployeeSalary(Employee):
    def __init__(self,first_name,last_name,hour,fix_base=5500):
        super().__init__(first_name,last_name)
        self.hour = hour
        self.fix_base = fix_base

    def count_salary(self):
        base = 160
        hour = input("Podaj liczbę godzin przepracowanych:")
        fix_base = 5500
        salary = int(hour)/base * fix_base
        return salary


empl1 =EmployeeSalary("Anna","Nowak",100)
#empl2 =EmployeeSalary()
print(empl1.count_salary())


