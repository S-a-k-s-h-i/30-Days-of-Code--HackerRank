#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    lst=[]
    
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    # sum=0
    # for i in range(6):
    #     for j in range(6):
    #         if i<4 and j<4:
    #             # print(arr[i][j],arr[i][j+1],arr[i][j+2],arr[i+1][j+1],arr[i+2][j],arr[i+2][j+1],arr[i+2][j+2])
    #             sum=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
    #             # print(sum)
    #             lst.append(sum)
    #             sum=0
    # print(lst)
    for i in range(4):
        for j in range(4):
            lst.append((sum(arr[i][j:j+3])+arr[i+1][j+1]+sum(arr[i+2][j:j+3])))
    print(max(lst))

