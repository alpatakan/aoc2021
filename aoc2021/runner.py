#!/usr/bin/env python3

import importlib
import time
import importlib.resources
from os import path


Answer = 'tuple[str, str, str, str]'


def _file_type(file):
    if path.exists(file):
        return file
    else:
        raise argparse.ArgumentTypeError()


def run(day, part, ext_file) -> Answer:
    day = f'day{"0" if day < 10 else ""}{day}'
    part = f'part{part}'

    try:
        handler = importlib.import_module(f'aoc2021.{day}.{part}')
    except ModuleNotFoundError:
        print(f'{day} {part} is not implemented!')
        exit(-1)
    except Exception as e:
        print(e)
        exit(-1)

    input = open(ext_file).read() if ext_file is not None else importlib.resources.read_text(
        f'aoc2021.{day}', 'input.txt')
    before = time.time()
    answer = handler.compute(input)
    after = time.time()
    elapsed = (after - before) * 1000
    unit = 'ms'
    if elapsed < 1:
        elapsed *= 1000
        unit = 'μs'

    return day, part, str(answer), f'{int(elapsed)} {unit}'


def run_day(day) -> 'list[Answer]':
    answers = []
    for part in range(1, 3):
        answers.append(run(day, part, None))

    return answers


def run_all() -> 'list[Answer]':
    answers = []
    for d in range(1, 26):
        day = f'day{"0" if d < 10 else ""}{d}'
        try:
            if importlib.resources.contents(f'aoc2021.{day}') is not None:
                for p in range(1, 3):
                    answers.append(run(d, p, None))
        except:
            continue

    return answers


def main():
    import argparse

    parser = argparse.ArgumentParser(formatter_class=lambda prog: argparse.HelpFormatter(
        prog, max_help_position=25, width=120))
    parser.add_argument('-d', '--day', type=int)
    parser.add_argument('-p', '--part', type=int)
    parser.add_argument('-i', '--input', type=_file_type,
                        metavar='FILE', help='external input file')
    parser.add_argument('-a', '--all', action='store_true', help='compute all')
    args = parser.parse_args()

    answers = []
    if args.all:
        answers = run_all()
    elif args.day:
        if args.part:
            answers.append(run(args.day, args.part, args.input))
        else:
            answers = run_day(args.day)
    else:
        parser.print_help()
        exit(-1)

    for answer in answers:
        print(f'{answer[0]} {answer[1]}')
        print(f'  answer  :\t {answer[2]}')
        print(f'  elapsed :\t {answer[3]}')
