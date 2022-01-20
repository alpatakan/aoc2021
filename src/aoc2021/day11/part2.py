from .part1 import parse_input, increase_by_one, flash_and_increase_adjacents, count_and_reset_flashes, MAP_LEN


def compute(input):
    octomap = parse_input(input)
    step = 0

    while True:
        step += 1
        increase_by_one(octomap)
        flash_and_increase_adjacents(octomap)
        if count_and_reset_flashes(octomap) == MAP_LEN * MAP_LEN:
            return step
