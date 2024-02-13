products = ["Bubblegum", "Toffee", "Ice cream", "Milk chocolate", "Doughnut", "Pancake"]
amount_of_products = len(products)
prices = [2, 0.2, 5, 4, 2.5, 3.2]
earned = [202, 118, 2250, 1680, 1075, 80]

print("Earned amount:")
counter = 0
sum_income = 0
while counter < amount_of_products:
    print(f"{products[counter]}: ${earned[counter]}")
    sum_income += earned[counter]
    counter += 1

income = float(sum_income)
print(f"Income: ${income}")