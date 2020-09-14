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
        #print(word)
        #if the key is not there count is 0
        """old_count = di.get(word, 0)
        print(word, "old", old_count)
        new_count = old_count + 1
        di[word] = new_count
        print(word, "new",new_count)
        """
        # idiom
        di[word] = di.get(word, 0) +1
        print(word, "new", di[word])




        """if word in di:
            di[word] = di[word] + 1
            #print("***Existing***")
        else:
            di[word] = 1
            #print("***NEW***")
        #print(word, di[word])"""
print(di)
#finding most commone word
commone = -1
most_commone_word = None
for word, value in di.items():
    print(word, value)
    if value > commone:
        commone = value
        most_commone_word = word
print("the most commone word Is : ")
print(most_commone_word, commone)
