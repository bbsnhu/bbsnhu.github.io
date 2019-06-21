class PyQueue():

    def __init__(self, list):
        self.__queue = []
        for value in list:
            self.__queue.append(value)

    def enqueue(self, value):
        print("Adding " + str(value))
        self.__queue.append(value)
        print(self.__queue)

    def dequeue(self):
        if len(self.__queue) > 0:
            print("Removing " + str(self.__queue[0]))
            a = self.__queue.pop(0)
            print(self.__queue)
            return a
        else:
            print("Queue is empty.")
            return False
