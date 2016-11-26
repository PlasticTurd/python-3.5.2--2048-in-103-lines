import itertools
import CustomTools as f
import random

GameBoard_Primary = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
GameBoard_Primary = f.TileSpawnInit(GameBoard_Primary)
GameBoard_Primary = f.TileSpawnInit(GameBoard_Primary)
f.GridPrint(GameBoard_Primary)
while 1 == 1:
    axis = int(input("1 for up, 2 for down, 3 for left, 4 for right"))
    if axis < 3:
        GameBoard_Primary = f.transpose(GameBoard_Primary)
    GameBoard_Secondary = f.CustomSort(GameBoard_Primary, axis)
    GameBoard_Primary = list(itertools.chain.from_iterable(GameBoard_Secondary))
    GameBoard_Secondary = f.MergeLogic(GameBoard_Primary)
    GameBoard_Primary = list(itertools.chain.from_iterable(GameBoard_Secondary))
    GameBoard_Secondary = f.CustomSort(GameBoard_Primary, axis)
    GameBoard_Primary = list(itertools.chain.from_iterable(GameBoard_Secondary))
    GameBoard_Primary = f.TileSpawn(GameBoard_Primary)#easily the worst part of the code but haven't found a way to streamline
    if axis < 3:
        GameBoard_Primary = f.transpose(GameBoard_Primary)
    f.GridPrint(GameBoard_Primary)
    f.score(GameBoard_Primary)
