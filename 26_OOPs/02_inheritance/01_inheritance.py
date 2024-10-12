

class Employee:
    def __init__(self,name,id,dept):
        self.name = name
        self.id = id
        self.dept = dept

    def showInfo(self):
        print(f"Name:- {self.name}\nId:- {self.id}\nDepartment:- {self.dept}")    


class Programmer(Employee):
    def showLanguage(self):
        print("The default language is python")



e1 = Employee("Ravindra Singh",101,"IT")
e2 = Employee("Tilak Jangir",102,"HR")
e3 = Employee("Divyam Maharashi",103,"Manager")
e1.showInfo()
e2.showInfo()
e3.showInfo()

e4 = Programmer("Bharat Chhedawal",120,"Sr. Manager")
e4.showInfo()
e4.showLanguage()




      