import random
import readchar
import replit

score = 0
best = 0 

#1
def deepClone(bored):
    new = []
    for b in bored:
        if type(b) == type([]):
            new.append(deepClone(b))
        else:
            new.append(b)
    return new


#2
def bor():
    width = 4
    height = 4

    b = []
    for i in range(height):
        l = []
        for j in range(width):
            l.append("")
        b.append(l)
    return b


#3
def spawn(bur):
    num = 2
    if random.randint(1, 100) <= 10:
        num = 4

    while True:
        x = random.randint(0, len(bur[0]) - 1)
        y = random.randint(0, len(bur) - 1)
        if bur[y][x] != "":  # not bur[y][x] == ""
            continue
        bur[y][x] = num
        break


#4
def start(bur):
    i = 0
    while i < 2:
        spawn(bur)
        i = i + 1


#5
def borPrint(bur):
    global score
    global best
    space = -3
    replit.clear()
    print("Score: " + str(score) + "\tBest: " + str(best))
    print("-" * (len(bur[0]) * abs(space) + len(bur[0]) + 1))
    for i in range(len(bur)):
        for j in range(len(bur[i])):
            print("|" + ("%" + str(space) + "s") % bur[i][j], end="")
        print("|")
        print("-" * (len(bur[0]) * abs(space) + len(bur[0]) + 1))


#6
def gameover(map):
    clone = deepClone(map)
    dir = ["w", "a", "s", "d"]
    for i in range(len(dir)):
        if move(clone, dir[i], True):
            return False
    return True


#7
def move(bor, m, sim=False):
    global score
    flag = False
    if m == "w":
        for i in range(1, len(bor)):
            for j in range(len(bor[i])):
                if bor[i][j] == "":
                    continue
                y = i
                x = j
                while y - 1 >= 0 and bor[y - 1][x] == "":
                    flag = True
                    bor[y - 1][x] = bor[y][x]
                    bor[y][x] = ""
                    y = y - 1
        for i in range(1, len(bor)):
            for j in range(len(bor[i])):
                if bor[i][j] == "":
                    continue
                y = i
                x = j
                if y - 1 >= 0 and bor[y][x] == bor[y - 1][x]:
                    flag = True
                    bor[y][x] = ""
                    bor[y - 1][x] = bor[y - 1][x] * 2
                    if not sim:
                        score = score + bor[y - 1][x]
        for i in range(1, len(bor)):
            for j in range(len(bor[i])):
                if bor[i][j] == "":
                    continue
                y = i
                x = j
                while y - 1 >= 0 and bor[y - 1][x] == "":
                    flag = True
                    bor[y - 1][x] = bor[y][x]
                    bor[y][x] = ""
                    y = y - 1
    elif m == "a":
        for i in range(len(bor)):
            for j in range(1, len(bor[i])):
                if bor[i][j] == "":
                    continue
                y = i
                x = j
                while x - 1 >= 0 and bor[y][x - 1] == "":
                    flag = True
                    bor[y][x - 1] = bor[y][x]
                    bor[y][x] = ""
                    x = x - 1
        for i in range(len(bor)):
            for j in range(1, len(bor[i])):
                if bor[i][j] == "":
                    continue
                y = i
                x = j
                if x - 1 >= 0 and bor[y][x] == bor[y][x - 1]:
                    flag = True
                    bor[y][x] = ""
                    bor[y][x - 1] = bor[y][x - 1] * 2
                    if not sim:
                        score = score + bor[y][x - 1]
        for i in range(len(bor)):
            for j in range(1, len(bor[i])):
                if bor[i][j] == "":
                    continue
                y = i
                x = j
                while x - 1 >= 0 and bor[y][x - 1] == "":
                    flag = True
                    bor[y][x - 1] = bor[y][x]
                    bor[y][x] = ""
                    x = x - 1
    elif m == "s":
        for i in range(len(bor) - 2, -1, -1):
            for j in range(len(bor[i]) - 1, -1, -1):
                if bor[i][j] == "":
                    continue
                y = i
                x = j
                while y + 1 < len(bor) and bor[y + 1][x] == "":
                    flag = True
                    bor[y + 1][x] = bor[y][x]
                    bor[y][x] = ""
                    y = y + 1
        for i in range(len(bor) - 2, -1, -1):
            for j in range(len(bor[i]) - 1, -1, -1):
                if bor[i][j] == "":
                    continue
                y = i
                x = j
                if y + 1 < len(bor) and bor[y][x] == bor[y + 1][x]:
                    flag = True
                    bor[y][x] = ""
                    bor[y + 1][x] = bor[y + 1][x] * 2
                    if not sim:
                        score = score + bor[y + 1][x]
        for i in range(len(bor) - 2, -1, -1):
            for j in range(len(bor[i]) - 1, -1, -1):
                if bor[i][j] == "":
                    continue
                y = i
                x = j
                while y + 1 < len(bor) and bor[y + 1][x] == "":
                    flag = True
                    bor[y + 1][x] = bor[y][x]
                    bor[y][x] = ""
                    y = y + 1
    elif m == "d":
        for i in range(len(bor) - 1, -1, -1):
            for j in range(len(bor[i]) - 2, -1, -1):
                if bor[i][j] == "":
                    continue
                y = i
                x = j
                while x + 1 < len(bor[i]) and bor[y][x + 1] == "":
                    flag = True
                    bor[y][x + 1] = bor[y][x]
                    bor[y][x] = ""
                    x = x + 1
        for i in range(len(bor) - 1, -1, -1):
            for j in range(len(bor[i]) - 2, -1, -1):
                if bor[i][j] == "":
                    continue
                y = i
                x = j
                if x + 1 < len(bor[i]) and bor[y][x] == bor[y][x + 1]:
                    flag = True
                    bor[y][x] = ""
                    bor[y][x + 1] = bor[y][x + 1] * 2
                    if not sim:
                        score = score + bor[y][x + 1]
        for i in range(len(bor) - 1, -1, -1):
            for j in range(len(bor[i]) - 2, -1, -1):
                if bor[i][j] == "":
                    continue
                y = i
                x = j
                while x + 1 < len(bor[i]) and bor[y][x + 1] == "":
                    flag = True
                    bor[y][x + 1] = bor[y][x]
                    bor[y][x] = ""
                    x = x + 1
    return flag
    
#8
def save():
    global score
    global best
    if score > best:
        best = score
        outfile = open("Best score.txt", "w")
        outfile.write(str(score))
        outfile.close()

#9
def load():
    global best
    try:
        infile = open("Best score.txt", "r")
        best = int(infile.read())
        infile.close()
    except:
        pass
    
#10
def main():
    map = bor()
    start(map)
    load()
    borPrint(map)
    while True:
        k = readchar.readchar()
        if move(map, k):
            save()
            spawn(map)
        borPrint(map)
        if gameover(map):
            print("GAME OVER!")
            break


main()
