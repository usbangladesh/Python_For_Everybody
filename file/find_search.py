import re
open_file = open('intro.txt')
for line in open_file:
    line = line.rstrip()
    #if line.startswith("the"):
        #print(line)
    new_line = re.findall('^the (\S+m\S+)', line)
    print(new_line)
my_favor_num = 'My Favorate numbers are 1, 2, 7, 9'
find_nums = re.findall('[0-9]+' ,my_favor_num)
print(find_nums)
find_nums = re.search('[0-9]+' ,my_favor_num)
print(find_nums)