from algorithms.minimum_remaining_values import MRV
from shared.responseModel import ResponseModel
from Models.hall import Hall
from copy import deepcopy


def checkAll(halls : list[Hall]) -> bool:
    for hall in halls:
        if (hall.getValue() is None):
            return False
    
    return True


#forward checking algorithm
def forwardChecking(halls: list[Hall], index: int = 0) -> ResponseModel:
    """forward checking algorithm"""
    
    hall = MRV(halls)
    
    index = halls.index(hall)
    
    # check if hall has prefrences to assign value
    if (len(hall.getPefrences()) == 0):
        return ResponseModel([], True, 'No prefrences')
    
    for prefrence in hall.getPefrences():
        copy_halls = deepcopy(halls)
        hall = copy_halls[index]
        
        hall.setValue(prefrence)

        # remove prefrence from nighbors
        for nighbor in hall.getNighbors():
            nighbor.removePrefrence(prefrence)

        # all halls are checked
        if (checkAll(copy_halls)):
            return ResponseModel(copy_halls, False, 'forward checking completed')
        
        # check if forward checking is completed successfully in the next halls  
        if (not forwardChecking(copy_halls, halls.index(MRV(halls))).hasError):
            next_index = halls.index(MRV(halls))
            
            copy_halls = forwardChecking(copy_halls, next_index).result 
            
            return ResponseModel(copy_halls, False, 'forward checking completed')