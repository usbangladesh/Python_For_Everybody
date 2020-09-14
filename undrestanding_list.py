countries = ["bangladesh", "usa", 'india', "japan", "pakistan", "china"]

for i in range(len(countries)):
    country = countries[i]
    print("welcome to ", country)
#another way to print samething
print(" ")
for country in countries:
    print(f'welcome to {country}')

#adding two lests
letters = ["a", "b", "c", "g", "e"]
numbers = [1, 2, 3]
print(numbers +letters)

print(type(numbers))
print(dir(numbers))

empty_list =list()
empty_list.append("Md")
print(empty_list)

print(4 in numbers)
print(1 in numbers)
print(5 not in numbers)
letters.sort()
print(letters)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(f"{sum(numbers)/ len(numbers)} this is the avarage of the numbers")

#find the avrage
total = 0
count = 0
while True:
    input_num = input("Enter a Number (1-9): ")
    if input_num == "done": break
    value = float(input_num)
    total = total + value
    count += 1
print("this is avrg of the list", total/count)

#2nd way to do samething
numbers_list = list()
while True:
    input_num = input("Eeter a number: ")
    if input_num == "done": break
    value = float(input_num)

    numbers_list.append(value)
print("Avarage:", sum(numbers_list)/len(numbers_list))










