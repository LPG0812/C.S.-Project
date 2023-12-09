import random
letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
number='0123456789'
symbols='\'!@#$%^&*()_+}{|:"?><-=[]\;/.,'
pw=''

sym=int(input('Enter amount of symbols in the password:'))
for i in range(sym):
    pw+=(symbols[random.randrange(len(symbols))])

n=int(input("Enter amount of numbers in password:"))
for i in range(n):
    pw+=(number[random.randrange(len(number))])

let=int(input("Enter amount of letters in your password:"))
for i in range(let):
    pw+=(letters[random.randrange(len(letters))])



if let+n+sym<4:
    print('The length of the password is too short:')
else:
    a=''.join(random.sample(pw,len(pw)))
    print(a)
