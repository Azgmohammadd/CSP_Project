class Group():
    __name: str
    
    def __init__(self, name=None):
        self.__name = name
    
    def __str__(self):
        # return f'GroupName: {self.__name}'
        return self.__name