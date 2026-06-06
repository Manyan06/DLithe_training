def is_safe(board, row, col, n):
  #Check Column
  for i in range(row):
    if board[i][col] == "Q":
      return False
  #Check upper-left diagonal
  i, j = row - 1, col - 1
  while i >= 0 and j >= 0:
    if board[i][j] == "Q":
      return False
    i -= 1
    j -= 1
  #Check upper-right diagonal
  i, j = row - 1, col + 1
  while i >= 0 and j < n:
    if board[i][j] == "Q":
      return False
    i -= 1
    j += 1
  return True
  
def solve_n_queens(board, row, n):
  if row == n :
    for r in board:
      print(" ".join(r))
    print("\n")
    return True
  found_solution = False
  for col in range(n):
    if is_safe(board, row, col, n):
      board[row][col] = "Q"
      found_solution = solve_n_queens(board, row + 1, n) or found_solution
      board[row][col] = "."
  return found_solution

#Main program
n = int(input("Enter the value of N: "))
board = [["." for _ in range(n)] for _ in range(n)]
if not solve_n_queens(board, 0, n):
  print("No solution exists.")