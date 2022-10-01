from ast import Break
import math
from pickle import TRUE

def formatacao() :
    print("===" * 10)


def operacao():
    print("""   ____           _                  _               _                        
  / ___|   __ _  | |   ___   _   _  | |   __ _    __| |   ___    _ __    __ _ 
 | |      / _` | | |  / __| | | | | | |  / _` |  / _` |  / _ \  | '__|  / _` |
 | |___  | (_| | | | | (__  | |_| | | | | (_| | | (_| | | (_) | | |    | (_| |
  \____|  \__,_| |_|  \___|  \__,_| |_|  \__,_|  \__,_|  \___/  |_|     \__,_|
                                                                              """)
    soma = (print("1. Soma"))
    print("---" * 10)
    sub = print("2. Subtração")
    print("---" * 10)
    multi = (print("3. Multiplicação"))
    print("---" * 10)
    divi = print("4. Divisão")
    print("---" * 10)
    raiz = print("5. Raiz")
    print("---" * 10)


def soma () :
    a = float(input("Digite o Primeiro Valor: "))
    formatacao()
    b = float(input("Digite o Segundo valor: "))
    formatacao()
    c = a + b
    return c


def sub() :
    a = float(input("Digite o Primeiro Valor: "))
    formatacao()
    b = float(input("Digite o Segundo valor: "))
    formatacao()
    c = a - b 
    return c


def multi () :
    a = float(input("Digite o Primeiro Valor: "))
    formatacao()
    b = float(input("Digite o Segundo valor: "))
    formatacao()
    c = a * b 
    return c


def divi () :
    a = float(input("Digite o Primeiro Valor: "))
    formatacao()
    b = float(input("Digite o Segundo valor: "))
    formatacao()
    c = a / b 
    return c


def raiz () :
    a = float(input("Digite Valor: "))
    formatacao()
    c = math.sqrt(a)
    return c   




while True:
    operacao()
    formatacao()
    entrada = input("Digite a operaçao: ")

    if entrada.upper() == "1" :
        formatacao()
        print(f"O Resultado da soma : {soma()}")
        formatacao()

    elif entrada == "2" :
        formatacao()
        print(f"O Resultado da subtração: {sub()}")
        formatacao()

    elif entrada == "3" :
        formatacao()
        print(f"O Resultado da multiplicação: {multi()}")
        formatacao()

    elif entrada == "4" :
        formatacao()
        print(f"O Resultado da Divisão {divi()}")
        formatacao()

    elif entrada == "5" :
        formatacao()
        print(f"A Raiz é {raiz()}")
        formatacao()

    else :
        print("Você é lesado ? ")


    e2 = (input("Deseja Continuar? \n 1.Sim / 2.Não: "))

    if e2 == "2" :
        print('PROGRAMA ENCERRADO COM SUCESSO...')
        break

    elif e2 == "1" :
        pass

    else:
        print("NÃOOOOOOOO")
        break
            
  
        
    
    

    