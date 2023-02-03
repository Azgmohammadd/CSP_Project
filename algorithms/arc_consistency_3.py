from copy import deepcopy
from shared.responseModel import ResponseModel
from Models.hall import Hall

def AC3(halls: list[Hall]) -> ResponseModel:
    """AC3 algorithm"""
    queue = [(hall, nighbor) for hall in halls for nighbor in hall.getNighbors()]
    
    while queue:
        hall, nighbor = queue.pop(0)
        if revise(hall, nighbor):
            if len(hall.getPefrences()) == 0:
                return ResponseModel([], True, 'Contradiction detected in AC3')
            
            for n in hall.getNighbors():
                if n != nighbor:
                    queue.append((n, hall))
                    
    return ResponseModel(halls, False, 'AC3 completed successfully')


def revise(hall: Hall, nighbor: Hall) -> bool:
    """check if hall and nighbor have a common value in their preferences, 
    if not remove the value from hall's preferences"""
    revised = False
    
    for value in hall.getPefrences():
        if value not in nighbor.getPefrences():
            hall.removePrefrence(value)
            revised = True
            
    return revised
