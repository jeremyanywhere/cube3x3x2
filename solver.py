
#cube is numbered thus.
#front face from top left to bottom right in three rows
#    0,1,2
#    3,4,5
#    6,7,8
# then along the top from top left.. anti clock wise, around to the left top. 
# 9-20
# the back face, done the same, but in mirror image, or as if you were looking through \
# the front face if it was transparent 
# 21,22,23
# 24,25,26,
# 27,28,29  etc.
# then along the top from the top left (looking through the front face) anti clock
# around to left top
# 30-41
#
from itertools import permutations
import time

cube = list(range(42))
MAX_DEPTH =6
TOP_ROW = [9,10,11,12,30,31,32,33,0,1,2,20,41,21,22,23]
all_positions = [[] for _ in range(MAX_DEPTH+1)]

moves = ['front_anticlock', 'left_col_rot', 'back_anticlock', 'front_180', 'top_row_rot',
         'middle_row_rot', 'right_col_rot', 'back_180', 'front_clock', 'middle_col_rot',
         'bottom_row_rot', 'back_clock']

move_dict = {'front_clock':((0, 6), (1, 3), (2, 0), (3, 7), (4, 4), (5, 1),
                                (6, 8), (7, 5), (8, 2), (9, 18), (10, 19), (11, 20),
                                (12, 9), (13, 10), (14, 11), (15, 12), (16, 13), (17, 14),
                                (18, 15), (19, 16), (20, 17)),
            'front_anticlock':((0, 2), (1, 5), (2, 8), (3, 1), (5, 7),
                                (6, 0), (7, 3), (8, 6), (9, 12), (10, 13),
                                (11, 14), (12, 15), (13, 16), (14, 17), (15, 18),
                                (16, 19), (17, 20), (18, 9), (19, 10), (20, 11)),
            'front_180':( (0, 8), (1, 7), (2, 6), (3, 5), (5, 3),
                                (6, 2), (7, 1), (8, 0), (9, 15), (10, 16),
                                (11, 17), (12, 18), (13, 19), (14, 20), (15, 9),
                                (16, 10), (17, 11), (18, 12), (19, 13), (20, 14)),
            'back_clock':((21, 27), (22, 24), (23, 21),(24, 28), (25, 25), (26, 22),
                                (27, 29), (28, 26), (29, 23),(30, 39), (31, 40), (32, 41),
                                (33, 30), (34, 31), (35, 32),(36, 33), (37, 34), (38, 35),
                                (39, 36), (40, 37), (41, 38)),
            'back_anticlock':((21, 23), (22, 26), (23, 29),
                                (24, 22), (26, 28),(27, 21), (28, 24), (29, 27),
                                (30, 33), (31, 34), (32, 35),(33, 36), (34, 37), (35, 38),
                                (36, 39), (37, 40), (38, 41),(39, 30), (40, 31), (41, 32)),
            'back_180':((21, 29), (22, 28), (23, 27),(24, 26), (26, 24),
                                (27, 23), (28, 22), (29, 21),(30, 36), (31, 37), (32, 38),
                                (33, 39), (34, 40), (35, 41),(36, 30), (37, 31), (38, 32),
                                (39, 33), (40, 34), (41, 35)),
            'top_row_rot':((9, 32), (10, 31), (11, 30),(30, 11), (31, 10), (32, 9),
                                (0, 23), (1, 22), (2, 21),(23, 0), (22, 1), (21, 2),
                                (20, 33), (12, 41),(33, 20), (41, 12)),
            'middle_row_rot':((3, 26), (4, 25), (5, 24),(26, 3), (25, 4), (24, 5),
                                (13, 40), (19, 34),(34, 19), (40, 13)),
            'bottom_row_rot':((6, 29), (7, 28), (8, 27),(29, 6), (28, 7), (27, 8),
                                (15, 38), (16, 37), (17, 36),(38, 15), (37, 16), (36, 17),
                                (14, 39), (36, 18),(39, 14), (18, 36)),
            'left_col_rot':((18, 41), (19, 40), (20, 39),(41, 18), (40, 19), (39, 20),
                                (0, 27), (3, 24), (6, 21),(27, 0), (24, 3), (21, 6),
                                (9, 38), (38, 9),(30, 17), (17, 30)),
            'middle_col_rot':((1, 28), (4, 25), (7, 22),(28, 1), (25, 4), (22, 7),
                                (10, 37), (37, 10),(31, 16), (16, 31)),
            'right_col_rot':((12, 35), (13, 34), (14, 33),(35, 12), (34, 13), (33, 14),
                                (2, 29), (5, 26), (8, 23),(29, 2), (26, 5), (23, 8),
                                (11, 32), (32, 11),
                                (36, 15), (15, 36))}

def apply_move(move, current_pos):
    new_pos = current_pos[:]
    for swap in move_dict[move]:
        new_pos[swap[0]] = current_pos[swap[1]]
    return new_pos
# generate all valid combinations of depth 2 moves (e.g. ['right_col_rot', 'back_180'] 
# or ['front_clock', 'middle_col_rot'])

# idea, maybe do the sanity checking in the task, so that the tasks can throw away 
# bad pairs. That way we can initiate with a simple list of permutation pairs
# either way, parameters should be the first two moves..

def generate_depth_2s():
    perm_list = []
    for pair in permutations(moves, 2):
        perm_list.append(list(pair))
    return perm_list

def is_bad_pairing(pair):
    bad_pairings =['_anticlock','_clock','back','front','top','middle_col','middle_row','right','left','col_rot','row_rot']
    bad_combos = [['back','front'],['bottom','top'],['left','right']]
    for bp in bad_pairings:
        if bp in pair[0] and bp in pair[1]:
            return True
        for bc in bad_combos:
            if (bc[0] in pair[0] and bc[1] in pair[1]):
                return True
            if (bc[1] in pair[0] and bc[0] in pair[1]):
                return True     
    return False
# this would be done outside of this script.. the actual task is "find_path_with_two_move etc."

def start_from_depth2(source, target, depth2s):
    count_ = 1
    for pair in depth2s:
        count_ += 1
        find_path_with_two_move_start(pair, source, target)

def compare(source, target):
    if len(source) != len(target) :
        print ("Lengths not equal " + str(len(source)) +","+str(len(target)))
    for i in range(len(source)):
        if source[i] != target[i] and target[i] != '?':
            return False
    return True

#recursive. does the main work. This needs to be called as a single task. A pair of moves are passed
# with the assumption that they are unique in the problem space and that they have 
def find_path_with_two_move_start(pair_of_moves, source, target):
    if is_bad_pairing(pair_of_moves):
        print(f"bad pairing {pair_of_moves}")
        return False # reject bad moves straight away. 
    # fnc = globals()[pair_of_moves[0]]
    res = apply_move(pair_of_moves[0],source)
    res2 = apply_move(pair_of_moves[1],res)
    #print(f"transformed source {res2}, target {target}")
    find_path(2, res2, target, pair_of_moves)


def find_path(depth, source, target, breadcrumbs):  
    if depth > MAX_DEPTH:
        #print(f"Hello max - {depth}")
        return False
    # step through all possible moves, if we have the target in any case, stop iterating and return. 
    # If we don't have the target make the move, add to breadcrumbs and recurse. 
    # TODO, also create param with list of lists which is all the aggregated solutions.
    for move in move_dict.keys():
        if is_skippable(move, breadcrumbs):
            continue
        if is_redundant(breadcrumbs+[move]):
            continue
        res = apply_move(move, source)
        if compare(res, target):  
            print (f"{len(breadcrumbs)+1} {breadcrumbs + [move]}")
            found = True
        # print(f" breadcrumbs are.. {breadcrumbs} ")
        result  =  find_path(depth+1, res, target, breadcrumbs + [move])

# if we have just moved a face (front or back) then moving that face again is pointless
def is_skippable(move, breadcrumbs):
    if len(breadcrumbs) < 1:
        return False
    last_underscore_index = breadcrumbs[-1].rfind('_')
    prefix = breadcrumbs[-1][:last_underscore_index]
    # don't do two moves the same
    if breadcrumbs[-1] == move:
        return True
    # don't do two consecutive front moves or back moves
    if ("front" in prefix or "back" in prefix) and move.startswith(prefix):
        return True
    return False
# paths with repeated front/back/front are redundant and will be equivalent to shorter paths, ultimately
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

# helps fill a cube with numbers
def fill(lst, squares):
    for c in squares:
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
    source = apply_move('middle_row_rot',source)
    source = apply_move('left_col_rot',source)
    source = apply_move('middle_row_rot',source)
    source = apply_move('right_col_rot',source)
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
    start_from_depth2(MAX_DEPTH, source, target, generate_depth_2s())

def fit_edge_bottom_to_side():
    #fill with -1, so those squares don't matter
    source = [-1 for _ in range(42)]
    # try to fit edge on second row (from 7 -> 13), so top face needs to stay the same, and middle row apart from corner.
    fill(source, [0,1,2,21,22,23,9,10,11,30,31,32,20,41,3,4,5,24,25,26,19,40,7]) #front right middle and back right middle and lower left corner for constraint
    target = source [:]
    target[5] = source[7]
    target[7] = '?'
    print(f"targ... is {target}  \nsource. is {source}")
    start_from_depth2(source, target, generate_depth_2s())
    #find_path(0,source,target,[])

def swap_last_7_and_5():
    source = list(range(42))
    # swap last remaining 7 and 5
    target = source [:]
    target[5] = source[7]
    target[7] = source[5]
    print(f"targ is... is {target}  \nsource is.. {source}")
    start_from_depth2(source, target, generate_depth_2s())
    #find_path(0,source,target,[])

def mapToSelf():
    source = list(range(42))
    target = source [:]
    print(f"targ... is {target}  \nsource. is {source}")
    find_path(0,source,target,[])

def test5():
    source = list(range(42))
    # swap last remaining 7 and 5
    target = source [:]
    target[7] = source[28]
    target[28] = source[7]
    target[16] = source[37]
    target[37] = source[16]
    print(f"targ... is {target}  \nsource. is {source}")
    find_path(0,source,target,[])

def go(runner):
    fncr = globals()[runner]
    print(f"Running method: {runner}()")
    print(f"Starting with depth: {MAX_DEPTH}..")
    start_time = time.time()
    #mapToSelf()
    fncr()
    elapsed_time = time.time() - start_time
    # Convert the elapsed time to hours and minutes
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)
    # Print the elapsed time
    print(f"Elapsed time: {hours} hrs {minutes} mins {seconds} seconds")
# gd2 = generate_depth_2s()
# print(f"generate_depth_2s (found {len(gd2)}) - {gd2}")
# do_depth2_transforms(cube,gd2)
go('fit_edge_bottom_to_side') 


    


