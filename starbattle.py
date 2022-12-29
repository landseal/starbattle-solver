import copy
import time

#
v1b2p4x8 = [
    [1,1,1,1,2,3,3,3],
    [1,1,3,3,2,3,3,3],
    [1,1,3,3,3,3,4,3],
    [1,5,6,3,4,4,4,4],
    [1,5,6,3,6,4,4,4],
    [7,7,6,6,6,4,4,4],
    [7,7,6,6,6,6,4,4],
    [7,7,6,0,0,6,6,6]
]

v1b1p1x10 = [
    [0,0,0,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,2,0,1,1],
    [3,4,4,4,0,2,2,2,1,1],
    [3,3,3,3,5,6,6,2,1,1],
    [3,3,3,5,5,5,6,6,1,1],
    [3,3,7,5,5,5,6,6,1,1],
    [3,3,7,7,7,6,6,6,8,1],
    [3,3,3,3,3,3,6,6,8,1],
    [3,9,9,9,9,9,9,9,8,8],
    [9,9,9,9,9,9,9,9,9,8]
]

easyclamp = [
    [1,1,2,2,],
    [1,1,2,2,],
    [3,3,0,0,],
    [3,3,0,0,],
]

sixclamp = [
    [1,1,1,1,2,2,],
    [1,1,3,3,2,2,],
    [1,1,3,3,3,3,],
    [1,1,3,3,4,4,],
    [5,0,0,4,4,4,],
    [5,0,0,0,4,4,],
]

easyclampanswer = [
    ['-','X','-','-'],
    ['-','-','-','X'],
    ['X','-','-','-'],
    ['-','-','X','-'],
]

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

def validsolution(areas, starmap, areacount, starcount):
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
    
    # check that every column and row has exactly starcount Xs
    for row in range(starmapsize):
        rowcount = 0
        for col in range(starmapsize):
            if starmap[row][col] == 'X':
                rowcount += 1
        if rowcount != starcount: return False
    for col in range(starmapsize):
        colcount = 0
        for row in range(starmapsize):
            if starmap[row][col] == 'X':
                colcount += 1
        if colcount != starcount: return False

    # check if every area has exactly starcount Xs
    for areaindex in range(areacount):
        count = 0
        for row in range(starmapsize):
            for col in range(starmapsize):
                if areas[row][col] == areaindex and starmap[row][col] == 'X':
                    count += 1
        if count != starcount:
            return False

    return True

def checkvalid(starmap, starcount):
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
        if rowcount > starcount: return False
    for col in starmaprange:
        colcount = 0
        for row in starmaprange:
            if starmap[row][col] == 'X':
                colcount += 1
        if colcount > starcount: return False
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

def smartaddstar(starmap, symbol='X'):
    copymap = copy.deepcopy(starmap)
    starmapsize = len(starmap)
    starmaprange = range(starmapsize)
    for row in starmaprange:
        for col in starmaprange:
            if starmap[row][col] == ' ':
                copymap[row][col] = 'X'
                # set row to -
                for i in starmaprange:
                    if copymap[row][i] == ' ': copymap[row][i] = '-'
                # set col to -
                for i in starmaprange:
                    if copymap[i][col] == ' ': copymap[i][col] = '-'
                # set around to -
                if row != 0:
                    if copymap[row-1][col] == ' ': copymap[row-1][col]='-'
                    if col != 0:
                        if copymap[row-1][col-1] == ' ': copymap[row-1][col-1] = '-'
                    if col != starmapsize-1:
                        if copymap[row-1][col+1] == ' ': copymap[row-1][col+1] = '-'
                if row != starmapsize-1:
                    if copymap[row+1][col] == ' ': copymap[row+1][col] = '-'
                    if col != 0:
                        if copymap[row+1][col-1] == ' ': copymap[row+1][col-1] = '-'
                    if col != starmapsize-1:
                        if copymap[row+1][col+1] == ' ': copymap[row+1][col+1] = '-'
                if col != 0:
                    if copymap[row][col-1] == ' ': copymap[row][col-1] = '-'
                if col != starmapsize-1:
                    if copymap[row][col+1] == ' ': copymap[row][col+1] = '-'
                # set area to -
                

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


def recursivesolver(areas, starmap, starcount, debug=False):
    if debug:
        for row in starmap:
            print(row)
        print('')
    if checkfull(starmap):
        if validsolution(areas, starmap, len(starmap), starcount):
            print('valid')
            for row in starmap:
                print(row)
            print('valid')
            # a = input('> ')
            return True
        else:
            return False
    elif not checkvalid(starmap, starcount):
        # print('invalid')
        return False
    else:
        # recursivesolver(areas, addsymbol(starmap, 'X'), starcount, debug)
        recursivesolver(areas, smartaddstar(starmap), starcount, debug)
        recursivesolver(areas, addsymbol(starmap, '-'), starcount, debug)

def starbattlesolver(areas, starcount=0, debug=False):
    if starcount == 0:
        if len(areas) < 10:
            starcount = 1
        elif len(areas) < 14:
            starcount = 2
        else:
            starcount = 3
    print(starcount)
    areacount = len(areas)*starcount
    starttime = time.time()
    recursivesolver(areas, blankmap(len(areas)), starcount)
    print('elapsed time is', time.time()-starttime, 's')
