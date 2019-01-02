"""
Clone of 2048 game.
""" 
   
import poc_2048_gui
import random
# Directions, DO NOT MODIFY 
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4 
  
# Offsets for computing tile indices in each direction. 
# DO NOT MODIFY this dictionary. 
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}
 
def merge(line):
    line_merge = line[:]

    def _arrange(num_list):
        pop_num = 0
        while 0 in num_list:
            num_list.remove(0)
            pop_num+=1
        for _times in range(pop_num):
            num_list.append(0)
        return num_list
    
    for line_merge_idx in range(len(line_merge)):
        _arrange(line_merge)
        if line_merge_idx+1 < len(line_merge):
            if line_merge[line_merge_idx] == line_merge[line_merge_idx+1]:
                line_merge[line_merge_idx] += line_merge[line_merge_idx]
                line_merge[line_merge_idx+1] = 0

    line_merge = _arrange(line_merge)
    return line_merge

class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self.reset()
        
    def reset(self):
        self._value = [[ 0 for _col_num in range(self._grid_width)]
                           for _row_num in range(self._grid_height)]
        for _times in range(2):
            row_reset_idx = random.randrange(0,self._grid_height)
            cow_reset_idx = random.randrange(0,self._grid_width)
            self._value[row_reset_idx][cow_reset_idx] = 2
        

    def __str__(self):
        return str(self._value)

    def get_grid_height(self):
         return self._grid_height

    def get_grid_width(self):
        return self._grid_width

    def move(self, direction):
        before_value = str(self._value[:])
        
        if direction == DOWN:
            for _col_num in range(0,self._grid_width):
                temp_lst = []
                for _row_num in range(self._grid_height-1,-1,-1):
                    temp_lst.append(self._value[_row_num][_col_num])
                temp_lst = merge(temp_lst)
                for _row_num in range(self._grid_height-1,-1,-1):
                    temp_num = self._grid_height-_row_num-1
                    self._value[_row_num][_col_num] = temp_lst[temp_num]
        elif direction == UP:
            for _col_num in range(0,self._grid_width):
                temp_lst = []
                for _row_num in range(self._grid_height):
                    temp_lst.append(self._value[_row_num][_col_num])
                temp_lst = merge(temp_lst)
                for _row_num in range(self._grid_height):
                    temp_num = _row_num
                    self._value[_row_num][_col_num] = temp_lst[temp_num]        
        elif direction == LEFT:
            for _row_num in range(self._grid_height):
                temp_lst = []
                for _col_num in range(0,self._grid_width):
                    temp_lst.append(self._value[_row_num][_col_num])
                temp_lst = merge(temp_lst)
                for _col_num in range(0,self._grid_width):
                    temp_num = _col_num
                    self._value[_row_num][_col_num] = temp_lst[temp_num]
        elif direction == RIGHT:
            for _row_num in range(0,self._grid_height):
                temp_lst = []
                for _col_num in range(self._grid_width-1,-1,-1):
                    temp_lst.append(self._value[_row_num][_col_num])
                temp_lst = merge(temp_lst)
                for _col_num in range(self._grid_width-1,-1,-1):
                    temp_num = self._grid_width-_col_num-1
                    self._value[_row_num][_col_num] = temp_lst[temp_num]
        if str(self._value) != before_value:
            self.new_tile()
                                
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        possible_lst = [2,2,2,2,2,2,2,2,2,4]
        _moveable = False
        for _row in range(self._grid_height):
            for _cow in range(self._grid_width):
                if self._value[_row][_cow] == 0:
                    _moveable = True
        while _moveable:
            _row_reset_idx = random.randrange(0,self._grid_height)
            _cow_reset_idx = random.randrange(0,self._grid_width)
            if self._value[_row_reset_idx][_cow_reset_idx] == 0:
                self._value[_row_reset_idx][_cow_reset_idx]= random.choice(possible_lst)
                break 
            
            
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._value[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._value[row][col]

poc_2048_gui.run_gui(TwentyFortyEight(4,4))

