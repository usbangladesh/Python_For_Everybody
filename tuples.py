x = ("a", 2, "b")
print(x[2])

(a,b) = ("a", "b")
print(a,b)
print(a)

print("+++++++++++++++++++++++\n")
d = dict()
d["x"] = 2
d["y"] = 4
for (k, v) in d.items():
    print(k, v)
    dictionary = d.items()
print(dictionary)

print("sorting list of traples\n ")
line_dict = {'a': 1, 'b':2, 'c': 0}
print(line_dict.items())
print("sorted the traples \n ")
print(sorted(line_dict.items()))

#another way
print("if we used for loop and sorted we get this\n")
for k,v in sorted(line_dict.items()):
    print(k,v)
#trples ordered by value of the key
print("sorted by value")
tam_list = list()
for k, v in line_dict.items():
    tam_list.append((v , k))
print(tam_list)
tam_list = sorted(tam_list, reverse = True)
print(tam_list)