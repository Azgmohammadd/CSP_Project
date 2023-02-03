from Models.group import Group
from shared.responseModel import ResponseModel


class Hall():
    __name: str
    __value: Group
    __nighbors: set['Hall']
    __prefrences: set[Group] 
    
    def __init__(self, name: str):
        self.__name = name
        self.__value = None
        self.__nighbors = set()
        self.__prefrences = set()
    
    
    def getName(self) -> str:
        return self.__name
    
        
    def setValue(self, value: Group):
        if (self.isExistPrefrence(value)):
            self.__value = value
        else:
            raise Exception("value must be one of the perferences")


    def getValue(self) -> Group:
        return self.__value
    
    
    def updateNighbors(self, nighbors: set['Hall']):
        self.__nighbors = nighbors
        
    
    def addNighbor(self, nighbor: 'Hall'):
        # if (self.__value == nighbor.getValue()):
            # raise Exception('Duplicate value')
        # else:
            self.__nighbors.add(nighbor)
    
    
    def getNighbors(self) -> set['Hall']:
        return self.__nighbors
    
    
    def addPrefrence(self, prefrence: Group):
        self.__prefrences.add(prefrence)
        
    
    def addPrefrences(self, prefrences: set[Group]):
        self.__prefrences = prefrences
    
    
    def isExistPrefrence(self, prefrence: Group) -> bool:
        for perf in self.__prefrences:
            if (perf.getName() == prefrence.getName()):
                return True

        return False
    
    
    def removePrefrence(self, prefrence: Group) -> ResponseModel:
        self.__prefrences = set(filter(lambda x: x.getName() != prefrence.getName(), self.__prefrences))
        
        if(len(self.__prefrences) == 0):
            return ResponseModel(self.__prefrences, False, 'No prefrences')
    
        return ResponseModel(self.__prefrences, True, 'Prefrence removed')
    
    
    def getPefrences(self) -> set[Group]:
        return self.__prefrences