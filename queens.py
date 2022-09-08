def noConflicts(board, current):
  '''
  Considers columns to the left of the current column to check for
  row and diagonal conflicts in the board.
  Returns:
    -False to indicate a conflict exists in the board
    -True to indicate no conflicts exist in the board
  '''
  for i in range(current):
      if board[i] == board[current]:
          return False
  for i in range(current):
      if board[current] - board[i] == current - i or board[current] - board[i] == i - current:
          return False
  if board[current] < 0 or board[current] >= len(board):
      return False
  return True


def EightQueensIterative(n=8):
    board = [-1] * n
    for i in range(n):
        board[0] = i
        for j in range(n):
            board[1] = j
            if not noConflicts(board, 1):
                continue
            for k in range(n):
                board[2] = k
                if not noConflicts(board, 2):
                    continue
                for l in range(n):
                    board[3] = l
                    if not noConflicts(board, 3):
                        continue
                    for m in range(n):
                        board[4] = m
                        if not noConflicts(board, 4):
                            continue
                        for o in range(n):
                            board[5] = o
                            if not noConflicts(board, 5):
                                continue
                            for p in range(n):
                                board[6] = p
                                if not noConflicts(board, 6):
                                    continue
                                for q in range(n):
                                    board[7] = q
                                    if noConflicts(board, 7):
                                        print (board)
    return


def EightQueens_returnN(numsol, n=8):
  '''
  Finds mulitple solutions to the 8 queens problem.
  Returns a list of board solutions with length = numsol
  If numsol is greater than the total number of solutions, returns a
  list with all solutions.
  '''
  listOfBoards = []

  board = [-1] * n
  if numsol == 0:
      return []
  for i in range(n):
      board[0] = i
      for j in range(n):
          board[1] = j
          if not noConflicts(board, 1):
              continue
          for k in range(n):
              board[2] = k
              if not noConflicts(board, 2):
                  continue
              for l in range(n):
                  board[3] = l
                  if not noConflicts(board, 3):
                      continue
                  for m in range(n):
                      board[4] = m
                      if not noConflicts(board, 4):
                          continue
                      for o in range(n):
                          board[5] = o
                          if not noConflicts(board, 5):
                              continue
                          for p in range(n):
                              board[6] = p
                              if not noConflicts(board, 6):
                                  continue
                              for q in range(n):
                                  board[7] = q
                                  if noConflicts(board, 7):
                                      listOfBoards.append(board[:])
                                      if len(listOfBoards) == numsol or len(listOfBoards) == 92:
                                          return listOfBoards
  return listOfBoards

def EightQueens_fill(locations):
  '''
  Generates a solution to the 8-Queens problem that is consistent with a given list of
  queen locations.

  For example, locations = [-1, 4, -1, -1, -1, -1, -1, 0] has two queens placed in
  the second and eighth columns. EightQueens_returnN should return [2, 4, 1, 7, 5, 3, 6, 0]
  as a solution consistent with the prescribed queen locations.

  If no solution exists, return None
  '''
  n = len(locations)
  board = [-1] * n
  for i in range(n):
      if locations[0] >= 0 and locations[0] != i:
          continue
      board[0] = i
      for j in range(n):
          if locations[1] >= 0 and locations[1] != j:
              continue
          board[1] = j
          if not noConflicts(board, 1):
              continue
          for k in range(n):
              if locations[2] >= 0 and locations[2] != k:
                  continue
              board[2] = k
              if not noConflicts(board, 2):
                  continue
              for l in range(n):
                  if locations[3] >= 0 and locations[3] != l:
                      continue
                  board[3] = l
                  if not noConflicts(board, 3):
                      continue
                  for m in range(n):
                      if locations[4] >= 0 and locations[4] != m:
                          continue
                      board[4] = m
                      if not noConflicts(board, 4):
                          continue
                      for o in range(n):
                          if locations[5] >= 0 and locations[5] != n:
                              continue
                          board[5] = o
                          if not noConflicts(board, 5):
                              continue
                          for p in range(n):
                              if locations[6] >= 0 and locations[6] != p:
                                  continue
                              board[6] = p
                              if not noConflicts(board, 6):
                                  continue
                              for q in range(n):
                                  if locations[7] >= 0 and locations[7] != q:
                                      continue
                                  board[7] = q
                                  if noConflicts(board, 7):
                                      return board
  return None


def prettyPrint(board):
  '''
  Generates a two-dimensional board representation of the single list of Queen row positions.
  A period ( . ) signifies an empty square on the board, and a Q signifies a queen.
  There should be a single space between each pair of periods/Q's.

  Returns a list of strings in the above format, one string per row.
  '''
  rows = []
  n = len(board)
  for i in range(n):
      queen = -1
      for j in range(n):
          if board[j] == i:
              queen = j
      if queen >= 0:
          rows.append(('. ' * queen + 'Q ' + '. ' * (n - queen - 1))[:-1])
      else:
          rows.append(('. ' * n)[:-1])

  return rows

def nQueens(board, current, size):
    if (current == size):
        return True
    else:
        for i in range(size):
            board[current] = i
            if (noConflicts(board, current)):
                done = nQueens(board, current + 1, size)
                if (done):
                    return True
        return False

def nQueens_fill(board, current, size, locations):
  '''
   Generates solutions with queens already placed in a list of locations,
   and returns one if it exists.For example, locations = [-1, -1, 4, -1, -1, -1, -1, 0, -1, 5]
   has three queens placed in the third, eighth, and tenth rows for a 10 × 10 board.

   Your nQueens_fill function should return a list of column locations for a solution
   that is consistent with the entered locations.
   If no solution exists, return None
   '''
  if (current == size):
      return board
  else:
      for i in range(size):
          if locations[current] >= 0 and locations[current] != i:
              continue
          board[current] = i
          if (noConflicts(board, current)):
              done = nQueens(board, locations, current + 1, size)
              if done:
                  return done
      return None


if __name__ == "__main__":
    incompleteBoard1 = [0, 6, 4, 7, 3, -1, -1, -1]
    incompleteBoard2 = [0, 6, 4, 7, 1, 6, -1, -1]
    solution1 = [2, 4, 1, 7, 5, 3, 6, 0]
    incompleteSolution1 = [2, -1, -1, 7, 5, -1, -1, -1]
    print(noConflicts(incompleteBoard1, 4), "Two queens on the same diagonal")
    print(noConflicts(incompleteBoard2, 5), "Two queens on the same row")
    print(noConflicts(solution1, 7), "No conflicts")
    print(EightQueens_returnN(4))
    prettyPrint(EightQueens_fill(incompleteSolution1))
    prettyPrint(incompleteBoard1)
    prettyPrint(solution1)
    prettyPrint(nQueens_fill(incompleteSolution1))
