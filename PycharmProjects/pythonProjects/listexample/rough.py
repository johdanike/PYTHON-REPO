
def output_tuple():
    x = []
    n = [0] * 2
    for _ in range(2):
        x.append(n)

   # x[0][1] = that_gets()
    #x[1][0] = 1
    x[1][1] = that_gets()
    return x

print(output_tuple())

tuple2 = ("Orange", [10, 20, 30], (5, 15, 25))


def that_gets():
    # value_1 = tuple2[1]
    # value_2 = tuple2[2]
    # for index in tuple2:
    #   for element in index:
    #      value_1 += element[1]
    #     value_2 += element[2]

    #  value_1 = tuple2[1][1]
    # value_2 = tuple2[2][2]
    value_1 = 0
    value_2 = 0

    tuple2 = list(tuple2)
    for i in tuple2:
        if num in tuple2[1][1] == 20:
            value_1 = num
        if
    return value_1, value_2


result1 = that_gets()
print(result1)
