X = int (input("Digite a altura:  "))
Y = int (input("\nDigite a altura:  "))
M = int (input("\nDigite quantas peças possui:  "))

for x in range (0, M) : 
    Xi = int(input("\nQual a largura do cliente:  "))
    Yi = int(input("\nQual a altura do cliente:  "))
    if Xi > X:
        print ("Não dá pra fazer")
    elif Yi > Y:
        print ("Não dá pra fazer")
    else:
        print ("Tem como ser feito")
    
    
