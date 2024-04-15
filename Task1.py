
def isEven(value):
    return value % 2 == 0

def isEvenBitwise(value):
    return (value & 1) == 0


if __name__ == '__main__':
    print(isEven(10))
    print(isEven(7))
    
    print(isEvenBitwise(10))
    print(isEven(7))


