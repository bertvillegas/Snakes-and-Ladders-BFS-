from collections import deque
def minimum_moves(board):

  def neighbors(position,board):
    return_list=[]
    for i in range(1,7):
      if position+i <= len(board)-1:
        if board[position+i] != -1:       
          return_list.append(board[position+i])
        else:
          return_list.append(position+i)
      else: return return_list
    return return_list
      

  if not board: return -1

  q, visited = deque(), set()
  rolls=0

  start = 0
  q.append((start,rolls))

  while q:
    position, rolls = q.popleft()
    if position in visited: continue
    visited.add(position)  
    if position == len(board)-1: return rolls
    position_neighbors = neighbors(position,board)
    for neighbor in position_neighbors:
      if neighbor not in visited:
        q.append((neighbor,rolls+1))
    #if not q: return rolls
  return -1 

print(minimum_moves([-1, -1, -1, 7, -1, -1, -1,-1,16,7,-1,-1,-1,-1,-1,-1,-1,-1]))
