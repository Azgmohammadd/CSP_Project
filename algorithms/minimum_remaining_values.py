from copy import deepcopy
from shared.responseModel import ResponseModel
from Models.hall import Hall

def MRV(halls: list[Hall]) -> ResponseModel:
    copy_halls = deepcopy(halls)
    copy_halls.sort(key=lambda hall: len(hall.getPefrences()))
    
    for hall in copy_halls:
        if (hall.getValue() == None):
            return ResponseModel(halls.index(hall), False, 'MRV value found')
    
    return ResponseModel([], True, 'MRV value not found')