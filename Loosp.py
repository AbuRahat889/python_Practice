
#   qs 1
# i = 0
# while i<= 10:
#     # print(i)
#     i+=1

# qs 2 (multipication table) 
# n=5
# while i<= 10:
#     multiple = n * i
#     print("the multiple are:" , multiple)
#     i+=1

# qs 3
# num = [1,4,9,16,25,36,49,64,81,100]

# while i < len(num):
#     print(num[i])
#     i+=1


# qs 4
i = 0
num = (1,4,9,16,25,36,49,64,81,100)
n = int(input("Enter a number: "))

while i < len(num):
    if(num[i] == n):
        print("match the number",i)
    # else:
    #     print("Dont Match")
    i+=1