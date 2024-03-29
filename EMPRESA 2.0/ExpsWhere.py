# Símbolos e sintaxe básica do Where: https://www.w3schools.com/sql/sql_where.asp
# Conectores do Where: https://www.w3schools.com/sql/sql_and_or.asp
# Como utilizar o Where: https://www.devmedia.com.br/sql-clausula-where/37645

if __name__ == "__main__":
    import psycopg2
    from classConexao import Conexao

    try:
        con = Conexao(parametroDb="Empresa", parametroHost="localhost", parametroPort="5432", parametroUser="postgres", parametroPassword="postgres")

        # Consulta básica, pega todos
        # funcionarios = con.consultarBanco('''
        # Select * FROM "Funcionarios"
        # ORDER BY "ID" ASC
        # ''')

        # for funcionario in funcionarios:
        #     print(f'''
        #     {funcionario[0]} - {funcionario[1]} - {funcionario[2]} - {funcionario[3]}
        #     ''')

        #Consulta Operador =, usando o ID

        # funcEscolhido = input("Escolha o ID do funcionario que deseja consultar")
        # funcionario = con.consultarBanco(f'''
        # SELECT * FROM "Funcionarios"
        # WHERE "ID" = '{funcEscolhido}'
        # ''')

        # print(funcionario)

        #Consulta Operador =, usando o Nome

        # nomePesquisa = input("Digite o nome do Funcionário: ")
        # funcionario = con.consultarBanco(f'''
        # SELECT * FROM "Funcionarios"
        # WHERE "Nome" = '{nomePesquisa}'
        # ''')
    
        # Consulta Operador=, Usando o Salario

        # salarioPesquisa = input("Digite o Salario que deseja consultar")
        # funcionario = con.consultarBanco(f'''
        # SELECT * FROM "Funcionarios"
        # WHERE "Salario" = '{salarioPesquisa}'
        # ''')
        # print(funcionario)




    
    except(Exception, psycopg2.Error) as error:
        print("Ocorreu um erro", error)