class Vertex:

    def __init__(self, value, distance : float, depth : int):
        self.value = value
        self.parent = None
        self.children = []
        self.is_leaf = True
        self.is_root = False
        self.distance = distance
        self.depth = depth
        # self.move = move


    def add_child(self, child):
        self.children.append(child)
        self.is_leaf = False

    def get_parent(self):
        return self.parent

    def get_value(self):
        return self.value

    def get_move(self):
        return self.move

    def __eq__(self, other):
        return self.value == other.value