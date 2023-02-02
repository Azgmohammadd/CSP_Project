from Models.hall import Hall
from Models.group import Group
from copy import deepcopy

#forward checking algorithm
def forwardChecking(root: 'Hall', value: Group):
    hall: Hall = deepcopy(root)
    
    hall.setValue(value)
    
    for nighbor in hall.getNighbors():
        if (nighbor.isExistPrefrence(value)):
            nighbor.removePrefrence(value)
            
    
    print(hall)
    