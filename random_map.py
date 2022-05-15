from random import randint


def make_arrays(steps, possibilities, only_ones):
    counter = []
    for i in only_ones:
        counter.append(0)
    x = []
    if steps == 1:
        for i in possibilities:
            x.append([i])
        return x
    else:
        for i in possibilities:
            for j in make_arrays(steps - 1, possibilities, only_ones):
                x.append([i] + j)
        return x


def control_arrays(only_ones, map):
    oo_counter = []
    new_arrays = []

    for i in arrays:
        oo_counter = [0 for j in only_ones]
        for index, j in only_ones:
            for k in i:
                if k == j:
                    oo_counter[index] += 1
        if max(oo_counter) > 2:
            new_arrays.append(arrays[i])

    return new_arrays


def every_array(size):
    o = 'o'
    x = 'x'
    p = 'p'
    n = ' '
    b = 'b'
    f = 'f'
    things = [x, n, b]
    only_ones_in_map = [p, f]

    arrays = make_arrays(size, things, only_ones_in_map)

    return arrays

def can_be_finished(mop, pos_p):
    space = []
    space.append(pos_p)
    s_found = False
    f_found = False

    for i in (space):
        i_x = i[1]
        i_y = i[0]
        up_pos = [i_y -1, i_x]
        up = mop[i_y -1][i_x]
        down_pos = [i_y +1, i_x]
        down = mop[i_y +1][i_x]
        left_pos = [i_y, i_x -1]
        left = mop[i_y][i_x -1]
        right_pos = [i_y,i_x +1]
        right = mop[i_y][i_x +1]

        if up == ' ' or up == 'b':
            if up_pos not in space:
                space.append(up_pos)
        elif up == 's':
            s_found = True
        elif up == 'f':
            f_found = True

        if down == ' ' or down == 'b':
            if down_pos not in space:
                space.append(down_pos)

        elif down == 's':
            s_found = True
        elif down == 'f':
            f_found = True

        if left == ' ' or left == 'b':
            if left_pos not in space:
                space.append(left_pos)
        elif left == 's':
            s_found = True
        elif left == 'f':
            f_found = True

        if right == ' ' or right == 'b':
            if right_pos not in space:
                space.append(right_pos)
        elif right == 's':
            s_found = True
        elif right == 'f':
            f_found = True

        if s_found and f_found:
            return True

    return False


def random_map(arrays):
    random_mop = []
    arrays = arrays
    for i in range(12):
        random_mop.append(arrays[randint(0, len(arrays) - 1)])

    p = []
    f = []
    s = []

    while p == f or p == s or s == f:
        p = [randint(0, 11), randint(0, 11)]
        f = [randint(0, 11), randint(0, 11)]
        s = [randint(0, 11), randint(0, 11)]

    random_mop[p[0]][p[1]] = 'p'
    random_mop[f[0]][f[1]] = 'f'
    random_mop[s[0]][s[1]] = 's'

    first_and_last_array = ['h' for i in range(14)]

    mop = []
    mop.append(first_and_last_array[:])

    for index, i in enumerate(random_mop):
        mop.append([])
        mop[index + 1].append('h')

        for j in i:
            mop[index + 1].append(j)
        mop[index + 1].append('h')
    mop.append(first_and_last_array[:])

    if can_be_finished(mop, [p[0] +1, p[1] +1]):
        return mop
    else:
        return random_map(arrays)


arrays = every_array(12)

if __name__ == "__main__":
    while input() == '':
        print(*random_map(arrays), sep='\n')
