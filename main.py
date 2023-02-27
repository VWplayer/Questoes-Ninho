import psycopg2
from classConexao import Conexao


def verClientes(conexao):

    clientes = conexao.consultarBanco('''
    Select * FROM "Clientes"
    ORDER BY "ID_Cliente" ASC
    ''')
    print("ID | Nome | Cpf | Endereço")

    for cliente in clientes:

        print(f'{cliente[0]} | {cliente[1]} | {cliente[2]} | {cliente[3]}')

def verCadastroClientes(conexao):

    cdcs = conexao.consultarBanco('''
    Select * FROM "Cadastro de Clientes"
    ORDER BY "ID_Cadastro" ASC
    ''')
    print("ID Cadasro | ID Cliente | ID Carro")

    for cdc in cdcs:

        print(f'{cdc[0]} | {cdc[1]} | {cdc[2]}')

def verCompras(conexao):

    compras = conexao.consultarBanco('''
    Select * FROM "Compra"
    ORDER BY "ID_Compra" ASC
    ''')
    print("ID Compra | ID Peça | Quantidade | Data |  ")

    for compra in compras:

        print(f'{compra[0]} | {compra[1]} | {compra[2]} | {compra[3]}')

def verPeçasdeCarro(conexao):

    peças = conexao.consultarBanco('''
    Select * FROM "Peças de Carros"
    ORDER BY "ID" ASC
    ''')
    print("ID Peça | Nome Peça | preço Peça | ID Carro")

    for peça in peças:

        print(f'{peça[0]} | {peça[1]} | {peça[2]} | {peça[3]}')

def verPedidos(conexao):

    pedidos = conexao.consultarBanco('''
    Select * FROM "Pedidos"
    ORDER BY "ID_Pedido" ASC
    ''')
    print("ID Pedido | ID Compra | ID Cliente")

    for pedido in pedidos:

        print(f'{pedido[0]} | {pedido[1]} | {pedido[2]} |')

def verModelosdeCarro(conexao):

    MdCs = conexao.consultarBanco('''
    Select * FROM "Modelos de Carros"
    ORDER BY "ID" ASC
    ''')
    print("ID Carro | Nome do Carro | Ano do Carro")

    for MdC in MdCs:

        print(f'{MdC[0]} | {MdC[1]} | {MdC[2]} |')




try:

    con = Conexao("BDATVFINAL","localhost","5432","postgres","postgres")

    while True:

        print('''Bem vindo a WM MOTORS
        
        Menu:
        1. Ver Cadastro de clientes
        2. Ver Clientes
        3. Ver Compras 
        4. Ver pedidos
        5. Ver peças de Carros
        6. Ver Modelos de Carros 
        0. Sair
        
        ''')

        opcoes = input("Digite a opção escolhida: ")

        match opcoes:
            case "1":
                verCadastroClientes(con)
            case "2":
                verClientes(con)
            case "3":
                verCompras(con)
            case "4":
                verPedidos(con)
            case "5":
                verPeçasdeCarro(con)
            case "6":
                verModelosdeCarro(con)
            case "0":
                break
            case _:
                print("Você escolheu uma opção inválida!\n")

        input("Tecle Enter para continuar.")
    con.fechar()


except(Exception, psycopg2.Error) as error:

    print("Ocorreu um erro", error)