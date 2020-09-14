counts = dict()
print("Enter some strings: ")

lines = input(" ")
words = lines.split()
print(f'Words: {words}')

print("continue...")
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)

print('+++++++++++++++++++++++ ')

jjj = {"apple" : 5, "orange" : 6, "banana" : 4, "mango" : 2 }
for aaa, bbb in jjj.items():
    print(aaa, bbb)

print("++++++++++++++++++++++") #4:57 minutes video
file_name = input("Enter a text file name: ")
open_file = open(file_name)

counts = dict()
for line in open_file:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    print(counts)

print('+++++++++++++++++++++++++++')
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
    print(bigcount, bigword)


