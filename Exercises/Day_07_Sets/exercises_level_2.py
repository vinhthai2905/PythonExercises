
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Join A and B
A_B = A.union(B)
print(A_B)
# Find A intersection B
a_inter_b = A.intersection(B)
print(a_inter_b)
# Is A subset of B
# Are A and B disjoint sets
# Join A with B and B with A
# What is the symmetric difference between A and B
# Delete the sets completely
A_B.clear()