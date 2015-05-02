'''Paint-by-numbers solver.'''

class Puzzle(object):
  '''A paint-by-numbers puzzle.'''

  def __init__(self, clues):
    self.clues = clues
    self.num_rows = len(clues['rows'])
    self.num_columns = len(clues['columns'])
    self.cells = []
    for i in range(self.num_rows):
      self.cells.append([])
      for j in range(self.num_columns):
        self.cells[i].append(None)

  def __str__(self):
    result = str(self.num_rows) + ' rows, ' + str(self.num_columns) + ' columns\n'
    for row in self.cells:
      result += '\n'
      for cell in row:
        if (cell == None):
          result += '  '
        else:
          result += cell + ' '
    return result

  def set_cell(self, row, column, value):
    '''Sets the color of the provided cell.'''
    self.cells[row][column] = value

  def solve(self):
    for i, row in enumerate(self.cells):
      row_clues = self.clues['rows'][i]


clues = {
  'rows': [[2], [1]],
  'columns': [[2], [1]],
}
puzzle = Puzzle(clues)
puzzle.set_cell(0, 0, 'b')
puzzle.set_cell(1, 1, 'w')
print puzzle
