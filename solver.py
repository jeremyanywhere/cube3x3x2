
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


cube = list(range(42))

moves = ['front_clock', 'front_anticlock', 'front_180',
         'back_clock', 'back_anticlock','back_180', 
         'top_row_rot','middle_row_rot','bottom_row_rot',
         'left_col_rot','middle_col_rot','right_col_rot']

def front_clock(current):
    new_pos = current[:]
    new_pos[0] = current[6];  new_pos[1] = current[3]; new_pos[2] = current[0]
    new_pos[3] = current[7];  new_pos[4] = current[4]; new_pos[5] = current[1]
    new_pos[6] = current[8];  new_pos[7] = current[5]; new_pos[8] = current[2]
    new_pos[9] = current[18]; new_pos[10] = current[19]; new_pos[11] = current[20]
    new_pos[12] = current[9]; new_pos[13] = current[10]; new_pos[14] = current[11]
    new_pos[15] = current[12]; new_pos[16] = current[13]; new_pos[17] = current[14]
    new_pos[18] = current[15]; new_pos[19] = current[16]; new_pos[20] = current[17]
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

def back_anti_clock(current):
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
    return []

def bottom_row_rot(current=[]):
    return []

def left_col_rot(current=[]):
    return []

def middle_col_rot(current=[]):
    return []

def right_col_rot(current=[]):
    return []

