'''Input a String, count and display the number of vowels, consonants, uppercase, lowercase
characters in string'''
a=input('Enter the string: ')
v=0
c=0
up=0
lc=0
for i in a:
    if i not in ' ':
        if i in 'AEIOUaeiou':
            v+=1
        else:
            c+=1
        if i.isupper():
            up+=1
        if i.islower():
            lc+=1
print('Number of vowels are',v)
print('Number of consonants are',c)
print('Number of uppercase letters are',up)
print('Number of lowercase letters are',lc)
