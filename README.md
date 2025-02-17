# Web Scraping com Python
## Coletando dados de Fundos de Investimentos Imobiliários do Portal [Fundadamentus](https://www.fundamentus.com.br/)

![Badge de Status](https://img.shields.io/badge/status-em%20desenvolvimento-orange)
![Licença](https://img.shields.io/github/license/usuario/repo)
![Contribuições](https://img.shields.io/badge/contribui%C3%A7%C3%B5es-bem%20vindas-brightgreen)

Este projeto é uma aplicação escrita na linguagem Python, que realiza coleta de dados fundamentalista do portal [Fundadamentus](https://www.fundamentus.com.br/) de Fundos de Investimentos Imiboliário - FII, utilizando técnica de **[web scraping](https://pt.wikipedia.org/wiki/Web_scraping)**. Objetivo desse Projeto é automatizar a coleta de dados de FII's, para geraçao de relatórios para análise desse tipo de ativo. 

## 📌 Índice

- [Sobre](https://github.com/MaercioMamedes/web_scraping_fundamentus_fii?tab=readme-ov-file#-sobre)
- [Tecnologias](https://github.com/MaercioMamedes/web_scraping_fundamentus_fii?tab=readme-ov-file#-tecnologias)
- [Instalação](https://github.com/MaercioMamedes/web_scraping_fundamentus_fii?tab=readme-ov-file#-instala%C3%A7%C3%A3o)
- [Uso](#uso)
- [Contribuição](#contribui%C3%A7%C3%A3o)
- [Licença](#licen%C3%A7a)
- [Contato](#contato)

## 📖 Sobre

A automatização na coleta de dados é crucial para garantir eficiência e precisão na obtenção de grandes volumes de informações. O web scraping é uma técnica que permite extrair dados de websites de maneira automatizada, facilitando o acesso a informações que seriam difíceis de compilar manualmente. coletar os dados de forma estruturados da página, é possível gerar relatórios detalhados a partir de arquivos CSV, o que proporciona uma análise mais rápida e precisa, auxiliando na tomada de decisões e no monitoramento de tendências dos ativos.


## 🛠 Tecnologias

Principais Tecnologias Utilizadas

- Python
- Pandas
- Selenium
  
## 🚀 Instalação

Para instalar e executar a aplicação, certifique-se que o interpretador Python esteja instalado na máquina, na versão 3.12 ou superior.

1. Clone o repositório:
   ```sh
   git clone https://github.com/MaercioMamedes/web_scraping_fundamentus_fii.git
   ```
2. Acesse o diretório do projeto:
   ```sh
   cd web_scraping_fundamentus_fii
   ```
3. [Crie um ambiente virtual Python](https://www.alura.com.br/artigos/ambientes-virtuais-em-python?srsltid=AfmBOortk62KHQFExQEWIq1LtfrRpBE7zhNz1vJWCxJJk_oRAfgM3hbV) para melhor gerenciar o projeto em sua máquina e evitar conflito de versões de dependências
   ```sh
   python3 -m venv nome_do_ambiente_virtual  
   ```
4. a) Ative o ambiente Virtual(Linux)
    ```sh
    source nome_do_ambiente_virtual/bin/activate
    ```
4. b) Ative o ambiente Virtual(Windows)
    ```sh
    nome_do_ambiente_virtual\Scripts\Activate
    ```
5. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## 📌 Uso

A página, a qual a aplicação irá fazer a coleta dos dos dados encontra-se no seguinte endereço:
- https://www.fundamentus.com.br/fii_resultado.php

Para executar, no diretório do projeto e com o ambiente virtual ativado, realize os seguintes passos:

```sh
python main.py
```
Após a execução, um arquivo *.csv* será gerado e salvo no diretório `./dados`. Com os dados já carregado em sua máquina, no formato csv, diversas análises podem ser feitas. 

Uma Análise Exploratória simples foi realizada no arquivo [exploratory_analysis.ipynb](https://github.com/MaercioMamedes/web_scraping_fundamentus_fii/blob/main/exploratory_analysis.ipynb)

## 🤝 Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b minha-feature`).
3. Faça commit das mudanças (`git commit -m 'Adicionando minha feature'`).
4. Faça push para a branch (`git push origin minha-feature`).
5. Abra um Pull Request.

## 📜 Licença

Este projeto está sob a licença [Nome da Licença](LICENSE).

## 📬 Contato

- Nome: Maercio Mamedes
- Email: maerciomamedes@hotmail.com
- LinkedIn: [Maercio Mamedes](https://www.linkedin.com/in/maerciomamedes/)

---

> Este README foi gerado como um modelo base para repositórios públicos no GitHub.
