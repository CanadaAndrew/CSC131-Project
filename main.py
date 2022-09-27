"""""
class first:

    # constructor
    def __init__(self):
        # class second object
        # is created
        self.fst = second()

    def first_method(self):
        print("Inside first method")


# define class second
class second:

    # constructor
    def __init__(self):
        self.snd = "GFG"

    def second_method(self):
        print("Inside second method")


# make object of first class
obj1 = first()
# print(obj1)
print(obj1.first_method())
# make object of second class
# with the help of first
obj2 = obj1.fst
# print(obj2)

# access attributes and methods
# of second class
print(obj2.snd)

obj2.second_method()
"""

"""
class Person:
    # Class Variable
    #animal = 'dog'

    # The init method or constructor
    def __init__(self, name, age, ssn):
        # Instance Variable
        self.name = name
        self.age = age

    # Adds an instance variable
    def setAge(self, age):
        self.age = age

    # Retrieves instance variable
    def getAge(self):
        return self.age

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


# Driver Code
Adrian = Person("Doge", 12)
Adrian.setAge(20)
Adrian.setName("Adrian")
print(Adrian.getName())
print(Adrian.getAge())
"""


class Person:
    def __init__(self, ssn):
        self.ssn = ssn
       # self.soc = self.SocialSecurity("", "", "", 0, "", 0)
       # self.dmv = self.DMV()

    #   def show(self):
    #    print('In outer class')
    #    print('Name:', self.ssn)

    #Dont use self

    def setSSN(self, ssn):
        self.ssn = ssn

    def getSSN(self):
        return self.ssn

    # create a 1st Inner class
    class SocialSecurity:
        def __init__(self, fName, mName, lName, birthDay, birthMonth, birthYear):
            self.fName = fName
            self.mName = mName
            self.lName = lName
            self.birthDay = birthDay
            self.birthMonth = birthMonth
            self.birthYear = birthYear

        def getfName(self):
            return self.fName

        def getmName(self):
            return self.mName

        def getlName(self):
            return self.lName

        def getbirthDay(self):
            return self.birthDay

        def getbirthMonth(self):
            return self.birthMonth

        def getbirthYear(self):
            return self.birthYear

        def setfName (self, fName):
            self.fName = fName

        def setmName(self, mName):
            self.mName = mName

        def setlName(self, lName):
            self.lName = lName

        def setbirthDay(self, birthDay):
            self.birthDay = birthDay

        def setbirthMonth(self, birthMonth):
            self.birthMonth = birthMonth

        def setbirthYear(self, birthYear):
            self.birthYear = birthYear

    # create a 2nd Inner class
    class DMV:
        def __init__(self, name):
            self.name = name

        def display(self):
            print("Name:", self.name)


# create a object
# of outer class
Adrian = Person(1234)
Adrian.setSSN(4321)
print(Adrian.getSSN())

Adrian.SocialSecurity.setfName(fName="Adrian")
print(Adrian.SocialSecurity.getfName())
#print(Adrian.SocialSecurity.getfName())

# create a object
# of 1st inner class
# d1 = Adrian.soc

# create a object
# of 2nd inner class
# d2 = Adrian.dmv
# print()
# d1.display()
# print()
# d2.display()