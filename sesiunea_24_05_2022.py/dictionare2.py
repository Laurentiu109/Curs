user_info = {
    "name" : "Alex",
    "age" : 28,
    "email" : "alex.radu@email.com",
    "gender" : "M"
}

# lista cheilor 

print(user_info.keys())

user_info['address'] = "Bucharest"

for key in user_info.keys():
    print(key)