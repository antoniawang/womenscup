# Enter your code here. Read input from STDIN. Print output to STDOUT
def pearl(n_list):
    sums = []
    while len(n_list) > 1:
        print "original list is", n_list
        smallest = min(n_list)
        print "smallest is", smallest        
        n_list.remove(smallest)
        print "removed smallest, list is now", n_list
        second_small = min(n_list)
        print "second smallest is", second_small
        n_list.remove(second_small)
        print "removed second smallest, list is now", n_list
        restrung = smallest + second_small
        "smallest + second_small =", restrung
        n_list.append(restrung)
        "Added the sum of two smallest to list, list is now", n_list
        sums.append(restrung)
        "sums list is", sums
        print "\n"
        
    if len(n_list) == 1:
        return int(sum(sums))
    
N = raw_input()
N_string = raw_input().split()
N_pearls = [float(n) for n in N_string]

print pearl(N_pearls)