import random
while True:
    ll='abcdefghijklmnopqrstuvwxyz'
    ul='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dig='0123456789'
    sym='\'!@#$%^&*()_+}{|:"?><-=[]\;/.,'
    comb=ll+ul+dig+sym
    temp_pw=''
    rand_ll=random.choice(ll)
    rand_ul=random.choice(ul)
    rand_dig=random.choice(dig)
    rand_sym=random.choice(sym)

    length=int(input("Enter the length of the password:"))

    temp_pw=rand_ll+rand_ul+rand_dig+rand_sym

    if length<4:
        print("The minimum password length is 4 characters.")
    else:
        for i in range(length-4):
            temp_pw=temp_pw+random.choice(comb)

        pw=''.join(random.sample(temp_pw,len(temp_pw)))
        print(pw)
    repeat=input('Would you like to try again? Yy/Nn')
    if repeat in 'Nn':
        break