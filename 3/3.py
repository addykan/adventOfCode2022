
import string


def readFile(path):
    with open(path, "rt") as f:
        return f.read()


def getPriorities():
    s = '0' + string.ascii_lowercase + string.ascii_uppercase
    res = dict()
    for i in range(len(s)):
        res[s[i]] = i
    return res


def part1():
    data = readFile('input.txt')
    priorities = getPriorities()
    res = 0
    for line in data.splitlines():
        left = line[:len(line) // 2]
        right = line[len(line) // 2:]
        leftSet = set(left)
        rightSet = set(right)
        intersection = leftSet & rightSet
        for c in intersection:
            res += priorities[c]
    print(res)


def part2():
    data = readFile('input.txt')
    lines = data.splitlines()
    priorities = getPriorities()
    res = 0
    for i in range(0, len(lines), 3):
        line1, line2, line3 = lines[i], lines[i+1], lines[i+2]
        intersection = set(line1) & set(line2) & set(line3)
        for c in intersection:
            res += priorities[c]
    print(res)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
