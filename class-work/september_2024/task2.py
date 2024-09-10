def single_string_from_two_strings(A, B):

    new_group = ""
    for index1 in range(len(B)):
        if B[index1] == B[2]:
            new_group += A[2]
            break
        new_group += B[index1]
    for index in range(len(A)):
        if A[index] == A[2]:
            new_group += B[2]
            break
        new_group += A[index]

    return new_group

result = single_string_from_two_strings("abc", "xyz")
print(result)


def swap_method(A,B):
    new_string_a = B[0:2] + A[2:]
    new_string_b = A[0:2] + B[2:]
    return new_string_a + " " + new_string_b

output = swap_method("abc", "xyz")
print(output)

