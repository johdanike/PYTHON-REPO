print("\nTHIS PROGRAM CALCULATES THE SMALLEST AND LARGEST")

number = int(input("\nEnter number: "))

digit_5 = (number // 1 % 10)
digit_4 = (number // 10 % 10) 
digit_3 = (number // 100 % 10)
digit_2 = (number // 1000 % 10)
digit_1 = (number // 10000 % 10)

print(digit_1," " , digit_2," ", digit_3," ",digit_4," ",digit_5)



