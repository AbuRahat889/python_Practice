# object create
# class rahat:
#     name = "shaum"
#     age = 25


# s1 = rahat()
# print(s1.name, "age :", s1.age)


# constructor
class constructor:
    def __init__(self, name):  # want to pass multiple perametter
        self.fullName = name
        print("this is constructor")


s2 = constructor("Rahat")
print(s2.fullName)
