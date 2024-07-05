from itertools import permutations
wrong_flag = "abbaa$$$cccddd$$$aaaddd"

def sol()->list:
    parted_flag = wrong_flag.split('$$$')
    all_permutations = [''.join(p) for p in permutations(parted_flag)]
    return all_permutations

permutations = sol() 
for p in permutations:
    print(p)
print(permutations)
