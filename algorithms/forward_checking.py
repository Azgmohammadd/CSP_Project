from shared.responseModel import ResponseModel
from Models.hall import Hall
from copy import deepcopy



#forward checking algorithm
def FC(halls: list[Hall], index: int = 0, MRV = None, LCV = None, AC3= None) -> ResponseModel:
    """forward checking algorithm"""
    halls = AC3(halls).result if AC3 is not None and not AC3(halls).hasError else halls 
    
    hall = MRV(halls) if MRV is not None else halls[index % len(halls)]
    
    index = halls.index(hall)
    
    # check if hall has prefrences to assign value
    if (len(hall.getPrefrences()) == 0):
        return ResponseModel([], True, f'No prefrences for {hall.getName()}')
    
    prefrences = LCV(hall) if LCV is not None else hall.getPrefrences()
    
    for prefrence in prefrences:
        copy_halls = deepcopy(halls)
        hall = copy_halls[index]
        
        hall.setValue(prefrence)

        # remove prefrence from nighbors
        for nighbor in hall.getNeighbors():
            nighbor.removePrefrence(prefrence)

        # all halls are checked
        if (Hall.checkAll(copy_halls)):
            return ResponseModel(copy_halls, False, 'forward checking completed')
        
        # check if forward checking is completed successfully in the next halls  
        forward = FC(halls = copy_halls, index = halls.index(MRV(halls)), MRV= MRV, LCV= LCV, AC3= AC3) if MRV is not None else FC(halls = copy_halls, index= index + 1)
                
        if (not forward.hasError):
            copy_halls = forward.result 
            
            return ResponseModel(copy_halls, False, 'forward checking completed')