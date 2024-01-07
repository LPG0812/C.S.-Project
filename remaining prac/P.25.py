import circle
import rectangle
while True:
    print('Which of the following you want to calculate?(choose according from 1 to 5):\n[1] Area of a circle.\n[2] Circumference of the circle.\n[3] Area of a rectangle.\n[4] Perimeter of a rectangle.\n[5] Exit.')
    ch=int(input('Please enter your choice: '))
    if ch==1:
        radius=int(input('Enter the radius: '))
        print("The area of the circle:",circle.area_circle(radius))
    if ch==2:
        radius=int(input('Enter the radius: '))
        print("The circumference of the circle:",circle.circumference_circle(radius))
    if ch==3:
        length=int(input('Enter the length: '))
        breadth=int(input('Enter the breadth: '))
        print('The area of the rectangle:',rectangle.area_rectangle(length,breadth))
    if ch==4:
        length=int(input('Enter the length: '))
        breadth=int(input('Enter the breadth: '))
        print('The perimeter of the rectangle:',rectangle.perimeter_rectangle(length,breadth))
    if ch==5:
        break
    re=input('Do you want to try again?(Yy/Nn): ')
    if re in 'Nn':
        break