#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
list1= []
list2 = []
list3 = []
def plusMinus(arr,n):
    for i in arr:
        if i < 0:
            list1.append(i)
        if i > 0:
            list2.append(i)
        if(i == 0):
            list3.append(i)

    print(len(list2)/n)
    print(len(list1)/n)
    print(len(list3)/n)
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr,n)
