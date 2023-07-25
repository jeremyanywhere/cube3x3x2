cube = (0..41).toList()
MAX_DEPTH = 7
TOP_ROW = [9, 10, 11, 12, 30, 31, 32, 33, 0, 1, 2, 20, 41, 21, 22, 23]
all_positions = (0..MAX_DEPTH).collect { [] }

moves = [
  'front_anticlock', 'left_col_rot', 'back_anticlock', 'front_180', 'top_row_rot',
  'middle_row_rot', 'right_col_rot', 'back_180', 'front_clock', 'middle_col_rot',
  'bottom_row_rot', 'back_clock'
]

def front_clock(current) {
  def new_pos = current.clone()
  new_pos[0] = current[6];  new_pos[1] = current[3]; new_pos[2] = current[0]
  new_pos[3] = current[7];  new_pos[4] = current[4]; new_pos[5] = current[1]
  new_pos[6] = current[8];  new_pos[7] = current[5]; new_pos[8] = current[2]
  new_pos[9] = current[18]; new_pos[10] = current[19]; new_pos[11] = current[20]
  new_pos[12] = current[9]; new_pos[13] = current[10]; new_pos[14] = current[11]
  new_pos[15] = current[12]; new_pos[16] = current[13]; new_pos[17] = current[14]
  new_pos[18] = current[15]; new_pos[19] = current[16]; new_pos[20] = current[17]
  new_pos
}

def front_anticlock(current) {
  def new_pos = current.clone()
  new_pos[0] = current[2]; new_pos[1] = current[5]; new_pos[2] = current[8]
  new_pos[3] = current[1];                          new_pos[5] = current[7]
  new_pos[6] = current[0]; new_pos[7] = current[3]; new_pos[8] = current[6]
  new_pos[9] = current[12]; new_pos[10] = current[13]; new_pos[11] = current[14]
  new_pos[12] = current[15]; new_pos[13] = current[16]; new_pos[14] = current[17]
  new_pos[15] = current[18]; new_pos[16] = current[19]; new_pos[17] = current[20]
  new_pos[18] = current[9]; new_pos[19] = current[10]; new_pos[20] = current[11]
  new_pos
}

def front_180(current) {
  def new_pos = current.clone()
  new_pos[0] = current[8]; new_pos[1] = current[7]; new_pos[2] = current[6]
  new_pos[3] = current[5];                          new_pos[5] = current[3]
  new_pos[6] = current[2]; new_pos[7] = current[1]; new_pos[8] = current[0]
  new_pos[9] = current[15]; new_pos[10] = current[16]; new_pos[11] = current[17]
  new_pos[12] = current[18]; new_pos[13] = current[19]; new_pos[14] = current[20]
  new_pos[15] = current[9]; new_pos[16] = current[10]; new_pos[17] = current[11]
  new_pos[18] = current[12]; new_pos[19] = current[13]; new_pos[20] = current[14]
  new_pos
}

def back_clock(current) {
  def new_pos = current.clone()
  new_pos[21] = current[27]; new_pos[22] = current[24]; new_pos[23] = current[21]
  new_pos[24] = current[28]; new_pos[25] = current[25]; new_pos[26] = current[22]
  new_pos[27] = current[29]; new_pos[28] = current[26]; new_pos[29] = current[23]
  new_pos[30] = current[39]; new_pos[31] = current[40]; new_pos[32] = current[41]
  new_pos[33] = current[30]; new_pos[34] = current[31]; new_pos[35] = current[32]
  new_pos[36] = current[33]; new_pos[37] = current[34]; new_pos[38] = current[35]
  new_pos[39] = current[36]; new_pos[40] = current[37]; new_pos[41] = current[38]
  new_pos
}

def back_anticlock(current) {
  def new_pos = current.clone()
  new_pos[21] = current[23]; new_pos[22] = current[26]; new_pos[23] = current[29]
  new_pos[24] = current[22];                            new_pos[26] = current[28]
  new_pos[27] = current[21]; new_pos[28] = current[24]; new_pos[29] = current[27]
  new_pos[30] = current[33]; new_pos[31] = current[34]; new_pos[32] = current[35]
  new_pos[33] = current[36]; new_pos[34] = current[37]; new_pos[35] = current[38]
  new_pos[36] = current[39]; new_pos[37] = current[40]; new_pos[38] = current[41]
  new_pos[39] = current[30]; new_pos[40] = current[31]; new_pos[41] = current[32]
  new_pos
}

List<Integer> back_180(List<Integer> current) {
    List<Integer> new_pos = current.clone();
    new_pos[21] = current[29]; new_pos[22] = current[28]; new_pos[23] = current[27];
    new_pos[24] = current[26];                            new_pos[26] = current[24];
    new_pos[27] = current[23]; new_pos[28] = current[22]; new_pos[29] = current[21];
    new_pos[30] = current[36]; new_pos[31] = current[37]; new_pos[32] = current[38];
    new_pos[33] = current[39]; new_pos[34] = current[40]; new_pos[35] = current[41];
    new_pos[36] = current[30]; new_pos[37] = current[31]; new_pos[38] = current[32];
    new_pos[39] = current[33]; new_pos[40] = current[34]; new_pos[41] = current[35];
    return new_pos;
}

List<Integer> top_row_rot(List<Integer> current) {
    List<Integer> new_pos = current.clone();
    new_pos[9] = current[32]; new_pos[10] = current[31]; new_pos[11] = current[30];
    new_pos[30] = current[11]; new_pos[31] = current[10]; new_pos[32] = current[9];
    new_pos[0] = current[23]; new_pos[1] = current[22]; new_pos[2] = current[21];
    new_pos[23] = current[0]; new_pos[22] = current[1]; new_pos[21] = current[2];
    new_pos[20] = current[33]; new_pos[12] = current[41];
    new_pos[33] = current[20]; new_pos[41] = current[12];
    return new_pos;
}

List<Integer> middle_row_rot(List<Integer> current) {
    List<Integer> new_pos = current.clone();
    new_pos[3] = current[26]; new_pos[4] = current[25]; new_pos[5] = current[24];
    new_pos[26] = current[3]; new_pos[25] = current[4]; new_pos[24] = current[5];
    new_pos[13] = current[40]; new_pos[19] = current[34];
    new_pos[34] = current[19]; new_pos[40] = current[13];
    return new_pos;
}

List<Integer> bottom_row_rot(List<Integer> current) {
    List<Integer> new_pos = current.clone();
    new_pos[6] = current[29]; new_pos[7] = current[28]; new_pos[8] = current[27];
    new_pos[29] = current[6]; new_pos[28] = current[7]; new_pos[27] = current[8];
    new_pos[15] = current[38]; new_pos[16] = current[37]; new_pos[17] = current[36];
    new_pos[38] = current[15]; new_pos[37] = current[16]; new_pos[36] = current[17];
    new_pos[14] = current[39]; new_pos[36] = current[18];
    new_pos[39] = current[14]; new_pos[18] = current[36];
    return new_pos;
}

List<Integer> left_col_rot(List<Integer> current) {
    List<Integer> new_pos = current.clone();
    new_pos[18] = current[41]; new_pos[19] = current[40]; new_pos[20] = current[39];
    new_pos[41] = current[18]; new_pos[40] = current[19]; new_pos[39] = current[20];
    new_pos[0] = current[27]; new_pos[3] = current[24]; new_pos[6] = current[21];
    new_pos[27] = current[0]; new_pos[24] = current[3]; new_pos[21] = current[6];
    new_pos[9] = current[38]; new_pos[38] = current[9];
    new_pos[30] = current[17]; new_pos[17] = current[30];
    return new_pos;
}

List<Integer> middle_col_rot(List<Integer> current) {
    List<Integer> new_pos = current.clone();
    new_pos[1] = current[28]; new_pos[4] = current[25]; new_pos[7] = current[22];
    new_pos[28] = current[1]; new_pos[25] = current[4]; new_pos[22] = current[7];
    new_pos[10] = current[37]; new_pos[37] = current[10];
    new_pos[31] = current[16]; new_pos[16] = current[31];
    return new_pos;
}

List<Integer> right_col_rot(List<Integer> current) {
    List<Integer> new_pos = current.clone();
    new_pos[12] = current[35]; new_pos[13] = current[34]; new_pos[14] = current[33];
    new_pos[35] = current[12]; new_pos[34] = current[13]; new_pos[33] = current[14];
    new_pos[2] = current[29]; new_pos[5] = current[26]; new_pos[8] = current[23];
    new_pos[29] = current[2]; new_pos[26] = current[5]; new_pos[23] = current[8];
    new_pos[11] = current[32]; new_pos[32] = current[11];
    new_pos[36] = current[15]; new_pos[15] = current[36];
    return new_pos;
}

boolean compare(List<Integer> source, List<Integer> target) {
    if (source.size() != target.size()) {
        println("Lengths not equal " + source.size() + "," + target.size());
    }
    for (int i = 0; i < source.size(); i++) {
        if (source[i] != target[i] && target[i] != '?') {
            return false;
        }
    }
    return true;
}

boolean find_path(int depth, List<Integer> source, List<Integer> target, List<String> breadcrumbs) {
    if (depth > MAX_DEPTH) {
        return false;
    }
    for (String move : moves) {
        if (is_skippable(move, breadcrumbs)) {
            println(breadcrumbs + [move]);
            continue;
        }
        Closure fnc = this.&"$move";
        List<Integer> res = fnc.call(source);
        if (compare(res, target)) {
            println(breadcrumbs + [move]);
            return true;
        }
        if (find_path(depth + 1, res, target, breadcrumbs + [move])) {
            return true;
        }
    }
    return false;
}
boolean is_skippable(String move, List<String> breadcrumbs) {
    if (breadcrumbs.size() < 1) {
        return false;
    }
    int last_underscore_index = breadcrumbs[-1].lastIndexOf('_');
    String prefix = breadcrumbs[-1].substring(0, last_underscore_index);
    if (move.startsWith(prefix) && prefix != 'middle') {
        return true;
    }
    return false;
}

boolean is_redundant(List<String> current_path) {
    if (current_path.size() < 3) {
        return false;
    }
    if (current_path[-1].startsWith('front') &&
        current_path[-2].startsWith('back') &&
        current_path[-3].startsWith('front')) {
        return true;
    }

    if (current_path[-1].startsWith('back') &&
        current_path[-2].startsWith('front') &&
        current_path[-3].startsWith('back')) {
        return true;
    }

    if (current_path[-1].startsWith('right') &&
        current_path[-2].startsWith('left') &&
        current_path[-3].startsWith('right')) {
        return true;
    }

    if (current_path[-1].startsWith('left') &&
        current_path[-2].startsWith('right') &&
        current_path[-3].startsWith('left')) {
        return true;
    }

    return false;
}

boolean position_already_reached(int depth, List<Integer> current) {
    for (int i = 0; i < depth; i++) {
        List<Integer> lol = all_positions[i];
        if (efficient_match(current, lol)) {
            return true;
        }
    }
    return false;
}

boolean efficient_match(List<Integer> list1, List<List<Integer>> lol) {
    return lol.any { sublst -> list1 == sublst };
}

void efficient_match2(List<Integer> list1, List<List<Integer>> lol) {
    List<Integer> matching_indices = (0..(lol.size() - 1)).toList();
    int el = 0;
    while (matching_indices.size() > 0 && el < list1.size()) {
        List<Integer> next_matches = [];
        for (int m : matching_indices) {
            if (list1[el] == lol[m][el]) {
                next_matches.add(m);
            }
        }
        el++;
        matching_indices = next_matches;
    }
}

void fill(List<Integer> lst, List<Integer> colors) {
    for (int c : colors) {
        lst[c] = c;
    }
}

void test1() {
    // fill with -1, so those squares don't matter
    List<Integer> source = [-1] * 42
    fill(source, [13, 34]) // front right middle and back right middle
    fill(source, [])
    List<Integer> target = source.clone()
    target[13] = source[34]
    target[34] = source[13]
    println("targ... is ${target}\nsource. is ${source}")
    source = middle_row_rot(source)
    println("after  middle_row_rot: source. is ${source}")
    source = left_col_rot(source)
    println("after left_col_rot: source. is ${source}")
    source = middle_row_rot(source)
    println("after  middle_row_rot: source. is ${source}")
    //source = right_col_rot(source)
    //println("after right_col_rot:\ntarg... is ${target} -\nsource. is ${source}")
    println(compare(source, target))
    // find_path(0, source, target, [])
}

void test2() {
    // fill with -1, so those squares don't matter
    List<Integer> source = [-1] * 42
    fill(source, [13, 34, 8]) // front right middle and back right middle and lower left corner for constraint
    List<Integer> target = source.clone()
    target[13] = source[34]
    target[34] = source[13]
    println("targ... is ${target}\nsource. is ${source}")
    find_path(0, source, target, [])
}

void test3() {
    // fill with -1, so those squares don't matter
    List<Integer> source = [-1] * 42
    // try to fit corners on second row (from 7 -> 13), so top face needs to stay the same, and middle row apart from corner.
    fill(source, [0, 1, 2, 21, 22, 23, 9, 10, 11, 30, 31, 32, 20, 41, 3, 4, 5, 24, 25, 26, 19, 40, 7]) // front right middle and back right middle and lower left corner for constraint
    List<Integer> target = source.clone()
    target[5] = source[7]
    target[7] = '?'
    println("targ... is ${target}\nsource. is ${source}")
    find_path(0, source, target, [])
}

void test4() {
    // fill with -1, so those squares don't matter
    List<Integer> source = (0..41).toList()
    // swap last remaining 7 and 5
    List<Integer> target = source.clone()
    target[5] = source[7]
    target[7] = source[5]
    println("targ... is ${target}\nsource. is ${source}")
    find_path(0, source, target, [])
}

void mapToSelf() {
    List<Integer> source = (0..41).toList()
    // swap last remaining 7 and 5
    List<Integer> target = source.clone()
    println("targ... is ${target}\nsource. is ${source}")
    find_path(0, source, target, [])
}

void test5() {
    // fill with -1, so those squares don't matter
    List<Integer> source = (0..41).toList()
    // swap last remaining 7 and 5
    List<Integer> target = source.clone()
    target[7] = source[28]
    target[28] = source[7]
    target[16] = source[37]
    target[37] = source[16]
    println("targ... is ${target}\nsource. is ${source}")
    find_path(0, source, target, [])
}

void go() {
    println("Starting with depth: ${MAX_DEPTH}..")
    long start_time = System.currentTimeMillis()
    //mapToSelf()
    test2()
    long elapsed_time = System.currentTimeMillis() - start_time
    // Convert the elapsed time to hours and minutes
    int hours = (int) (elapsed_time / 3600000)
    int minutes = (int) ((elapsed_time % 3600000) / 60000)
    // Print the elapsed time
    println("Elapsed time: ${hours} hrs ${minutes} mins")
}

go()



