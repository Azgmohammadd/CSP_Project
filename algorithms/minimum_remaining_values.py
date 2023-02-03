from copy import deepcopy
from shared.responseModel import ResponseModel
from Models.hall import Hall


def MRV(halls: list[Hall]) -> Hall:
    min_remaining_values = float('-inf')
    selected_hall = None

    for hall in halls:
        if len(hall.getNighbors()) > min_remaining_values and hall.getValue() is None:
            min_remaining_values = len(hall.getNighbors())
            selected_hall = hall
    
    return selected_hall