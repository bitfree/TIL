#!/usr/bin/env python

# @File : cow.py
# @author : bitfree@gmail.com
# @Ver : 0.0.1
# @Date : 2015.12.29
# @Desc :
#
# ToDo : implement algorithm how to change mirror

# 1. STDIN 첫 행의 처음 숫자를 읽어와서 행렬을 만든다.
# 2. STDIN 첫행의 두번째와 세번째를 읽어와서 헛간의 위치를 정한다.
# 3. STDIN 첫 행의 첫 번째 숫자만큼 행렬을 만든 후 나머지 값을 이용해 거울을 설치할 위치를 정한다. 
# 4. 존의 농장을 그려본다.
# 5. 존이 앉아 있는 House 의 위치에서 오른쪽으로 헛간의 위치를 볼 때  시야를 가리지 않아야 한다.
# 6. 5의 알고리즘을 구현한다. --> TODO
# 7. 5의 알고리즘은 헛간이 잘 보일 경우 0 을 출력하고 잘 보이지 않을 경우 하나의 거울의 위치를 조정하여 헛간이 보일 때 그 거울의 번호를 출력하고
# 하나의 거울을 바꿨음에도 불구하고 헛간이 보이지 않을 경우 -1을 출력한다. 


import sys
import numpy as np

M=[]
array_size, bx, by = map(int, sys.stdin.readline().split())
# 5 6 2 
for k in range(1,array_size+1):
	M.append(map(int,sys.stdin.readline().split()))

#3 0 1
#0 2 1
#1 2 1
#3 2 0
#1 3 0

print M.index([3,2,1])
