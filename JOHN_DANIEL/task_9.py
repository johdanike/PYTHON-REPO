"""PROGRAM PRINTS A PAYROLL STATEMENT"""
"""PSEUDOCODE"""
#Collect employees name and store string as name
#Collect number of hours worked per week and store in number_of_hours
#collect hourly pay rate and store as hourly_pay_rate
#Set federal tax rate as constant
#set state tax rate as constant

#print result
"""Execution"""

name = input(Enter employee's name: )
number_of_hours = int(input("Enter number of hours worked in a week: "))
hourly_pay_rate = int(input("Enter hourly pay rate: "))
STATE_TAX_RATE = int(input("Enter state tax withholding rate: "))
FEDERAL_TAX_RATE = int(input("Enter federal tax withholding rate: "))

gross_pay = hourly_pay_rate * number_of_hours
federal_withholding = (FEDERAL_TAX_RATE / 100) * gross_pay
state_withholding = (STATE_TAX_RATE / 100) * gross_pay
total_deductions = state_withholding - federal_withholding 
net_pay = gross_pay - total_deductions   

deductions = 
