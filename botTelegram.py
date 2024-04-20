import telebot
import keys
import banco

apiKey = keys.botKey
bot = telebot.TeleBot(apiKey)

estado_usuario = {}
@bot.message_handler(commands=['ajuda'])
def ajuda(message):
    bot.send_message(message.chat.id, """Escolha uma das opcoes a baixo:
    
/adicionar | Adiciona um item a lista
/remover | Remove um item da lista
/listar | Lista todos os items da lista
/github | Mostrar meu GitHub""")

@bot.message_handler(commands=['adicionar'])
def adicionar(mensagem):
    userID = mensagem.from_user.id
    bot.send_message(userID, "Informe o Nome, Quantidade e Valor do produto no formato:\n\nNome Quantidade Valor\n\nExemplo:\n\nPastel 2 10.50")
    estado_usuario[userID] = 'adicionar_produto'

@bot.message_handler(func=lambda message: estado_usuario.get(message.from_user.id) == 'adicionar_produto')
def adicionar_produto(mensagem):
    try:
        userID = mensagem.from_user.id
        dados = mensagem.text.split()
        if len(dados) == 3:
            nome, quantidade, valor = dados

            banco.adicionarProdutos(userID, nome, quantidade, valor)
            bot.send_message(userID, f"Produto adicionado:\nNome: {nome}\nQuantidade: {quantidade}\nValor: {valor}")
        else:
            bot.send_message(userID, "Formato incorreto. Por favor, siga o formato: Nome Quantidade Valor")

        del estado_usuario[userID]
    except KeyError:
        bot.send_message(userID, "Por favor, digite /adicionar antes de enviar os dados.")




@bot.message_handler(commands=['remover'])
def remover(mensagem):
    userID = mensagem.from_user.id
    bot.send_message(userID, "Informe o ID do produto que deseja remover:\n\nExemplo: 5")
    estado_usuario[userID] = 'remover_produto'

@bot.message_handler(func=lambda message: estado_usuario.get(message.from_user.id) == 'remover_produto')
def remover_produto(mensagem):
    try:
        userID = mensagem.from_user.id
        idProduto = mensagem.text
        idProduto = int(idProduto)
        produto = banco.removerProduto(userID, idProduto)
        bot.reply_to(mensagem, produto)
        del estado_usuario[userID]
    except Exception as e:
        bot.send_message(userID, f"Insira um ID de produto valido")
@bot.message_handler(commands=['listar'])
def listar(mensagem):
    userID = mensagem.from_user.id
    listaProdutos = banco.listarProdutos(userID)
    print(listaProdutos)
    if listaProdutos:
        mensagem_enviar = "Lista de produtos:\n"
        valor_total = 0
        for produto in listaProdutos:
            id_produto , nome_produto , valor_produto, quantidade_produto, _ = produto
            valor_total += valor_produto * quantidade_produto
            mensagem_enviar += f"\nID Produto: {id_produto}\nNome: {nome_produto}\nQuantidade: {quantidade_produto}\nValor: R${valor_produto}\n\n"
        mensagem_enviar += f"Valor Total: R${valor_total}"
    else:
        mensagem_enviar = "Lista vazia"
    bot.send_message(userID, mensagem_enviar)



@bot.message_handler(commands=['github'])
def like(mensagem):
    bot.send_message(mensagem.chat.id, "https://github.com/DilkerWinter ⛄")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, "Oi! Digite /ajuda para ver as opções.")




bot.polling()

