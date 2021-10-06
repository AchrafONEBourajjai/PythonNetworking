import re
with open("test.txt",'r') as file:
    for line in file:
        if re.search("CISCO|cisco",line):
            print(f"{line} \n",end='')
