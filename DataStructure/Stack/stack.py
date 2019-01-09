
class Stack(object):
    def __init__(self, limit = 10):
        self.stack = []
        self.limit = limit

    # for printing the stack contents
    def __str__(self):
        return ' '.join([str(i) for i in self.stack])

    # for pushing an element on to the stack
    def push(self, data):
        if len(self.stack) >= self.limit:
            print('Stack Overflow')
        else:
            self.stack.append(data)


    # for popping the uppermost element
    def pop(self):
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack.pop()



   def peek(self):
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack[len(self.stack) - 1]
