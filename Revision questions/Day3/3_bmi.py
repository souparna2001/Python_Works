# write a program to calculate BMI and give message "overweight,underweight,healthy"

weight_in_kg=int(input("enter the weight in kg"))
height_in_cm=int(input("enter the height in cm")) 

height_in_meter=(height_in_cm/100)
bmi=(weight_in_kg)/height_in_meter**2
print(f"bmi={bmi}") 

if bmi>=25 and bmi<30:
      print("overweight")
elif bmi<19:
   print("underweight")
elif bmi>=18.5 and bmi<25: 
      print("healthy")



