import math


def readFile(path):
    with open(path, "rt") as f:
        return f.read()


def inBounds(L, row, col):
    return row >= 0 and row < len(L) and col >= 0 and col < len(L[row])


def constructGraph(data):
    listified = list(map(lambda x: list(x), data.splitlines()))
    graph = dict()
    for row in range(len(listified)):
        for col in range(len(listified[row])):
            reachableCells = []
            for drow, dcol in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                if inBounds(listified, row + drow, col + dcol):
                    if ord(listified[row + drow][col + dcol]) - ord(listified[row][col]) <= 1:
                        reachableCells.append((row + drow, col + dcol))
            graph[(row, col)] = (listified[row][col], reachableCells)
    return graph


def findShortestPathFromGivenCell(graph, start):
    parentsDict = dict()
    toVisit = [start]
    visited = set()
    while toVisit != []:
        row, col = toVisit.pop(0)
        if (graph[(row, col)][0] == 'E'):
            break
        else:
            for adjCell in graph[(row, col)][1]:
                if adjCell not in visited:
                    toVisit.append(adjCell)
                    visited.add(adjCell)
                    parentsDict[adjCell] = (row, col)
    if graph[(row, col)][0] != 'E':
        return math.inf
    stepCount = 0
    while (row, col) != start:
        row, col = parentsDict[(row, col)]
        stepCount += 1
    return stepCount


def part1():
    data = readFile('input.txt')
    graph = constructGraph(data)
    return findShortestPathFromGivenCell(graph, (0, 0))


def part2():
    data = readFile('input.txt')
    graph = constructGraph(data)
    minDist = math.inf
    rows = data.splitlines()
    for row in range(len(rows)):
        for col in range(len(rows[row])):
            if rows[row][col] == 'a':
                shortestPath = findShortestPathFromGivenCell(graph, (row, col))
                if shortestPath < minDist:
                    print(
                        f'shorterPath of length {shortestPath} found from {(row, col)}')
                    minDist = shortestPath
    return minDist


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
