#lists of functions
import math
print(' ')
print('CHOOSE THE MATH FUNCTION YOU WANT TO USE')
print('1: function that uses π')
print('2: factorial')
print('3: check if prime number')
print('4: length of hypotenuse in right angle triangle')
print('5: square root of a number')
choose = int(input('enter the number of function: '))
print(' ')

if choose < 6:

 #lists of functions that use π
 if choose == 1:
   print('1: area of circle')
   print('2: volume of cylinder')
   print('3: volume of sphere')
   pi = int(input('enter the number of function that uses π: '))
   print(' ')

   #area of circle
   if pi == 1:
     circle = float(input('Enter the radius of a circle: '))
     #if radius is negative number
     if circle < 0:
       print("Sorry, area of circle does not work with a negative radius")
     #if radius is positive number print
     if circle > 0:
       area = math.pi*(circle**2)
       print('The area of the circle with a radius of',circle, 'is', area)

   #volume of cylinder 
   if pi == 2:
     cylinder = float(input('Enter the radius of a cylinder: '))
     height = float(input('Enter the height of a cylinder: '))
     #if radius or height is negative number
     if cylinder < 0 or height < 0:
       print('Sorry, volume of cylinder does not work with a negative number')
     #if radius is positive number
     else: 
       volume_c = math.pi*(cylinder**2)*(height)
       print('The volume of the cylinder with a radius of', cylinder, 'and a height of ', height, 'is', volume_c)

   #volume of sphere
   if pi ==3:
     sphere = float(input('Enter the radius of a sphere: '))
     #if radius is negative number
     if sphere < 0:
       print('Sorry, volume of sphere does not work with a negative radius')
     #if radius is positive number
     if sphere > 0:
       volume_s = math.pi*(sphere**3)*(4/3)
       print('The volume of the sphere with a radius of', sphere, 'is', volume_s)

   
 #factorial
 elif choose == 2:
   fact=int(input('Enter a number for factorial: '))
   factorial = 1
   # check if the number is negative, positive or zero
   if fact < 0:
     print("Sorry, factorial does not exist for negative numbers")
   elif fact == 0:
     print("The factorial of 0 is 1")
   else:
     for i in range(1,fact + 1):
       factorial = factorial*i
     print("The factorial of",fact,"is",factorial)
   

 #check if prime number
 elif choose == 3:
  prime=int(input('Enter a number to check if it is a prime number: '))
  if prime > 1: 
    # Iterate from 2 to n / 2 
    for i in range(2, prime): 
      # If prime is divisible by any number between 2 and n/2, it is not prime 
      if (prime % i) == 0: 
        print(prime, "is not a prime number") 
        break
    else: 
        print(prime, "is a prime number") 
  #check if number is negative
  if prime < 1:
    print('sorry, negative numbers cannot be prime')


 #length of hypotenuse in right angle triangle
 elif choose == 4:
   print('a² + b² + = c²')
   pyth_a=float(input('Enter the length of a in a²: '))
   #check of pyth_a is negative
   if pyth_a < 1:
     print('sorry, right angle triangles with negative lines do not exist')
   elif pyth_a > 0:
     pyth_b=float(input('Enter the length of a in b²: '))
     #check of pyth_b is negative
     if pyth_b < 1:
       print('sorry, right angle triangles with negative lines do not exist')
     else: 
       pyth_c=float(math.sqrt(pyth_a**2 + pyth_b**2))
       print('The length of c in c² is', pyth_c)
  

 #sqare root of a number 
 elif choose == 5:
   sqr=float(input('Enter a number for square root: '))
   #if number is negative
   if sqr < 0:
     print('square roots for negative number numbers are imaginary')
   #if number is positive
   if sqr > 0:
     sqr_rt=math.sqrt(sqr)
     print(sqr_rt) 

  
 #lists of functions
 print(' ')
 print('CHOOSE THE MATH FUNCTION YOU WANT TO USE')
 print('1: function that uses π')
 print('2: factorial')
 print('3: check if prime number')
 print('4: length of hypotenuse in right angle triangle')
 print('5: square root of a number')
 choose = int(input('enter the number of function: '))
 print(' ')
