f = open('workfile', 'w')
f.write('This is the first line of the file.\n')
f.write('Second line of the file.\n')
f.close()

print('test1')
f = open('workfile', 'r')
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

print('test2')
f = open('workfile', 'r')
for line in f:
    print(line, end='')

f.close()

print('test3')

with open('workfile', 'r') as f:
    read_data = f.read()

print(read_data)

