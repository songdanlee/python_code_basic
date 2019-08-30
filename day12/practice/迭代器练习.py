from collections.abc import Iterable, Iterator


# Problem 1: Write an iterator class reverse_iter, that takes a
# list and iterates it from the reverse direction. ::
# 描述 [1,2,3,4] --> 4,3,2,1


class reverse_iter:

    def __init__(self, lists):
        self.lists = lists
        self.lens = len(self.lists)

    def __iter__(self):
        return self

    def __next__(self):
        if self.lens > 0:
            self.lens -= 1
            return self.lists[self.lens]
        else:
            raise StopIteration("超出")


# g = reverse_iter([1, 2, 3, 4])
# print(isinstance(g,Iterable))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# Problem 2: Write a program that takes one or more filenames as arguments and prints
# all the lines which are longer than 40 characters.
def readfiles(filenames):
    for f in filenames:
        for line in open(f,mode='r',encoding="utf-8"):
            yield line.strip()


def grep(lines):
    return (line for line in lines if len(line) >= 40)


def printlines(lines):
    for line in lines:
        print(line)


def main(filenames):
    lines = readfiles(filenames)
    lines = grep(lines)
    printlines(lines)
main(['../log.properties'])
