add_dictionary = dict()
add_dictionary["money"] = 12
add_dictionary["age"] = 30
add_dictionary["School"] = "CSULA"
print(add_dictionary)
print("++++++++++++++++++++++++++++++++++++++++++")
one_line_dict = {"Banana" : 6,"Orange" : 4, "Apple" : 5 }
print(one_line_dict)
for key in one_line_dict:
    print(key, one_line_dict[key])
print("using list, key,balues, and items for one lie dictionary\n ++++++++++++++++++++++")
print(list(one_line_dict))
print(one_line_dict.keys())
print(one_line_dict.values())
print(one_line_dict.items())
print("========================================")
count = dict()
names = ["Md", "Arif", "Islam", "Md", "Islam"]
for name in names:
    if name not in count:
        count[name] = 1
    else:
        count[name] = count[name] + 1
print(count)
#another way to write this
counts =dict()
names_list = ['Arif', "Md", "Islam", "Arif", "Md"]
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)


