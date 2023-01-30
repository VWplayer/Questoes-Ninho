import psycopg2

def createTableFuncionario(cursor, conexao):
    cursor.execute('''
    DROP TABLE IF EXISTS "Funcionarios";

    CREATE TABLE "Funcionarios"(
        "ID" int GENERATED ALWAYS AS IDENTITY,
        "Nome" varchar(255) NOT NULL,
        "CPF" char(11),
        "Salario" money,
        "ID_Departamento" int,
        CONSTRAINT fk_departamento
            FOREIGN KEY("ID_Departamento")
            REFERENCES "Departamentos"("ID")
            ON DELETE NO ACTION
            ON UPDATE NO ACTION,

        PRIMARY KEY ("ID")
    );
    ''')
    con.commit()

def inserirFuncionario(cur,conexao):
    i = 1
    while  i <= 3:
        novoNome = input("Insira o nome do novo funcionário: ")

        while True:
            novoCpf = input("Insira o CPF do novo funcionário: ")
            if len(novoCpf) != 11:
                 print("Tamanho inválido, o cpf precisa conter 11 digitos")
            else:
                 break
        
        novoSalario = input("Insira o Salário do novo funcionário: ")
        novoDepartamento = input("Insira o Departamento a qual o funcionario faz parte:")
        cur.execute(f'''
        INSERT INTO "Funcionarios"
        VALUES(default, '{novoNome}', '{novoCpf}', {novoSalario},'{novoDepartamento}')
        ''')
        conexao.commit()
        i = i+1

def createTableDepartamentos(cursor,conexao):
    cursor.execute('''
    DROP TABLE IF EXISTS "Departamentos" CASCADE;
    CREATE TABLE "Departamentos"(

        "ID" int GENERATED ALWAYS AS IDENTITY,
        "Nome" varchar(255) NOT NULL,
        PRIMARY KEY ("ID")
    );
    ''')
    con.commit()


def inserirDepartamento(cur,conexao):
    i = 1
    while  i <= 3:

        novoNome = input("Insira o nome do novo departamento: ")

        cur.execute(f'''
        INSERT INTO "Departamentos"
        VALUES(default, '{novoNome}')
        ''')
        conexao.commit()
        i = i+1
try :
    
    con = psycopg2.connect(database = "Empresa",user = "postgres", password = "postgres", host = "localhost", port = "5432")

    cursor = con.cursor()

    createTableDepartamentos(cursor,con)

    createTableFuncionario(cursor,con)
    inserirDepartamento(cursor,con)
    inserirFuncionario(cursor,con)
    cursor.close()
    con.close()
    

except(Exception, psycopg2.Error) as error:
    print("Ocorreu um erro", error)