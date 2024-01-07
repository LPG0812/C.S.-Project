'''Q17. Write a menu driven program to perform the following tasks:
(i) To find the median from the given list of integers.
(ii) To find the mode from the given list of integers.
(iii) To find the range from the given list of integers.'''
re=0
a=[]
mode=[]
final_mode=[]
final_final_mode=[]
n=int(input('enter the size of list: '))
for i in range(n):
    ele=int(input('enter the element: '))
    a.append(ele)
while re!=4:
    print('[1]The median of the given list.\n[2]The mode of the given list.\n[3]The range of the given list.\n[4]Exit.')
    opt=int(input('Which of the following you want to find out about the list of integers(enter from 1 to 4 respectively): ' ))
    if opt==1:
        #for median
        #for even no of obserbations
        if n%2==0:
            a.sort()
            print('The median of the given list is',(a[int(n/2)-1]+a[int(n/2)])/2)
        #for odd number of observations
        if n%2!=0:
            a.sort()
            print('The median of the given list is',a[int((n+1)/2)-1])
    if opt==2:
        #for mode
        mod=0
        for j in a:
            for k in range(n):
                if j==a[k] and a.index(j)!=k:
                    mod+=1
        if mod==0:
            print('There is no mode of the given list as no element is repeated')
        if mod!=0:
            for l in a:
                num=0
                if l not in mode:
                    mode.append(l)
                    for m in range(n):
                        if l==a[m]:
                            num+=1
                    mode.append(num)
        for q in range(1,len(mode),2):
            final_mode.append(mode[q])
        for r in range(0,len(mode),2):
            final_final_mode.append(mode[r])
        for x in range(len(final_mode)):
            if max(final_mode)==final_mode[x]:
                print('The mode of the given list is',final_final_mode[x])
    if opt==3:
        #for range
        a.sort()
        print('The range of the given list is',a[len(a)-1]-a[0])
    if opt==4:
        break
    retry=input('Do you want to try again?(Yy/Nn): ')
    if retry in 'Yy':
        re+=1
    else:
        break

