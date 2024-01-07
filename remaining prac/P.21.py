tup=()
n=int(input('enter the number of values: '))
for i in range (n):
    ele=int(input('enter the element: '))
    tup+=(ele,)
print('This is the tuple:',tup)
print('the maximum value from the list of elements is',max(tup))
print('The minimum value from the list of elements is',min(tup))