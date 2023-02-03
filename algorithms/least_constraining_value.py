from copy import deepcopy
from shared.responseModel import ResponseModel
from Models.hall import Hall

def LCV(hall: Hall) -> list:
    """Least Constraining Value heuristic"""
    
    nighbors = hall.getNighbors()
    prefrences = hall.getPefrences()
    
    # sort the prefrences based on the number of remaining options of nighbors
    sorted_prefrences = sorted(prefrences, key=lambda x: sum(1 for n in nighbors if x in n.getPefrences()))
    
    return sorted_prefrences
