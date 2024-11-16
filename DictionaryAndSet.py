

# Dictionary

dic= {
    "name": "Rahat",
    "age": 24,
    "student": True,
    "cgp":2.78,
    "subject": ["python","c","c++"],

    "score":{ #nested dictionary
        "oop": 50,
        "DSA": 54,
        "Algorithm": 10
    }
}


dic["fullName"]= "Abu Rahat" # add new value

# print(dic)
# print(dic["age"])
# print(dic["score"]["oop"])

# print(dic.keys())#print all keys
# print(len(dic.keys()))

# print(dic.values())#print all values
# print(dic.get("fullName"))#print keys value

# new_dic = {"city":"Dhaka"}#update old dic
# dic.update(new_dic)
# print(dic)


# Set in Python*********

set1 = {1,2,3,4,5,66,5,7,8,"rahat",1,2,5,4}
set2 = {2,3,5,8,7,9,"abuRahat"}

set1.add(100)#add value in set

union = set1.union(set2) #union
intersection = set.intersection(set2)

# print(union)
# print("Length of Union :", len(union))
# print(intersection)
# print("Length of intersection :", len(intersection))

# set1.clear()#clear set1




# solving some question

dic1 = {}

new_dic1= {
    "table": ["a piece of furniture","list of facts & figures"],
    "cat": "a small animal"
}

dic1.update(new_dic1)
# print(dic1)

# problem 2

sub1 = {"python", "c++",'python', 'javascript'}
sub2 = {"java",'python','java','c++','c'}

classRoom = sub1.union(sub2)
print("Total ClassRoom",len(classRoom))




