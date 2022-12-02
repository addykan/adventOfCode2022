
def readFile(path):
    with open(path, "rt") as f:
        return f.read()


def getMoveScore(myMove):
    if myMove == 'X':
        return 1
    elif myMove == 'Y':
        return 2
    elif myMove == 'Z':
        return 3


def calculateScore(opponentMove, myMove):
    combo = opponentMove + myMove
    if combo in ['AX', 'BY', 'CZ']:
        res = 3
    elif combo in ['AY', 'BZ', 'CX']:
        res = 6
    elif combo in ['AZ', 'BX', 'CY']:
        res = 0
    return res + getMoveScore(myMove)


def part1():
    res = 0
    data = readFile('input.txt')
    for line in data.splitlines():
        opponent, mine = line.split()
        res += calculateScore(opponent, mine)
    print(res)


def findMyMove(opponentMove, baseScore):
    loseDict = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    drawDict = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    winDict = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    if baseScore == 0:
        move = loseDict[opponentMove]
    elif baseScore == 3:
        move = drawDict[opponentMove]
    else:
        move = winDict[opponentMove]
    return getMoveScore(move)


def calculateNewScore(opponentMove, myRes):
    if myRes == 'X':
        baseScore = 0
    elif myRes == 'Y':
        baseScore = 3
    elif myRes == 'Z':
        baseScore = 6
    return baseScore + findMyMove(opponentMove, baseScore)


def part2():
    res = 0
    data = readFile('input.txt')
    for line in data.splitlines():
        opponentMove, myRes = line.split()
        res += calculateNewScore(opponentMove, myRes)
    print(res)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
