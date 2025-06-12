import mysql.connector
import csv
import requests
import matplotlib.pyplot as plt

db_params = {
    'database': 'RICHARD',
    'user': 'RICHARD',
    'password': '123',
    'host': '191.252.109.103',
    'port': '3306'
}

def run():

    conn = mysql.connector.connect(**db_params)
    cur = conn.cursor()

    # Tabela de cidades de CE
    cur.execute("""
    CREATE TABLE IF NOT EXISTS cidades_ce (
        id INT PRIMARY KEY,
        nome VARCHAR(100),
        numero_habitantes INT,
        distancia_capital FLOAT,
        ano_emancipacao INT
    )
    """)
    conn.commit()

    csv_file_url = 'https://vps9431.publiccloud.com.br/home_publico/cidades_RICHARD.csv'
    resposta = requests.get(csv_file_url)
    resposta.encoding = 'utf-8'
    reader = csv.reader(resposta.text.splitlines(), delimiter=";")
    next(reader)

    linhas_inseridas = 0
    linhas_ignoradas = 0

    for row in reader:
        if len(row) == 5:
            try:
                cur.execute("""
                    INSERT INTO cidades_ce (id, nome, numero_habitantes, distancia_capital, ano_emancipacao)
                    VALUES (%s, %s, %s, %s, %s)
                """, (int(row[0]), row[1], int(row[2]), float(row[3]), int(row[4])))
                linhas_inseridas += 1
            except Exception as e:
                print(f"Erro ao inserir linha {row}: {e}")
                linhas_ignoradas += 1
        else:
            print(f"Linha com dados insuficientes: {row}")
            linhas_ignoradas += 1

    conn.commit()

    print(f"\n✅ Inserção finalizada: {linhas_inseridas} linhas inseridas com sucesso.")
    if linhas_ignoradas:
        print(f"⚠️ {linhas_ignoradas} linhas ignoradas por erro ou dados incompletos.")


    # Tabela de cidades de SP
    cur.execute("""
    CREATE TABLE IF NOT EXISTS cidades_sp (
        id INT PRIMARY KEY,
        nome VARCHAR(100),
        numero_habitantes INT,
        distancia_capital FLOAT,
        ano_emancipacao INT
    )
    """)
    conn.commit()

    csv_file_url = 'https://vps9431.publiccloud.com.br/home_publico/cidades_EDUARDO.csv'
    resposta = requests.get(csv_file_url)
    resposta.encoding = 'utf-8'
    reader = csv.reader(resposta.text.splitlines())
    next(reader)

    linhas_inseridas = 0
    linhas_ignoradas = 0

    for row in reader:
        if len(row) == 5:
            try:
                cur.execute("""
                    INSERT INTO cidades_sp (id, nome, numero_habitantes, distancia_capital, ano_emancipacao)
                    VALUES (%s, %s, %s, %s, %s)
                """, (int(row[0]), row[1], int(row[2]), float(row[3]), int(row[4])))
                linhas_inseridas += 1
            except Exception as e:
                print(f"Erro ao inserir linha {row}: {e}")
                linhas_ignoradas += 1
        else:
            print(f"Linha com dados insuficientes: {row}")
            linhas_ignoradas += 1

    conn.commit()

    print(f"\n✅ Inserção finalizada: {linhas_inseridas} linhas inseridas com sucesso.")
    if linhas_ignoradas:
        print(f"⚠️ {linhas_ignoradas} linhas ignoradas por erro ou dados incompletos.")


    # Tabela de cidades de SP
    cur.execute("""
    CREATE TABLE IF NOT EXISTS cidades_ba (
        id INT PRIMARY KEY,
        nome VARCHAR(100),
        numero_habitantes INT,
        distancia_capital FLOAT,
        ano_emancipacao INT
    )
    """)
    conn.commit()

    csv_file_url = 'https://vps9431.publiccloud.com.br/home_publico/cidades_ANA.csv'
    resposta = requests.get(csv_file_url)
    resposta.encoding = 'utf-8'
    reader = csv.reader(resposta.text.splitlines())
    next(reader)

    linhas_inseridas = 0
    linhas_ignoradas = 0

    for row in reader:
        if len(row) == 5:
            try:
                cur.execute("""
                    INSERT INTO cidades_ba (id, nome, numero_habitantes, distancia_capital, ano_emancipacao)
                    VALUES (%s, %s, %s, %s, %s)
                """, (int(row[0]), row[1], int(row[2]), float(row[3]), int(row[4])))
                linhas_inseridas += 1
            except Exception as e:
                print(f"Erro ao inserir linha {row}: {e}")
                linhas_ignoradas += 1
        else:
            print(f"Linha com dados insuficientes: {row}")
            linhas_ignoradas += 1

    conn.commit()
    cur.close()
    conn.close()

    print(f"\n✅ Inserção finalizada: {linhas_inseridas} linhas inseridas com sucesso.")
    if linhas_ignoradas:
        print(f"⚠️ {linhas_ignoradas} linhas ignoradas por erro ou dados incompletos.")
         

if __name__ == "__main__":
    run()


conn = mysql.connector.connect(**db_params)
cur = conn.cursor()

def pegar_top10_populacao(nome_tabela):
    cur.execute(f"""
        SELECT nome, numero_habitantes 
        FROM {nome_tabela} 
        ORDER BY numero_habitantes DESC 
        LIMIT 10
    """)
    return cur.fetchall()

top10_ce = pegar_top10_populacao('cidades_ce')
top10_sp = pegar_top10_populacao('cidades_sp')
top10_ba = pegar_top10_populacao('cidades_ba')

cur.close()
conn.close()

nomes_ce, pop_ce = zip(*top10_ce)
nomes_sp, pop_sp = zip(*top10_sp)
nomes_ba, pop_ba = zip(*top10_ba)

fig, axes = plt.subplots(3, 1, figsize=(12, 18))

# Gráfico Ceará
axes[0].barh(nomes_ce, pop_ce, color='blue')
axes[0].set_title('Top 10 Cidades por População - Ceará')
axes[0].invert_yaxis()
axes[0].set_xlabel('Número de Habitantes')

# Gráfico São Paulo
axes[1].barh(nomes_sp, pop_sp, color='green')
axes[1].set_title('Top 10 Cidades por População - São Paulo')
axes[1].invert_yaxis()
axes[1].set_xlabel('Número de Habitantes')

# Gráfico Bahia
axes[2].barh(nomes_ba, pop_ba, color='orange')
axes[2].set_title('Top 10 Cidades por População - Bahia')
axes[2].invert_yaxis()
axes[2].set_xlabel('Número de Habitantes')

plt.tight_layout()
plt.show()
