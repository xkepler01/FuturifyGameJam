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
    oo_couter = []
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
    all_maps = []
    only_ones_in_map = [p, f]

    arrays = make_arrays(size, things, only_ones_in_map)


    return arrays


def random_map(arrays):
    random_map = []
    n = []

    for i in range(12):
        random_map.append(arrays[randint(0, len(arrays) - 1)])

    p = []
    f = []

    while p == f:
        p = [randint(0, 11), randint(0, 11)]
        f = [randint(0, 11), randint(0, 11)]

    random_map[p[0]][p[1]] = 'p'
    random_map[f[0]][f[1]] = 'f'

    first_and_last_array = ['h' for i in range(14)]

    mop = []
    mop.append(first_and_last_array[:])

    for index, i in enumerate(random_map):
        mop.append([])
        mop[index + 1].append('h')

        for j in i:
            mop[index + 1].append(j)
        mop[index + 1].append('h')
    mop.append(first_and_last_array[:])

    return mop


arrays = every_array(12)
while input() == '':
   print(*random_map(arrays), sep='\n')