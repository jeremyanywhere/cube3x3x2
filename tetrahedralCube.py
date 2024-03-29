
#cube is numbered thus.
#The main triangular pieces are number on each face, 1, 
#then 234, then on the face to the right, 5, 678 etc. but the corner pieces are tetrahedrons and 
#have 3 faces themselves, 
# so each one of those gets an a,b,c.  The middle pieces don't, but to keep the model
# of teh cube consistent and simple we divide each middle piece into 3 triangles, 
# each divided triangle being adjacent to a corner.
# That gives us an effective total count of 24 pieces
# we have 9 moves

import time

MAX_DEPTH = 7

all_positions = [[] for _ in range(MAX_DEPTH+1)]
start_position = my_dict = {"1a": "1a", "1b": "1b", "1c": "1c", "2a": "2a", "2b": "2b", "2c": "2c", 
                            "3a": "3a", "3b": "3b", "3c": "3c", "4a": "4a", "4b": "4b", "4c": "4c", 
                            "5a": "5a", "5b": "5b", "5c": "5c", "6a": "6a", "6b": "6b", "6c": "6c", 
                            "7a": "7a", "7b": "7b", "7c": "7c", "8a": "8a", "8b": "8b", "8c": "8c"}

moves = ['right_forward', 'right_back', 'right_180',
         'left_forward', 'left_back', 'left_180',
         'top_left', 'top_right', 'top_180']


def front_clock(current):
    new_pos = current.copy()
    new_pos["4a"] = "8a"
    new_pos["4b"] = "8c"

    return new_pos

def front_anticlock(current):
    new_pos = current[:]
    new_pos[0] = current[2]; new_pos[1] = current[5]; new_pos[2] = current[8]
    new_pos[3] = current[1];                          new_pos[5] = current[7]
    new_pos[6] = current[0]; new_pos[7] = current[3]; new_pos[8] = current[6]
    new_pos[9] = current[12]; new_pos[10] = current[13]; new_pos[11] = current[14]
    new_pos[12] = current[15]; new_pos[13] = current[16]; new_pos[14] = current[17]
    new_pos[15] = current[18]; new_pos[16] = current[19]; new_pos[17] = current[20]
    new_pos[18] = current[9]; new_pos[19] = current[10]; new_pos[20] = current[11]
    return new_pos

def front_180(current=[]):
    new_pos = current[:]
    new_pos[0] = current[8]; new_pos[1] = current[7]; new_pos[2] = current[6]
    new_pos[3] = current[5];                          new_pos[5] = current[3]
    new_pos[6] = current[2]; new_pos[7] = current[1]; new_pos[8] = current[0]
    new_pos[9] = current[15]; new_pos[10] = current[16]; new_pos[11] = current[17]
    new_pos[12] = current[18]; new_pos[13] = current[19]; new_pos[14] = current[20]
    new_pos[15] = current[9]; new_pos[16] = current[10]; new_pos[17] = current[11]
    new_pos[18] = current[12]; new_pos[19] = current[13]; new_pos[20] = current[14]
    return new_pos

def back_clock(current):
    new_pos = current[:]
    new_pos[21] = current[27]; new_pos[22] = current[24]; new_pos[23] = current[21]
    new_pos[24] = current[28]; new_pos[25] = current[25]; new_pos[26] = current[22]
    new_pos[27] = current[29]; new_pos[28] = current[26]; new_pos[29] = current[23]
    new_pos[30] = current[39]; new_pos[31] = current[40]; new_pos[32] = current[41]
    new_pos[33] = current[30]; new_pos[34] = current[31]; new_pos[35] = current[32]
    new_pos[36] = current[33]; new_pos[37] = current[34]; new_pos[38] = current[35]
    new_pos[39] = current[36]; new_pos[40] = current[37]; new_pos[41] = current[38]
    return new_pos

def back_anticlock(current):
    new_pos = current[:]
    new_pos[21] = current[23]; new_pos[22] = current[26]; new_pos[23] = current[29]
    new_pos[24] = current[22];                            new_pos[26] = current[28]
    new_pos[27] = current[21]; new_pos[28] = current[24]; new_pos[29] = current[27]
    new_pos[30] = current[33]; new_pos[31] = current[34]; new_pos[32] = current[35]
    new_pos[33] = current[36]; new_pos[34] = current[37]; new_pos[35] = current[38]
    new_pos[36] = current[39]; new_pos[37] = current[40]; new_pos[38] = current[41]
    new_pos[39] = current[30]; new_pos[40] = current[31]; new_pos[41] = current[32]
    return new_pos

def back_180(current):
    new_pos = current[:]
    new_pos[21] = current[29]; new_pos[22] = current[28]; new_pos[23] = current[27]
    new_pos[24] = current[26];                            new_pos[26] = current[24]
    new_pos[27] = current[23]; new_pos[28] = current[22]; new_pos[29] = current[21]
    new_pos[30] = current[36]; new_pos[31] = current[37]; new_pos[32] = current[38]
    new_pos[33] = current[39]; new_pos[34] = current[40]; new_pos[35] = current[41]
    new_pos[36] = current[30]; new_pos[37] = current[31]; new_pos[38] = current[32]
    new_pos[39] = current[33]; new_pos[40] = current[34]; new_pos[41] = current[35]
    return new_pos

def top_row_rot(current):
    new_pos = current[:]
    new_pos[9] = current[32]; new_pos[10] = current[31]; new_pos[11] = current[30]
    new_pos[30] = current[11]; new_pos[31] = current[10]; new_pos[32] = current[9]
    new_pos[0] = current[23]; new_pos[1] = current[22]; new_pos[2] = current[21]
    new_pos[23] = current[0]; new_pos[22] = current[1]; new_pos[21] = current[2]
    new_pos[20] = current[33]; new_pos[12] = current[41]
    new_pos[33] = current[20]; new_pos[41] = current[12]
    return new_pos

def middle_row_rot(current):
    new_pos = current[:]
    new_pos[3] = current[26]; new_pos[4] = current[25]; new_pos[5] = current[24]
    new_pos[26] = current[3]; new_pos[25] = current[4]; new_pos[24] = current[5]
    new_pos[13] = current[40]; new_pos[19] = current[34]
    new_pos[34] = current[19]; new_pos[40] = current[13]
    return  new_pos

def bottom_row_rot(current=[]):
    new_pos = current[:]
    new_pos[6] = current[29]; new_pos[7] = current[28]; new_pos[8] = current[27]
    new_pos[29] = current[6]; new_pos[28] = current[7]; new_pos[27] = current[8]
    new_pos[15] = current[38]; new_pos[16] = current[37]; new_pos[17] = current[36]
    new_pos[38] = current[15]; new_pos[37] = current[16]; new_pos[36] = current[17]
    new_pos[14] = current[39]; new_pos[36] = current[18]
    new_pos[39] = current[14]; new_pos[18] = current[36]
    return new_pos

def left_col_rot(current):
    new_pos = current[:]
    new_pos[18] = current[41]; new_pos[19] = current[40]; new_pos[20] = current[39]
    new_pos[41] = current[18]; new_pos[40] = current[19]; new_pos[39] = current[20]
    new_pos[0] = current[27]; new_pos[3] = current[24]; new_pos[6] = current[21]
    new_pos[27] = current[0]; new_pos[24] = current[3]; new_pos[21] = current[6]
    new_pos[9] = current[38]; new_pos[38] = current[9]
    new_pos[30] = current[17]; new_pos[17] = current[30]
    return new_pos

def middle_col_rot(current):
    new_pos = current[:]
    new_pos[1] = current[28]; new_pos[4] = current[25]; new_pos[7] = current[22]
    new_pos[28] = current[1]; new_pos[25] = current[4]; new_pos[22] = current[7]
    new_pos[10] = current[37]; new_pos[37] = current[10]
    new_pos[31] = current[16]; new_pos[16] = current[31]
    return  new_pos

def right_col_rot(current):
    new_pos = current[:]
    new_pos[12] = current[35]; new_pos[13] = current[34]; new_pos[14] = current[33]
    new_pos[35] = current[12]; new_pos[34] = current[13]; new_pos[33] = current[14]
    new_pos[2] = current[29]; new_pos[5] = current[26]; new_pos[8] = current[23]
    new_pos[29] = current[2]; new_pos[26] = current[5]; new_pos[23] = current[8]
    new_pos[11] = current[32]; new_pos[32] = current[11]
    new_pos[36] = current[15]; new_pos[15] = current[36]
    return new_pos

def compare(source, target):
    if len(source) != len(target) :
        print ("Lengths not equal " + str(len(source)) +","+str(len(target)))
    for i in range(len(source)):
        if source[i] != target[i] and target[i] != '?':
            return False
    return True

#recursive. does the main work.
def find_path(depth, source, target, breadcrumbs):  
    if depth > MAX_DEPTH:
        return False
    # step through all possible moves, if we have the target in any case, stop iterating and return. 
    # If we don't have the target make the move, add to breadcrumbs and recurse. 
    # TODO, also create param with list of lists which is all the aggregated solutions.
    for move in moves:
        #TODO - do we keep these or just use a look up for all loop
        if is_skippable(move, breadcrumbs):
            print ({breadcrumbs+[move]})
            continue
        # if is_redundant(breadcrumbs+[move]):
        #     continue
        fnc = globals()[move]
        res = fnc(source)
        # check to see if this position is in the global list of positions
        # if the position exists in a smaller or equal depth, abandon
        # if the position exists in a deeper depth, kill that position.
        #if position_already_reached(depth,  res):
            #print(f"found an existing position ->{depth}: {res}")
            #break
        #all_positions[depth].append(res)
        if compare(res, target):  
            #print (f"Path ({len(breadcrumbs)+1}) is: {breadcrumbs+[move]}\n\n\n")
            # to persist for later
            print ({breadcrumbs+[move]})
            found = True
            break
        return find_path(depth+1, res, target, breadcrumbs + [move])

def is_skippable(move, breadcrumbs):
    if len(breadcrumbs) < 1:
        return False
    last_underscore_index = breadcrumbs[-1].rfind('_')
    prefix = breadcrumbs[-1][:last_underscore_index]
    if move.startswith(prefix) and prefix != 'middle':
        return True
    return False
# paths with repeated front/back/front are redundant and will be equivalent shorter paths, ultimately
def is_redundant(current_path):
    if len(current_path) < 3:
        return False
    if current_path[-1].startswith('front') and  \
        current_path[-2].startswith('back') and \
        current_path[-3].startswith('front'):
        return True
    
    if  current_path[-1].startswith('back') and \
        current_path[-2].startswith('front') and \
        current_path[-3].startswith('back'):
        return True
    
    if  current_path[-1].startswith('right') and \
        current_path[-2].startswith('left') and \
        current_path[-3].startswith('right'):
        return True
    
    if  current_path[-1].startswith('left') and \
        current_path[-2].startswith('right') and \
        current_path[-3].startswith('left'):
        return True
    
    return False
# an imperfect prune. If there is already a similar position reached with a shorter depth of recursion, 
# then move on.. if there is one with a longer depth.. tough. It got there. It stays. 
def position_already_reached(depth, current):
    for i in range(depth):
        lol = all_positions[i]
        if (efficient_match(current, lol)):
            return True
    return False

# works through a list of list, finding if another list exists
# goes through the list first, and keeps all indices that match the first element then goes through all indices, etc.
def efficient_match(list1, lol):
    return any(list1 == sublst for sublst in lol)


def efficient_match2(list1, lol):
    matching_indices = list(range(len(lol))) # start with all lists matching element 0
    el = 0   #start by looking at element 0
    while len(matching_indices) > 0 and el < len(list1): # while we still have matching lists.
        next_matches = []
        for m in matching_indices:  #what index are we checking..
            if list1[el] == lol[m][el]:
                    next_matches.append(m) # this element matches. That list survives to the next round.        
        el+= 1
        matching_indices = next_matches
    

# lol = [[1,2,3,4],[1,2,3,5],[1,2,3,6],[1,2,4,0], [0,3,4,3],[1,4,4,5]]
# list1 = [9,2,3,9]
# efficient_match(list1, lol)

# helps fill a cube with numbers
def fill(lst, colors):
    for c in colors:
        lst[c] = c

def test1():
    #fill with -1, so those squares don't matter
    source = [-1 for _ in range(42)]
    #fill(source, TOP_ROW)
    fill(source, [13,34]) #front right middle and back right middle
    fill(source, [])
    target = source [:]
    target[13] = source[34]
    target[34] = source[13]
    print(f"targ... is {target}  \nsource. is {source}")
    source = middle_row_rot(source)
    source = left_col_rot(source)
    source = middle_row_rot(source)
    source = right_col_rot(source)
    print(f"after  rot: \ntarg... is {target} - \nsource. is {source}")
    print (compare(source, target))
    #find_path(0,source,target,[])
 
def test2():
    #fill with -1, so those squares don't matter
    source = [-1 for _ in range(42)]
    #fill(source, TOP_ROW)
    fill(source, [13,34,8]) #front right middle and back right middle and lower left corner for constraint
    target = source [:]
    target[13] = source[34]
    target[34] = source[13]
    print(f"targ... is {target}  \nsource. is {source}")
    find_path(0,source,target,[])

def test3():
    #fill with -1, so those squares don't matter
    source = [-1 for _ in range(42)]
    # try to fit corners on second row (from 7 -> 13), so top face needs to stay the same, and middle row apart from corner.
    fill(source, [0,1,2,21,22,23,9,10,11,30,31,32,20,41,3,4,5,24,25,26,19,40,7]) #front right middle and back right middle and lower left corner for constraint
    target = source [:]
    target[5] = source[7]
    target[7] = '?'
    print(f"targ... is {target}  \nsource. is {source}")
    find_path(0,source,target,[])

def test4():
    #fill with -1, so those squares don't matter
    source = list(range(42))
    # swap last remaining 7 and 5
    target = source [:]
    target[5] = source[7]
    target[7] = source[5]
    print(f"targ... is {target}  \nsource. is {source}")
    find_path(0,source,target,[])
def mapToSelf():
    source = list(range(42))
    # swap last remaining 7 and 5
    target = source [:]
    print(f"targ... is {target}  \nsource. is {source}")
    find_path(0,source,target,[])

def test5():
    #fill with -1, so those squares don't matter
    source = list(range(42))
    # swap last remaining 7 and 5
    target = source [:]
    target[7] = source[28]
    target[28] = source[7]
    target[16] = source[37]
    target[37] = source[16]
    print(f"targ... is {target}  \nsource. is {source}")
    find_path(0,source,target,[])

def go():
    print(f"Starting with depth: {MAX_DEPTH}..")
    start_time = time.time()
    mapToSelf()
    #test3()
    elapsed_time = time.time() - start_time
    # Convert the elapsed time to hours and minutes
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    # Print the elapsed time
    print(f"Elapsed time: {hours} hrs {minutes} mins")

go() 


    


