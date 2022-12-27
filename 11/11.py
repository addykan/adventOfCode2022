

def readFile(path):
    with open(path, "rt") as f:
        return f.read()


class Monkey:
    modAll = 2 * 17 * 19 * 3 * 5 * 13 * 7 * 11

    def __init__(self, startingItems, operation, test, trueCase, falseCase):
        self.items = startingItems
        self.operation = operation
        self.test = test
        self.trueCase = trueCase
        self.falseCase = falseCase
        self.inspectionCount = 0

    def takeTurn(self, isPart1):
        while self.items != []:
            self.inspectionCount += 1
            worry = self.items.pop(0)
            worry = self.operation(worry)
            if isPart1:
                worry //= 3
            else:
                worry %= Monkey.modAll
            if self.test(worry):
                self.trueCase(worry)
            else:
                self.falseCase(worry)


def constructMonkeys(data):
    modAll = 2 * 17 * 19 * 3 * 5 * 13 * 7 * 11
    # hardcoded monkeys because string parsing was a pain
    monkeys = [
        Monkey([83, 62, 93], lambda x: x * 17, lambda x: (x % 2) == 0,
               lambda x: monkeys[1].items.append(x), lambda x: monkeys[6].items.append(x)),
        Monkey([90, 55], lambda x: x + 1, lambda x: (x % 17) == 0,
               lambda x: monkeys[6].items.append(x), lambda x: monkeys[3].items.append(x)),
        Monkey([91, 78, 80, 97, 79, 88], lambda x: x + 3, lambda x: (x % 19) == 0,
               lambda x: monkeys[7].items.append(x), lambda x: monkeys[5].items.append(x)),
        Monkey([64, 80, 83, 89, 59], lambda x: x + 5, lambda x: (x % 3) == 0,
               lambda x: monkeys[7].items.append(x), lambda x: monkeys[2].items.append(x)),
        Monkey([98, 92, 99, 51], lambda x: x * x, lambda x: (x % 5) == 0,
               lambda x: monkeys[0].items.append(x), lambda x: monkeys[1].items.append(x)),
        Monkey([68, 57, 95, 85, 98, 75, 98, 75], lambda x: x + 2, lambda x: (x % 13) ==
               0, lambda x: monkeys[4].items.append(x), lambda x: monkeys[0].items.append(x)),
        Monkey([74], lambda x: x + 4, lambda x: (x % 7) == 0,
               lambda x: monkeys[3].items.append(x), lambda x: monkeys[2].items.append(x)),
        Monkey([68, 64, 60, 68, 87, 80, 82], lambda x: x * 19, lambda x: (x % 11) == 0,
               lambda x: monkeys[4].items.append(x), lambda x: monkeys[5].items.append(x))
    ]
    return monkeys


def part1():
    data = readFile('input.txt')
    monkeys = constructMonkeys(data)
    for i in range(20):
        for monkey in monkeys:
            monkey.takeTurn(True)
    maxCount = secondMax = -1
    for monkey in monkeys:
        if monkey.inspectionCount > maxCount:
            secondMax = maxCount
            maxCount = monkey.inspectionCount
        elif monkey.inspectionCount > secondMax:
            secondMax = maxCount
    return maxCount * secondMax


def part2():
    data = readFile('input.txt')
    monkeys = constructMonkeys(data)
    for i in range(10000):
        print(f"round {i}")
        for monkey in monkeys:
            monkey.takeTurn(False)
    maxCount = secondMax = -1
    for monkey in monkeys:
        if monkey.inspectionCount > maxCount:
            secondMax = maxCount
            maxCount = monkey.inspectionCount
        elif monkey.inspectionCount > secondMax:
            secondMax = maxCount
    return maxCount * secondMax


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
