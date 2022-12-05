
def readFile(path):
    with open(path, "rt") as f:
        return f.read()


def getIndexDict(line):
    res = dict()
    for i in range(len(line)):
        if line[i].isdigit():
            res[i] = int(line[i])
    return res


def part1():
    data = readFile('input.txt')
    stacks = [[] for _ in range(10)]
    lines = data.splitlines()
    indexDict = getIndexDict(lines[8])
    for line in lines[:8]:
        for i in range(len(line)):
            if i in indexDict and line[i].isalpha():
                stacks[indexDict[i]].append(line[i])
    for stack in stacks:
        stack.reverse()
    # print(stacks)

    for line in lines[10:]:
        count, startStack, endStack = map(lambda x: int(
            x), filter(lambda x: x.isdigit(), line.split()))
        for i in range(count):
            stacks[endStack].append(stacks[startStack].pop())
    # print(stacks)
    for stack in stacks:
        if stack != []:
            print(stack[-1], end='')
    print()


def part2():
    data = readFile('input.txt')
    stacks = [[] for _ in range(10)]
    lines = data.splitlines()
    indexDict = getIndexDict(lines[8])
    for line in lines[:8]:
        for i in range(len(line)):
            if i in indexDict and line[i].isalpha():
                stacks[indexDict[i]].append(line[i])
    for stack in stacks:
        stack.reverse()
    # print(stacks)

    for line in lines[10:]:
        count, startStack, endStack = map(lambda x: int(
            x), filter(lambda x: x.isdigit(), line.split()))
        toRemove = []
        for i in range(count):
            toRemove.append(stacks[startStack].pop())
        toRemove.reverse()
        stacks[endStack].extend(toRemove)
    # print(stacks)
    for stack in stacks:
        if stack != []:
            print(stack[-1], end='')
    print()


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
