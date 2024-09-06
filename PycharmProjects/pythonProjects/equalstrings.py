
def equal_strings(param, param1):
    if len(param)==len(param1) and sorted(param)==sorted(param1):
        return True
    else:
        return False


print(equal_strings("semicolon", "colon"))


