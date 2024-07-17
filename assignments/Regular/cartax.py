print("Program calculates road tax")

car_price = int(input("How much is the car worth? : "))

if(car_price < 1_000_000):
	tax = car_price * (10 / 100)

if(car_price > 1_000_000 and car_price < 3_000_000):
	tax = car_price * (15 / 100)

if(car_price > 3_000_000 and car_price < 5_000_000):
	tax = car_price * (20 / 100)

if(car_price > 5_000_000):
	tax = car_price * (25 / 100)

print(f"Your tax on your car that cost {car_price} is {tax}")

