#!/usr/bin/python

import decimal
import sys


def smart_sum(s):
    num_chars = filter(lambda c: c in "\t\n -.0123456789", s)
    return str(sum(map(decimal.Decimal, num_chars.split())))


def main():
    if sys.stdin.isatty():
        print "STDIN is emtpy"
        return

    print smart_sum(str(sys.stdin.read()))


if __name__ == "__main__":
    main()