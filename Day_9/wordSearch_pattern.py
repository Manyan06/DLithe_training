def search_pattern(grid, pattern):
  rows = len(grid)
  cols = len(grid[0])

  def backtrack(r, c, index):
    if index == len(pattern):
      return True
    if (r<0 or r >= rows or c<0 or c >= cols or grid[r][c] != pattern[index]):
      return False
    temp = grid[r][c]
    grid[r][c] = '#'
    found = (
      backtrack(r + 1, c, index + 1) or backtrack(r - 1, c, index + 1) or backtrack(r, c + 1, index + 1) or backtrack(r, c - 1, index + 1)
    )
    grid[r][c] = temp
    return found
  for i in range(rows):
    for j in range(cols):
      if backtrack(i, j, 0):
        return True
  return False

grid = [
  ['C','A','T','D','O','G'],
  ['X','Z','T','R','A','T'],
  ['Y','O','G','B','I','R'],
  ['L','I','O','N','E','E'],
  ['T','I','G','E','R','S'],
  ['M','O','U','S','E','P']
]
patterns = ["CAT", "DOG", "RAT", "LION", "TIGER", "MOUSE", "BIRD"]

for word in patterns:
  if search_pattern(grid, word):
    print(word, "-> Pattern found")
  else:
    print(word, "-> Pattern Not found")