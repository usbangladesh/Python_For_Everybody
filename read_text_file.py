open_text_file = open(something.txt)
for contant in open_text_file:
    print(contant)


#count character in something.text
count = 0
for contant in open_text_file:
    count = count +1
print("total charecters: ", count)

#reading whole file

reading = open_text_file.read()
print(len(reading))#print total charecters of the file
print(reading[ : 100])

#reading  a line form spacific charecter
for line in open_text_file:
    line = line.rstrip()# delate white space on the right hand side
    if line.startswith("From: "):
        print(line)

#another way to do it
for line in open_text_file:
    line = line.rstrip()
    if not line.startswith("From:"):
        continue
    print(line)

#using in oparator
for line in open_text_file:
    line = line.rstrip()
    if not "something" in open_text_file:
        continue
    print(line)

#asking user to enter a file name
user_file = input("Enter a file name: ")
try:
    open_user_file = open(user_file)
except:
    print("this file cannot be open: ", user_file)
    quit()
count =0
for line in user_file:
    if line.startswith("Subject: "):
        count += 1
    print(f'There were {count}, subject line in{user_file}')





