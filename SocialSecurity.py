class SocialSecurity:
    def __init__(self, fName, mName, lName, birthDay, birthMonth, birthYear):
        self.fName = fName
        self.mName = mName
        self.lName = lName
        self.birthDay = birthDay
        self.birthMonth = birthMonth
        self.birthYear = birthYear

    @property
    def FName(self):
        return self.fName

    @property
    def MName(self):
        return self.mName

    @property
    def LName(self):
        return self.lName

    @property
    def BirthDay(self):
        return self.birthDay

    @property
    def BirthMonth(self):
        return self.birthMonth

    @property
    def BirthYear(self):
        return self.birthYear

    @FName.setter
    def FName(self, fname):
        fName = fname
        self.fName = fName

    @MName.setter
    def MName(self, mname):
        mName = mname
        self.mName = mName

    @LName.setter
    def LName(self, lname):
        lName = lname
        self.lName = lName

    @BirthDay.setter
    def BirthDay(self, birthday):
        birthDay = birthday
        self.birthDay = birthDay

    @BirthMonth.setter
    def BirthMonth(self, birthmonth):
        birthMonth = birthmonth
        self.birthMonth = birthMonth

    @BirthYear.setter
    def BirthYear(self, birthyear):
        birthYear = birthyear
        self.birthYear = birthYear

    @property
    def FullName(self):
        return '{} {} {}'.format(self.fName, self.mName, self.lName)

    @property
    def BirthInfo(self):
        return '{} {}, {}'.format(self.birthMonth, self.birthDay, self.birthYear)




