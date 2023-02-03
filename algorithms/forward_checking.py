from algorithms.minimum_remaining_values import MRV
from algorithms.least_constraining_value import LCV
from shared.responseModel import ResponseModel
from Models.hall import Hall
from copy import deepcopy


#forward checking algorithm
def forwardChecking(halls: list[Hall], index: int = 0) -> ResponseModel:
    """forward checking algorithm"""
    
    # all halls are checked
    if (index == len(halls)):
        return ResponseModel(halls, False, 'forward checking completed')
        
    # hall = halls[index]
    hall = MRV(halls).result
    
    # check if hall has prefrences to assign value
    if (len(hall.getPefrences()) == 0):
        return ResponseModel([], True, 'No prefrences')
    
    # sort the preferences based on LCV heuristic
    sortedPrefrences = LCV(hall, halls)

    for prefrence in hall.getPefrences():
        copy_halls = deepcopy(halls)
        hall = copy_halls[index]
        
        hall.setValue(prefrence)

        # remove prefrence from nighbors
        for nighbor in hall.getNighbors():
            nighbor.removePrefrence(prefrence)

        # check if forward checking is completed successfully in the next halls  
        if (not forwardChecking(copy_halls, index + 1).hasError):
            next_index = MRV(copy_halls).result
            
            copy_halls = forwardChecking(copy_halls, next_index).result 
            
            return ResponseModel(copy_halls, False, 'forward checking completed')