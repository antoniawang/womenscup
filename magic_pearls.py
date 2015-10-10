def pearl(n_list):
    sums = []
    while len(n_list) > 1:
        smallest = min(n_list)
        n_list.remove(smallest)
        second_small = min(n_list)
        n_list.remove(second_small)
        restrung = smallest + second_small
        sums.append(restrung)
        n_list.append(restrung)
        
    if len(n_list) == 1:
        return sum(sums)
    
N = raw_input()
N_string = raw_input().split()
N_pearls = [int(n) for n in N_string]

print pearl(N_pearls)
