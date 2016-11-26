import random

def transpose(GameBoard_Primary):
    GameBoard_Primary = [list(i) for i in zip(*GameBoard_Primary)]
    return GameBoard_Primary

def CustomSort(GameBoard_Primary, axis):
    GameBoard_Secondary = []
    for i in range(0, 4):
        GameBoard_memory = []
        for item in GameBoard_Primary[i]:
            GameBoard_memory.append(item)
        if axis == 3 or axis == 1:
            GameBoard_memory.sort(key=bool, reverse=True)
        else:
            GameBoard_memory.sort(key=bool)
        GameBoard_Secondary.append([GameBoard_memory])
    return GameBoard_Secondary

def GridPrint(GameBoard_Primary):
    for i in range(0, 4):
        print(GameBoard_Primary[i])
    
def score(GameBoard_Primary):
    score = []
    for i in range(0, 4):
        for item in GameBoard_Primary[i]:
            score.append(item)
    print(sum(score))
    
def MergeLogic(GameBoard_Primary):
    Row1 = GameBoard_Primary[0]
    Row2 = GameBoard_Primary[1]
    Row3 = GameBoard_Primary[2]
    Row4 = GameBoard_Primary[3]
    GameBoard_memory = []
    z = 3
    while z > -1:
        t = int(z - 1)
        if Row1[z] == Row1[t]:
            Row1[z] = int(Row1[t] * 2)
            Row1[t] = 0
        if Row2[z] == Row2[t]:
            Row2[z] = int(Row2[t] * 2)
            Row2[t] = 0
        if Row3[z] == Row3[t]:
            Row3[z] = int(Row3[t] * 2)
            Row3[t] = 0
        if Row4[z] == Row4[t]:
            Row4[z] = int(Row4[t] * 2)
            Row4[t] = 0
        z = int(z - 1)
    GameBoard_memory.append([Row1])
    GameBoard_memory.append([Row2])
    GameBoard_memory.append([Row3])
    GameBoard_memory.append([Row4])
    return GameBoard_memory

def TileSpawn(GameBoard_Primary):
    val = random.choice([2, 4])
    PrimaryIndex = random.randrange(0, 3)
    SecondaryIndex = random.randrange(0, 3)
    List_Memory = GameBoard_Primary[PrimaryIndex]
    while List_Memory[SecondaryIndex] != 0:
        PrimaryIndex = random.randrange(0, 3)
        SecondaryIndex = random.randrange(0, 3)
    List_Memory[SecondaryIndex] = val
    GameBoard_Primary[PrimaryIndex] = List_Memory
    return GameBoard_Primary

def TileSpawnInit(GameBoard_Primary):
    PrimaryIndex = random.randrange(0, 3)
    SecondaryIndex = random.randrange(0, 3)
    List_Memory = GameBoard_Primary[PrimaryIndex]
    while List_Memory[SecondaryIndex] != 0:
        PrimaryIndex = random.randrange(0, 3)
        SecondaryIndex = random.randrange(0, 3)
    List_Memory[SecondaryIndex] = 2
    GameBoard_Primary[PrimaryIndex] = List_Memory
    return GameBoard_Primary
