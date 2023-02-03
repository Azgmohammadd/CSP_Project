from algorithms.minimum_remaining_values import MRV
from algorithms.least_constraining_value import LCV
from shared.responseModel import ResponseModel
from Models.hall import Hall
from copy import deepcopy



#forward checking algorithm
def forwardChecking(halls: list[Hall], index: int = 0, MRV = None, LCV = None) -> ResponseModel:
    """forward checking algorithm"""
    
    hall = MRV(halls) if MRV is not None else halls[index % len(halls)]
    
    index = halls.index(hall)
    
    # check if hall has prefrences to assign value
    if (len(hall.getPrefrences()) == 0):
        return ResponseModel([], True, 'No prefrences')
    
    prefrences = LCV(hall) if LCV is not None else hall.getPrefrences()
    
    for prefrence in prefrences:
        copy_halls = deepcopy(halls)
        hall = copy_halls[index]
        
        hall.setValue(prefrence)

        # remove prefrence from nighbors
        for nighbor in hall.getNighbors():
            nighbor.removePrefrence(prefrence)

        # all halls are checked
        if (Hall.checkAll(copy_halls)):
            return ResponseModel(copy_halls, False, 'forward checking completed')
        
        # check if forward checking is completed successfully in the next halls  
        forward = forwardChecking(halls = copy_halls, index = halls.index(MRV(halls)), MRV= MRV, LCV= LCV) if MRV is not None else forwardChecking(halls = copy_halls, index= index + 1)
                
        if (not forward.hasError):
            copy_halls = forward.result 
            
            return ResponseModel(copy_halls, False, 'forward checking completed')