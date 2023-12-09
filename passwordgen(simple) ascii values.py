import random
print('Welcome to our password generator!')
while True:
    u=random.randrange(65,91)
    l=random.randrange(97,123)
    n=random.randrange(48,58)
    r=random.randrange(4)
    if r==0:
        s=random.randrange(33,48)
    if r==1:
        s=random.randrange(58,65)
    if r==2:
        s=random.randrange(91,97)
    if r==3:
        s=random.randrange(123,128)
    c=chr(u)+chr(l)+chr(n)+chr(s)
    temp=''.join(random.sample(c,len(c)))
    length=int(input("Enter the length of the password: "))
    if length<4:
        print('The minimum password length is 4.')
    else:
        for i in range(length-4):
            temp+=chr(random.randrange(33,128))
        pw=''.join(temp)
        print(pw)
    repeat=input('Would you like to try again? Yy/Nn:')
    if repeat in 'Nn':
        print('Thank you for using our password generator!')
        break
