input = [1,2,3,4,5]



def get_key_cubes_in_the_dict(args):
   return {number: number **3 for number in args }

def raise_to_power_3(args):
    dictionary = {}
    for index in args:
       dictionary[index] = index ** 3
    return dictionary


set_in = raise_to_power_3(input)

print(set_in)



