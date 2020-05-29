marks=eval(input('Enter the Marks:'))

if(marks>0 and marks<35):

    grade='F'

elif(marks<45):

    grade='S'

elif(marks<65):

    grade='C'


elif(marks<75):

    grade='B'

elif(marks<=100):

    grade='A'

else:

    grade='ENTER A VALID MARK'


print('YOUR GRADE:',grade)
