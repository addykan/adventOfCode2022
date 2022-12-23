import math

def readFile(path):
    with open(path, "rt") as f:
        return f.read()


class Folder:
    def __init__(self, name, parent, children: dict):
        self.name = name
        self.parent = parent
        self.children = children
        self.size = sum(child.getSize() for child in self.children)

    def addChild(self, child):
        self.children[child.name] = child
        self.size += child.getSize()

    def getSize(self):
        return sum(self.children[child].getSize() for child in self.children)

    def getChildrenNames(self):
        return list(map(lambda x: self.children[x].name, self.children))

    def __repr__(self):
        return f'Folder{self.name}({[repr(child) for child in self.children]})'

    def __hash__(self):
        return hash(self.__repr__())


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def getSize(self):
        return self.size

    def __repr__(self):
        return f'File {self.name} with size {self.size}'

    def __hash__(self):
        return hash(self.__repr__())


def constructFileTree(data):
    topFolder = Folder('/', None, dict())
    currFolder = topFolder
    for line in data.splitlines()[1:]:
        if line.startswith('$'):
            match line.split()[1:]:
                case ['cd', folder]:
                    print("cd command, folder = ", folder)
                    if folder == '..':
                        currFolder = currFolder.parent
                    elif folder not in currFolder.getChildrenNames():
                        newFolder = Folder(folder, currFolder, dict())
                        currFolder.addChild(newFolder)
                        currFolder = newFolder
                    else:
                        currFolder = currFolder.children[folder]
        else:
            first, second = line.split()
            if not first.isdigit():
                folder = Folder(second, currFolder, dict())
                currFolder.addChild(folder)
            else:
                file = File(second, int(first))
                currFolder.addChild(file)
    return topFolder


def getMaxSizes(folder):
    if not isinstance(folder, Folder):
        return 0
    else:
        children = sum(getMaxSizes(
            folder.children[child]) for child in folder.children)
        return (folder.getSize() if folder.getSize() < 100000 else 0) + children


def part1():
    data = readFile('input.txt')
    topFolder = constructFileTree(data)
    return getMaxSizes(topFolder)


def findMinSizeFolder(topFolder, dataToDelete):
    if not isinstance(topFolder, Folder):
        return math.inf
    else:
        minSizeFolder = topFolder.getSize()
        minFolderName = topFolder.name
        for child in topFolder.children:
            childSize = topFolder.children[child].getSize()
            if childSize >= dataToDelete and childSize < minSizeFolder:
                minSizeFolder = childSize
                minFolderName = topFolder.children[child].name

def part2():
    data = readFile('input.txt')
    topFolder = constructFileTree(data)
    dataToDelete = 70000000 - topFolder.getSize()
    return findMinSizeFolder(topFolder, dataToDelete)


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
