import sys
import math
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    S = list(map(int, input().split()))
    print(max(S))