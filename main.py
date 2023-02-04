from Models.group import Group
from Models.hall import Hall
from algorithms.forward_checking import FC
from algorithms.minimum_remaining_values import MRV
from algorithms.least_constraining_value import LCV
from algorithms.arc_consistency_3 import AC3
from shared.responseModel import ResponseModel
    


def main():
    # read text file
    with open('test/input.txt', 'r') as file:  
        lines = file.read()
        
    # split text file into list of lines
    lines = lines.splitlines()

    # create list of nodes
    numberOfHalls, numberOfGroups = tuple(map(int, lines[0].split()))
    
    # create list of halls and groups
    halls: list[Hall] = [Hall(f'Hall{index + 1}') for index in range(numberOfHalls)]
    groups: list[Group] = [Group(f'Group{index + 1}') for index in range(numberOfGroups)]
    
    # add prefrences to halls
    for index in range(1, numberOfGroups + 1):
        prefences = lines[index].split()
        
        for preference in prefences:
            halls[int(preference) - 1].addPrefrence(groups[index - 1])
            
    # add nighbors to halls
    for index in range(numberOfGroups + 2, len(lines)):
        hall_i, hall_j = lines[index].split()
        
        halls[int(hall_i) - 1].addNeighbor(halls[int(hall_j) - 1])
        halls[int(hall_j) - 1].addNeighbor(halls[int(hall_i) - 1])
          
    file.close()
          
    fc_result = FC(halls= halls, index= 0, MRV= MRV, LCV= LCV, AC3 = AC3)
    
    ResponseModel.printResponse(fc_result)
    
if __name__ == '__main__':
    main()