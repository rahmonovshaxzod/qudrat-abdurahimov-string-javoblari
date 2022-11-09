n1 = int(input("n1 = "))
n2 = int(input("n2 = "))
s1 = input("s1 = ")
s2 = input("s2 = ")
yangi_satr = ''
for i in range(n1):
    yangi_satr += s1[i]
for i in range(len(s2)-n2,len(s2)):
    yangi_satr += s2[i]
print('yangi suz = ',yangi_satr)