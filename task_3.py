import os
x_files = [x for x in os.listdir() if x == '1.txt' or x == '2.txt' or x == '3.txt']
x_files = list(reversed(x_files))
with open('result.txt', 'a+') as file:
    count = []
    for x in x_files:
        f = open(x).readlines()
        count = (len(f))
        file.write(x)
        file.write('\n')
        file.write(str(count))
        file.write('\n')
        res = open(x).read()
        file.write(res)
