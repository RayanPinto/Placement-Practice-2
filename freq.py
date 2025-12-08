str="abcabc"
str1=list(str)
print(str1)
str3=sorted(str1)
print(str3)
for i in range(len(str3)):
    print(','.join(str3[i]),end='')
dict={}
for i in range(len(str1)):
    dict[i]=str1[i]
print(dict)
str4=list(dict.values())
print(str4)

