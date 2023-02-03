from Models.group import Group
from Models.hall import Hall
from algorithms.forward_checking import forwardChecking


def main():
    # read text file
    with open('input.txt', 'r') as file:  
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
        
        hall = halls[int(hall_i) - 1]
        hall.addNighbor(halls[int(hall_j) - 1])
          
          
    forwardChecking(halls)
            
if __name__ == '__main__':
    main()