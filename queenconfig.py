from random import randrange, choice
from copy import deepcopy
#Class state represents state of given problem
class State:
    instance_counter = 0
    def __init__(self, queen_positions=None, queen_num=8, parent=None, path_cost=0, f_cost=0, side_length=8):
        self.side_length = side_length
        if queen_positions is None:
            self.queen_num = queen_num
            self.queen_positions = frozenset(self.random_queen_position())
        else:
            self.queen_positions = queen_positions
            self.queen_num = len(self.queen_positions)
        self.path_cost = 0
        self.f_cost = f_cost
        self.parent = parent
        self.id = State.instance_counter
        State.instance_counter += 1

    def __str__(self):
        # print function
        return '\n'.join([' '.join(['*' if (col, row) not in self.queen_positions else 'Q' for col in range(self.side_length)]) for row in range(self.side_length)])

    def __hash__(self):
        # Hash function to remove duplicate
        return hash(self.queen_positions)

    def __eq__(self, other):
        # To check if 2 nodes are same
        return self.queen_positions == other.queen_positions

    def __lt__(self, other):
        # Cost comparison
        return self.f_cost < other.f_cost or (self.f_cost == other.f_cost and self.id > other.id)

    def random_queen_position(self):
        # Random queen configuration
        open_columns = list(range(self.side_length))
        queen_positions = [(open_columns.pop(randrange(len(open_columns))), randrange(self.side_length)) for _ in range(self.queen_num)]
        return queen_positions

    def get_children(self):
        # Get children from current state node
        children = []
        parent_queen_positions = list(self.queen_positions)
        for queen_index, queen in enumerate(parent_queen_positions):
            new_positions = [(queen[0], row) for row in range(self.side_length) if row != queen[1]]
            for new_position in new_positions:
                queen_positions = deepcopy(parent_queen_positions)
                queen_positions[queen_index] = new_position
                children.append(State(queen_positions))
        return children

    def random_child(self):
        # Random child
        queen_positions = list(self.queen_positions)
        random_queen_index = randrange(len(self.queen_positions))
        queen_positions[random_queen_index] = (queen_positions[random_queen_index][0], choice([row for row in range(self.side_length) if row != queen_positions[random_queen_index][1]]))
        return State(queen_positions)

    def range_between(self, x, y):
        # Return positions between x and y
        if x > y:
            return range(x-1, y, -1)
        elif x < y:
            return range(x+1, y)
        else:
            return [x]

    def zip_repeat(self, x, y):
        # Repeat
        if len(x) == 1:
            x *= len(y)
        elif len(y) == 1:
            y *= len(x)
        return zip(x, y)

    def points_between(self, x, y):
        # Repeat zipped positions between x and y
        return self.zip_repeat(list(self.range_between(x[0], y[0])), list(self.range_between(x[1], y[1])))

    def is_attacking(self, queens, x, y):
        # Check if 2 positions have attacked each other
        if (x[0] == y[0]) or (x[1] == y[1]) or (abs(x[0]-y[0]) == abs(x[1]-y[1])):
            for between in self.points_between(x, y):
                if between in queens:
                    return False
            return True
        return False

    def queen_attacks(self):
        # Calculate number of queen attacking
        attacking_pairs = []
        queen_positions = list(self.queen_positions)
        left_to_check = deepcopy(queen_positions)
        while left_to_check:
            x = left_to_check.pop()
            for y in left_to_check:
                if self.is_attacking(queen_positions, x, y):
                    attacking_pairs.append([x, y])
        return attacking_pairs

    def num_queen_attack(self):
        # queen attack
        return len(self.queen_attacks())

class Problem:
    def __init__(self, start_state=None):
        if not start_state:
            start_state = State()
        self.start_state = start_state

    def is_goal(self, state):
        # Check goal
        return state.num_queen_attack() == 0

    def cost_function(self, state):
        # Cost function
        return state.num_queen_attack()
