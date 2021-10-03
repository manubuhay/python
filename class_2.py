class Person:
    def __init__(self, pfirst, plast, page, pocc):
        self.fname = pfirst
        self.lname = plast
        self.age = page
        self.occ = pocc
    def about(self):
        print(self.fname)
        print(self.lname)
        print(self.age)
        print(self.occ)

class PersonNoConst:
    def about(self):
        print(self.fname)
        print(self.lname)
        print(self.age)
        print(self.occ)

new_person = Person("manu","buhay",32,"IT")
new_person.about()

new_person2 = PersonNoConst()
new_person2.fname = "clone manu"
new_person2.lname = "clone buhay"
new_person2.age = 31
new_person2.occ = "clone IT"
new_person2.about()
