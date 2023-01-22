class Player:
    __battlegrid = []

    def __init__(self, battleground, moves, ships):
        self.__battlegrid = battleground
        self.moves_left = int(moves)
        self.ships = int(ships)
        self.hits = 0
    
    def getBattleGrid(self):
        return self.__battlegrid

    def setBattleGrid(self, grid):
        self.__battlegrid = grid

    