#lekarz, pacjent, kazdy lekarz ma liste pacjentow , moze wciagu 8h przyjąć 4 osob nie mozna wpisac więcej nic to
# nie wolno dopisac wiecej niz
# Doctor,Pacient, clinic , Day?
# per dzien liczba pacientow

# Clinic - mozliwość zapisywania pacjenta, per day, per_doc
#

class Day(object):
    def __init__(self,name):
        self.name = name
        self.schedule = {}

    def append(self,doctor,patient):
        if not doctor.full_name in self.schedule:
            self.schedule[doctor.full_name] = []
        self.schedule[doctor.full_name].append(patient)


class Clinic(object):

    calendar = {}

    @classmethod
    def schedule(cls,day, doctor,patient):
        "zapisuje pacjenta do doktora"
        if not day.name in cls.calendar:
            cls.calendar[day.name] = day
        cls.calendar[day.name].append(doctor,patient)

    @classmethod
    def print_per_doc(cls,first_name):
        "wyswietla pacjentow per doc"
        pass
    @classmethod
    def print_per_day(cls):
        "wyswietla pacjentow per day "
        pass



    # def add_to_schedule(self,name,schedule=[]):
    #
    #     schedule.append(name)

# append.menu
#max_dlugosc
class Human(object):

    def __init__(self, first_name, last_name, ):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"{self.first_name}{self.last_name}"

class Doctor(Human):
    pass


class Pacient(Human):
    pass


doc = Doctor("Gregory","House")
p1 = Pacient("Anna","Nowak")
p2 = Pacient("Jan","Kowalski")
p3 = Pacient("Tomasz", "Nowak")
p4 = Pacient("Maja","Kowalska")
p5 = Pacient("Antoni","Żurek")

day = Day("poniedziałek")

Clinic.schedule(pn,doc,p1)
Clinic.print_per_day()
