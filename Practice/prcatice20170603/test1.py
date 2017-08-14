#encoding=utf-8

def factorial(number):
    number = int(number)
    if (number == 0) or (number == 1):
        return 1
    else:
        return reduce(lambda x, y: x * y, range(1, number + 1))

if __name__ == '__main__':
    for i in range(4):
        print factorial(i)
