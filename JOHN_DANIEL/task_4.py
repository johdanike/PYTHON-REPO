"""PROGRAM READS SUBTOTAL AND GRATUITY RATE FROM USER AND COMPUTES GRATIUTY AND TOTAL"""
"""PSEUDOCODE"""
#Prompt & Initialise and read entry as subtotal from user input
#Prompt & Initialise and read entry as gratiuty from user input
#Divide gratuity by 100 (as its in percentage) and store in new_gratuity
#Add subtotal to gratuity_new to get total
#Output result

"""Execution"""
subtotal = int(input("Enter subtotal: "))
gratuity = int(input("Enter gratuity: "))
new_gratuity = (gratuity / 100) * subtotal
total = subtotal + new_gratuity
print("The total is", total)