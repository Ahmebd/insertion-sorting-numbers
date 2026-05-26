numlist=[]
listlen=input("enter the number of the numbers:")
for i in range(int(listlen)):
    i2=str(i+1)
    numlist.append(int(input("enter number "+i2+":")))
def insertion(numlist):
    for i in range(1,len(numlist)):
        k=i
        while numlist[k-1]>numlist[k] and k>0:
            numlist[k-1],numlist[k]=numlist[k],numlist[k-1]
            k-=1
print(numlist)
insertion(numlist)
print (numlist)