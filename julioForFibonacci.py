print ("--"*12)
print (" Definição de Fibonacci" )
print ("--"*12)

quantidade = 1



while (quantidade  != 0): #função usada para parar a operação
    quantidade = int(input("\n\nDefina a Quantidade de numeros que quer ser mostrado:"))
    print ("--"*27)
    num1 = 0
    num2 = 1
    aux = 0
    contador = 0     
    print(aux, end = " ")
   
    for c in range (quantidade - 1):  
       
        num1 = num2
        num2 = aux
        aux = num1 + num2
           
        print(aux, end = " ")
print("\n\n\nA partir de (0),não é possivel mostar, fim da contagem.") 
print ("--"*27)     
    