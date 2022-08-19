# Avaliação 02 individual
# Autor: Erick Costa

# Quando finalizar a tarefa, salve o arquivo com o seu nome_completo

# Esta avaliação deverá ser individual.
# Competências observadas:
#   - Saber interpretar o que foi solicitado;
#   - Conhecer os comando básicos da linguagem python;
#   - Saber utilizar a estrutura de lista da linguagem;
#   - Desenvolver uma solução viável para o problema proposto


'''
Faça um algoritmo que implemente o menu abaixo.

MENU
1- Cadastrar Login e Senha
2- Aumento de 10%
3- Relatório
4- Cadastrar Funcionário
Escolha:

Para implementar seu código você deverá utilizar
as seguintes listas:
login = []
senha = []
funcionarios = ['Pedro' , 'Ana'   , 'Carlos', 'Maria Clara', 'João Antonio']
salarios     = [ 3470.00,  2200.00,  3970.34,  7450.23     ,  5677.33 ]


Descrição:
Na opção 1 - Você deverá cadastrar login e senha nas listas correspondentes.
             Critério: login não poderá se repetir. Verificar se nome consta
             na lista de funcionarios.

Para executar as opções 2 e 3, você deverá validar seu login e senha

Na opção 2 - Após validar login e senha, seu código deverá aumentar
             o salário dos funcionários em 10%. Mas somente
             se o funcionário ganhar abaixo da média em relação
             a lista de salarios.

Na opção 3 - Após confirmar login e senha, você deverá fazer um
             relatório mostrando o nome e o salario, conforme exemplo:

                 Maria Clara  - 7450.23
                 João Antonio - 5677.33
                 Carlos       - 3970.34
                 Pedro        - 3470.00
                 Ana          - 2200.00

Na opção 4 - Você deverá cadastrar o nome e o salário de um
             novo funcionário.

'''

# Você pode utilizar o código abaixo para iniciar o seu, ou
#   construir o menu como desejar

#Declarando as variaveis utilizadas
from xml.sax.saxutils import prepare_input_source


login = ['erick']
senha = ['temp']
funcionarios = ['Pedro','Ana','Carlos','Maria Clara','João Antonio']
salarios     = [3470.00,2200.00,3970.34,7450.23,5677.33]
soma=0
media=0
iteracao=0
identificacao=0



def cadastro_usuario():
    import getpass
    iteracao=0
    while True:
        usuario = input("Favor insira o Usuario a ser cadastrado: ")        
        
        if usuario in funcionarios:
            print("Usuario ja existente. Favor inserir Usuario a ser cadastrado.")
        
        if usuario in login:
            print("Usuario ja existente. Favor inserir Usuario a ser cadastrado.")
        
        if usuario  not in funcionarios and usuario not in login:
            iteracao=iteracao+1
            login.append(usuario)
            break


    while True:
        pwd = getpass.getpass("Digite sua senha a ser cadastrada")
        pwd2=getpass.getpass("Favor confirme sua senha")
        if pwd==pwd2:
            senha.append(pwd)
            break
        if pwd!=pwd2:
            print("As senhas digitadas não coincidem.")

def verifica_login():
    import getpass
    identificacao = 0
    while True:
        x = input("Login:")
        for t in range(len(login)):
            if x == login[t]:
                while True:
                    y = getpass.getpass("Senha:")
                    if y == senha[t]:
                        identificacao=1
                        break

                    else:
                        print("Senha errada. Favor digite a senha corretamente.")
                        break

        if x not in login:
            print("Usuario nao encontrado")

        if identificacao==1:
            print("Login realizado com sucesso! \n")
            break


while True:
    escolha = input(
        '''
    
        MENU
        1 - Cadastrar Login e Senha
        2 - Aumento de 10%
        3 - Relatório
        4 - Cadastrar Funcionário
        6 - Ver variaveis
        5 - Encerrar o Programa
        Escolha a opção desejada=> '''
    )

    if escolha == '1':
        cadastro_usuario()

    if escolha == '2':
        verifica_login()
        for p in range(len(salarios)):
            soma=soma+salarios[p]
        media=soma/len(salarios)
        print(funcionarios)
        while True:
            entrada=input("Isira o funcionario a receber 10% de aumento caso esteja abaixo da media:")
            for p in range (len(funcionarios)):
                if entrada==funcionarios[p]:
                    if salarios[p]<media:
                        salarios[p]=salarios[p]*1.1
                        print("o Funcionario (a)",funcionarios[p],"recebeu aumento de 10%")
                        iteracao=1

                    if float(salarios[p])>=float(media):
                        print("o Funcionario (a)",funcionarios[p],"já recebe o salário acima da média, portanto nao poderá receber um aumento de 10%")
                        iteracao=1

            if iteracao!=1:
                print("Funcionario nao encontrado")
            break

    if escolha == '3':
        verifica_login()
        print("\n")
        print(f"{'Funcionario':<15}-{'Salário':>10}")
        for i in range (len(funcionarios)):
            print(f"{funcionarios[i]:<15}-{salarios[i]:>10}")


    if escolha == '4':
        verificacao=False
        while True:
            while True:
                cad_user = input("Quantos usuarios deseja cadastrar")
                try:
                    cad_user=int(cad_user)
                    break
                except:
                    print("Entrada inválida. Digite um numero para a quantidade de funcionários a serem inseridos")

            if type(cad_user) is int:
                for r in range (cad_user):
                    while True:
                        user_ent=input("Digite o nome do funcionario a ser inserido")
                        verificacao=False

                        if user_ent in funcionarios:
                            print("Funcionario ja existente.")

                        if user_ent not in funcionarios:
                            funcionarios.append(user_ent)
                            break

                    while verificacao==False:
                        sal_ent = input("Digite o salario a ser cadastrado para o funcionário")

                        try:
                            int (sal_ent)
                            verificacao=True
                            sal_ent=float(sal_ent)
                            salarios.append(sal_ent)

                        except:
                            try:
                                float(sal_ent)
                                verificacao=True
                                salarios.append(sal_ent)
                            except:
                                print("Favor inserir um salario na forma numérica")
            break



    if escolha == '5':
        exit()