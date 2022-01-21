from .part1 import parse_input, is_lp


def check_adjacent_basins(hmap, bp, basin_points, max_x, max_y):
    x = bp[0]
    y = bp[1]
    if x + 1 < max_x:
        if hmap[y][x + 1] != 9 and [x + 1, y] not in basin_points:
            basin_points.append([x + 1, y])
    if y + 1 < max_y:
        if hmap[y + 1][x] != 9 and [x, y + 1] not in basin_points:
            basin_points.append([x, y + 1])
    if x > 0:
        if hmap[y][x - 1] != 9 and [x - 1, y] not in basin_points:
            basin_points.append([x - 1, y])
    if y > 0:
        if hmap[y - 1][x] != 9 and [x, y - 1] not in basin_points:
            basin_points.append([x, y - 1])


def compute(input):
    hmap, max_x, max_y = parse_input(input)
    low_points, basin_sets, largets_basins = [], [], []

    for y, r in enumerate(hmap):
        for x, n in enumerate(r):
            if is_lp(hmap, n, x, y, max_x, max_y):
                low_points.append([x, y])

    # print(low_points)

    for lp in low_points:
        basin_points = []
        basin_points.append(lp)
        for bp in basin_points:
            checked_points = []
            if lp not in checked_points:
                check_adjacent_basins(hmap, bp, basin_points, max_x, max_y)
                checked_points.append(bp)
        basin_sets.append(basin_points)

    for bp_set in basin_sets:
        if len(largets_basins) < 3:
            largets_basins.append(len(bp_set))
        else:
            if len(bp_set) > min(largets_basins):
                largets_basins.append(len(bp_set))
                largets_basins.remove(min(largets_basins))

    return largets_basins[0] * largets_basins[1] * largets_basins[2]
