for i in range(0,4,1):
    for j in range(0,4,1):
        if i == 0 or i == 3 or j == 0 or j == 3:
            print('*', end='')
        else:
            print(' ', end='')
    print('')
    
    