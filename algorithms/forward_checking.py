from Models.hall import Hall
from Models.group import Group
from copy import deepcopy

#forward checking algorithm
def forwardChecking(halls: list[Hall]):
    
    # hall: Hall = deepcopy(root)
    
    for hall in halls:
        if hall.getValue() != None:
            continue
        
        try:
            for value in hall.getPefrences():
                hall.setValue(value)
                
                for nighbor in hall.getNighbors():
                    copy_nighbor = deepcopy(nighbor)
                    if (copy_nighbor.isExistPrefrence(value)):
                        if (copy_nighbor.removePrefrence(value).hasError):
                            print("remove prefrence")
    
        except Exception as e:
            print(e)
            print('Failed to forward checking')
            pass    