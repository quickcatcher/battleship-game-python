class BattleGround:
    
    def __init__(self, size):
        cols = []
        self.grid = []
        for i in range(size):
            cols.append('_')
        for i in range(size):
            self.grid.append(list(cols))

    def get_grid(self):
        return self.grid

    def set_grid(self, grid):
        self.grid = grid