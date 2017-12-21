def tower_builder(n_floors):
    tower =[]
    counter = 0
    for floor in range(n_floors):
      counter += 1
      floor = "*" * counter
      tower.insert(len(tower), floor)
      counter += 1
      print(counter)
    print(tower)

# clever soultions 
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]