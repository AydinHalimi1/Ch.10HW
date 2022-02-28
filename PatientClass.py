class patient:
    def __init__(self,Id,Name,Address,Phone,Veteran_Status):
        self.__id = Id
        self.__Name = Name
        self.__Address = Address
        self.__Phone = Phone
        self.__Vet = Veteran_Status

    def get__id(self):
        return self.__id
    def get__Name(self):
        return self.__Name
    def get__Address(self):
        return self.__Address
    def get__Phone(self):
        return self.__Phone
    def get__Vet(self):
        return self.__Vet