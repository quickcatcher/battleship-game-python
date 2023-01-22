from battleground import BattleGround
from player import Player


def place_ships(player, positions):
    player_battleGrid = player.getBattleGrid()
    grid = player_battleGrid.get_grid()
    for i in positions:
        x = int(i.split(':')[0])
        y = int(i.split(':')[1])
        grid[x][y] = 'B'

    player_battleGrid.set_grid(grid)
    player.setBattleGrid(player_battleGrid)

def MakeaMove(player, opposition, position):
    player.moves_left-=1
    
    opposition_battleground = opposition.getBattleGrid()
    grid = opposition_battleground.get_grid()
    x = int(position.split(',')[0])
    y = int(position.split(',')[1])
    if(grid[x][y] == 'B'):
        grid[x][y] = 'X'
        opposition.ships-=1
        player.hits+=1
    else:
        grid[x][y] = 'O'
    
    opposition_battleground.set_grid(grid)
    opposition.setBattleGrid(opposition_battleground)

def printGrid(grid):
    gridStr = ""
    for i in grid:
        for j in i:
            gridStr+= j+" "
        gridStr+="\n"
    return gridStr

inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

grid_size = inputLines[0].strip()
number_of_ships = inputLines[1].strip()
number_of_misiles = inputLines[4].strip()

player1_ground = BattleGround(int(grid_size))
player1 = Player(player1_ground, number_of_misiles, number_of_ships)

player2_ground = BattleGround(int(grid_size))
player2 = Player(player2_ground, number_of_misiles, number_of_ships)

player1_ship_positions = inputLines[2].strip().split(',')
place_ships(player1, player1_ship_positions)

player2_ship_positions = inputLines[3].strip().split(',')
place_ships(player2, player2_ship_positions)

player1_moves = inputLines[5].strip().split(':')
for i in player1_moves:
    MakeaMove(player1, player2, i)

player2_moves = inputLines[6].strip().split(':')
for i in player2_moves:
    MakeaMove(player2, player1, i)

g1 = player1.getBattleGrid().get_grid()
g2 = player2.getBattleGrid().get_grid()

ansString = "Player1\n"
ansString+=printGrid(g1)
ansString+="\n\nPlayer2\n"
ansString+=printGrid(g2)
ansString+="\n\nP1:"
ansString+=str(player1.hits)
ansString+="\nP2:"
ansString+=str(player2.hits)
if(player1.hits>player2.hits):
    ansString+="\nPlayer1 wins"
elif(player2.hits>player1.hits):
    ansString+="\nPlayer2 wins"
else:
    ansString+="\nIt is a draw"

#print(ansString)

outputFile = open('output.txt', 'w')
outputFile.writelines(ansString)
outputFile.close()