#!/usr/bin/env python3.10

import argparse
import importlib
import time
from os import path


def input_file(file):
    if path.exists(file):
        return file
    else:
        raise argparse.ArgumentTypeError()


def read_input(file_input):
    with open(file_input) as f:
        return f.read()


def compute(day, part, input):
    day = f'day{"0" if day < 10 else ""}{day}'
    part = f'part{part}'
    file_input = input if input is not None else f'{day}/input.txt'

    try:
        handler = importlib.import_module(f'{day}.{part}')
    except ModuleNotFoundError:
        print(day + ' ' + part + ' is not implemented!')
        return -1
    except Exception as e:
        print(e)
        return -1

    input = read_input(file_input)
    before = time.time()
    answer = handler.compute(input)
    after = time.time()
    elapsed = (after - before) * 1000
    unit = 'ms'
    if elapsed < 1:
        elapsed *= 1000
        unit = 'μs'

    print(f'{day} {part}')
    print(f'  answer  :\t {answer}')
    print(f'  elapsed :\t {int(elapsed)} {unit}')


def main():
    days, part = [], []
    parser = argparse.ArgumentParser(formatter_class=lambda prog: argparse.HelpFormatter(
        prog, max_help_position=25, width=120))
    parser.add_argument('-d', '--day', type=int)
    parser.add_argument('-p', '--part', type=int)
    parser.add_argument('-i', '--input', type=input_file,
                        metavar='FILE', help='external input file')
    parser.add_argument('-a', '--all', action='store_true', help='compute all')
    args = parser.parse_args()

    if args.day is None and args.part is None and args.all is False:
        parser.print_help()
        return -1

    if args.all:
        parts = [1, 2]

        for d in range(25):
            if path.isdir(f'day{"0" if d < 10 else ""}{d}'):
                days.append(d)
    elif args.day:
        days = [args.day]
        if args.part:
            parts = [args.part]
        else:
            parts = [1, 2]

    for day in days:
        for part in parts:
            compute(day, part, args.input)


if __name__ == '__main__':
    exit(main())
