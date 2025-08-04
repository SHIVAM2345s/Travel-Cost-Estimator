# Travel Cost Estimator


name = input("Enter your name: ")
destination = input("Enter destination: ")
days = int(input("Number of days: "))
cost_per_day = float(input("Cost per day: ₹"))

total = days * cost_per_day
print(f"{name}, your trip to {destination} will cost ₹{total}")
