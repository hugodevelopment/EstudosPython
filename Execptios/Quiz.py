try:
    print(1)
    print(20/0)
    print(2)
except ZeroDivisionError:
    print(3)
finally:
    print(4) 


print()


x = 3
try: 
  x+="2"
except:
  x+=2
else:
  x+=4
finally:
  print(x)