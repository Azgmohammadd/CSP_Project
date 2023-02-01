from group import Group
from shared.responseModel import ResponseModel


class Hall():
    __name: str
    __value: Group = None
    __nighbors: set['Hall'] = []
    __likes: set[Group] = []
    
    def __init__(self, name: str):
        self.__name = name
        self.__value = None
    
    
    def getName(self) -> str:
        return self.__name
    
        
    def setValue(self, value: Group):
        if (value in self.__likes):
            self.__value = value
        else:
            raise Exception("value must be one of the likes")


    def getValue(self) -> Group:
        return self.__value
    
    
    def addNighbor(self, nighbor: 'Hall'):
        if (self.__value == nighbor.getValue()):
            raise Exception('Duplicate value')
        else:
            self.__nighbors.add(nighbor)
    
    
    def addLike(self, prefrence: Group):
        self.__likes.add(prefrence)
        
    
    def addLikes(self, likes: set[Group]):
        self.__likes = likes
    
    
         