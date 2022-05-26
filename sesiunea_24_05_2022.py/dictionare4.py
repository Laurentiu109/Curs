user_info = {
    "name" : "Alex",
    "age" : 28,
    "email" : "alex.radu@email.com",
    "gender" : "M"
}

china_years = {
    2010:"Dragonului",
    2011:"Cocosului",
    2012:"Iepurului"
}

colors = {
    "red": "#FF0000",
    "green" : "",
    "blue" : "#0000FF"
}

# lista chei-valori

k_v_china_years = china_years.items()

print(k_v_china_years)

# [
#     (2010, 'Dragonului'), 
#     (2011, 'Cocosului'), 
#     (2012, 'Iepurului')
#     ]

# for kv in china_years.items():
#     # print(type(kv))
#     # print(kv)
#     print("Anul", kv[0], "a fost anul", kv[1])

for k, v in china_years.items():
    print("Anul", k, "a fost anul", v)