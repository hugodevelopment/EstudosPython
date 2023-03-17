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
  print(x)
else:
  print("oi")
  x+=4
finally:
  print(x)


print()

x = 10
try:
  x+=3
  raise ValueError
except NameError:
  x+=1
except ValueError:
  x+=1
else:
  x+=1
finally:
  x+=1

print(x)


try:
    name = input()
    if len(name) < 4:
        raise ValueError
except:
    print("Invalid Name")
else:
    print("Account Created") 