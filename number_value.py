while(1):

  print '0: 정수의 절댓값 구하기 /n 1: 배수 알기 /n 2: 사각형의 둘레와 넓이 구하기 /n 3:끝내기 /n/n숫자를 입력하세요'
  menu = input()

  if(menu==0):
   print '정수를 입력하세요'
   a=input()
   b=abs(a)
   print b
  
  else if(menu==1):
    print '정수1을 입력하세요'
    n1=input()
    print '정수2을 입력하세요'
    n2=input
  
    if(n1>n2):
      rest=n1%n2
    else:
      rest=n2%n1
  
   if(rest!=0):
     print '두 수 중 큰 수는 작은 수의 배수가 아닙니다.'
     
    else:
      print '두 수 중 큰 수는 작은 수의 배수 입니다.'
    
  else if(menu==2):
      print '점1의 x좌표와 y좌표를 입력해주세요.'
      x1=input()
      y1=input()
      
      print '점2의 x좌표와 y좌표를 입력해주세요.'
      x2=input()
      y2=input()
      
      if(x1>x2):
        length=x1-x2
      else:
        length=x2-x1
        
      if(y1>y2):
        width=y1-y2
       else:
        width=y2-y1
        
      print '둘레:' , 2*length + 2*width
      print '넓이:' , length*width
  
  else if(menu==3):
    break
    
  else:
    print '0,1,2 중 골라주세요'
