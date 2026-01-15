# 터렛
# 백준 레벨8 (백준)
# 문제 링크: https://www.acmicpc.net/problem/1002
# 알고리즘: 수학
# 작성자: ㅅㅅㅅ
# 작성일: 2026-01-15

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    d_sq = (x2 - x1) ** 2 + (y2 - y1) ** 2
    d = d_sq ** 0.5
    
    # 두 원이 완전히 같은 경우
    if d == 0 and r1 == r2:
        print(-1)
    # 한 원이 다른 원 내부에 (접점 없이)
    elif d < abs(r1 - r2):
        print(0)
    # 내접
    elif d == abs(r1 - r2):
        print(1)
    # 두 점에서 교차
    elif d < r1 + r2:
        print(2)
    # 외접
    elif d == r1 + r2:
        print(1)
    # 떨어져 있음
    else:
        print(0)