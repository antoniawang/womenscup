# Problem Statement

# You are given a set S = {1, 2, 3,…,N}. 
#Find two integers A and B (A<B) from the set S such that the value of A & B is the maximum possible and less than the given integer K. 
#In this case, & represents the operator bitwise AND.
import itertools
def find_max(n, k):
    combos = tuple(itertools.combinations(xrange(1,n+1),2))
    answers = [0]
    for x, y in combos:
    	if x < y:
        	sumxy = (x & y)
        	answers.append(sumxy)
    answer = max([m for m in answers if m < k])
    print answer   	

T = int(raw_input())
for _ in range(T):
    S = raw_input().split()
    num = int(S[0])
    K = int(S[1])
    find_max(num, K)