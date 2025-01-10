import pandas as pd
from dotenv import load_dotenv
import psycopg2
import os


load_dotenv()

conn = psycopg2.connect(
  dbname=os.getenv("DB_NAME"),
  user=os.getenv("DB_USER"),
  password=os.getenv("DB_PASSWORD"),
  host=os.getenv("DB_HOST"),
  port=os.getenv("DB_PORT"),
  options="-c client_encoding=UTF8"
)

#produtos mais vendidos

query_produtos_vendidos = """

  SELECT p.nome_produto, SUM(pe.quantidade) AS total_vendido
  FROM pedido pe
  JOIN produto p ON pe.produto_id = p.produto_id
  GROUP BY p.nome_produto
  ORDER BY total_vendido DESC
  LIMIT 50
"""

produtos_vendidos = pd.read_sql(query_produtos_vendidos, conn)
print(produtos_vendidos)

query_produtos_vendidos = """
    SELECT p.nome_produto, SUM(pe.quantidade) AS total_vendido
    FROM pedido pe
    JOIN produto p ON pe.produto_id = p.produto_id
    GROUP BY p.nome_produto
    ORDER BY total_vendido DESC
    LIMIT 5;
"""
produtos_vendidos = pd.read_sql(query_produtos_vendidos, conn)
print(produtos_vendidos)

query_clientes_fieis = """
    SELECT c.nome, COUNT(pe.pedido_id) AS total_pedidos
    FROM pedido pe
    JOIN cliente c ON pe.cliente_id = c.cliente_id
    GROUP BY c.nome
    ORDER BY total_pedidos DESC
    LIMIT 5;
"""
clientes_fieis = pd.read_sql(query_clientes_fieis, conn)
print(clientes_fieis)

query_sazonalidade = """
    SELECT EXTRACT(MONTH FROM data_pedido) AS mes, SUM(quantidade) AS total_vendas
    FROM pedido
    GROUP BY mes
    ORDER BY mes;
"""
sazonalidade = pd.read_sql(query_sazonalidade, conn)
print(sazonalidade)

conn.close()