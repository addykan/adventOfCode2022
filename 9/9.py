

def readFile(path):
    with open(path, "rt") as f:
        return f.read()


def part1():
    data = readFile('input.txt')
    headRow = 0
    headCol = 0
    tailRow = 0
    tailCol = 0
    tailVisited = {(0, 0)}
    for line in data.splitlines():
        match line.split():
            case ['U', drow]:
                for _ in range(int(drow)):
                    headRow -= 1
                    if abs(headRow - tailRow) >= 2:
                        assert (tailRow > headRow)
                        tailCol = headCol
                        tailRow = headRow + 1
                    tailVisited.add((tailRow, tailCol))
            case ['D', drow]:
                for _ in range(int(drow)):
                    headRow += 1
                    if abs(headRow - tailRow) >= 2:
                        assert (tailRow < headRow)
                        tailCol = headCol
                        tailRow = headRow - 1
                    tailVisited.add((tailRow, tailCol))
            case ['L', dcol]:
                for _ in range(int(dcol)):
                    headCol -= 1
                    if abs(headCol - tailCol) >= 2:
                        assert (tailCol > headCol)
                        tailRow = headRow
                        tailCol = headCol + 1
                    tailVisited.add((tailRow, tailCol))
            case ['R', dcol]:
                for _ in range(int(dcol)):
                    headCol += 1
                    if abs(headCol - tailCol) >= 2:
                        assert (tailCol < headCol)
                        tailRow = headRow
                        tailCol = headCol - 1
                tailVisited.add((tailRow, tailCol))

    return len(tailVisited)


def part2():
    data = readFile('input.txt')


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
