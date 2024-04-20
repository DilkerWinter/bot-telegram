<p align="center">
<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=26&pause=1000&color=FFFFFFDD&center=true&vCenter=true&random=false&width=550&height=75&lines=Bot+do+Telegram" alt="Typing SVG" /></a>
</p>

## 📖 Descrição
* Projeto criado usando Python, TelegramBotAPI e PostgresSQL
* Adicionar, remover e listar produtos
* Soma total do valor dos produtos 

## 📷 Galeria
![img.png](img.png)

## 💻 Pré-requisitos
* Criar banco de dados
* Criar um Bot no Telegram para resgatar sua chave de API

### Banco de Dados
```
CREATE TABLE produto (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    valor NUMERIC(10,2) NOT NULL,
    quantidade INTEGER NOT NULL,
    id_telegram BIGINT
);
```
## 🚀 Futuras Atualizações

Este projeto poderá ser atualizado com as seguintes possibilidades:

- [ ] Criar API para se comunicar com o Banco
- [ ] Adicionar mais funcionalidades

## 🤖 Tecnologias

<img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"><img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white">
