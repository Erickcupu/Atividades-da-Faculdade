# Tarefa 03 - Lógica de programação
# Seu nome Aqui: Erick Melonio da Costa.

# Competências a serem avaliadas:
# - Saber interpretar corretamente o que foi pedido;
# - Desenvolver uma solução viável para o problema proposto;
# - Saber utilizar os comandos/funções vistos durante o semestre;
# - Saber utilizar listas.


"""
Problema:
---------
    Um vendedor necessita de um algoritmo que calcule o preço total devido por
um cliente em compras. O algoritmo deve ler o nome do cliente, o código de um
produto e a quantidade comprada de cada item. Calcular o preço total por item.

    Quando o código digitado for 'fim' deve encerrar o programa e
mostrar o total a ser pago de todos itens digitados.

TABELA DE PRODUTOS E PREÇOS
Código do Produto - Preço unitário
            1001  - 5.32
            1324  - 6.45
            6548  - 2.37
            2987  - 5.32
            7623  - 6.45

EXEMPLO: Ao ser digitado 'fim' mostrar o resumo das compras:
----------------------------------------
Nome: Pedro
Produto - Qtd.  -      Preço
   1001  -  2   -      10.64
   2987  -  1   -       5.32
   6548  -  3   -       7.11
   Total:              23.07

"""

lista_produtos = ['1001', '1324', '6548', '2987', '7623'] #lista de produtos (Estoque)
lista_preços =   [ 5.32 ,  6.45 ,  2.37 ,  5.32 ,  6.45 ] #Lista de preços dos produtos em estoque

lista_qtde=      [0,0,0,0,0] #Lista que armazena a quantidade de produtos comprados

def ler_produtos():
    
    while True:
        produto=input("Insita o codido do produto a ser comprado:")
        
        #Se o codigo digitado estiver contido na lista de estoque
        if produto in lista_produtos:

            #Variavel que localiza o indice do codigo na lista te estoque
            indice=lista_produtos.index(produto)
            
            #Laço para validar a quantidade e registrar na lista de quantidades da compra do cliente
            while True:
                try:
                    qtde=int(input("Insira a quantidade:"))
                    break
                
                except:
                    ValueError
                    print("Digite um valor em numeros inteiros")

            lista_qtde[indice]=lista_qtde[indice]+qtde
            
            print("Produto registrado com Sucesso!")
        
        if produto=="fim":
            break

        if produto not in lista_produtos:
            print("Produto não encontrado. Favor insira um produto válido !")


def relatorio():
    #Linhas de codigo abaixo imprimem o cabeçalho do relatorio formatado
    print("-"*50)
    print('{:^50}'.format('RELATORIO DE VENDAS'))
    print("-"*50,end='\n')
    print("Cliente: ",cliente)
    print("-"*50)
    print(f"{'Produto':<10}{'-':^5}{'Quantidade':^15}{'-':^5}{'Valor Unitário':>10}")
    print("-"*50)

    
    total=0
    for i in range(len(lista_qtde)):
    
        #Esta condição itera somente se o cliente estiver comprando pelo menos 1 item do produto
        if lista_qtde[i]!=0:

            #itera somando ao valor total da compra o valor de cada item comprado
            total=round(total+(lista_qtde[i]*lista_preços[i]),2)
            print(f"{lista_produtos[i]:<15}{round(lista_qtde[i],2):^15}{'R$ '+str(round(lista_qtde[i]*lista_preços[i],2)):>19}")
    total=round(total,2)
    total="R$ "+str(total)

    #Linhas de comando que fazem o Valor Total ser impresso em Negrito. 
    print("",'\033[1m')
    print('{:<23}'.format("Valor Total"),'{:>25}'.format(total),'\033[0m')
    print("-"*50,"\n")

while True:
    cliente=input("Favor insira o nome do Cliente: ")
    ler_produtos()
    relatorio()
    print("iniciar outra compra ?")
    x=input("Sim ou Não => ").lower()
    if x=="sim":
        continue
    else:
        exit()