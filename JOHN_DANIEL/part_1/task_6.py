"""PROGRAM PROMPTS USER TO ENTER MINUTES AND DISPLAYS THE NUMBER OF YEARS AND DAYS """
"""PSEUDOCODE"""
#Prompt, Initialise and read entry as 'minutes_entry' from user input
#Initialize minutes in a day to be = 1440, and store as day_minutes
#Initialize minutes in a year to be 1440 * 365 = 525600, and store as year_minutes
#Dividing 'minutes_entry' by year_minutes gets the number of years as the quotient with some remainder
#Divide minutes by  year_minutes(%) to extract the remainder
#divide again by day_minutes to get the number of remaining days
#Output result

"""Execution"""
minutes_entry = int(input("Enter the minutes: "))
DAY_MINUTES = 1440
YEAR_MINUTES = 525_600
number_of_years = minutes_entry // YEAR_MINUTES
days_remainder = minutes_entry  % YEAR_MINUTES // DAY_MINUTES
print(f'{minutes_entry}mins equates to {number_of_years}years and {days_remainder}days')
