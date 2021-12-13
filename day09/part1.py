def parse_input(input):
    hmap = []
    for l in input.splitlines():
        hmap.append([int(n) for n in l])

    return hmap, len(hmap[0]), len(hmap)


def is_lp(hmap, n, x, y, max_x, max_y):
    adjacent_points = []

    if x + 1 < max_x:
        adjacent_points.append(hmap[y][x + 1])
    if y + 1 < max_y:
        adjacent_points.append(hmap[y + 1][x])
    if x > 0:
        adjacent_points.append(hmap[y][x - 1])
    if y > 0:
        adjacent_points.append(hmap[y - 1][x])

    for p in adjacent_points:
        if n >= p:
            return False

    return True


def compute(input):
    hmap, max_x, max_y = parse_input(input)
    total = 0

    for y, r in enumerate(hmap):
        for x, n in enumerate(r):
            if is_lp(hmap, n, x, y, max_x, max_y):
                total += n + 1

    return total
