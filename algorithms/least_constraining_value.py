from Models.hall import Hall

def LCV(hall: Hall) -> list:
    """Least Constraining Value heuristic"""
    
    neighbors = hall.getNeighbors()
    prefrences = hall.getPreferences()
    
    # sort the prefrences based on the number of remaining options of neighbors
    sorted_prefrences = sorted(prefrences, key=lambda x: sum(1 for neighbor in neighbors if x in neighbor.getPreferences()))
    
    return sorted_prefrences
