s = "Hello world"
str1 = s.split(" ")
dict1 = {}

for i in range(len(str1)):
    dict1[i] = str1[i].lower()

arr1 = {}
for i in range(len(dict1)):
    arr1[i] = sorted(dict1[i])

arr3 = []
for i in range(len(arr1)):
    arr3.extend(arr1[i])
    if i != len(arr1) - 1:   # add a space between words
        arr3.append(" ")

print(arr3)

arr2 = ''.join(arr3)
print(arr2)
