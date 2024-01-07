'''Q16. Write a program that returns the largest and the smallest even number in the list of integers. If
there is no even number in the input, print “No even element”.'''
n=eval(input('Enter the list: '))
b=[]
for i in n:
    if i%2==0:
        if i not in b:
            b.append(i)
flag=len(b)
if flag>0:
    print('The biggest even number is:',max(b))
    print('The smallest even number is:',min(b))
if flag==0:
    print('There is no even number in the given list')
