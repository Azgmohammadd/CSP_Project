from shared.responseModel import ResponseModel
from Models.hall import Hall


def AC3(halls: list[Hall]) -> ResponseModel:
    """AC3 algorithm"""
    queue: list[tuple(Hall, Hall)] = [(hall, neighbor) for hall in halls for neighbor in hall.getNeighbors()]
    
    while queue:
        hall, neighbor = queue.pop(0)
        
        if revise(hall, neighbor):
            if len(hall.getPrefrences()) == 0:
                return ResponseModel([], True, f'Contradiction detected in AC3. No prefrences for {hall.getName()}')
            
            for n in hall.getNeighbors():
                if n != neighbor:
                    queue.append((n, hall))
                     
    return ResponseModel(halls, False, 'AC3 completed successfully')


def revise(hall: Hall, neighbor: Hall) -> bool:
    """check if hall and neighbor have a common value in their preferences, 
    if not remove the value from hall's preferences"""
    revised = False
    
    for value in hall.getPrefrences():
        if not any(prefrence.getName() != value.getName() for prefrence in neighbor.getPrefrences()):
            hall.removePrefrence(value)
            revised = True
            
    return revised