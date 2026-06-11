class Driver:
  def __init__(self, name, distance):
    self.name = name
    self.distance = distance

drivers = [
  Driver("Driver 1", 5),
  Driver("Driver 2", 2),
  Driver("Driver 3", 8),
  Driver("Driver 4", 3)
]

nearest = drivers[0]
for driver in drivers:
  if driver.distance < nearest.distance:
    nearest = driver

print("Nearest Driver :",nearest.name)
print("Distance :",nearest.distance, "km")