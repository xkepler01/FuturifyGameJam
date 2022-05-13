# porovnavani s predchozimi
# cesta k cili
# od nejvice zdi
# jen 1x p a 1x o


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


def sort_arrays(maps):  # funguje?
    f_maps = []
    p_maps = []
    p_f_maps = []
    _maps = []

    for i in maps:
        counter_p_f = [0, 0]
        for j in i:
            for k in j:
                if k == 'p':
                    counter_p_f[0] += 1
                elif k == 'f':
                    counter_p_f[1] += 1
            if counter_p_f[0] == 1 and counter_p_f[1] == 1:
                p_f_maps.append(i)
            elif counter_p_f[0] == 1 and counter_p_f[1] == 0:
                p_maps.append(i)
            elif counter_p_f[0] == 0 and counter_p_f[1] == 1:
                f_maps.append(i)
            elif counter_p_f[0] == 0 and counter_p_f[1] == 0:
                _maps.append(i)

        return [p_maps, f_maps, p_f_maps, _maps]

    counter = 0
    for index, i in enumerate(x):
        p = 0
        o = 0
        for j in i:
            for k in j:
                if k == 'p':
                    p += 1
                elif k == 'f':
                    f += 1
        if not (p == 1 and o == 1):
            x.pop(index)  # - counter)
            counter += 1

    return x


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
    # almost_map = make_arrays(size, arrays, []) # !

    # first_and_last_array = [x for i in range(size + 2)]

    # for i in almost_map:
    # mop = []
    # mop.append(first_and_last_array[:])

    # for index,j in enumerate(i):
    # mop.append([])
    # mop[index + 1].append(x)

    # for k in j:
    # mop[index + 1].append(k)
    # mop[index + 1].append(x)
    # mop.append(first_and_last_array[:])
    # all_maps.append(map)

    return arrays  # all_maps


def random_map(arrays):
    # arrays = every_array(12)
    # sorted_arrays = sort_arrays(small_maps) # [p_maps, f_maps, p_f_maps, _maps]
    # arrays = []
    random_map = []
    n = []

    # arrays.append(sorted_maps[0][randint(0, len(sorted_arrays[0]) -1)])
    # arrays.append(sorted_maps[1][randint(0, len(sorted_arrays[1]) -1)])
    for i in range(12):
        random_map.append(arrays[randint(0, len(arrays) - 1)])

    # for i in random_map:
    #    for j in i:
    #        if j == ' ':
    #            n.append([i, j])

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
# print(*every_map(12), sep='\n')
# for map in every_map(3):
# print(*map, sep='\n')
# print('\n')
