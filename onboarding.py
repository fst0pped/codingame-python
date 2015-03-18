import sys, math

# CodinGame planet is being attacked by slimy insectoid aliens.


# game loop
while 1:
    enemy1 = input() # name of enemy 1
    dist1 = int(input()) # distance to enemy 1
    enemy2 = input() # name of enemy 2
    dist2 = int(input()) # distance to enemy 2
    
    enemies = {enemy1:dist1,enemy2:dist2}
    nearest = min(enemies,key=enemies.get)
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    print(enemies,file=sys.stderr)
    
    print(nearest) # replace with correct ship name
