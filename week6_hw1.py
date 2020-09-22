name = input("Enter file:")
di = dict()
handle = open(name)
for line in handle :
    if line.startswith("From ") :
        line = line.split()
        line = line[5].split(":")
        if line[0] in di:
            di[line[0]] = di.get(line[0], 0) + 1
        else:
            di[line[0]] = di.get(line[0], 1)

lst = list()
smallest = '99'

while di :
    for key1 in di:
        if smallest > key1:
            smallest = key1
    lst.append((smallest,di[smallest]))
    del di[smallest]
    smallest = '99'

for idx in range(0, len(lst)) :
    print(lst[idx][0], lst[idx][1])