from json import load

f=open("C:\\Users\\souparna\\Desktop\\Python Works\\json_work\\rest_countries\\data.json",encoding="utf-8")

data=load(f)

# print(len(data)) 


                             #    1. all country names

all_country_names=[c.get("name") for c in data]
# print(all_country_names)

                              #    2. independent country names

ind_country_na=[c.get("name")for c in data if c.get("independent")==True]
# print(ind_country_na)

                              #     3. all regions

all_regions={c.get("region") for c in data}
# print(all_regions)

                               #     4. asian country names

asian=[c.get("name") for c in data if c.get("region")=="Asia"]
# print(asian)  

                                #     5. capital of ukraine

c_ukraine=[c.get("capital") for c in data if c.get("name")=="Ukraine"]
# print(c_ukraine)

                                #     6.  capital of all country name

countries_capital=[(c.get("name"),c.get("capital")) for c in data] 
# print(countries_capital)

                               #      7.   print all country_name and currencies

for c in data:
    if "currencies" in c:
        currency_data=c.get("currencies")[0]     #to avoid list[]
    #     print(currency_data.)
    # break    
        # print(currency_data.get("name"),",",c.get("name"))


                              #       8.  borders shared countries of india

india_borders=[c.get("borders") for c in data if c.get("name")=="India"][0]
print(india_borders)
india_border_names=[c.get("name") for c in data if c.get("alpha3Code") in india_borders]
print(india_border_names) 


                            #      9.  print the countries having borders > 4

# for c in data:
#     if "borders" in c and len(c.get("borders"))>4:
#         print(c.get("name")) 


        





