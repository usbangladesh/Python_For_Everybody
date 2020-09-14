

# find the most commone 10 words of txt file
file_name = open('intro.txt')
counts = dict()
for line in file_name:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
#convart truple to list
list_word = list()
for key , value in counts.items():
    value_key = (value, key)
    list_word.append(value_key)
list_word = sorted(list_word, reverse = True)
for value , key in list_word[:10]:
    print(key, value)
#this one line does last half of the part
print("++++++++++this one line does last half of the part+++++++++++++")
c = {"x":2, "y":3, "z":1}
print(sorted([(v, k) for k,v in c.items()]))