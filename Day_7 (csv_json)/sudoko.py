def is_valid(board, row, col, num):

  for i in range(9):
    if board[row][i] == num:
      return False
  for i in range(9):  
    if board[row][i] == num:
      return False
    
  start_row = row - row % 3
  start_col = col - col % 3

  for i in range(3):
    for j in range(3):
      if board[start_row + i][start_col + i] == num:
        return False
  return True

def solve_sudoku(board):
  for row in range(9):
    for col in range(9):
      if board[row][col] == 0:
        for num in range(1, 10):
          if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
              return True
            board[row][col] = 0
        return False
  return True

board = [
  [3,0,6,5,7,8,4,0,0],
  [5,2,0,0,0,0,0,0,0],
  [0,8,7,0,0,0,0,3,1],
  [0,0,3,0,1,0,0,8,0],
  [9,0,0,8,6,3,0,0,5],
  [0,5,0,0,9,0,6,0,0],
  [1,3,0,0,0,0,2,5,0],
  [0,0,0,0,0,0,0,7,4],
  [0,0,5,2,8,6,3,0,0]
]
solve_sudoku(board)
for row in board:
  print(row)