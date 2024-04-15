import random


def generate_random_array(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]

class TimSort:
    def __init__(self, arr):
        self.arr = arr

    def insertion_sort(self, left, right):
        for i in range(left + 1, right + 1):
            key = self.arr[i]
            j = i - 1
            while j >= left and self.arr[j] > key:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key

    def merge(self, left, mid, right):
        left_len = mid - left + 1
        right_len = right - mid

        left_arr = [0] * left_len
        right_arr = [0] * right_len

        for i in range(left_len):
            left_arr[i] = self.arr[left + i]
        for j in range(right_len):
            right_arr[j] = self.arr[mid + 1 + j]

        i = 0
        j = 0
        k = left

        while i < left_len and j < right_len:
            if left_arr[i] <= right_arr[j]:
                self.arr[k] = left_arr[i]
                i += 1
            else:
                self.arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < left_len:
            self.arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < right_len:
            self.arr[k] = right_arr[j]
            j += 1
            k += 1

    def timsort_impl(self, left, right, min_run=32):
        if right <= left:
            return

        if right - left < min_run:
            self.insertion_sort(left, right)
            return

        mid = (left + right) // 2
        self.timsort_impl(left, mid)
        self.timsort_impl(mid + 1, right)

        if self.arr[mid] > self.arr[mid + 1]:
            self.merge(left, mid, right)

    def sort(self):
        self.timsort_impl(0, len(self.arr) - 1)

    def __str__(self):
        return f"TimSort: {self.arr}"

    def print_initial(self):
        print("Initial array:", self.arr)

    def print_sorted(self, output="console"):
        if output == "console":
            print(self.arr)
        elif isinstance(output, str):
            with open(output, "w") as file:
                file.write(str(self.arr))
        else:
            raise ValueError("Invalid output value. Use 'console' or provide a file name as a string.")

if __name__ == '__main__':

    arr = generate_random_array(1000, 1, 100)

    ts = TimSort(arr)
    ts.print_initial()
    ts.sort()

    ts.print_sorted("console")
    ts.print_sorted("sorted_array.txt")