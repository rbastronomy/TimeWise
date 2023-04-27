class Subject():
    def __init__(self, name, id, parallel, semester, credits, lecturehours, modality, total):
        self.__Name = name
        self.__Id = id
        self.__Parallel = parallel
        self.__Semester = semester
        self.__Credits = credits
        self.__LectureHours = lecturehours
        self.__Modality = modality
        self.__Total = total

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
    