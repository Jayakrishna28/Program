num=int(input("enter the max value:"))
list=[]
for i in range(1,num+1):
    if i%2==0:
        continue
    else:
        list.append(i)
print(list)