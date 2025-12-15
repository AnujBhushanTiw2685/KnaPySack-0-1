from knapsack import Knapsack

# This file was created to test the knapsack module

n = 3
W = 5

wt = [1,3,4]
val = [10,40,50]

ks= Knapsack(n , W, wt, val)

print("Recursive",ks.kpRec(n,W))
print("Memoized",ks.kpMem(n,W))
print("Tabulated",ks.kpTab())