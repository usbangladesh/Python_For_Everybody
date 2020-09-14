my_name = "md arif Islam"
string_list = my_name.split()
print(len(string_list))

for i in string_list:
    print(i)
print("")
line = "Md Arif Islam, email: dhakapabna@yahoo.com"
words = line.split()
print(words)
email = words[-1]
print(email)
email_pieces = email.split("@")
print(email_pieces)
