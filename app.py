import psycopg2

conexao = psycopg2.connect(host ="localhost", database="bancodados", 
                           user= "bancodados", password = "bancodados")

cursor = conexao.cursor()

# sql = 'create table cidade (id serial primary key, nome varchar(50), uf varchar(2));'

# cursor.execute(sql)

# insert = "insert into cidade(nome, uf) values ('Paranagua', 'PR');"

# cursor.execute(insert)

select = 'select * from cidade'

print(cursor.execute(select))

cidades = cursor.fetchall()

for row in cidades:
    print("Id = ", row[0])
    print("Nome = ", row[1])
    print("UF = ", row[2])


