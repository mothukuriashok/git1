 a=float(input("enter the principle amount\n"))
b=float(input('enter the intrest rate\n'))
d1=int(input('enter the present date\n'))
if ( d1 > 31 and d1 != 0 ):
 print('enter the valid date')
else:
  m1=int(input('enter the present month\n'))
  if (m1>13 and m1==0):
   print('enter the valid month')
  else:
   y1=int(input('enter the presertnyear\n'))
  if (y1<1900 and y1==0):
   print('enter the valid month')
  else:
   d2=int(input('enter the end date\n'))
  if (d2>31 and d2==0):
    print('enter the valid date')
  else:    
   m2=int(input('enter the end month\n'))
  if (m2>13 and m2==0):
   print('enter the valid month')
  else: 
   y2=int(input('enter the not less than 1900 year\n'))
  if (y2<1900 and y2==0):
   print('enter the valid month')
if (a>100):
 print('The intrest per month is =',(a/100)*b)
 if (d1>d2):
     d3=d1-d2
     print('The counted days=',d3)
 else:
     m1=m1-1
     d3=((d1+30)-d2)
     print('The counted days=',d3)
 if(m1>m2):
     m3=m1-m2
     print('The counted months=',m3)
 else:
     y1=y1-1
     m3=(m1+12)-m2
     print('The counted months=',m3)
 if(y1>y2):
     y3=y1-y2
     print('The counted years=',y3)
 else:
     y3=y1-y2
     print('The counted years=',y3)
 t= ((a/100)*b)
 day=(t/30)
 
 print('The total intrest is =',((day*d3)+(m3*t)+(12*y3*t)))
 print("The total amount with intrest is =",((day*d3)+(m3*t)+(12*y3*t))+a)
