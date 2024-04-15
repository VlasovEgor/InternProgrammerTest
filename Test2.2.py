import array
import timeit
import random

class CircularBufferArray:
    def __init__(self, size):
        self.buffer = array.array('i', [0] * size)
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

    buffer_array = CircularBufferArray(1000000)

    time_append_array = timeit.timeit("buffer_array.append(random.randint(0, 10000))", globals=globals(), number=1000000)
    
    time_pop_array = timeit.timeit("buffer_array.pop()", globals=globals(), number=1000000)
    
    print("Time to append 1000000 elements to CircularBufferArray: ", time_append_array)
    print("Time to pop 1000000 elements from CircularBufferArray: ", time_pop_array)