def snail(snail_map):
    def move():
        nonlocal x, y, direction, should_break
        should_break = False
        
        if direction == 0:
            if x == len(snail_map) - 1 or (x < len(snail_map) - 1 and marked[y][x + 1] == 1):
                direction = 1
                should_break = True
            else:
                x += 1
                
        elif direction == 1:
            if y == len(snail_map) - 1 or (y < len(snail_map) - 1 and marked[y + 1][x] == 1):
                direction = 2
                should_break = True
            else:
                y += 1
                
        elif direction == 2:
            if x == -1:
                x = 0
                direction = 3
                should_break = True
                
            elif x > 0 and marked[y][x - 1] == 1:
                direction = 3
                should_break = True
            else:
                x -= 1
                
        elif direction == 3:
            if y == -1:
                y = 0
                direction = 0
                should_break = True
                
            elif y > 0 and marked[y - 1][x] == 1:
                direction = 0
                should_break = True
            else:
                y -= 1
        else:
            should_break = True
    
    if len(snail_map[0]) == 0:
        return []
        
    x = y = direction = 0
    should_break = True
    array = []
    marked = [[0 for _ in range(len(snail_map))] for _ in range(len(snail_map))] 
    
    for _ in range(len(snail_map) * 2):
        while True:
            if marked[y][x] == 0:
                array.append(snail_map[y][x])
                
            marked[y][x] = 1   
            move()
            
            if(should_break):
                break

    return array
