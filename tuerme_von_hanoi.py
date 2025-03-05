# Programm wurde zusammen mit Alex Keller und Duong Nguyen erstellt
# Sucht für einen gegebenen validen Zustand nach einer Lösung

import time
import Vertex

from setuptools.namespaces import flatten


def is_valid_state(state: list[list[int]]) -> bool:
    # Checks whether a state is a valid state
    for tower in state:
        if tower != []:
            n = float("inf")
            for i in range(0, len(tower)):
                if tower[i] > n:
                    return False
                n = tower[i]
    return True

def eq(state_1: list[list[int]], state_2: list[list[int]]) -> bool:
    # Checks whether two states a valid and equal
    if is_valid_state(state_1) is False: return False 
    return True if state_1 == state_2 else False

def move(state: list[list[int]], move: tuple[int, int]) -> list[list[int]]:
    # Takes a state and a move and returns the state after the move 
    if state[move[0]] != []:
        state[move[1]].append(state[move[0]][-1])
        state[move[0]].pop()
    return state

def all_moves_from_state(state: list[list[int]]) -> list[tuple[int, int]]:
    # Calculates all valid moves for a given state
    if is_valid_state(state) is False:
        print(state, "is not a valid state!")
    valid_moves: list[tuple[int, int]] = []
    for n in range(0, len(state)):
        if state[n] != []:
            for m in range(0, len(state)):
                if n != m:
                    if is_valid_state(move(state, (n, m))):
                         valid_moves += [(n, m)]
    return valid_moves

def number_of_discs(tower_list: list[list[int]]) -> int:
    # calculates the number of discs on a given list of towers
    return len(flatten_list(tower_list))

def print_state(tower_list: list[list[int]]):
    # prints the current distribution of discs on the towers
    # Example [[3, 2], [], [1]]
    #   |    |    |
    #  ##    |    |
    #  ###   |    #

    discs = number_of_discs(tower_list)
    print_list = []
    for _ in range(0, discs):
        tower_string = ""
        for tower in tower_list:
            if tower != []:
                tower_string += " " * ((discs - tower[len(tower)-1] + 1) // 2) + (tower[len(tower)-1]) * "#" + " " * ((discs - tower[len(tower)-1]) // 2)
                tower.pop(-1)
            else:
                tower_string += " " * (discs // 2) + "|" + " " * (discs // 2)
        print_list += [tower_string]
    print_list.reverse()
    for l in print_list:
        print(l)




def sort(input:list[list[int]]):
    # heuristic search through the search space
    # 1/2
    if not input or not is_valid_state(input):
        print("Fehler bei der Eingabe")
        return False


    target = input.copy()

    for i in range(0,len(target)-1):
        target[i] = []


    input1 = input
    input1 = sorted(flatten_list(input1))
    input1.reverse()
    target[len(target)-1] = input1  # target state

    current_leaf = Vertex.Vertex(input, distance_to_target(input))


    while distance_to_target(current_leaf.value) != 0:
        moves = all_moves_from_state(current_leaf.value)
        for i in moves:
            current_leaf.add_child(Vertex.Vertex(move(current_leaf.value, i), distance_to_target(move(current_leaf.value,i))))


def min_in_dict(dictionary):
    return min(dictionary, key = dictionary.get[0]) # find dictionary key with minimal value



def distance_to_target(state : list[list[int]]) -> float:
    # describes the distance to the target position
    s = num_of_sorted_discs(state)
    k = len(state)
    d = 0

    d += 5 * (number_of_discs(state) - s)           # for each unsorted disc, add 5

    if k > 3 and state[k-2] != []:
        if len(state[k-2])!= 0:
            if state[k-2] != sorted(flatten_list(state))[number_of_discs(state)- num_of_sorted_discs(state)-1]:
                d += 10 * len(state[k-2])           # try to keep one empty, unless it's the on that is next to be placed on the target tower


    average_height = (number_of_discs(state) - s)/(k-2) # determine the average height of the tower, if you only look at the discs, that are not yet in the right position

    for i in range(0,len(state)-1):
        if len(state[i]) > average_height:
            d += len(state[i])-average_height     # for each tower, the height is above the average height, add some distance (depending on how "bad" it is)

    return d


#def list_of_same_dim(lst):
#    if isinstance(lst, list):
#        for i in range(len(lst)):
#            lst[i] = list_of_same_dim(lst[i])
#    else:
#        return []

def num_of_sorted_discs(state: list[list[int]]) -> int:
    # finds the number of sorted discs in the current state
    sorted_flat_list = sorted(flatten_list(state))          # the list of towers that we aim for
    flat_list = flatten_list(state[len(state) - 1])         # flattened list of discs in the last tower
    sorted_flat_list.reverse()                              # reverse that list, so we can later compare
    sorted_discs = 0                                        # counting variable

    for i in range(0, len(flat_list)): # not sure if there should be minus one or not
        if flat_list[i] == sorted_flat_list[i]:
            sorted_discs += 1                   # if the entries are equal, add one

    return sorted_discs




def flatten_list(lst):
    # turns nested list into a flat list
    flat  = []
    for i in lst:
        if isinstance(i, list):
            for j in i:
                flat.append(j)
        else:
            flat.append(i)
    return flat



def time_comp(input1: list[list[int]], input2: list[list[int]], input3: list[list[int]]):
    # compares the calculation time from three inputs
    input_1_timed = time.time()
    sort(input1)
    input_1_timed = round((time.time() - input_1_timed) * 1000, 4)
    discs_1 = number_of_discs(input1)

    input_2_timed = time.time()
    sort(input2)
    input_2_timed = round((time.time() - input_2_timed) * 1000, 4)
    discs_2 = number_of_discs(input2)


    input_3_timed = time.time()
    sort(input3)
    input_3_timed = round((time.time() - input_3_timed) * 1000, 4)
    discs_3 = number_of_discs(input3)

    print("--------")
    print(f"The first input (%d towers and %d discs) took %f milliseconds to compute." % (len(input1), discs_1, input_1_timed))
    print(f"The second input (%d towers and %d discs) took %f milliseconds to compute." % (len(input2), discs_2, input_2_timed))
    print(f"The last input (%d towers and %d discs) took %f milliseconds to compute." % (len(input3), discs_3, input_3_timed))



a = [[7],[8,6],[9,5,3,2,1]]

#print(sorted(flatten_list(a)))
#print(flatten_list(a[len(a) - 1]))

print(distance_to_target(a))
print(number_of_discs(a))
print(num_of_sorted_discs(a))

#print(flatten_list(a))

sort(a)
