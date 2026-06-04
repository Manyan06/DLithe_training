from collections import deque
def bfs(city_map, start):
  visited = set()
  queue = deque([start])
  visited.add(start)
  print("Locations visited: ")
  while queue:
    location = queue.popleft()
    print(location, end = " ")
    for neighbour in city_map[location]:
      if neighbour not in visited:
        visited.add(neighbour)
        queue.append(neighbour)
city_map = {
        "Airport" : ["Mall", "Railway Station"],
        "Mall" : ["Hospital", "College"],
        "Railway Station" : ["Bustand"],
        "Hospital" : [],
        "College" : [],
        "Bustand" : []
}
start_location = input("Enter starting location: ")
bfs(city_map, start_location)


