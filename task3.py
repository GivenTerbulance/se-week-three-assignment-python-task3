price = int(input("Enter the price:"))
discount_percentage = int(input("Enter the discount_percentage:"))
def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        on_dis = price * (discount_percentage/100)
        print("The amount discounted: ", on_dis)
    else: 
        print("The normal price: ", price)

print(calculate_discount(price, discount_percentage))