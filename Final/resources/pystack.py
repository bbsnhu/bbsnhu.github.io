class PyStack():

    def __init__(self, list):
        self.__stack = []
        for value in list:
            self.__stack.append(value)

    def push(self, value):
        self.__stack.append(value)
        print(self.__stack)

    def pop(self):
        if len(self.__stack) > 0:
            index = len(self.__stack) - 1
            print("Pop Requested..")
            print("Popping", self.__stack[index])
            a = self.__stack.pop(index)
            print(self.__stack)
            return a
        else:
            print("Stack is empty.")
            return False
