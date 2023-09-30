from math import inf
from collections import *
import math, os, sys, heapq, bisect, random, threading
from functools import lru_cache, reduce
from itertools import *


def inp(): return sys.stdin.readline().rstrip("\r\n")


def out(var): sys.stdout.write(str(var))  # for fast output, always take string


def inpu(): return int(inp())


def lis(): return list(map(int, inp().split()))


def stringlis(): return list(map(str, inp().split()))


def sep(): return map(int, inp().split())


def strsep(): return map(str, inp().split())


def fsep(): return map(float, inp().split())


# Write your code here
sys.stdin = open("test", 'r')
n, x = sep()
a = lis()
