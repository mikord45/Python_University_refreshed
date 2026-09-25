# f = open('file.txt', mode='rt', encoding='utf-8')
# f.close()

#######

# with open("file.txt", encoding='utf-8') as f:
#     txt = f.read()
#
# print(txt)

########

# f = open('file.txt')
# txt = f.read() #f.read(40)
# f.close()
# print(txt)
# print(repr(txt))

#########

# f = open('file.txt')
# # seek = f.seek(9)
# # print(seek)
# a = f.readline()
# print(a)
# b = f.readlines()
# print(b)
# f.close()

#########

# f = open('file.txt')
# for line in f:
#     print(line)
# f.close()

########

with open("file2.txt", mode="w", encoding='utf-8') as f:
    r = range(1,51)
    res = [(a, b) for a in r for b in [a ** c for c in [2]] if b < 1000]
    print(res)
    for (a, b) in res:
        f.write('wartość: %2d - potęga: %3d\n' % (a, b))

print(open('file2.txt').read())
