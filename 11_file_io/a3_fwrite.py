                                            # 1) to write years



# path="C:\\Users\\souparna\\Desktop\\Python Works\\11_file_io\\years.txt"
# f=open(path,"w")
# f.write("hello")



                                            # 2) to write colors 




path="C:\\Users\\souparna\\Desktop\\Python Works\\11_file_io\\colors.txt"

f=open(path,"w")

colors=["red","green","blue"]

for c in colors:
    f.write(c+"\n") 
                #   red
                #   green 
                #   blue
    
    # f.write(c+"") red green blue

    # f.write(c) colors   (only this will print,contents doesn't print)





                   # 3) write all century year from 1800 to 2024 into century years.txt   



# path="C:\\Users\\souparna\\Desktop\\Python Works\\file_io\\century_years.txt"

# f=open(path,"w")


# for year in range(1800,2025):
#      if year%100==0:
#        f.write(str(year)+"\n")


                                              




                                # 4) print all years from 1800 to 2024 into years.txt



# path="C:\\Users\\souparna\\Desktop\\Python Works\\file_io\\all_years.txt"

# f=open(path,"w")


# for year in range(1800,2025):
#         f.write(str(year)+"\n")








                          # 5) read all years from years.txt and print leap years




# path="C:\\Users\\souparna\\Desktop\\Python Works\\file_io\\all_years.txt"

# f=open(path,"r")
# for line in f:
#     year=int(line.rstrip("\n"))
#     if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
#         print(year)









                      #6) write all_years into leap_years.txt





# read_path="C:\\Users\\souparna\\Desktop\\Python Works\\file_io\\all_years.txt"

# write_path="C:\\Users\\souparna\\Desktop\\Python Works\\file_io\\leap_years.txt"

# fw=open(write_path,"w")                
# fr=open(read_path,"r")                  

# for line in fr:
#     year=int(line.rstrip("\n"))
#     if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
#         fw.write(str(year)+"\n")


                     



          



