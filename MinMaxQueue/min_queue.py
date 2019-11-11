from collections import deque


class Pair:

    def __init__(self, first, second):
        self.first = first
        self.second = second


class MinQueue(deque):

    def __init__(self):
        super(MinQueue, self).__init__()

    def back(self):
        return self[-1]

    def front(self):
        return self[0]

    def find_min(self):
        return self.front()

    def empty(self):

        return len(self) == 0

    def insert(self, value):

        while not self.empty() and self.back() > value:
            self.pop()

        self.append(value)
