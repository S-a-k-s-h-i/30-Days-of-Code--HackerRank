#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    b10=''
    n = int(input())
    while n:
       p = n % 2
       n = n // 2
       b10+=str(p)
    b10=b10[::-1]
    l=list(b10)
    ct=0
    lst=[]
    for i in range(len(l)):
       if i<(len(l)-1) and l[i]==l[i+1]:
          ct+=1
       else:
          ct+=1
          lst.append(ct)
          ct=0
    print(max(lst))
