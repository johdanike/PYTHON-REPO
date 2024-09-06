num_student = int(input("Enter number of students: "))
num_subject = int(input("Enter number of subjects: "))


def main():
    print(set_register())
    print(total_average_score(register))


def set_register(input):
    inner_list = []
    register = []
    for number in range(num_student):
        for subject in range(num_subject):
            inner_list.append(0)
        register.append(inner_list)
        inner_list = []

    print(register)
    for outer in range(len(register)):
        print(f"Student {outer + 1}: ")
        for inner in range(len(register[outer])):
            register[outer][inner] = int(input(f"Enter score for subject {inner + 1}: "))
    print(register)
    return register



def total_average_score(register):
    total = []
    average = []
    sum = 0
    for index in range(len(register)):
        for index2 in range(len(register[index])):
            sum = sum + register[index][index2]
            mid = sum / num_student
            average.append(mid)
            total.append(sum)
            sum = 0
            mid = 0
    print(f"Total: {total}")
    print(f"Average: {average}")
    return total, average






