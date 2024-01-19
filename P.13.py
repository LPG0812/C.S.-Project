'''WAP that should perform the following four tasks:
(i) After getting a word (of input) from the user, your program should use a while (or for) loop to
print out each of the letters of the word.
(ii) Your program should then use another loop to print out each of the letters of the (same) word in
reverse order.
(iii) Make a new variable that is the original word in reverse and print that variable.
(iv) Ask the user for a letter to count. Use another loop to count how many times that letter appears
in the original word.
Print out this count.'''
a=input('Enter a string: ')
for i in a:
    print(i)
for j in range(len(a)-1,-1,-1):
    print(a[j])
for k in range(len(a)-1,-1,-1):
    print(a[k],end='')
l=input('\nEnter the letter to count: ')
c=0
for m in a:
    if l in m:
        c+=1
print('The amount of times the letter',l,'has appeared are',c)  

