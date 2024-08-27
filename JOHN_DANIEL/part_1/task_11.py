"""FUNCTION THAT PROMPTS A USER TO ENTER AN INTEGER AND CHECKS WHETHER IT IS DIVISIBLE BY 5 & 6"""
"""PSEUDOCODE"""
#Initialize a variable called number
#Prompt user for input 
#if number is divisible by 5 and 6 output boolean False
#Elif number is divisible by 5 or 6 output True
#Elif number is divisible by 5 or 6 output True

#Output result

"""Execution"""
number = int(input("Enter numberr: "))
if number / 5 == 0 and number / 6 == 0:
	print(f"Is {number} divisible by 5 and 6? False")
