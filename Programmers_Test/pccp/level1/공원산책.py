def solution(park, routes):
    width = len(park[0]) # y
    height = len(park) # x

    for i in range(height):
        for j in range(width):
            if "S" == park[i][j]:
                current_x, current_y = i, j

    for route in routes:
        road = route.split()
        target_x = current_x
        target_y = current_y
        check = True

        for i in range(int(road[1])):
            if road[0] == "N":
                target_x -= 1
            elif road[0] == "S":
                target_x += 1
            elif road[0] == "W":
                target_y -= 1
            else:
                target_y += 1
            
            if target_x < 0 or target_x >= height or target_y < 0 or target_y >= width:
                check = False
                break
            elif park[target_x][target_y] == "X":
                check = False
                break
        
        if (0 <= target_x < height) and (0 <= target_y < width) and check:
            current_x = target_x
            current_y = target_y

    return [current_x, current_y]


park = ["OSO","OOO","OXO","OOO"]	
routes = ["E 2","S 3","W 1"]
print(solution(park, routes))