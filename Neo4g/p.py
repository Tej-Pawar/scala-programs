1. Subject teacher should conduct first lab practical on basic
programs using python for introducing and using python
environment such as,
a) Program to print multiplication table for given no.


num = int(input("Enter the number: "))
print("Multiplication Table of", num)
for i in range(1, 11):
 print(num,"X",i,"=",num * i)
Output
Enter the number: 12
Multiplication Table of 12
12 X 1 = 12
12 X 2 = 24
12 X 3 = 36
12 X 4 = 48
12 X 5 = 60
12 X 6 = 72
12 X 7 = 84
12 X 8 = 96
12 X 9 = 108
12 X 10 = 120


b) Program to check whether the given no is prime or not.

number = int(input("Enter any number: "))
if number > 1:
 for i in range(2, number):
 if (number % i) == 0:
 print(number, "is not a prime number")
 break
 else:
 print(number, "is a prime number")
else:
 print(number, "is not a prime number")
Output
Enter any number: 23
23 is a prime number

c) Program to find factorial of the given no

def factorial(num):

 if num == 1:
 return num
 else:
 return num * factorial(num - 1)
num = int(input("Enter a Number: "))
if num < 0:
 print("Factorial cannot be found for negative numbers")
elif num == 0:
 print("Factorial of 0 is 1")
else:
 print("Factorial of", num, "is: ", factorial(num))
Output
Enter a Number: 5
Factorial of 5 is: 120

d) Program to print fibonacci series upto given no

nterms = int(input("How many terms? "))
# first two terms
n1 = 0
n2 = 1
count = 0
# check if the number of terms is valid
if nterms <= 0:
 print("Please enter a positive integer ")
elif nterms == 1:
 print("Fibonacci Series upto ",nterms," : ")
 print(n1)
else:
 print("Fibonacci series upto ",nterms," : ")
 while count < nterms:
 print(n1,end=' , ')
 nth = n1 + n2
 # update values
 n1 = n2
 n2 = nth
 count += 1

Output
How many terms? 10
Fibonacci series upto 10 :
0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34 ,


2.Write a program to implement List Operations(Nested list,
Length, Concatenation, Membership ,Iteration ,Indexing and
Slicing), List Methods(Add, Append, Extend & Delete)

List1 = [34,'shubham',45,'python',657,'scala',9999]
List2 = [788,5,499,45,499,67]
Sum = sum(List2)
print("Sum of all elements in List2 : ",Sum)
# nested list
Nested_List = ["Happy", [2,0,1,5],['s','k']]
print("Nested List is : ",Nested_List)
# length
Length = len(List1)
print("Length of List1 : ",Length)
# concatenation
List3=List1+List2
print("Concatenation of List1 & List2 is : ",List3)
# membership
ele='shubham'
if ele in List1:
 print(ele,"is member of List1")
else:
 print(ele,"is not a member of List1")
# list iteration
print("Iteration in List1 : ")
for i in List1:
 print(i)
print()
# indexing
print("Index of 499 in List2 : ",List2.index(499))
# slicing
Slice_List1 = List1[2:5]
print("Slice_List1 is elements from 2 to 5 index of List1 : ",Slice_List1)
# insertion in list
List1.insert(2,'kulkarni')
print("List1 after Inserting 'kulkarni' at position 2 : ",List1)
# append to the list
List1.append(205)
print("List1 after Appending 205 : ",List1)
# extend a list into another list
List1.extend(List2)
print("After Adding List2 into List1 : ",List1)
# remove item at index
List2.pop(4)
print("List2 after delete element at 4 position : ",List2)
print("List2 after sorting : ",sorted(List2))
Output
Sum of all elements in List2 : 1903
Nested List is : ['Happy', [2, 0, 1, 5], ['s', 'k']]
Length of List1 : 7
Concatenation of List1 & List2 is : [34, 'shubham', 45, 'python', 657,
'scala', 9999, 788, 5, 499, 45, 499, 67]
shubham is member of List1
Iteration in List1 :
34
shubham
45
python
657
scala
9999
Index of 499 in List2 : 2
Slice_List1 is elements from 2 to 5 index of List1 : [45, 'python', 657]
List1 after Inserting 'kulkarni' at position 2 : [34, 'shubham',
'kulkarni', 45, 'python', 657, 'scala', 9999]
List1 after Appending 205 : [34, 'shubham', 'kulkarni', 45, 'python', 657,
'scala', 9999, 205]
After Adding List2 into List1 : [34, 'shubham', 'kulkarni', 45, 'python',
657, 'scala', 9999, 205, 788, 5, 499, 45, 499, 67]
List2 after delete element at 4 position : [788, 5, 499, 45, 67]
List2 after sorting : [5, 45, 67, 499, 788]


3.Write a program to Illustrate Different Set Operations.

A = {0, 2, 4, 6, 8};
B = {1, 2, 3, 4, 5};
print("Set A : ",A)
print("Set B : ",B)
# union
print("Union :", A | B)

# intersection
print("Intersection :", A & B)

# difference = elements in A not in B
print("Difference :", A - B)

# symmetric difference = elements in A not in B & elements in B not in A
print("Symmetric difference :", A ^ B)
Output
Set A : {0, 2, 4, 6, 8}
Set B : {1, 2, 3, 4, 5}
Union : {0, 1, 2, 3, 4, 5, 6, 8}
Intersection : {2, 4}
Difference : {0, 8, 6}
Symmetric difference : {0, 1, 3, 5, 6, 8}


5.Write a program to implement Breadth First Search Traversal.

graph = {
 'A' : ['B','C','D'],
 'B' : ['E'],
 'C' : ['F'],
 'D' : ['E','F'],
 'E' : ['G'],
 'F' : ['G'],
 'G' : [],
 }
def bfs_connected_component(graph, start):
 # keep track of all visited nodes
 explored = []
 # keep track of nodes to be checked
 queue = [start]
 levels = {} # this dict keeps track of levels
 levels[start]= 0 # depth of start node is 0
 visited= [start] # to avoid inserting the same node twice into thequeue
 # keep looping until there are nodes still to be checked
 while queue:
 # pop shallowest node (first node) from queue
 node = queue.pop(0)
 explored.append(node)
 neighbours = graph[node]
 # add neighbours of node to queue
 for neighbour in neighbours:
 if neighbour not in visited:
 queue.append(neighbour)
 visited.append(neighbour)
 levels[neighbour]= levels[node]+1
 # print(neighbour, ">>", levels[neighbour])
 print(levels)
 return explored
ans = bfs_connected_component(graph,'A')
print(ans)
Output
{'A': 0, 'B': 1, 'C': 1, 'D': 1, 'E': 2, 'F': 2, 'G': 3}
['A', 'B', 'C', 'D', 'E', 'F', 'G']


6.Write a program to implement Depth First Search Traversal.

graph1 = {
 'A' : ['B','C','D'],
 'B' : ['E'],
 'C' : ['F'],
 'D' : ['E','F'],
 'E' : ['G'],
 'F' : ['G'],
 'G' : [],
}
def dfs(graph, node, visited):
 if node not in visited:
 visited.append(node)
 for n in graph[node]:
 dfs(graph,n, visited)
 return visited
visited = dfs(graph1,'A', [])
print(visited)
Output
['A', 'B', 'E', 'G', 'C', 'F', 'D']


7.Write a program to implement Water Jug Problem.

from collections import defaultdict
jug1, jug2, aim = 4, 3, 2
visited = defaultdict(lambda: False)
def waterJugSolver(amt1, amt2):
 if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
 print(amt1, amt2)
 return True
 # Checks if we have already visited the
 # combination or not. If not, then it proceeds further.
 if visited[(amt1, amt2)] == False:
 print(amt1, amt2)
 # Changes the boolean value of
 # the combination as it is visited.
 visited[(amt1, amt2)] = True

 # Check for all the 6 possibilities and
 # see if a solution is found in any one of them.
 return (waterJugSolver(0, amt2) or
 waterJugSolver(amt1, 0) or
 waterJugSolver(jug1, amt2) or
 waterJugSolver(amt1, jug2) or
 waterJugSolver(amt1 + min(amt2, (jug1-amt1)),
 amt2 - min(amt2, (jug1-amt1))) or
 waterJugSolver(amt1 - min(amt1, (jug2-amt2)),
 amt2 + min(amt1, (jug2-amt2))))

 # Return False if the combination is
 # already visited to avoid repetition otherwise
 # recursion will enter an infinite loop.
 else:
 return False
print("Steps: ")

# Call the function and pass the
# initial amount of water present in both jugs.
waterJugSolver(0, 0)
Output
Steps:
0 0
4 0
4 3
0 3
3 0
3 3
4 2
0 2