import math

INPUT_FILE = '12-input.txt'
STARTING_POINT = 'S'
EXIT_POINT = 'E'
HEIGHTS = 'abcdefghijklmnopqrstuvwxyz'

class Cell:
    def __init__(self):
        self.height = None
        self.proximity = math.inf
        self.line = None
        self.column = None
        self.visited = False

    def to_string(self):
        return f"Cell: line={self.line}, column={self.column}, height={self.height}, proximity={self.proximity}, visited={self.visited}"

    def set_coordinates(self, line, column):
        self.line = line
        self.column = column

    def update_proximity(self, new_proximity):
        if new_proximity < self.proximity:
            self.proximity = new_proximity
        print(self.to_string())

    def get_neighbor_coordinates(self, grid_height, grid_width):
        coordinates = []
        if self.line != 0:
            coordinates.append([self.line - 1, self.column])
        if self.line != grid_height - 1:
            coordinates.append([self.line + 1, self.column])
        if self.column != 0:
            coordinates.append([self.line, self.column - 1])
        if self.column != grid_width - 1:
            coordinates.append([self.line, self.column + 1])
        return coordinates

    def is_reachable_neighbor(self, cell):
        if abs(self.line - cell.line) not in [0, 1]:
            print("line")
            return False
        if abs(self.column - cell.column) not in [0, 1]:
            print("column")
            return False
        if self.height - cell.height >= -1:
            print("height")
            return True

    def get_unvisited_reachable_neighbors(self, grid):
        coordinates = self.get_neighbor_coordinates(grid.height, grid.width)
        unvisited_neighbors = []
        for coordinate in coordinates:
            cell = grid.get_cell(*coordinate)
            if not cell.visited and self.is_reachable_neighbor(cell):
                unvisited_neighbors.append(cell)
        return unvisited_neighbors

class Grid:
    def __init__(self, lines, columns):
        self.grid = [[Cell() for _ in range(columns)] for _ in range(lines)]
        self.height = lines
        self.width = columns
        self.starting_point = None
        self.exit_point = None

    def get_cells(self):
        cells = []
        for i in range(self.height):
            for j in range(self.width):
                cells.append(self.get_cell(i, j))
        return cells

    def get_cell(self, line, column):
        return self.grid[line][column]

    def set_starting_point(self, line, column):
        self.starting_point = self.get_cell(line, column)
        self.starting_point.proximity = 0

    def set_exit_point(self, line, column):
        self.exit_point = self.get_cell(line, column)

    def find_shortest_path_length(self):
        unvisited_cells = self.get_cells()

        starting_point_cell = self.starting_point
        current_cell = starting_point_cell

        exit_point_cell = self.exit_point

        while current_cell != exit_point_cell and len(unvisited_cells) > 1 and current_cell.proximity != math.inf and not current_cell.visited:
            print(f"Current cell: {current_cell.to_string()}")
            neighbors = current_cell.get_unvisited_reachable_neighbors(self)
            print(f"Neighbors: {[neighbor.to_string() for neighbor in neighbors]}")
            for neighbor in neighbors:
                neighbor.update_proximity(current_cell.proximity + 1)
            current_cell.visited = True
            unvisited_cells.remove(current_cell)
            unvisited_cells.sort(key=lambda o: o.proximity)
            print([unvisited_cell.to_string() for unvisited_cell in unvisited_cells])
            current_cell = unvisited_cells[0]

        return self.exit_point.proximity

def build_grid():
    with open(INPUT_FILE) as f:
        lines = f.readlines()
        columns_nb = len(lines[0][:-1])
        lines_nb = len(lines)
        grid = Grid(lines_nb, columns_nb)
        for i in range(len(lines)):
            line = lines[i][:-1]
            if STARTING_POINT in line:
                column = line.index(STARTING_POINT)
                grid.set_starting_point(i, column)
            if EXIT_POINT in line:
                column = line.index(EXIT_POINT)
                grid.set_exit_point(i, column)
            for j in range(len(line)):
                cell = grid.get_cell(i, j)
                cell.line = i
                cell.column = j
                if STARTING_POINT == line[j]:
                    cell.height = 0
                elif EXIT_POINT == line[j]:
                    cell.height = 26
                else:
                    cell.height = HEIGHTS.index(line[j])
    return grid

grid = build_grid()
print(grid.find_shortest_path_length())
