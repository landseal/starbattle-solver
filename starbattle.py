import copy

#
v1b2p4x8 = [
    [1,1,1,1,2,3,3,3],
    [1,1,3,3,2,3,3,3],
    [1,1,3,3,3,3,4,3],
    [1,5,6,3,4,4,4,4],
    [1,5,6,3,6,4,4,4],
    [7,7,6,6,6,4,4,4],
    [7,7,6,6,6,6,4,4],
    [7,7,6,8,8,6,6,6]
]
mapsize = 8

blanklol = [
    [' ', ' ', ' ', ' ', ' ',' ',' ',' '],
    [' ', ' ', ' ', ' ', ' ',' ',' ',' '],
    [' ', ' ', ' ', ' ', ' ',' ',' ',' '],
    [' ', ' ', ' ', ' ', ' ',' ',' ',' '],
    [' ', ' ', ' ', ' ', ' ',' ',' ',' '],
    [' ', ' ', ' ', ' ', ' ',' ',' ',' '],
    [' ', ' ', ' ', ' ', ' ',' ',' ',' '],
    [' ', ' ', ' ', ' ', ' ',' ',' ',' '],
]
def blankmap(size):
    lol = []
    for row in range(size):
        helper = []
        for col in range(size):
            helper += [' ']
        lol += [helper]
    return lol

def validsolution(areas, starmap):
    starmapsize = len(starmap)
    # check no Xs next to each other
    for row in range(starmapsize):
        for col in range(starmapsize):
            if starmap[row][col] == 'X':
                if row != starmapsize-1:
                    # check square below
                    if starmap[row+1][col] == 'X': return False
                if col != starmapsize-1:
                    # check square to right
                    if starmap[row][col+1] == 'X': return False
                if row != starmapsize-1 and col != starmapsize-1:
                    # check square below and right
                    if starmap[row+1][col+1] == 'X': return False
                if row != starmapsize-1 and col != 0:
                    # check square below and left
                    if starmap[row+1][col-1] == 'X': return False
    
    # check that every column and row has exactly 1 X
    for row in range(starmapsize):
        rowcount = 0
        for col in range(starmapsize):
            if starmap[row][col] == 'X':
                rowcount += 1
        if rowcount != 1: return False
    for col in range(starmapsize):
        colcount = 0
        for row in range(starmapsize):
            if starmap[row][col] == 'X':
                colcount += 1
        if colcount != 1: return False

    # check if every area has exactly 1 X
    for areaindex in range(mapsize):
        count = 0
        for row in range(starmapsize):
            for col in range(starmapsize):
                if areas[row][col] == areaindex and starmap[row][col] == 'X':
                    count += 1
        if count != 1:
            return False
    return True

def checkvalid(starmap):
    starmapsize = len(starmap)
    starmaprange = range(starmapsize)
    # check no Xs next to each other
    # validity = True
    for row in starmaprange:
        for col in starmaprange:
            if starmap[row][col] == 'X':
                if row != starmapsize-1:
                    # check square below
                    if starmap[row+1][col] == 'X': return False
                if col != starmapsize-1:
                    # check square to right
                    if starmap[row][col+1] == 'X': return False
                if row != starmapsize-1 and col != starmapsize-1:
                    # check square below and right
                    if starmap[row+1][col+1] == 'X': return False
                if row != starmapsize-1 and col != 0:
                    # check square below and left
                    if starmap[row+1][col-1] == 'X': return False
    
    # check if any column or row has more than 2 Xs
    for row in starmaprange:
        rowcount = 0
        for col in starmaprange:
            if starmap[row][col] == 'X':
                rowcount += 1
        if rowcount > 1: return False
    for col in starmaprange:
        colcount = 0
        for row in starmaprange:
            if starmap[row][col] == 'X':
                colcount += 1
        if colcount > 1: return False
    return True
                    

def checkfull(starmap):
    # print(starmap)
    for row in starmap:
        if ' ' in row: return False
    return True

def addsymbol(starmap, symbol):
    copymap = copy.deepcopy(starmap)
    starmapsize = len(starmap)
    starmaprange = range(starmapsize)
    for row in starmaprange:
        for col in starmaprange:
            if starmap[row][col] == ' ':
                copymap[row][col] = symbol
                return copymap

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
    for row in starmap:
        print(row)
    print('')
    if checkfull(starmap) and validsolution(v1b2p4x8, starmap):
        print('valid')
        for row in starmap:
            print(row)
        print('valid')
        return True
    elif not checkvalid(starmap):
        print('invalid')
        return False
    else:
        recursivesolver(areas, addsymbol(starmap, 'X'))
        recursivesolver(areas, addsymbol(starmap, '-'))

recursivesolver(v1b2p4x8, blanklol)
