from node import Node

def main():
    # read text file
    with open('input.txt', 'r') as file:  
        lines = file.read()
        
    # split text file into list of lines
    lines = lines.splitlines()

    # create list of nodes
    numberOfGroup, numberOfRoom = lines[0].split(" ")

    
if __name__ == '__main__':
    main()