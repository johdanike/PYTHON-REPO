def object_creator(obj):
    arr = {}
    for index in obj:
        arr[index] = obj.count(index)
    return arr

val = object_creator([1,1,2,3,2])
print(val)
