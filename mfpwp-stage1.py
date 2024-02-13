products = ["Bubblegum", "Toffee", "Ice cream", "Milk chocolate", "Doughnut", "Pancake"]
amount_of_products = len(products)
prices = [2, 0.2, 5, 4, 2.5, 3.2]
print("Prices:")
counter = 0
while counter < amount_of_products:
    print(f"{products[counter]}: ${prices[counter]}")
    counter += 1
