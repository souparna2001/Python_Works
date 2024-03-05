from json import load
f=open("C:\\Users\\souparna\\Desktop\\Python Works\\json_work\\products\\items.json",encoding="utf-8")  
data=load(f)
# print(len(data))    



# print all category

# categories={p.get("category") for p in data}
# print(categories)

# # print all electronic products 


# elect_products=[p for p in data if p.get("category")=="electronics"]
# print(elect_products)
# print(len(elect_products))

# print all jewelery products

# jew_products=[p for p in data if p.get("category")=="jewelery"]
# print(jew_products)
# print(len(jew_products))

 