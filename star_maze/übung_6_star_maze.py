from contextlib import nullcontext

from dill import load
from collections.abc import Callable
import time
import Vertex


class Maze:
    """
    The given external form of the maze comes as a string, with the following characters:
    '#' stands for a wall tile
    ' ' a space stands for a walkable tile
    'S' stands for the start, this tile exists only once
    'F' stands for a finish, it could exist multiple times or not at all
    The outside of the maze is blocked completely by walls '#'
    The maze is given in multiple lines, spaced by '\n".

    An example generated maze could be:
    #######
    #     #
    # # # #
    #S  # #
    ### # #
    #F  #F#
    #######

    Your representation needs to be suitable to solve the underlying search problem to find the fastest way to
    a finish from the start. After a maze is solved, the solution is returned as a string, replacing the
    empty spaces of the path taken by '*' characters. The optimal solution of the maze problem is one, where
    the amount of '*' characters is minimal, connecting 'S' and one 'F' over tiles that were previously filled with
    spaces ' '. For an unsolvable maze (no 'F' can be reached from the 'S'), no stars should be added!

    The solution for the above example would be:
    #######
    #     #
    # # # #
    #S**# #
    ###*# #
    #F**#F#
    #######


    Task 1: Create an internal representation of your maze (10P)
    Define the maze as a search problem, where the task is to find the shortest path from the start to a finish.
    Encode your search problem as a graph: states are nodes and can be expanded by executing a transition function
    - Define all necessary values for the maze to be representing a search state in the __init__ function,
      this includes also a way to retrieve the path that was taken until here with its costs.
    - Define a transition function, which checks which states are neighboring a given state.
    - Define a solved function, which returns if the maze is solved in its current state
    - Define a function __eq__(other_state) to check efficiently if two search-states are the same!
    - Define a function g() which returns the cost of the path to this state from the start
    - Define a function: to_text() which returns the current state as a text, with the path taken from the 'S'
      replaced by '*' characters
    ====================================================================================================================
    HINT: To reduce unnecessary redundancy between states, feel free to globally store immutable information.
    Also feel free to add additional arguments to your function definitions as seen fit
    ====================================================================================================================
    """
    def __init__(self, maze_representation: list[list[str]], current_pos: tuple[int, int]): 
        """
        Stores all required variables for you representation in the state.
        """
        self.maze=maze_representation
        self.start_pos: tuple[int, int] = None
        self.end_pos: list[tuple[int, int]] = None # type list, since there can be more than one list
        if current_pos:
            self.current_pos = current_pos
        else:
            self.current_pos = (0,0)
        self.path: list[tuple[int, int]] = []

    @classmethod
    def from_string(cls, raw_lab_text: str):
        """
        Sets up a suitable representation of the given maze, given as a string raw_lab_text
        """
        lines = raw_lab_text.strip().split('\n')

        maze_representation = [list(row) for row in lines]

        # Find the location of "S" and all "F"s
        start_pos= None
        end_pos= []
        for i, row in enumerate(maze_representation):
            for j, cell in enumerate(row):
                if cell == "S":
                    start_pos= (i,j)
                elif cell =="F":
                    end_pos.append((i,j))

        if start_pos is None or end_pos is []:
            raise ValueError("Maze must contain both a start ('S') and at least one end ('F') position.")

        maze_instance = cls(maze_representation, start_pos)
        maze_instance.start_pos = start_pos
        maze_instance.end_pos= end_pos
        return maze_instance

    def transition(self) -> list[tuple[tuple[int, int], float]]:
        """
        returns a list of states that are neighboring the current state with their respective costs to get to from this
        current state
        """
        neighbors = []
        x,y = self.current_pos
        directions= [(0,1),(1,0), (0,-1), (-1,0) ] # up, right, down, left

        for dx, dy in directions:
            nx, ny = x + dx, y + dy # find all possible transitions

            if 0 <= nx < len(self.maze) and 0 <= ny < len(self.maze[0]) and self.maze[nx][ny] != "#":
                if (nx,ny) not in self.path:
                    cost = my_heuristic(Maze(self.maze, (nx, ny)))
                    neighbors.append(((nx, ny), cost))
        return neighbors
        
    def solved(self) -> bool:
        """
        returns true if the state of the maze is solved by reaching a finish 'F' from the start 'S' , else false
        """
        start_found = self.maze[self.path[0][0]][self.path[0][1]] == "S"
        finish_found= self.current_pos in self.end_pos
        return start_found and finish_found

    def __eq__(self, other_state) -> bool:
        """
        returns true if the other_state is equal to this maze state
        """
        if not isinstance(other_state, Maze):
            raise TypeError("Type(other_state) is not Maze")
        if self.current_pos != other_state.current_pos:
            return False
        if self.end_pos != other_state.end_pos:
            return False
        if self.start_pos != other_state.start_pos:
            return False
        if self.path != other_state.path:
            return False
        return True

    def g(self) -> float:
        """
        returns the costs of the path taken until this state
        """
        return float(len(self.path))

    def to_string(self) -> str:
        """
        returns the string representation as given, but with the path taken from the start to the current state
        replaced by '*' characters (-> see example above in class description)
        """
        text_maze= [list(row) for row in self.maze]
        for x,y in self.path:
            if text_maze[x][y] != "S" and text_maze[x][y] != "F":
                text_maze[x][y]= "*"
        return '\n'.join(''.join(row) for row in text_maze)

def a_search(start_state: Maze, heuristics: Callable[[Maze], float]) -> list[tuple[int, int]]:
    """
    Task 2: Create the A Algorithm with closed and open list. As a reminder, these are the steps: (6P)
    1. Let the open list be the list of start nodes for the problem (first state of the maze after initialization)
    2. If the open list is empty, report a failure by returning an empty list. Otherwise, select the node n from the
       open list for which f(n) = g(n) + h(n) is minimal, g(n) being the costs of the path from start to this node,
       and h(n) the estimated costs from this state to the closest goal state by your heuristic.
    3. If the current node n represents a goal node, report success and return the solution path from the start_state to
       goal as a list of tuples.
    4. Otherwise, remove n from open_list (and add it to the set of already visited nodes) and add all its successor
       nodes to the open_list, if they weren't already. Update the successor nodes with the path to the start node.
    5. Continue with step 2!

    Add any missing necessary attributes and functions to your maze state to effectively execute your a_search
    algorithm as seen fit!

    Question (2P): 
    A becomes A* for admissible heuristics. Does A* always return the optimal solution first even if
    it won't use a closed list to keep track of all already visited states? Explain your answer!

    Answer:
    As stated in the script A* it will always return an optimal solution,
    as long as the heuristic is valid (which means that it never overestimates the costs).
    Whether the algorithm uses a closed list or not does not have an influence on that. 
    
    It does however have an influence on the time and energy efficiency of the algorithm:
    Looking at a certain state more than one time means that the algorithm itself does not have the optimal
    runtime.
    """

    if not start_state.start_pos:
        return []
    if not start_state.end_pos:
        return []

    current_state_v = Vertex.Vertex(start_state.start_pos, heuristics(start_state),0)
    open_list = [current_state_v]
    closed_list_of_pos = []

    while not current_state_v.value in start_state.end_pos:
        new_elements = Maze(start_state.maze,current_state_v.value).transition() #current_state_v.value.transition()
        for new_element in new_elements:    
            if new_element[0] not in closed_list_of_pos:
                new_vertex = Vertex.Vertex(new_element[0], new_element[1]+ current_state_v.depth, current_state_v.depth + 1)
                open_list.append(new_vertex)
                current_state_v.add_child(new_element)
                new_vertex.parent = current_state_v
        open_list.remove(current_state_v)
        closed_list_of_pos.append(current_state_v.value)
        if not open_list:
            return []
        current_state_v = min_vertex_in_list(open_list)
    return path_to_root(current_state_v)

def path_to_root(v : Vertex) -> list[tuple[int,int]]:
    path : list[tuple[int,int]] = [v.value]
    while current_node.get_parent() is not None:
        path.append(current_node.get_parent().value)
        current_node = current_node.get_parent()
    path.reverse()
    return path

def vertex_list_to_pos_list(vert_lst : list[Vertex]) -> list[tuple[int,int]]:
    pos_lst = []
    for v in vert_lst:
        pos_lst.append(v.value)
    return pos_lst

def min_vertex_in_list(lst: list[Vertex]) -> Vertex:
    mini = float('inf')
    min_element = None
    for i in range(len(lst)):
        if lst[i].distance < mini:
            mini = lst[i].distance
            min_element = lst[i]
    return min_element

def eq_in_list(lst : list[Maze], pos : list[tuple[int, int]]) -> bool:
    pass

def my_heuristic(lab: Maze) -> float:
    """
    Task 3: Write an admissible (zulässig) and monotone heuristic, that is based on the location of the finishes. (2P)
    Assume that each of the finishes (Bernsteinzimmer) can be detected by a scanner, that gives you the distance
    from your current position to said finish. Based on this information and the ability to see down the hallways
    from where you are standing, choose a heuristic which is also efficient to calculate in your representation of the
    maze!
    (If necessary, add the values you need in your representation or as arguments to make this calculation efficient!)
    """
    current_x, current_y = lab.current_pos
    distances = []

    for i, row in enumerate(lab.maze):
        for j, cell in enumerate(row):
            if cell == 'F':
                #calculate Manhattan Distance
                distance = abs(current_x - i) + abs(current_y - j)
                distances.append(distance)
    if not distances:
        return float('inf')
    return min(distances)

# Try it out, when it is all put together:
if __name__ == '__main__':
    """
    IMPORTANT: you can change method signatures and input arguments as seen fit, as long as the main function can be
    executed as prepared in this example (for automatically testing your solution).
    """
    with open("maze.dill", "rb") as f:
        generate_random_maze = load(f)
    maze1 = generate_random_maze(15)
    maze2 = generate_random_maze(200)
    maze3 = generate_random_maze(16180)
    maze4 = generate_random_maze(31415)
    mazes= [maze1, maze2, maze3, maze4]


    for idx, maze_str in enumerate(mazes,1):
        try:
            print(f"\nSolving maze {idx}:")
            rep_of_maze = Maze.from_string(maze_str)
            start_time = time.perf_counter()
            solution = a_search(Maze.from_string(maze_str), my_heuristic)
            duration = time.perf_counter() - start_time
            maze_solved = Maze.from_string(maze_str)
            maze_solved.path = solution
            if solution:
                print(maze_solved.to_string())
            else:
                print(f"No solution found for maze {idx}.")
            print(f" Solve duration for maze {idx}: {duration:.2f} seconds")
        except ValueError as e:
            print(f"Error with maze {idx}: {e}. Skipping to the next maze.")
    
    print("press enter to end process")
    input()