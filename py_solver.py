from argparse import *
from termcolor import colored

def End_position(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 'E':
                return i, j

def End_start(x, y, m):
    if m[x + 1][y] == ' ':
        m[x + 1][y] = 'U'
    if m[x - 1][y] == ' ':
        m[x - 1][y] = 'D'
    if m[x][y + 1] == ' ':
        m[x][y + 1] = 'L'
    if m[x][y - 1] == ' ':
        m[x][y - 1] = 'D'
    return m

def extand(m):
    ok = False
    while not ok:
        m, ok, x, y = __extand(m)
    return m, x, y

def __extand(m):
    L = positions(m)
    ok = False
    i, j = 0, 0
    for x, y in L:
        if m[x - 1][y] == 'S':
            m[x - 1][y] = 'v'
            ok = True
        if m[x - 1][y] == ' ':
            m[x - 1][y] = 'D'
        if m[x + 1][y] == 'S':
            m[x + 1][y] = '^'
            ok = True
        if m[x + 1][y] == ' ':
            m[x + 1][y] = 'U'
        if m[x][y + 1] == 'S':
            m[x][y + 1] = '<'
            ok = True
        if m[x][y + 1] == ' ':
            m[x][y + 1] = 'L'
        if m[x][y - 1] == 'S':
            m[x][y - 1] = '>'
            ok = True
        if m[x][y - 1] == ' ':
            m[x][y - 1] = 'R'
        if ok:
            i, j = x,  y
            return m, ok, x, y
        m[x][y] = m[x][y].lower()
    return m, ok, i, j

def positions(m):
    L = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] in ['U', 'D', 'R', 'L']:
                L.append((i, j))
    return L

def recover(x, y, m):
    while m[x][y] != 'E':
        if m[x][y].lower() == 'd':
            m[x][y] = 'v'
            x += 1
        elif m[x][y].lower() == 'u':
            m[x][y] = '^'
            x -= 1
        elif m[x][y].lower() == 'r':
            m[x][y] = '>'
            y += 1
        else:
            m[x][y] = '<'
            y -= 1
    return m

def print_maze(m):
    for line in m:
        for c in line:
            if c.lower() in ['d', 'u', 'l', 'r']:
                c = ' '
            if c in ['>', '<', '^', 'v']:
                print(colored(c, 'red'), end='')
            elif c == 'E':
                print(colored('@', 'green'), end='')
            else:
                print(c, end='')
        print()

def maze2list(m):
    L = []
    for i in range(len(m)):
        l = []
        for c in m[i]:
            if c != '\r' and c != '\n':
                l.append(c)
        L.append(l)
    return L

if __name__ == "__main__":
    parser = ArgumentParser(description="Maze solver, fast trajectory")
    parser.add_argument('maze', metavar="Maze to solve", type=str)

    args = parser.parse_args()

    path_maze = args.maze

    file_maze = open(path_maze, "r")
    maze = file_maze.readlines()
    file_maze.close()

    maze = maze2list(maze)

    x, y = End_position(maze)
    maze = End_start(x, y, maze)
    maze, x_s, y_s = extand(maze)

    maze = recover(x_s, y_s, maze)
    print_maze(maze)

