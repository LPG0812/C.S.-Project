a=eval(input('Enter the list: '))
print('Old list:',a)
b=[]
for i in a:
    if i>=0:
        b.append(i)
for j in a:
    if j<0:
        b.append(j)
print('New list:',b)
