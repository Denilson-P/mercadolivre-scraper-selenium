# Mercadolivre Scraper (Selenium)

Script de **web scraping automatizado** que coleta informações de notebooks no Mercado Livre utilizando **Selenium** e organiza os dados em um arquivo CSV para análise.

O projeto simula a navegação de um usuário real, percorrendo múltiplas páginas de resultados e extraindo dados relevantes dos produtos.

---

# Funcionalidades

* Coleta automática de produtos (notebooks)
* Navegação entre páginas (paginação)
* Evita duplicidade de produtos
* Extração de dados como:

  * Título
  * Preço
  * Avaliação
  * Quantidade de reviews
  * Informações de frete
  * Link do produto
* Exportação dos dados para CSV
* Tratamento de elementos opcionais

---

# Tecnologias utilizadas

* Python
* Selenium
* Pandas

---

# Estrutura do projeto

```
.
├── data/
│   └── tabela.csv
├── scraper/
│   └── scraper.py
├── main.py
└── requirements.txt
```

---

# Como executar

```bash

git clone https://github.com/SEU-USUARIO/mercadolivre-scraper-selenium.git


cd mercadolivre-scraper-selenium


python -m venv env


env\Scripts\activate  


pip install -r requirements.txt


python main.py
```

---

# Saída

Os dados coletados são salvos em:

```
data/tabela.csv
```

---

# Objetivo do projeto

Este projeto foi desenvolvido com foco em:

* Prática de **web scraping com Selenium**
* Manipulação de dados com **Pandas**
* Simulação de comportamento real de navegação
* Organização de dados para análise

---

# Observações

* O scraping depende da estrutura HTML do site, podendo quebrar caso haja alterações
* Uso apenas para fins educacionais
