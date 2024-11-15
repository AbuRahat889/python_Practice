



# arr = [10,20,51,52,41,52,41,"rahat"]
# print(arr)
# print(type(arr))

# arr.pop(5)
# print(arr)


# # touple 

# tup = (1,5,4,1,2,1,39,4,1)# , comma mendetory


# print(tup[2:6])
# print(tup.index(4))
# print(tup.count(1))

# solving some problem

# problem 1

# movieName = []

# movieName.append(input("Enter 1st movie name: "))
# movieName.append(input("Enter 2nd movie name: "))
# movieName.append(input("Enter 3rd movie name: "))

# print(movieName)


# check palindrome  

arr = [1,"Abu","Rahat","Abu",1]

arr2 = arr.copy()

arr2.reverse()

if(arr == arr2):
    print("array are palindrome")
else:
    print("Array are not palindrome")