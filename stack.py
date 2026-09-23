class stack:
    def __init__(self):
        self._a = []
        self._top = None

    def push(self, data):
        if self._top is None:
            ar = [0]
            self._top = 0
            ar[self._top] = data
            self._a = ar
        else:
            ar = [0 for i in range(self._top + 2)]

            for i in range(self._top + 1):
                ar[i] = self._a[i]

            ar[-1] = data
            self._top += 1
            self._a = ar

    def peek(self):
        if self._top is None:
            return "we dont have any elements"

        return self._a[self._top]

    def apnd(self, data):
        ar = [0 for i in range(self._top + 2)]

        for i in range(self._top + 1):
            ar[i] = self._a[i]

        ar[-1] = data
        self._top += 1
        self._a = ar

    def pop(self):
        if self._top is None:
            return "we dont have any elements"

        data = self._a[self._top]
        self._top -= 1

        if self._top == -1:
            self._a = []
            self._top = None
        else:
            ar = [0 for i in range(self._top + 1)]

            for i in range(self._top + 1):
                ar[i] = self._a[i]

            self._a = ar

        return data


stack = stack()

stack.push(10)
stack.push(20)

print(stack.peek())

stack.apnd(30)
print(stack.peek())

removed = stack.pop()
print("removed:", removed)

print(stack.peek())