

def sum_number (a,b):
    sum = a + b
    print(int(sum))
    return sum

# a = float(input("Enter a number : "))
# b = float(input("Enter another number : "))
# sum_number(a,b)


def even_odd(n):
    if(n % 2 == 1 ):
        print("Odd")
    else:
        print("Even")

# even_odd(15)

# Recursion(call function it self)

def show(n):
    if(n == 0):
       return
    print(n)
    show(n-1)
# show(10)

# qs 1

def calculate (n):
    if(n == 0):
        return 0
    return calculate(n - 1) + n
    
sum = calculate(5)
print(sum)