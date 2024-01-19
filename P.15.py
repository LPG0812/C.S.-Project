'''Write a menu driven program to perform the following tasks:
(i) To check whether the string is a palindrome or not.
(ii) Reads a line, counts the words and then displays how many words are there in the line.
(iii) Reads a line, counts how many times a substring appears in the line and then displays the count.
(iv) Reads a line, counts and display the occurrence of words starting with a vowel in the given line.'''
a=input("Enter the string: ")
print('[1] Whether string is palindrome.\n[2] Count the words and display how many strings are there.\n[3] How many times a substring appears in the line and then displays the count.\n[4] Display the occurrence of words starting with a vowel in the given line.\n[5] Exit ')
while True:
    opt=int(input('Which of the follwing tasks you want to run(choose accordingly from 1 to 5): '))
    if opt==1:
        pal=''
        for i in range(len(a)-1,-1,-1):
            pal+=a[i]
        if a==pal:
            print("the string is palindrome.")
        else:
            print("The string is not palindrome.")
    if opt==2:
        wc=a.split()
        print('The number of the words in the given string are',len(wc))
    if opt==3:
        sub=input('Enter a substring: ')
        co=0
        wc=a.split()
        for i in wc:
            if i==sub:
                co+=1
        print('The substring',sub,'has appeared',co,'times.')
    if opt==4:
        v=0
        wc=a.split()
        for i in range(len(wc)):
            if wc[i][0] in 'AEIOUaeiou':
                v+=1
        print('The amount of the words that start with vowel are',v)
    if opt==5:
        break
    re=input('Do you want to try again[Yy/Nn]: ')
    if re in 'Nn':
        break

    
