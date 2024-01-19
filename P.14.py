'''Twisted Pig Latin. Prompt the user to enter a single word. Then form a new word by taking the
first letter of the original word, moving it to the end, and adding “ay”. Thus “school” becomes
“choolsay”.'''
a=input('Enter a string: ')
print(a[1:]+a[0]+'ay')