def parse_input(input):
    nav = [l for l in input.splitlines()]
    nav_parsed, stack = [], []
    opening_chars = ['(', '[', '{', '<']
    closing_chars = [')', ']', '}', '>']

    for i, l in enumerate(nav):
        for j, c in enumerate(l):
            if c in opening_chars:
                stack.append(c)
            elif c in closing_chars:
                if len(stack) < 1:
                    nav_parsed.append({'result': 'wtf', 'expected': None,
                                      'found': c, 'stack': stack.copy(), 'raw': [e for e in l]})
                    stack.clear()
                    break
                pc = stack.pop()
                if pc != opening_chars[closing_chars.index(c)]:
                    nav_parsed.append({'result': 'mismatch', 'expected': pc,
                                      'found': c, 'stack': stack.copy(), 'raw': [e for e in l]})
                    stack.clear()
                    break
            else:
                stack.clear()
                nav_parsed.append({'result': 'invalid', 'expected': None,
                                  'found': c, 'stack': stack.copy(), 'raw': [e for e in l]})
                break
            if j == len(l) - 1:
                nav_parsed.append({'result': 'incomplete', 'expected': None,
                                  'found': None, 'stack': stack.copy(), 'raw': [e for e in l]})
                stack.clear()
                break
    # print(*nav_parsed, sep='\n')
    return nav_parsed


def compute(input):
    nav_parsed = parse_input(input)
    score_points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    total_score = 0

    for elem in nav_parsed:
        if elem['result'] == 'mismatch':
            total_score += score_points[elem['found']]

    return total_score
