'''Q23. WAP to input names of n countries and their capital and currency, store it in a dictionary and
display in tabular form. Also search and display for a particular country.'''
n=int(input('enter the amount of countries: '))
list={}
print('.'*50)
for i in range(n):
    coun=input('Name of the country: ')
    cap=input('Enter the capital: ')
    cur=input('name of the currency: ')
    list[coun]=[cap,cur]
    print('.'*50)
while True:
    sear=input('enterthe country to search for: ')
    print('The capital and currency of the country',sear,'is',list[sear][0],'and',list[sear][1])
    re=input('Do you want to search again(Yy/Nn): ')
    if re in 'Nn':
        break

