import psycopg2
from classConexao import Conexao

def criarTabelaClientes(conexao):
    conexao.manipularBanco('''
    DROP TABLE IF EXISTS "Clientes" CASCADE;
    CREATE TABLE "Clientes"
    (
    "ID_Cliente" int NOT NULL,
    "Nome"       character varying(50) NOT NULL,
    "Endereço"   character varying(50) NOT NULL,
    "Cpf"        character(50) NOT NULL,
    PRIMARY KEY ( "ID_Cliente" )
    );
   
    ''')

def criarTabelaCompras(conexao):
    conexao.manipularBanco('''
    DROP TABLE IF EXISTS "Compras" CASCADE;
    CREATE TABLE "Compras"
    (
    "ID_Compra"  int NOT NULL,
    "ID_Peça_1"  int NOT NULL,
    "ID_Cliente_1" int NOT NULL,
    "Qtd_Peça"   int NOT NULL,
    PRIMARY KEY ( "ID_Compra" ),
    CONSTRAINT FK_1 FOREIGN KEY ( "ID_Peça_1" ) REFERENCES "Peças" ( "ID_Peça" ),
    CONSTRAINT FK_2 FOREIGN KEY ( "ID_Cliente_1" ) REFERENCES "Clientes" ( "ID_Cliente" )
    ON UPDATE NO ACTION
    ON DELETE CASCADE
    );
    ''')
 
def criarTabelaPeças(conexao):
    conexao.manipularBanco('''
    DROP TABLE IF EXISTS "Peças" CASCADE;
    CREATE TABLE "Peças"
    (
    "ID_Peça"   int NOT NULL,
    "Nome_Peça" character(50) NOT NULL,
    PRIMARY KEY ( "ID_Peça" )
    );
    ''')

def verClientes(conexao):

    clientes = conexao.consultarBanco('''
    Select * FROM "Clientes"
    ORDER BY "ID_Cliente" ASC
    ''')
    print("ID | Nome | Cpf | Endereço")

    for cliente in clientes:

        print(f'{cliente[0]} | {cliente[1]} | {cliente[2]} | {cliente[3]}')

def verCompras(conexao):

    compras = conexao.consultarBanco('''
    Select * FROM "Compras"
    ORDER BY "ID_Compra" ASC
    ''')
    print("ID Compra | ID Peça | ID Cliente | Quantidade |")

    for compra in compras:

        print(f'{compra[0]} | {compra[1]} | {compra[2]} | {compra[3]} |')

def verPeças(conexao):

    peças = conexao.consultarBanco('''
    Select * FROM "Peças" 
    ORDER BY "ID_Peça" ASC
    ''')
    print("ID Peça | Nome Peça | ")

    for peça in peças:

        print(f'{peça[0]} | {peça[1]}|')

def inserirPeça(conexao):
    ID = input("ID da peça: ")
    Nome = input("Nome da peça: ")
    conexao.manipularBanco(f'''
    INSERT INTO "Peças"
    VALUES ('{ID}','{Nome}')
    ''')
    print("Peça adcionada com sucesso!")


def inserirCliente(conexao):
    ID = input("ID do Cliente: ")
    Nome = input("Nome do Cliente: ")
    CPF = input("CPF do Cliente: ")
    Endereço = input("Endereço do Cliente: ")
    conexao.manipularBanco(f'''
    INSERT INTO "Clientes"
    VALUES ('{ID}','{Nome}','{CPF}','{Endereço}')
    ''')
    print("Cliente Adcionado com sucesso!")

def inserirCompra(conexao):
    ID = input("ID da Compra: ")

    peças = conexao.consultarBanco('''
    Select * FROM "Peças" 
    ORDER BY "ID_Peça" ASC
    ''')
    print("ID Peça | Nome Peça |")

    for peça in peças:

        print(f'{peça[0]} | {peça[1]} |')
    
    IDpeça = input("Escolha o ID da peça que deseja comprar: ")

    clientes = conexao.consultarBanco('''
    Select * FROM "Clientes"
    ORDER BY "ID_Cliente" ASC
    ''')
    print("ID | Nome | Cpf | Endereço")

    for cliente in clientes:

        print(f'{cliente[0]} | {cliente[1]} | {cliente[2]} | {cliente[3]}')

    IDcliente = input("Escolha o ID do cliente que fará a compra")
    Qtd = input("Quantidade de peças que deseja: ")

    conexao.manipularBanco(f'''
    INSERT INTO "Compras"
    VALUES ('{ID}','{IDcliente}','{IDpeça}','{Qtd}')
    ''')
    print("Compra Adcionada com sucesso!")

def atualizarClientes(conexao):
    clientes = conexao.consultarBanco('''
    Select * FROM "Clientes"
    ORDER BY "ID_Cliente" ASC
    ''')
    print("ID | Nome | Cpf | Endereço")

    for cliente in clientes:

        print(f'{cliente[0]} | {cliente[1]} | {cliente[2]} | {cliente[3]}')
    
    IDatualizar = input("Escolha o ID do cliente que deseja atualizar: ")
    Novonome = input("digite o novo nome do cliente: ")
    Novocpf = input("digite o novo cpf do cliente: ")
    Novonend = input("digite o novo endereço do cliente: ")
    clienteAtualizado = conexao.manipularBanco(f'''
    UPDATE * FROM "Clientes"
    SET "Nome" = '{Novonome}' , "Cpf" = '{Novocpf}' , "Endereço" = '{Novonend}'
    Where "ID_Cliente" = '{IDatualizar}';
    ''')
    print(f"{clienteAtualizado[0],clienteAtualizado[1],clienteAtualizado[2],clienteAtualizado[3]}")

def deletarClientes(conexao):
    clientes = conexao.consultarBanco('''
    Select * FROM "Clientes"
    ORDER BY "ID_Cliente" ASC
    ''')
    print("ID | Nome | Cpf | Endereço")

    for cliente in clientes:

        print(f'{cliente[0]} | {cliente[1]} | {cliente[2]} | {cliente[3]}')
    
    IDdeletar = input("Escolha o ID do cliente que deseja deletar: ")
    clienteDeletado = conexao.manipularBanco(f'''
    DELETE  FROM "Clientes" CASCADE
    Where "ID_Cliente" = '{IDdeletar}';
    ''')
    print(f"{clienteDeletado[0],clienteDeletado[1],clienteDeletado[2],clienteDeletado[3]}")


try:

    con = Conexao("postgres","localhost","5432","postgres","postgres")
    
    
    criarTabelaClientes(con)
    criarTabelaPeças(con)
    criarTabelaCompras(con)
   
   
    while True:

        print('''Bem vindo a WM MOTORS
        
        Menu:
        1. Ver Clientes
        2. Ver Peças
        3. Ver Compras 
        4. Inserir Cliente
        5. Inserir Peça
        6. Inserir Compra
        7. Atualizar Cliente
        8. Deletar Cliente
        0. Sair
        
        ''')

        opcoes = input("Digite a opção escolhida: ")

        match opcoes:
            case "1":
                verClientes(con)
            case "2":
                verPeças(con)
            case "3":
                verCompras(con)
            case "4":
                inserirCliente(con)
            case "5":
                inserirPeça(con)
            case "6":
                inserirCompra(con)
            case "7":
                atualizarClientes(con)
            case "8":
                deletarClientes(con)
            case "0":
                break
            case _:
                print("Você escolheu uma opção inválida!\n")

        input("Tecle Enter para continuar.")
    con.fechar()


except(Exception, psycopg2.Error) as error:

    print("Ocorreu um erro", error)