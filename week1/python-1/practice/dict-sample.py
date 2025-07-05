dict_sample={
    "name":{
        "first_name":"John",
        "last_name":"Doe"
    },
    "age":24
}
# print(dict_sample)

# print(dict_sample["name"])

dict_sample["name"]["first_name"]="Muzammil"
dict_sample["name"]["last_name"]="Ibrahim"
dict_sample["age"]=23
print(dict_sample)

print(list(dict_sample.keys()))
print(list(dict_sample.values()))


