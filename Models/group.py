class Group():
    __name: str
    
    def __init__(self, name=None):
        self.__name = name
    
    def __str__(self):
        return self.__name
    
    
    def getName(self):
        return self.__name