MAP_LEN = 10


def parse_input(input):
    octomap = [[[0 for z in range(2)] for x in range(MAP_LEN)]
               for y in range(MAP_LEN)]

    for y, l in enumerate(input.splitlines()):
        for x, n in enumerate(l):
            octomap[x][y][0] = int(n)

    return octomap


def get_adjacent_nodes(x, y):
    adjacent_nodes = []
    xr, xl, yb, ya = 0, 0, 0, 0

    if x + 1 < MAP_LEN:
        xr = True
    if y + 1 < MAP_LEN:
        yb = True
    if x > 0:
        xl = True
    if y > 0:
        ya = True

    if xr:
        adjacent_nodes.append([x + 1, y])
        if ya:
            adjacent_nodes.append([x + 1, y - 1])
        if yb:
            adjacent_nodes.append([x + 1, y + 1])
    if xl:
        adjacent_nodes.append([x - 1, y])
        if ya:
            adjacent_nodes.append([x - 1, y - 1])
        if yb:
            adjacent_nodes.append([x - 1, y + 1])
    if ya:
        adjacent_nodes.append([x, y - 1])
    if yb:
        adjacent_nodes.append([x, y + 1])

    return adjacent_nodes


def count_and_reset_flashes(octomap):
    num = 0
    for x in range(MAP_LEN):
        for y in range(MAP_LEN):
            if octomap[x][y][1] > 0:
                num += 1
                octomap[x][y][1] = 0

    return num


def increase_by_one(octomap):
    for x in range(MAP_LEN):
        for y in range(MAP_LEN):
            octomap[x][y][0] += 1


def rec_flash(octomap, x, y):
    if octomap[x][y][0] >= 10 and octomap[x][y][1] != 1:
        octomap[x][y][1] = 1
        octomap[x][y][0] = 0
        for node in get_adjacent_nodes(x, y):
            if octomap[node[0]][node[1]][1] == 0:
                octomap[node[0]][node[1]][0] += 1
                rec_flash(octomap, node[0], node[1])


def flash_and_increase_adjacents(octomap):
    for x in range(MAP_LEN):
        for y in range(MAP_LEN):
            rec_flash(octomap, x, y)


def compute(input):
    octomap = parse_input(input)
    steps = 100
    num_flashes = 0

    for i in range(steps):
        increase_by_one(octomap)
        flash_and_increase_adjacents(octomap)
        num_flashes += count_and_reset_flashes(octomap)

    return num_flashes
