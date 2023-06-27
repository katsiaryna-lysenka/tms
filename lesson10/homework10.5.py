class MyStack:
    def __init__(self, collection=None):
        self.stack = [] if collection is None else []
        if collection is not None:
            for item in collection:
                self.stack.append(item)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return not bool(self.stack)
    