

def readFile(path):
    with open(path, "rt") as f:
        return f.read()


def makeMap(data):
    return list(map(lambda x: list(map(lambda y: int(y), list(x))), data.splitlines()))


def isVisible(quadMap, i, j):
    treeHeight = quadMap[i][j]
    allLess = True
    for row in range(i):
        if quadMap[row][j] >= treeHeight:
            allLess = False
            break
    if allLess:
        return True

    allLess = True
    for row in range(i+1, len(quadMap)):
        if quadMap[row][j] >= treeHeight:
            allLess = False
            break
    if allLess:
        return True
    allLess = True
    for col in range(j):
        if quadMap[i][col] >= treeHeight:
            allLess = False
            break
    if allLess:
        return True
    allLess = True
    for col in range(j+1, len(quadMap[i])):
        if quadMap[i][col] >= treeHeight:
            allLess = False
            break
    return allLess


def part1():
    data = readFile('input.txt')
    quadMap = makeMap(data)
    visibleCount = 0
    for i in range(len(quadMap)):
        for j in range(len(quadMap[i])):
            if isVisible(quadMap, i, j):
                visibleCount += 1
    return visibleCount


def getScenicScore(quadMap, i, j):
    treeHeight = quadMap[i][j]
    # up
    upDist = 0
    for row in range(i-1, -1, -1):
        upDist += 1
        if quadMap[row][j] >= treeHeight:
            break
    # down
    downDist = 0
    for row in range(i+1, len(quadMap)):
        downDist += 1
        if quadMap[row][j] >= treeHeight:
            break
    # left
    leftDist = 0
    for col in range(j - 1, -1, -1):
        leftDist += 1
        if quadMap[i][col] >= treeHeight:
            break
    # right
    rightDist = 0
    for col in range(j+1, len(quadMap[i])):
        rightDist += 1
        if quadMap[i][col] >= treeHeight:
            break
    return upDist * downDist * leftDist * rightDist


def part2():
    data = readFile('input.txt')
    quadMap = makeMap(data)
    maxVal = -1
    for i in range(len(quadMap)):
        for j in range(len(quadMap[i])):
            maxVal = max(maxVal, getScenicScore(quadMap, i, j))
    return maxVal


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
