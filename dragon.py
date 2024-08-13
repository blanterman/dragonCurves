cont = True
turns = [0]
middle = [0]
while cont:
    print('next iteration: {}'.format(turns))
    choice = input('do next? [y/n] ')
    if choice == 'y' or choice == 'Y':
        oldturns = turns[:]
        begturns = [0 if turn == 1 else 1 for turn in turns]
        begturns.reverse()
        turns = []
        turns = begturns + middle + oldturns
    else:
        cont = False



