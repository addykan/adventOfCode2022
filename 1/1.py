

def readFile(path):
    with open(path, "rt") as f:
        return f.read()


def part1():
    inputData = readFile('input.txt')
    bestCalories = -1
    currCalorieCount = 0
    for line in inputData.splitlines():
        if line == '':
            if currCalorieCount > bestCalories:
                bestCalories = currCalorieCount
            currCalorieCount = 0
        else:
            currCalorieCount += int(line)
    print(bestCalories)


def part2():
    k = 3
    inputData = readFile('input.txt')
    bestCalories = [-1]*k
    currCalorieCount = 0
    for line in inputData.splitlines():
        if line == '':
            currCalorieCount = 0
        else:
            currCalorieCount += int(line)
            for i in range(len(bestCalories)):
                if currCalorieCount > bestCalories[i]:
                    bestCalories.insert(i, currCalorieCount) # doubly linked list would be more efficient as k grows
                    bestCalories.pop()
                    break
    print(sum(bestCalories))


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
