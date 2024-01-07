'''Q20. WAP to shift elements of a list so that the first element moves to the second index and the
second index moves to the third index, etc., and the last element shifts to the first position'''
a=[]
b=[]
n=int(input('enter the size of list: '))
for i in range(n):
    ele=int(input('enter the element: '))
    a.append(ele)
print('The original list:',a)
b.append(a[len(a)-1])
for j in range(len(a)-1):
    b.append(a[j])
print('The final list:',b)
