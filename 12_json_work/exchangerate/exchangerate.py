from json import load

f=open("C:\\Users\\souparna\\Desktop\\Python Works\\12_json_work\\exchangerate\\data.json",encoding="utf-8")
data=load(f)
# print(len(data)) 

source_currency=input("enter source currency code")  
destination_currency=input("enter destination_currency code")
amount=int(input("enter the amount"))
conversion_rates=data.get("conversion_rates")
# print(conversion_rates)

source_currency_code_rate=conversion_rates.get(source_currency)
destination_currency_code_rate=conversion_rates.get(destination_currency)

print(source_currency_code_rate)
print(destination_currency_code_rate) 

res=(amount/source_currency_code_rate)*destination_currency_code_rate
print(res)  




