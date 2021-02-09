lista_contatos = [['Clara','1091982','Namorada','9994243999'],
            ['Samara','1091982','Otaka','999992423499'],
            ['Diego','1091982','MonoAnivia','992312399'],
            ['Avelar','1091982','Avelindo','9999131999'],
            ['Vitória','1091982','Perturbada','9999131999']
            ]

def criaContato():
    nome = str(input('Digite o nome a ser inserido: '))
    codigo = str(input('Digite o codigo da pessoa: '))
    cargo = str(input('Digite o cargo da pessoa, Namorada só se o nome for Clara: '))
    telefone = str(input('Digite o telefone da pessoa: '))

    if nome == '' or codigo == '' or cargo == '' or telefone == '':
        print('Erro, todas as informções precisam ser preenchidas!')
        return False

    else:
        contato = [nome, codigo, cargo, telefone]
        lista_contatos.append(contato)
        return True


def buscaContato():
    cargo = str(input('Digite o cargo a ser buscado:'))
    resultado = list()
    for contato in lista_contatos:
        if contato[2] == cargo:
            resultado.append(contato)
    if len(resultado) == 0:
        print('Não foram encontrados resultados com o que foi pesquisado')
    else:
        print(resultado)
        return True

        
    return None



def main():
    print('=-'*20)
    print('1 - Criar um Contato')
    print('2 - Buscar um Contato Pelo Cargo')
    opc = int(input('O que deseja fazer ?: '))
    if opc > 2 or opc == 0:
        print('Erro, essa opção não existe!')
    else:
        if opc == 1:
            criaContato()
        elif opc == 2:
            buscaContato()
    
main()
    

