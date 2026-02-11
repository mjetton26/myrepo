s = open('rosalind_dna.txt', 'r')

for n in ["A", "C", "G", "T"]:
    print(s.count(n), end=' ')


