from teacher import Teacher
from classroom import Classroom
class Subject():
    def __init__(self, name:str, id:int, parallel:str, semester:int, credits:int, lecturehours:int, modality:str, total:int):
        self.__Name = name
        self.__Id = id
        self.__Parallel = parallel
        self.__Semester = semester
        self.__Credits = credits
        self.__LectureHours = lecturehours
        self.__Modality = modality
        self.__Total = total
        self.__Teacher = None
        self.__Classroom = None

    def GetName(self):
        return self.__Name
    def GetId(self):
        return self.__Id
    def GetParallel(self):
        return self.__Parallel
    def GetSemester(self):
        return self.__Semester
    def GetCredits(self):
        return self.__Credits
    def GetLectureHours(self):
        return self.__LectureHours
    def GetModality(self):
        return self.__Modality
    def GetTotal(self):
        return self.__Total
    def GetTeacher(self):
        return self.__Teacher
    def GetClassroom(self):
        return self.__Classroom
    
    def SetName(self, name:str):
        self.__Name = name
    def SetId(self, id=int):
        self.__Id = id
    def SetParallel(self, parallel:str):
        self.__Parallel = parallel
    def SetSemester(self, semester:int):
        self.__Semester = semester
    def SetCredits(self, credit:int):
        self.__Credits = credit
    def SetLectureHours(self, hours:int):
        self.__LectureHours = hours
    def SetModality(self, modality:str):
        self.__Modality = modality
    def SetTotal(self, total:int):
        self.__Total = total
    def SetTeacher(self, teacher:Teacher):
        self.__Teacher = teacher
    def SetClassroom(self, classroom:Classroom):
        self.__Classroom = classroom