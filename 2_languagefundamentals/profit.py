selling_price=int(input("enter selling price"))
cost_price=int(input("enter cost price"))
profit=selling_price-cost_price
profit_in_percentage=(profit/cost_price)*100
print(f"a product whose cost price is {cost_price} sold for {selling_price}rs %profit={profit_in_percentage}")