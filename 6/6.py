
def readFile(path):
    with open(path, "rt") as f:
        return f.read()


def part1():
    data = readFile('input.txt')
    last3 = []
    dupeCount = 0
    for i in range(len(data)):
        if len(last3) == 3 and data[i] not in last3 and dupeCount == 0:
            return i
        else:
            if len(last3) == 3:
                firstVal = last3.pop(0)
                if firstVal in last3:
                    dupeCount -= 1
            if data[i] in last3:
                dupeCount += 1
            last3.append(data[i])


def part15(): # bruh
    data = readFile('input.txt')
    for endIndex in range(4, len(data)):
        if len(set(data[endIndex - 4:endIndex])) == 4:
            return endIndex


def part2(): # bruh part 2
    data = readFile('input.txt')
    for endIndex in range(14, len(data)):
        if len(set(data[endIndex - 14:endIndex])) == 14:
            return endIndex


def main():
    print(part15())
    print(part2())


if __name__ == '__main__':
    main()
