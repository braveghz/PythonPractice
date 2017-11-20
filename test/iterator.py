# -*- coding:utf-8 -*-


from collections import Iterator


class Fibs(object):

    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a


def main():
    fibs = Fibs()
    if isinstance(fibs, Iterator):
        print "OOOO Iterator"

    for i in fibs:
        if i > 10:
            break
        print i


if __name__ == '__main__':
    main()
