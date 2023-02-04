from Models.group import Group
from shared.responseModel import ResponseModel


class Hall():
    __name: str
    __value: Group
    __neighbors: set['Hall']
    __prefrences: set[Group] 
    
    def __init__(self, name: str):
        self.__name = name
        self.__value = None
        self.__neighbors = set()
        self.__prefrences = set()
    
    
    def getName(self) -> str:
        return self.__name
    
        
    def setValue(self, value: Group):
        self.__value = value
        

    def getValue(self) -> Group:
        return self.__value
    
    
    def updateNeighbors(self, neighbors: set['Hall']):
        self.__neighbors = neighbors
        
    
    def addNeighbor(self, neighbor: 'Hall'):
        self.__neighbors.add(neighbor)
    
    
    def getNeighbors(self) -> set['Hall']:
        return self.__neighbors
    
    
    def addPrefrence(self, prefrence: Group):
        self.__prefrences.add(prefrence)
        
    
    def addPrefrences(self, prefrences: set[Group]):
        self.__prefrences = prefrences
    
    
    def isExistPrefrence(self, prefrence: Group) -> bool:
        for perf in self.__prefrences:
            if (perf.getName() == prefrence.getName()):
                return True

        return False
    
    
    def removePrefrence(self, prefrence: Group): # -> ResponseModel:
        self.__prefrences = set(filter(lambda x: x.getName() != prefrence.getName(), self.__prefrences))
    
    
    def getPrefrences(self) -> set[Group]:
        return self.__prefrences
    
    
    def checkAll(halls : list['Hall']) -> bool:
        for hall in halls:
            if (hall.getValue() is None):
                return False
        
        return True