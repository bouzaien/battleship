import numpy as np
import random
from PIL import Image
from matplotlib import pyplot as plt
import seaborn as sns
import sys

class Battleship(object):
    """
    This class is used to start a game: initialize a Field() and randomply place Ship()'s.
    """
    def __init__(self, num_ships=2, ship_sizes=[(1,3),(1,5)], field_size=(10,10)) -> None:
        """
        By default, 2 ships of size 1x3 and 1x5 are placed on a 10x10 field.
        """
        assert len(ship_sizes) == num_ships
        self.num_ships = num_ships
        self.ship_sizes = ship_sizes
        self.field_size = field_size
        self.field = Field(self.field_size)
        self.ships = [Ship(size) for size in self.ship_sizes]
        self.fire_count = 0

        for ship in self.ships:
            self.placeShip(ship)            
    
    def placeShip(self, ship):
        """
        Randomly place a ship in the field, and update its cells as well as the field occupied cells
        """
        init_coord = random.choice(list(self.field.cells.keys()))
        init_row, init_column = init_coord
        direction = random.choice([-1, 1])
        if ship.vertical:
            if (init_row + direction * (ship.size[1]-1)) not in range(self.field_size[0]):
                direction = -direction
            ship_coords = [(x,init_column) for x in range(init_row, init_row + direction * ship.size[1], direction)]
        else:
            if (init_column + direction * (ship.size[1]-1)) not in range(self.field_size[1]):
                direction = -direction
            ship_coords = [(init_row,y) for y in range(init_column, init_column + direction * ship.size[1], direction)]

        new_cells = [self.field.cells[ship_coord] for ship_coord in ship_coords]
        ship.setCells(new_cells)
        self.field.updateOccupied(new_cells)

    def fireCell(self, cell):
        if cell not in self.field.fired_cells:
            self.field.updateFired(cell)
            self.fire_count += 1
            return 1
        print("Cell already fired. Choose another one!")
        return 0

    def play(self):
        # self.showShips()
        # while there is at least undestroyed ship
        f, axarr = plt.subplots(1, 2, sharex=True, sharey=True)
        while not all(map(Ship.isDestroyed, self.ships)):
            b = False
            while not b:
                try:
                    sys.stdout.write("Move number {}\n".format(self.fire_count+1))
                    sys.stdout.write("\r x ")
                    x = int(input())
                    sys.stdout.flush()
                    sys.stdout.write("\r y ")
                    y = int(input())
                    b = self.fireCell(self.field.cells[(x,y)])
                except:
                    print("Invalid value!")
            
            self.showState(f, axarr)
        print("Finished after {} moves.".format(self.fire_count))

    def showState(self, f, axarr):
        fm = self.field.fire_matrix
        sm = self.field.ships_matrix
        sns.heatmap(sm, ax=axarr[0], vmin=0, vmax=2, cbar=False, linewidths=.5)
        sns.heatmap(fm * sm + fm, ax=axarr[1], vmin=0, vmax=2, cbar=False, linewidths=.5)
        for ax in axarr:
            ax.set(adjustable='box', aspect='equal')
        plt.ion()
        plt.show()

    def showFired(self):
        fm = self.field.fire_matrix
        plt.imshow(fm, interpolation='nearest')
        plt.show()

    def showShips(self):
        sm = self.field.ships_matrix
        plt.imshow(sm, interpolation='nearest')
        plt.show()
    

class Ship(object):

    def __init__(self, size: tuple):
        """
        Initialize the ship with given size
        """
        self.size = tuple(sorted(size)) # sorted dimensions
        self.vertical = random.choice([True, False]) # randomly choose the orientation of the ship
        self.cells = list() # this is initialized by the Battleship class depending on the fields size
    
    def setCells(self, cells):
        self.cells = list()
        for cell in cells:
            self.cells.append(cell)

    def isDestroyed(self):
        # A ship is considered as destroyed if all its cells are fired
        return all(map(Cell.isFired, self.cells))



class Field(object):

    def __init__(self, size: tuple):
        self.cells = {(x,y): Cell((x,y)) for x in range(size[0]) for y in range(size[1])}
        self.matrix = np.zeros(size+(2,))
        self.occupied_cells = list()
        self.fired_cells = list()
        self.ships_matrix = self.matrix[:,:,0]
        self.fire_matrix = self.matrix[:,:,1]
    
    def updateOccupied(self, new_occupied: list):
        for cell in new_occupied:
            cell.is_occupied = True
            self.matrix[cell.coords+(0,)] = 1.0
            self.occupied_cells.append(cell)

    def updateFired(self, firedCell):
        firedCell.fire()
        self.fired_cells.append(firedCell)
        self.matrix[firedCell.coords+(1,)] = 1.0

    def areOccupied(self, cells: list):
        # if there is at least one occupied cell in the list
        return any(map(Cell.isOccupied, cells))


class Cell(object):

    def __init__(self, coords):
        self.coords = coords
        self.is_occupied = False
        self.is_fired = False
        
    def isOccupied(self):
        return self.is_occupied

    def isFired(self):
        return self.is_fired

    def fire(self):
        self.is_fired = True

    def __eq__(self, other): 
        if not isinstance(other, Cell):
            return NotImplemented

        return self.coords == other.coords

    def __repr__(self):
        """
        To display coordinates when calling a cell.
        """
        return self.coords.__str__()


if __name__ == "__main__":
    bs = Battleship()
    bs.play()