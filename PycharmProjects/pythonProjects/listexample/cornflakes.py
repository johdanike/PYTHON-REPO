tuple2 = ("Orange", [10, 20, 30], (5, 15, 25))

def that_gets():
    value_1 = tuple2[1][1]
    value_2 = tuple2[2][2]

    return value_1, value_2
result1 = that_gets()
print(result1)

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
