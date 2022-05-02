from operator import itemgetter
import numpy as np
from scipy.linalg import eig
# take input from user
n = int(input("Enter the number of nodes:"))
c = int(input("Enter the number of connections:"))

matrix = np.zeros((n, n))
matrix1 = np.zeros((n, n))
for i in range(c):
    x, y = map(int, input().split())
    matrix[x - 1][y - 1] = 1
''' random teleportation with probability is a function of the number of nodes'''
a = 0.1
for i in range(n):
    count = 0
    for j in range(n):
        if matrix[i][j] == 1:
            count += 1
    for j in range(n):
        if matrix[i][j] == 1:
            matrix[i][j] = 1 / count
''' probability to go through a link is 1-a'''
matrix1 = matrix
matrix = matrix * (1 - a)
matrix = matrix + (a / n)

'''without random teleportations matrix1
 with random teleportations matrix'''

print(
    f"Probability transition matrix without random teleportations:\n{matrix1}\n")
''' left eigenvector of matrix1'''
w1, vl1 = eig(np.array(matrix1), left=True, right=False)
sum1 = 0
list1 = []
# eigen value can be 1 in case of no random teleportations
for x in w1:
    if x == 1:
        list1 = vl1[:, sum1]
    sum1 = sum1+1
''' vl1 left eigen vector of matrix1'''
print("Left eigen vector:", list1, "\n")
sum1 = 0
list2 = []
for i in range(len(list1)):
    sum1 = sum1+list1[i]
for i in range(len(list1)):
    list2.append(list1[i] / sum1)


print(
    f"Principal Left eigenvector of probability transition matrix without random teleportations:\n{list2}\n")
print(f"Probability transition matrix with random teleportations:\n{matrix}\n")
w, vl = eig(np.array(matrix), left=True, right=False)
sum = 0
list = []
maxeigenvalue = 0
maxeigenvalueindex = 0
''' eigen value can not be 1 but we have to consider max eigen valuesfor our calculation'''
for x in w:
    if x > maxeigenvalue:
        maxeigenvalue = x
        maxeigenvalueindex = sum
    sum = sum + 1
list = vl[:, maxeigenvalueindex]
sum = 0
print("list:", list)
for i in range(len(list)):
    sum = sum + list[i]
list3 = []
for i in range(len(list)):
    list3.append(list[i] / sum)
print(
    f"Normalized Principal Left eigenvector of probability transition matrix with random teleportations:\n{list3}\n")
# power method
# Normalization function for power iteration method


def normalise(x):
    fac = np.linalg.norm(x)
    x_n = x / fac
    return fac, x_n


print(f"Power method for probability transition matrix without random teleportations:")
a = np.array(matrix1)
max_iterations = 1000
atranspose = np.transpose(a)
x=np.ones(len(a))
y=np.ones(len(a))
 
for i in range(max_iterations):
    x = np.dot(a,x)
    poweigenval, x = normalise(x)
 
'''power eigenval is the eigenval calculated using power iteration method'''
 
for i in range(max_iterations):
    y = np.dot(atranspose, y)
    transpoweigen, y = normalise(y)
 
'''y is the lefteigenvector'''
 
print("Principal Left Eigenvector without Random Teleportations using Power Iteration:\n")
for x in y:
    print(x,end="  ")
print("\n")
 
index=1
result=[]
for x in y:
    result.append([index,y[index-1]])
    index=index+1
 
result=sorted(result,key=itemgetter(1),reverse=True)
 
print("Page Rankings:\nRank\tPage No\tProbablity")
index=1
for x in result:
    print(index,end="\t")
    for j in x:
        print(j,end="\t")
    index=index+1
    print("\n")

print(f"Power method for probability transition matrix with random teleportations:")
l1 = [1 / n] * n
list4 = []


def rec(l3):
    l2 = np.dot(l3, matrix)
    dist = np.sum((l3 - l2) ** 2)
    list4.append(l2)
    if dist > 0.001:
        dist = rec(l2)
    return list4


x = rec(l1)
for i in range(len(x)):
    print(x[i])
