

def readFile(path):
    with open(path, "rt") as f:
        return f.read()


def correctOrder(left, right):
    # print(f"Compare {left} vs {right}")
    if isinstance(left, list) and not isinstance(right, list):
        return correctOrder(left, [right])
    elif not isinstance(left, list) and isinstance(right, list):
        return correctOrder([left], right)
    if isinstance(left, list) and isinstance(right, list):
        if left == []:
            return True
        elif left != [] and right == []:
            return False
        first = correctOrder(left[0], right[0])
        if first == False:
            return False
        elif first == True:
            return True
        else:
            return correctOrder(left[1:], right[1:])
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return None
        elif left < right:
            return True
        elif left > right:
            return False
    print("returning None")


def part1():
    # 6138 too high, 6023 too low
    data = readFile('input.txt')
    lines = data.splitlines()
    res = 0
    for i in range(0, len(lines), 3):
        leftList = eval(lines[i])
        rightList = eval(lines[i+1])
        if correctOrder(leftList, rightList):
            res += (i//3) + 1
    return res


def part2():
    data = readFile('input.txt')


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
