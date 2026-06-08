def backtrack(path, used): 
  if len(path) == 3:
    print(path)
    return
  for num in [1, 2, 3]:
    if num not in used:
      path.append(num)
      used.add(num)
      backtrack(path, used)
      #Backtrack
      path.pop()
      used.remove(num)
backtrack([], set())