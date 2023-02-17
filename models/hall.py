from models.group import Group


class Hall():
    __name: str
    __value: Group
    __neighbors: set['Hall']
    __preferences: set[Group] 
    
    def __init__(self, name: str):
        self.__name = name
        self.__value = None
        self.__neighbors = set()
        self.__preferences = set()
    
    
    def getName(self) -> str:
        return self.__name
    
        
    def setValue(self, value: Group):
        self.__value = value
        

    def getValue(self) -> Group:
        return self.__value
        
    
    def addNeighbor(self, neighbor: 'Hall'):
        self.__neighbors.add(neighbor)
    
    
    def getNeighbors(self) -> set['Hall']:
        return self.__neighbors
    
    
    def addPreference(self, preference: Group):
        self.__preferences.add(preference)
        
    
    def removePreference(self, preference: Group): # -> ResponseModel:
        self.__preferences = set(filter(lambda x: x.getName() != preference.getName(), self.__preferences))
    
    
    def getPreferences(self) -> set[Group]:
        return self.__preferences
    
    
    def checkAll(halls : list['Hall']) -> bool:
        for hall in halls:
            if (hall.getValue() is None):
                return False
        
        return True
