#!/usr/bin/env python

import argparse
import importlib


def read_input(day):
    with open(day + '/input.txt') as f:
        return f.read()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--day', type=int, required=True)
    parser.add_argument('-p', '--part', type=int, required=True)
    args = parser.parse_args()

    package = 'day' + str(args.day)
    module = 'part' + str(args.part)

    try:
        handler = importlib.import_module(package + '.' + module)
    except:
        print(package + ' ' + module + ' is not implemented!')
        exit(-1)

    print(handler.compute(read_input(package)))


if __name__ == '__main__':
    exit(main())
