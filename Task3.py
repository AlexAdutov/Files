f1 = open('1.txt', 'rt')
f2 = open('2.txt', 'rt')
f3 = open('3.txt', 'rt')
lenght1=len(f1.readlines())
lenght2=len(f2.readlines())
lenght3=len(f3.readlines())
f1.close()
f2.close()
f3.close()

file_attr={lenght1:'1.txt', lenght2:'2.txt', lenght3:'3.txt'}
for _ in range(3):
    lenght_temp=(min(file_attr.keys()))
    #name_file=file_attr.pop(min(file_attr.keys()))
    name_file = file_attr.pop(lenght_temp)
    with open('res.txt','at') as f:
        f.write(name_file+'\n')
        #f.write('\n')
        f.write(str(lenght_temp)+'\n')
        #f.write('\n')
        for line in open(name_file, 'rt'):
            f.write(line)
        f.write('\n')
print('look at file - res.txt')

    # print(name_file)
    # print(lenght_temp)
    # for line in open(name_file, 'rt'):
    #     print(line,end='')
    # print()
