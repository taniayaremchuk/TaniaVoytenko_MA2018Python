"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        
        self._zombie_list = []
        self._human_list = []
        poc_grid.Grid.clear(self)
        
    def add_zombie(self, row, col):        
        self._zombie_list.append((row, col))
                
    def num_zombies(self):        
        return len(self._zombie_list)
          
    def zombies(self):        
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        self._human_list.append((row, col))
        
    def num_humans(self):
        return len(self._human_list)
    
    def humans(self):
        for human in self._human_list:
            yield human
        
    def compute_distance_field(self, entity_type):
        visited = poc_grid.Grid(self._grid_height, self._grid_width)
        distance_field = [[self._grid_height * self._grid_width for dummy_col in range(self._grid_width)]
                       for dummy_row in range(self._grid_height)]
        boundary = poc_queue.Queue()
        if entity_type == HUMAN:
            for human in self.humans():
                boundary.enqueue(human)
                visited.set_full(human[0], human[1])
                distance_field[human[0]][human[1]] = 0
        elif entity_type == ZOMBIE:
            for zombie in self.zombies():
                boundary.enqueue(zombie)
                visited.set_full(zombie[0], zombie[1])
                distance_field[zombie[0]][zombie[1]] = 0
        
        while len(boundary) > 0:
            current_cell = boundary.dequeue()
            for neighbor in visited.four_neighbors(current_cell[0], current_cell[1]):
                if visited.is_empty(neighbor[0], neighbor[1]) and self.is_empty(neighbor[0], neighbor[1]):
                    visited.set_full(neighbor[0], neighbor[1])
                    boundary.enqueue((neighbor[0], neighbor[1]))
                    distance_field[neighbor[0]][neighbor[1]] = distance_field[current_cell[0]][current_cell[1]] + 1
        
        return distance_field
    
    def move_humans(self, zombie_distance_field):
        for num_human in range(self.num_humans()):
            human = self._human_list[num_human]
            current_distance = zombie_distance_field[human[0]][human[1]]
            possible_moves = [human]

            for neighbor in self.eight_neighbors(human[0], human[1]):
                if self.is_empty(neighbor[0], neighbor[1]):
                    if zombie_distance_field[neighbor[0]][neighbor[1]] > current_distance:
                        current_distance = zombie_distance_field[neighbor[0]][neighbor[1]]
                        possible_moves = [neighbor]
                    elif zombie_distance_field[neighbor[0]][neighbor[1]] == current_distance:
                        possible_moves.append(neighbor)     
            self._human_list[num_human] = random.choice(possible_moves)
   
    
    def move_zombies(self, human_distance_field):
        for num_zombie in range(self.num_zombies()):
            zombie = self._zombie_list[num_zombie]
            current_distance = human_distance_field[zombie[0]][zombie[1]]
            possible_moves = [zombie]

            for neighbor in self.four_neighbors(zombie[0], zombie[1]):
                if self.is_empty(neighbor[0], neighbor[1]):
                    if human_distance_field[neighbor[0]][neighbor[1]] < current_distance:
                        current_distance = human_distance_field[neighbor[0]][neighbor[1]]
                        possible_moves = [neighbor]
                    elif human_distance_field[neighbor[0]][neighbor[1]] == current_distance:
                        possible_moves.append(neighbor)     
            self._zombie_list[num_zombie] = random.choice(possible_moves)

            
            
poc_zombie_gui.run_gui(Apocalypse(30, 40))
