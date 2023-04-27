class Studient():
    def __init__(self, name, rut, birthdate, email, career, semester):
        self.__Name = name
        self.__Rut = rut
        self.__BirthDate = birthdate
        self.__Email = email
        self.__Career = career
        self.__Semester = semester

    def GetName(self):
        return self.__Name
    def GetRut(self):
        return self.__Rut
    def GetBirthDate(self):
        return self.__BirthDate
    def GetEmail(self):
        return self.__Email
    def GetCareer(self):
        return self.__Career
    def GetSemester(self):
        return self.__Semester
