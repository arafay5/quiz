def rec(x,y):
    for char in range(y-1):
        print('*',end=' ')
    for char in range(x-1):
        print('*'+' '*((y*2)-3)+'*')
    for char in range(y):
        print('*',end=' ')
