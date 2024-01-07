'''Q24. WAP to store student names and their percentage in a dictionary, delete a particular student
name from the dictionary. Also display dictionary after deletion.'''
list={}
tot=int(input('Enter the amount of students: '))
print('.'*50)
for i in range (tot):
    stu=input('Enter the name of the student: ')
    per=input('Enter the percentage of said student: ')
    list[stu]=per
    print('.'*50)
while True:
    de=input('Who is the student you want to remove from the said list: ')
    del list[de]
    re=input('Do you want to remove more students?(Yy/Nn): ')
    if re in 'Nn':
        break
print('These are the students in the dictionary after deletion:')
print('Student\t | \tPercentage')
for j in list:
    print(j,'\t | \t',list[j])

