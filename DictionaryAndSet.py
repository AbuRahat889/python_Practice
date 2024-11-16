

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

print(dic)
print(dic["age"])
print(dic["score"]["oop"])

print(dic.keys())#print all keys
print(len(dic.keys()))

print(dic.values())#print all values
print(dic.get("fullName"))#print keys value

new_dic = {"city":"Dhaka"}#update old dic
dic.update(new_dic)
print(dic)
