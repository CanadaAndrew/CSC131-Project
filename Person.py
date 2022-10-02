import SocialSecurity
import DMV
import StateDepartment

class Person:
    def __init__(self, ssn):
        self.ssn = ssn
        self.ssInfo = SocialSecurity.SocialSecurity("Adrian", "p", "Pog", 12, 12, 2012)
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

    # create a 2nd Inner class



# create a object
# of outer class
Adrian = Person(1234)
Adrian.setSSN(4321)
print(Adrian.getSSN())

Adrian.ssInfo.FName = "Andrew"
Adrian.ssInfo.MName = "Poggo"
Adrian.ssInfo.LName = "McGee"
Adrian.ssInfo.birthDay = 20
Adrian.ssInfo.birthMonth = "April"
Adrian.ssInfo.birthYear = 2069
#print(Adrian.ssInfo.FName)
#print(Adrian.ssInfo.MName)
#print(Adrian.ssInfo.LName)
print(Adrian.ssInfo.FullName)
#print(Adrian.ssInfo.BirthDay)
#print(Adrian.ssInfo.BirthMonth)
#print(Adrian.ssInfo.BirthYear)
print(Adrian.ssInfo.BirthInfo)
Jeb = Person(1243)
Jeb.setSSN(3421)
print(Jeb.getSSN())
Jeb.ssInfo.FName = "George"
Jeb.ssInfo.MName = "alt"
Jeb.ssInfo.LName = "Curious"
print(Jeb.ssInfo.FullName)
print(Adrian.ssInfo.FullName)
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