

# read the file
file = open("test.txt", "r")
data = file.read()
# print(data)
file = open("test.txt", "w")
file.write("this is new line.")# w change the all data
 
# append data (append add the data at the end)
file = open("test.txt", "a")
file.write("\nthis is another new line")# w change the all data

print(data)




# Delete file
import os
os.remove("newFile.txt")

