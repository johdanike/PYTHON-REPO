print("\nPROGRAM THAT CALCULATES HEART RATE FOR EXERCISE")

age = int(input("\nEnter age: "))
target_heart_rate_range = int(input("\nEnter target heart rate (50 - 85%): "))
target_heart_rate_percentage = target_heart_rate_range / 100



average_max_heart_rate = 220
max_heart_rate = 220 - age

lower_limit = max_heart_rate * 0.64
upper_limit = max_heart_rate * 0.76

target_heart_rate = max_heart_rate * target_heart_rate_percentage

