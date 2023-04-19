Ir_a_praia = True

while Ir_a_praia:
    print("Vamos a praia")
    chuva= input("começou a chover ? S|N")
    if chuva == 'S':
        Ir_a_praia = False
        print("Ja era")
        print(Ir_a_praia) 
    else:
        print("Ok")   
