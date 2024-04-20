import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd, comb, lcm
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_list_by_one_string(): return [int(x) for x in input()]
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input() for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def main():
    sys.stdin = open("input.txt", "r")
    N = i_input()
    A = i_list()
    ans = []
    index_map = {value: idx for idx, value in enumerate(A)}
    for i in range(1, N+1):
        if A[i-1] == i: continue
        idx = index_map[i] # iのある場所（Idxは0〜N-1）

        ans.append(str(i) + " " + str(A[i-1])) # add ans

        # index_map swap
        index_map[i], index_map[A[i-1]] = i-1, idx

        A[i-1], A[idx] = A[idx], A[i-1] # 実際の値の交換

    print(len(ans))
    for a in ans: print(a)
    print(A)

if __name__ == '__main__':
    main()
