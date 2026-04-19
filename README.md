# Web Scraper e Análise de Dados - Mercado Livre

Projeto de automação desenvolvido em Python para coleta de dados de notebooks no Mercado Livre, seguido de tratamento, análise e geração de relatório em Excel.

## Descrição

O projeto realiza um pipeline completo de dados:

* Coleta automatizada de produtos utilizando Selenium
* Extração de informações relevantes dos anúncios
* Limpeza e tratamento dos dados com Pandas
* Análise de preços e agrupamento por marca
* Geração de relatório estruturado em Excel

## Funcionalidades

* Scraping de produtos diretamente do site
* Coleta dos seguintes campos:

  * Título do produto
  * Preço
  * Avaliação
  * Quantidade de avaliações
  * Frete
  * Link do produto
* Tratamento de dados:

  * Conversão de preços para formato numérico
  * Remoção de valores inválidos
  * Identificação de marca a partir do título
* Análises realizadas:

  * Ordenação por preço
  * Cálculo de preço médio
  * Identificação do produto mais barato e mais caro
  * Filtro de produtos acima de um valor mínimo
  * Análise de preços por marca (média, mínimo, máximo e quantidade)
* Geração de relatório em Excel com múltiplas abas

## Estrutura do Projeto

projeto/
│
├── scraper/         # Lógica de coleta de dados com Selenium
├── analysis/        # Tratamento e análise dos dados
├── data/            # Armazenamento dos dados brutos (CSV)
├── reports/         # Relatórios gerados (Excel)
├── main.py          # Arquivo principal de execução

## Tecnologias Utilizadas

* Python
* Selenium
* Pandas
* OpenPyXL

## Como Executar

1. Clonar o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git

2. Acessar o diretório do projeto:

cd seu-repositorio

3. Criar e ativar ambiente virtual:

python -m venv env
env\Scripts\activate  (Windows)

4. Instalar dependências:

pip install -r requirements.txt

5. Executar o projeto:

python main.py

## Saída

Após a execução:

* Um arquivo CSV será gerado em `data/df.csv`
* Um relatório Excel será gerado em `reports/notebooks_report.xlsx`

O relatório contém:

* Dados tratados
* Ranking de preços
* Produtos filtrados por faixa de preço
* Análise por marca
* Resumo com métricas principais

## Observações

* O site pode sofrer alterações de layout, o que pode impactar os seletores utilizados no scraping
* O projeto inclui tratamento de exceções para lidar com elementos ausentes
* Pequenos delays podem ser utilizados para evitar bloqueios durante a coleta

## Objetivo

Este projeto foi desenvolvido com foco em prática de automação, coleta de dados e análise, simulando um fluxo real utilizado em aplicações de dados no mercado.
