from sys import argv

SOLID = '*'


def parse_grid(file: str):
    grid = list()
    with open(file) as f:
        for line in f:
            grid.append([c for c in line.strip()])
    return grid

def parse_words(file: str):
    with open(file) as f:
        return {w.strip() for w in f}


def solve(grid, words):
    pass


if __name__ == '__main__':
    print(solve(parse_grid(argv[1]), parse_words(argv[2])))
