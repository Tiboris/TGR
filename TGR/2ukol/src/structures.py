#!/usr/python3
# Inspired from: https://stackabuse.com/stacks-and-queues-in-python/


# A simple class stack that only allows pop and push operations
class Stack:
    def __init__(self):
        self.stack = []

    def print_content(self):
        print("--------------------")
        print("Stack:")
        for index in range(self.size(), 0, -1):
            print(self.stack[index-1])

        print("--------------------")

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)


# And a queue that only has enqueue and dequeue operations
class Queue:
    def __init__(self):
        self.queue = []

    def print_content(self):
        print("--------------------")
        output = ""
        for record in self.queue:
            if output:
                output = output + ", " + record
            else:
                output = "Queue:\n" + record

        print(output)
        print("--------------------")

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)
