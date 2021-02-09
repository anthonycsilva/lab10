#tratar entradas, (opc, a,b,c):

def mostraEntrada(a,b,c):
    print(f'Primeiro Valor: {a}')
    print(f'Segundo Valor: {b}')
    print(f'Terceiro Valor: {c}')
def calcularTrapezio(a,b,c):
    mostraEntrada(a,b,c)
    #a = b
    #b = B
    #c = h
    area = ((a+b)*c)/2
    return area
def mult(a,b,c):
    mostraEntrada(a,b,c)
    return a*a,b*b,c*c
def media(a,b,c):
    mostraEntrada(a,b,c)
    return (a+b+c)/3
def main():
    print('1 - Calculando a Area do Trapézio')
    print('2 - Calculando os Multiplos!')
    print('3 - Calculando a Média')
    print('4 - Em construção')
    print('=-'*20)


    opc = int(input('Digite a Opção Desejada: ')) 
    a = int(input('Digite o Primeiro Numero:'))
    b = int(input('Digite o Segundo Numero:'))
    c = int(input('Digite o Terceiro Numero:'))
    print('=-'*20)

    if(a<b):
        print('Erro')
    elif opc == 1:
            print(f'Calculando a Area do Trapézio!')
            print(calcularTrapezio(a,b,c))
    elif opc == 2:
        print(f'Calculando os Multiplos!')
        print(mult(a,b,c))
    elif opc == 3:
        print(f'Calculando a Média')
        print(media(a,b,c))
    
    return None


main()