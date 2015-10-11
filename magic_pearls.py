# Enter your code here. Read input from STDIN. Print output to STDOUT
def pearl(n_list):
    sums = 0
    while len(n_list) > 1:
        print "original list is", n_list
        print "sum of original list is", sum(n_list)
        smallest = min(n_list)
        print "smallest is", smallest        
        n_list.remove(smallest)
        print "removed smallest, list is now", n_list
        second_small = min(n_list) 
        print "second smallest is", second_small
        n_list.remove(second_small)
        print "removed second smallest, list is now", n_list
        restrung = (smallest + second_small) % ((10 ** 9) + 7)
        print "smallest + second_small =", restrung
        n_list.append(restrung)
        print "Added the sum of two smallest to list, list is now", n_list
        sums += restrung
        print "sums is", sums
        print "\n"
        
    if len(n_list) == 1:
        return sums % ((10 ** 9) + 7)
# N = raw_input()
# N_string = raw_input().split()
# N_pearls = [float(n) for n in N_string]

print pearl([2, 4, 1, 2, 10, 2, 3])
print pearl([6, 5, 4, 1, 2])