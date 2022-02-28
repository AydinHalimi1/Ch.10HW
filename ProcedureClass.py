class Procedure:
    def __init__(self,NameProcedure,Date,Practitioner,Charges,PatientID):
        self.__Name = NameProcedure
        self.__Date = Date
        self.__Practitioner = Practitioner
        self.__Charges = Charges
        self.__PatID = PatientID

    def get_Name(self):
        return self.__Name
    def get_Date(self):
        return self.__Date
    def get_Practitioner(self):
        return self.__Practitioner
    def get_Charges(self):
        return self.__Charges
    def get_PatID(self):
        return self.__PatID