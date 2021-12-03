def compute(input):
    position = 0
    depth = 0
    aim = 0
    for l in input.splitlines():
        match l.split():
            case['forward', n]:
                position += int(n)
                depth += aim * int(n)
            case['down', n]:
                aim += int(n)
            case['up', n]:
                aim -= int(n)

    return position * depth
