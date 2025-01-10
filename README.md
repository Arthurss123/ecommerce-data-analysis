# Análise de E-commerce com PostgreSQL

## Descrição do Projeto

Este projeto tem como objetivo simular um e-commerce, utilizando um banco de dados PostgreSQL, e realizar análises sobre o comportamento de vendas, clientes e produtos. O projeto foi desenvolvido com o propósito de colocar em prática conceitos de análise de dados e SQL, além de proporcionar uma oportunidade de aprendizado prático ao manipular dados reais e gerar insights sobre o negócio.

### Principais Funcionalidades

- **Geração de Dados Fictícios**: Utilizando a biblioteca `Faker`, foram gerados dados simulados de clientes, produtos e pedidos.
- **Análises Realizadas**:
  - Produtos mais vendidos.
  - Clientes mais fiéis (com maior número de pedidos).
  - Análise da sazonalidade das vendas ao longo do ano.

### Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para interagir com o banco de dados, gerar dados e realizar as análises.
- **PostgreSQL**: Banco de dados relacional utilizado para armazenar e manipular os dados.
- **pandas**: Biblioteca Python para manipulação de dados e execução das consultas SQL diretamente no código.
- **Faker**: Biblioteca Python para geração de dados fictícios (clientes, produtos, etc.).
- **psycopg2**: Conector Python utilizado para conectar o código ao banco de dados PostgreSQL.

## Objetivos das Análises

### 1. **Produtos Mais Vendidos**


**Consulta SQL**:
```sql
SELECT p.nome_produto, SUM(pe.quantidade) AS total_vendido
FROM pedido pe
JOIN produto p ON pe.produto_id = p.produto_id
GROUP BY p.nome_produto
ORDER BY total_vendido DESC
LIMIT 50;
```

Essa consulta retorna os 50 produtos mais vendidos, classificando-os pela quantidade total vendida. Com os dados gerados, você pode obter uma visão clara dos produtos que mais atraem os clientes

### 2 Clientes mais fiéis

``` SQL
SELECT c.nome, COUNT(pe.pedido_id) AS total_pedidos
FROM pedido pe
JOIN cliente c ON pe.cliente_id = c.cliente_id
GROUP BY c.nome
ORDER BY total_pedidos DESC
LIMIT 5;
```
Esta consulta retorna os 5 clientes que mais fizeram pedidos, ajudando a entender os perfis de clientes com maior engajamento.

### 3 Sazonalidade das Vendas

``` SQL
SELECT EXTRACT(MONTH FROM data_pedido) AS mes, SUM(quantidade) AS total_vendas
FROM pedido
GROUP BY mes
ORDER BY mes;
```
Essa consulta retorna a soma das quantidades vendidas por mês, permitindo visualizar como as vendas variam ao longo do ano.


### Insights Possíveis

> - Produtos mais vendidos: Ao identificar os produtos mais vendidos, a empresa pode focar em estratégias de estoque para garantir que esses produtos estejam sempre disponíveis. Além disso, promoções voltadas para esses produtos podem aumentar ainda mais as vendas.

> - Clientes mais fiéis: Conhecer os clientes mais fiéis pode ajudar a direcionar campanhas de marketing segmentadas, oferecendo benefícios exclusivos para aumentar ainda mais a lealdade.

> - Sazonalidade: A análise de sazonalidade ajuda a prever quais meses terão maior demanda, permitindo uma melhor preparação de estoque e ações promocionais durante os períodos de pico.

# Conclusão

Esse projeto foi uma oportunidade para aplicar conceitos de SQL e análise de dados em um cenário simulado, utilizando dados ficticios e proporcionando uma visão prática de como obter insights valiosos de um e-commerce. 