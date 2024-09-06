#numbers = list(range(1, 101))

#def is_multiple_of_five(n):
 #   if n % 5 == 0:
  #      return n

#result = []
#for number in numbers:
 #   if is_multiple_of_five(number):
  #      result.append(number)


#result = [n for n in numbers if n % 5 == 0]
#print(result)

#print(numbers)

#multi dimensional lists
x = [[0 for _ in range (4)] for _ in range (5)]
#print(x)

samp = []
exterior = []
for x in range(5):
    samp.append(x)
    for y in range(4):
        exterior.append(y)


#print(exterior)


y = list(range(6))
x = []

for i in y:
    x.append(y)
#print(x)

for i in range(5):
    for j in range(4):
        x[i][j] = 8

#print(x)


#list in list
x = []
n = [0] * 4
for _ in range(5):
    x.append(n)

#print(x)


#turple:  a collection in python that can be homogenous or heterogeneous, they are enclosed in parentheses
score = (1,2,3,"Ada")
print(type(score))
#print(score)

x = []
n = [0] * 2
for _ in range(2):
    x.append(n)

print(x)

x[0][1] = 20
x[1][1] = 25

print(x)
tuple2 = ("Orange", [10, 20, 30], (5, 15, 25))
n = len(tuple2)
x = []
n = [0]
for _ in range(len(tuple2)):
    x.append(n)
print(x)


