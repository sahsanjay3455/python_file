"""
Encapsulation:it the process of wrapping the data together to provide security by using access specifier.
it is used to provide  security to the data

Access specifier:meaning of access is permission,specifier is telling to something
-->it tells us whether the user can access the data outside of the class or not

1.public:it can be access outside the class
eg:
class School:
    sname = "Kiit"
    loc = "bhubneshwar"

    def __init__(self, name, roll, branch):
        self.name = name
        self.roll = roll
        self.branch = branch

    def stud_data(self):
        print(self.name, self.roll, self.branch)


s1 = School("Taj", 201, "CSE")
s2 = School("swaroop", 202, "AI/ML")
print(School.sname, School._oc)
s1.stud_data()
s2.stud_data()

2.protected:it works just like public and it will not provide security
to create a protected memeber we have to use _(single underscore)before var name or method name
eg:

class School:
    _sname = "Kiit"
    _loc = "bhubneshwar"

    def __init__(self, name, roll, branch):
        self.name = name
        self.roll = roll
        self.branch = branch

    def _stud_data(self):
        print(self.name, self.roll, self.branch)


s1 = School("Taj", 201, "CSE")
s2 = School("swaroop", 202, "AI/ML")
print(School._sname, School._loc)
s1._stud_data()
s2._stud_data()


3.private: it provide the security to the data.private member cannot be access outside the class
to create a private member we have to use __(double underscore)before var_name or methodname
class School:
    __sname = "Kiit"
    __loc = "bhubneshwar"

    def __init__(self, name, roll, branch):
        self.name = name
        self.roll = roll
        self.branch = branch

    def __stud_data(self):
        print(self.name, self.roll, self.branch)


s1 = School("Taj", 201, "CSE")
s2 = School("swaroop", 202, "AI/ML")
print(School._School__sname)
print(s2._School__stud_data())
# s1.__stud_data()
# s2.__stud_data()
#to access private member outside the class
#syntax:
#obj/clas._classname__varname


"""


class School:
    __sname = "Kiit"
    __loc = "bhubneshwar"

    def __init__(self, name, roll, branch):
        self.name = name
        self.roll = roll
        self.branch = branch

    def __stud_data(self):
        print(self.name, self.roll, self.branch)


s1 = School("Taj", 201, "CSE")
s2 = School("swaroop", 202, "AI/ML")
print(School._School__sname)
print(s2._School__stud_data())
# s1.__stud_data()
# s2.__stud_data()
# to access private member outside the class
# syntax:
# obj/clas._classname__varname
