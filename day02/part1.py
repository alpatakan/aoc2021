def compute(input):
    position = 0
    depth = 0
    for l in input.splitlines():
        # for python 3.8 compatibility
        # match l.split():
        #     case['forward', n]:
        #         position += int(n)
        #     case['down', n]:
        #         depth += int(n)
        #     case['up', n]:
        #         depth -= int(n)
        lsplit = l.split()
        direction = lsplit[0]
        amount = lsplit[1]
        if direction == 'forward':
            position += int(amount)
        elif direction == 'down':
            depth += int(amount)
        else:
            depth -= int(amount)

    return position * depth
