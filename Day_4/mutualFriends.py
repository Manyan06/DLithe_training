def dfs(friends_network, person, visited):
  visited.add(person)
  print(person, end=" ")
  for friend in friends_network[person]:
    if friend not in visited:
      dfs(friends_network, friend, visited)

friends_network = {
  "Alice" : ["Bob", "Charlie"],
  "Bob"   : ["David", "Emma"],
  "Charlie" : ["Frank"],
  "David" : [],
  "Emma" : [],
  "Frank" : []
}

start_person = input("Enter starting friend: ")
visited= set()
print("Friends Network Traversal")
dfs(friends_network, start_person, visited)