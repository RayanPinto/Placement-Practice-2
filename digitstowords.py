num = input("Enter your number: ").strip()
print(num[2:3])

arr1 = ["zero","one","two","three","four","five","six","seven","eight","nine"]
digit_map = {i: w for i, w in enumerate(arr1)}
arr3=["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens_map={}
for i in range(11,len(arr3)):
    tens_map[i]=arr3[i]

t_map={20:"Twenty",30:"Thirty",40:"Forty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety"}
arr2=[]
n=len(num)
for i,ch in enumerate(num,1):
    print(n)
    
    ch1=int(ch)
    if n!=1:
        arr2.append(digit_map[int(ch)])
        
    if n==4:
        arr2.append("Thousand")
        n=n-1
    
    elif n==3:
        arr2.append("Hundred")
        n=n-1
    

    while( n==2 and int(num[n:n+1])*10 in t_map):
        
        arr2.append(t_map[int(num[n:n+1])*10])
        print(arr2)
        n=n-1
    
    nn=len(num)
    print(num[nn-1])
    if n==1:
        arr2.append(digit_map[int(num[nn-1:])])
        n=n-1
    if n==0:
        break   
for i in arr2:
    print(i,end=" ")
