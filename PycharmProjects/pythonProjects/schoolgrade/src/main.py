

num_student = int(input("Enter number of students: "))
num_subject = int(input("Enter number of subjects: "))



inner_list = []
register =[]
for number in range(num_student):
    for subject in range(num_subject):
        inner_list.append(0)
    register.append(inner_list)
    inner_list = []

print(register)
for outer in range(len(register)):
    print(f"\nStudent {outer+1}: ")
    for inner in range(len(register[outer])):

        register[outer][inner] = int(input(f"Enter score for subject {inner+1}: "))
print(register)

total = []
average = []
sorted = []
position = []
sum = 0
mid = 0
for index in range(len(register)):
    for index2 in range(len(register[index])):
        sum = sum + register[index][index2]
    mid = sum / num_student
    average.append(mid)
    total.append(sum)
    sorted.append(sum)
    sum = 0
    mid = 0
print(f"Total: {total}")
print(f"Average: {average}\n")



#sorting
for index in range(len(sorted)):
    for compare in range(len(sorted)):
        if sorted[index] > sorted[compare]:
            sorted[compare] = sorted[index] ^ sorted[compare]
            sorted[index] = sorted[compare] ^ sorted[index]
            sorted[compare] = sorted[index] ^ sorted[compare]
print(f"Sorted list: {sorted}\n")



#table printing
for index in range(100):
    print("=", end="")
print("\n")
print(f"STUDENT"," " * 6, end="")
for index in range(num_subject):
    print(f"SUBJECT {index+1}"," " * 2, end="")
print(" " * 5,"TOTAL", " " * 3, " AVE", " " * 5, " POS\n", end="")

for index in range(100):
    print("=", end="")
print("\n")
for index in range(num_student):
    print(f"\nStudent {index+1}"," " * 5, end="")
    for index2 in range(num_subject):
        print(register[index][index2]," " * 10, end="")
    print(f"{total[index]}", " " * 5, end="")
    #print(f"{average[index]}\n", " " * 5, end="")
    print("%.2f" % (average[index]))

counter = 1
for index in range(len(sorted)):
    print("index: ", counter, end="")
    position += [counter]
    counter += 1
print(position)
# for index in range(len(position)):
#     for compare in range(len(total)):
#         if total[compare] == sorted[index]:
#


print(position)
for index in range(100):
    print("=", end="")
print("\n")