def compute(input):
    position = 0
    depth = 0
    for l in input.splitlines():
        match l.split():
            case['forward', n]:
                position += int(n)
            case['down', n]:
                depth += int(n)
            case['up', n]:
                depth -= int(n)

    return position * depth
