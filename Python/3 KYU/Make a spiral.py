# https://www.codewars.com/kata/534e01fbbb17187c7e0000c6/train/python

def spiralize(size):
    def move():
        nonlocal x, y, direction, should_break
        should_break = False
        
        if direction == 0:
            if x == size - 1 or (x < size - 2 and spiral[y][x + 2] == 1):
                direction = 1
                should_break = True
            else:
                x += 1
                
        elif direction == 1:
            if y == size - 1 or (y < size - 2 and spiral[y + 2][x] == 1):
                direction = 2
                should_break = True
            else:
                y += 1
                
        elif direction == 2:
            if x == -1:
                x = 0
                direction = 3
                should_break = True
            elif x > 1 and spiral[y][x - 2] == 1:
                direction = 3
                should_break = True
            else:
                x -= 1
                
        elif direction == 3:
            if y == -1:
                y = 0
                direction = 0
                should_break = True
            elif y > 1 and spiral[y - 2][x] == 1:
                direction = 0
                should_break = True
            else:
                y -= 1
        else:
            should_break = True
    
    spiral = [[0 for x in range(size)] for y in range(size)] 
    
    x , y = 0, 0
    direction = 0
    should_break = True
    
    for _ in range(size):
        while True:
            spiral[y][x] = 1
            move()
            
            if(should_break):
                break

    for row in spiral:
        print(row)

    return spiral

spiralize(10)
