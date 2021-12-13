def parse_input(input):
    timers = input.split(',')
    return list(map(lambda t: int(t), timers))


def calculate_total(timers, days):
    timer_total = dict()
    total = 0

    for i in range(9):
        timer_total[i] = timers.count(i)

    for d in range(days):
        swap = timer_total[0]
        timer_total[0] = timer_total[1]
        timer_total[1] = timer_total[2]
        timer_total[2] = timer_total[3]
        timer_total[3] = timer_total[4]
        timer_total[4] = timer_total[5]
        timer_total[5] = timer_total[6]
        timer_total[6] = timer_total[7] + swap
        timer_total[7] = timer_total[8]
        timer_total[8] = swap

    for key in timer_total:
        total += timer_total[key]

    return total


def compute(input):
    return calculate_total(parse_input(input), 80)
