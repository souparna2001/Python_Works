# 2. Write a program to filter the dictionary, from a dictionary of people’s heights and you wanted to filter out anyone below a certain height.
# Let’s filter out anyone less than 170cm.

heights={"sona":150,"rose":155,"priyana":150,"sreya":175,"lena":180,"neha":165}

for name, height in heights.items():
    if height>= 170:
        print(f"{name}:{height}")                



