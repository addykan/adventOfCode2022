

def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def contains(left, right):
    l1, l2 = map(lambda x: int(x), left.split('-'))
    r1, r2 = map(lambda x: int(x), right.split('-'))
    if l1 <= r1 and l2 >= r2:
        return True
    else:
        return False

def part1():
    data = readFile('input.txt')
    res = 0
    for line in data.splitlines():
        left, right = line.split(',')
        if contains(left, right) or contains(right, left):
            res += 1
    print(res)

def intersects(left, right):
    l1, l2 = map(lambda x: int(x), left.split('-'))
    r1, r2 = map(lambda x: int(x), right.split('-'))
    if l1 <= r2 and l2 >= r1:
        return True
    else:
        return False

def part2():
    data = readFile('input.txt')
    res = 0
    for line in data.splitlines():
        left, right = line.split(',')
        if intersects(left, right) or intersects(right, left):
            res += 1
    print(res)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
