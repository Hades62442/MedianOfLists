import random

l1 = [random.randint(1, 100) for i in range(10)]
l2 = [random.randint(1, 100) for i in range(10)]

def findMed(l1, l2):
    l3 = [i for i in l1] + [j for j in l2]
    l3.sort()
    if len(l3) % 2 == 0:
        return (l3[int(len(l3)/2)] + l3[int((len(l3)/2)-1)]) / 2
    else:
        return l3[len(l3)//2]

median = findMed(l1, l2)
print(f"Median of\n{l1}\nand\n{l2}\nis {median}")