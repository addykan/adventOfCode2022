

def readFile(path):
    with open(path, "rt") as f:
        return f.read()


def getRegisterHistory(data):
    registerHistory = [0]
    register = 1
    for operation in data.splitlines():
        if operation == 'noop':
            registerHistory.append(register)
        else:
            addVal = int(operation.split()[-1])
            registerHistory.append(register)
            register += addVal
            registerHistory.append(register)
    return registerHistory


def part1():
    data = readFile('input.txt')
    registerHistory = getRegisterHistory(data)
    res = 0
    for i in range(20, 221, 40):
        res += registerHistory[i] * i
    return res


def part2():
    data = readFile('input.txt')
    screen = [['.' for _ in range(40)] for _ in range(6)]
    registerHistory = getRegisterHistory(data)
    for cycle in range(240):
        row = cycle // 40
        col = cycle % 40
        if abs(registerHistory[cycle] - col) <= 1:
            screen[row][col] = 'X'
    for row in screen:
        print(''.join(row))


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
