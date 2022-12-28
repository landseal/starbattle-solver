arealist = [
    [1,1,1,2,2,],
    '13332',
    '44422',
    '44422',
    '55555',
]
mapsize = 5

def blankmap(size):
    lol = []
    for row in range(size):
        helper = []
        for col in range(size):
            helper += [' ']
        lol += [helper]
    return lol

def checkvalid(areas, starmap):
    starmapsize = len(starmap)
    starmaprange = range(starmapsize)
    # check no Xs next to each other
    validity = True
    for row in starmaprange:
        for col in starmaprange:
            if starmap[row][col] == 'X':
                if row != starmapsize-1:
                    # check square below
                    if starmap[row+1][col] == 'X': validity = False
                if col != starmapsize-1:
                    # check square to right
                    if starmap[row][col+1] == 'X': validity = False
                if row != starmapsize-1 and col != starmapsize-1:
                    # check square below and right
                    if starmap[row+1][col+1] == 'X': validity = False
                if row != starmapsize-1 and col != 0:
                    # check square below and left
                    if starmap[row+1][col-1] == 'X': validity = False
    return validity
                    

def checkfull(starmap):
    # print(starmap)
    for row in starmap:
        if ' ' in row: return False
    return True

def addsymbol(starmap, symbol):
    starmapsize = len(starmap)
    starmaprange = range(starmapsize)
    notadded = True
    for row in starmaprange:
        for col in starmaprange:
            if starmap[row][col] == ' ':
                if notadded:
                    starmap[row][col] = symbol
                    notadded = False
    return starmap

def backtonotstar(starmap):
    starmapsize = len(starmap)
    starmaprange = range(starmapsize)
    added = False
    prevrow = 0
    prevcol = 0
    for row in starmaprange:
        for col in starmaprange:
            if starmap[row][col] == ' ':
                if not added:
                    starmap[prevrow][prevcol] = '-'
                    added = True
            else:
                prevrow = row
                prevcol = col
    return starmap


def recursivesolver(areas, starmap):
    # print('hi')
    for row in starmap:
        print(row)
    print(' ')
    if checkfull(starmap) and checkvalid(areas, starmap):
        print('valid')
        for row in starmap:
            print(row)
        return True
    elif not checkvalid(areas, starmap):
        print('invalid')
        return False
    else:
        # addstar = recursivesolver(areas, addsymbol(starmap, 'X'))
        # addnotstar = recursivesolver(areas, addsymbol(starmap, '-'))
        recursivesolver(areas, addsymbol(starmap, '-'))
        recursivesolver(areas, addsymbol(starmap, 'X'))

recursivesolver(arealist, blankmap(5))