from Models.group import Group
from shared.responseModel import ResponseModel


class Hall():
    __name: str
    __value: Group = None
    __nighbors: set['Hall'] = set()
    __prefrences: set[Group] = set()
    
    def __init__(self, name: str):
        self.__name = name
        self.__value = None
    
    
    def getName(self) -> str:
        return self.__name
    
        
    def setValue(self, value: Group):
        if (value in self.__prefrences):
            self.__value = value
        else:
            # raise Exception("value must be one of the likes")
            pass


    def getValue(self) -> Group:
        return self.__value
    
    
    def updateNighbors(self, nighbors: set['Hall']):
        self.__nighbors = nighbors
        
    
    def addNighbor(self, nighbor: 'Hall'):
        if (self.__value == nighbor.getValue()):
            # raise Exception('Duplicate value')
            pass
        else:
            self.__nighbors.add(nighbor)
    
    
    def getNighbors(self) -> set['Hall']:
        return self.__nighbors
    
    
    def addPrefrence(self, prefrence: Group):
        self.__prefrences.add(prefrence)
        
    
    def addPrefrences(self, prefrences: set[Group]):
        self.__prefrences = prefrences
    
    
    def isExistPrefrence(self, prefrence: Group) -> bool:
        return prefrence in self.__prefrences
    
    
    def removePrefrence(self, prefrence: Group):
        self.__prefrences.remove(prefrence)