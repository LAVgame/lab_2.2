print("Введите число |c|< 9 ")
c = int(input())
while abs(c) > 9: 
    print("Введите число по правилу |c|< 9 ")
    c = int(input())

if c == 0:
    print("Ноль")
else:
    if c > 0 :
     print("Плюс")
    else:
     print("Минус")

if abs(c) ==1:
    print("Один")
elif abs(c) ==2:
    print("Два")
elif abs(c) ==3:
    print("Три")
elif abs(c) ==4:
    print("Четыре")
elif abs(c) ==5:
    print("Пять")
elif abs(c) ==6:
     print("Шесть")
elif abs(c) ==7:
    print("Семь")
elif abs(c) == 8:
    print("Восемь")
elif abs(c) ==9:
    print("Девять")
    
    
    
    
    
    
    
   
    
    
    