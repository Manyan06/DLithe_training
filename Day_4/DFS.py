def dfs(graph, node, visited):
  visited.add(node)
  print(node, end="")
  for neighbour in graph[node]:
    if neighbour not in visited:
      dfs(graph, neighbour, visited)

graph = {
  'A':['B', 'C'],
  'B':['D', 'E'],
  'C':['F'],
  'D':[],
  'E':['F'],
  'F':[]
}

start_node = input("Enter starting node: ")
print("DFS Traversal: ")
visited = set()
dfs(graph, start_node, visited)