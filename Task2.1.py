import timeit
import random

class CircularBufferList:
    def __init__(self, size):
        self.buffer = [None] * size
        self.head = 0
        self.tail = 0
        self.size = size
        self.count = 0

    def append(self, item):
        if self.count < self.size:
            self.buffer[self.tail] = item
            self.tail = (self.tail + 1) % self.size
            self.count += 1
        else:
            print("Buffer is full")

    def pop(self):
        if self.count > 0:
            item = self.buffer[self.head]
            self.head = (self.head + 1) % self.size
            self.count -= 1
            return item
        else:
            print("Buffer is empty")

if __name__ == '__main__':

   buffer_list = CircularBufferList(1000000)
   
   time_append_list = timeit.timeit("buffer_list.append(random.randint(0, 10000))", globals=globals(), number=1000000)
   
   time_pop_list = timeit.timeit("buffer_list.pop()", globals=globals(), number=1000000)
   
   print("Time to append 1000000 elements to CircularBufferList: ", time_append_list)
   print("Time to pop 1000000 elements from CircularBufferList: ", time_pop_list)

