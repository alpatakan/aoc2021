def compute(input):
    position = 0
    depth = 0
    aim = 0
    for l in input.splitlines():
        # for python 3.8 compatibility
        # match l.split():
        #     case['forward', n]:
        #         position += int(n)
        #         depth += aim * int(n)
        #     case['down', n]:
        #         aim += int(n)
        #     case['up', n]:
        #         aim -= int(n)
        lsplit = l.split()
        direction = lsplit[0]
        amount = lsplit[1]
        if direction == 'forward':
            position += int(amount)
            depth += aim * int(amount)
        elif direction == 'down':
            aim += int(amount)
        else:
            aim -= int(amount)

    return position * depth
