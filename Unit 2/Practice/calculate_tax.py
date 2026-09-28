def calculate_tax(item, price, rate):
    taxed = round(float(price * rate + price), 2)
    price = str(round(price, 2))
    taxed = str(taxed)
    print(item + " costs $" + price + " before sales tax, and $" + taxed +" after tax.")

calculate_tax(input("Purchased item name:\n>> "), float(input("Item price $")), float(0.06875))
