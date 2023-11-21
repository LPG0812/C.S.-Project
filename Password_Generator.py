import random
print('Welcome to our password generator!')
while True:
    ll='abcdefghijklmnopqrstuvwxyz'
    ul='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dig='0123456789'
    sym='\'!@#$%^&*()_+}{|:"?><-=[]\;/.,'
    comb=ll+ul+dig+sym
    temp_pw=''
    random_ll=random.choice(ll)
    random_ul=random.choice(ul)
    random_dig=random.choice(dig)
    random_sym=random.choice(sym)

    length=int(input("Please enter the length of the required password: "))

    temp_pw=random_ll+random_ul+random_dig+random_sym

    if length<4:
        print("The minimum length of the password has to be atleast 4 characters.")
    else:
        for i in range(length-4):
            temp_pw+=random.choice(comb)

        pw=''.join(random.sample(temp_pw,len(temp_pw)))
        print('"'+pw+'"','is your required password.')
    repeat=input('Would you like to try again?(Yy/Nn): ')
    if repeat in 'Nn':
        print('Thank you for using our password generator!')
        break