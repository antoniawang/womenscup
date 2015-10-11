# Problem Statement

# You are given a set S = {1, 2, 3, N}. 
# Find two integers A and B (A<B) from the set S such that the value of A & B is the maximum possible and less than the given integer K. 
# In this case, & represents the operator bitwise AND.

def possible_max(n, k):
    print n, k
    answer = 0

    if n > (2**k):
        for i in range(k, n):
            print "i is", i
            bitand = i & n
            print "bitand:", bitand
            if answer < bitand < k:
                answer = bitand
    else:
        if k % 2 == 1:
            answer = k - 1
        else:
            answer = k - 2    

    print "answer is"
    return answer    

       
    
# T = int(raw_input())
# for _ in range(T):
#     S = raw_input().split()
#     N = int(S[0])
#     K = int(S[1])
#     print possible_max(N, K)

print possible_max(5,2)
print possible_max(8,5)
print possible_max(2,2)