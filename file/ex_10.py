fname = input("enter a file name: ")
if len(fname) < 1: fname = "clown.txt"
open_txt_file = open(fname)

di = dict()
for line in open_txt_file:
    line = line.rstrip()
    #print(line)
    words = line.split()
    #print(words)
    for word in words:

        # idiom
        di[word] = di.get(word, 0) +1
        #print(word, "new", di[word])

#print(di)

print("\nnew cord for ex_9.py\n")
tam_list = list()
for k, v in di.items():
    new_peer = (v, k)
    tam_list.append(new_peer)
#print(f"flipped k and v: {tam_list}\n")

tam_list = sorted(tam_list, reverse = True)
#
print(f"This is sorted by value list {tam_list}\n")

print("this is table vershion of v, k: \n")
for v,k in tam_list[:5]:
    print(v, k)