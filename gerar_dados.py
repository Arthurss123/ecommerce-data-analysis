import random
import os
from faker import Faker
import psycopg2
from dotenv import load_dotenv


load_dotenv()
fake = Faker()

# Conectar ao banco de dados
conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    options="-c client_encoding=UTF8"
)

cursor = conn.cursor()

def limpar_dados():
    # Limpa os dados existentes nas tabelas
    cursor.execute("TRUNCATE cliente, produto, pedido RESTART IDENTITY CASCADE;")
    conn.commit()
    print("Dados antigos apagados com sucesso!")

def gerar_dados():
    # Gerar 300 clientes
    for _ in range(300):
        cursor.execute(
            "INSERT INTO cliente (nome, email, cidade, data_registro) VALUES (%s, %s, %s, %s)",
            (fake.name(), fake.email(), fake.city(), fake.date_between(start_date="-2y", end_date="today"))
        )

    # Lista com nomes reais de produtos
    produtos_reais = [
        "Smartphone", "Camiseta", "Notebook", "Fones de ouvido", "Cadeira Gamer", 
        "Livro de Programação", "Câmera Digital", "Relógio Inteligente", "Tênis Esportivo", "Impressora"
    ]

    # Gerar 100 produtos com nomes reais
    for _ in range(100):
        cursor.execute(
            "INSERT INTO produto (nome_produto, categoria, preco) VALUES (%s, %s, %s)",
            (random.choice(produtos_reais), random.choice(["Eletrônicos", "Roupas", "Livros", "Brinquedos"]), round(random.uniform(10.0, 500.0), 2))
        )

    # Gerar 1000 pedidos
    for _ in range(1000):
        cursor.execute(
            "INSERT INTO pedido (cliente_id, produto_id, quantidade, data_pedido) VALUES (%s, %s, %s, %s)",
            (
                random.randint(1, 300),  # Referência ao cliente_id (300 clientes)
                random.randint(1, 100),  # Referência ao produto_id (100 produtos)
                random.randint(1, 5),    # Quantidade do produto
                fake.date_between(start_date="-1y", end_date="today")  # Data do pedido
            )
        )
    
    conn.commit()
    print("Novos dados inseridos com sucesso!")

# Apagar dados antigos e gerar novos
limpar_dados()
gerar_dados()

# Fechar a conexão com o banco de dados
cursor.close()
conn.close()
