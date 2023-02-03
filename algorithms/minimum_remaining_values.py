from copy import deepcopy
from shared.responseModel import ResponseModel
from Models.hall import Hall
from sys import maxsize

def MRV(halls: list[Hall]) -> Hall:
    min_remaining_values = maxsize
    selected_hall = None

    for hall in halls:
        if len(hall.getPrefrences()) < min_remaining_values and hall.getValue() is None:
            min_remaining_values = len(hall.getPrefrences())
            selected_hall = hall
    
    return selected_hall