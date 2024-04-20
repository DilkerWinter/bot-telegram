import telebot

apiKey = "6314554818:AAE6qkHC0JoUvGh9hOUSFedfbtnFWcbpzCc"

bot = telebot.TeleBot(apiKey)

@bot.message_handler(commands=['ajuda'])
def ajuda(message):
    bot.send_message(message.chat.id, """Escolha uma das opcoes a baixo:
    
/adicionar | Adiciona um item a lista
/remover | Remove um item da lista
/listar | Lista todos os items da lista
/somar | Soma o valor de todos os itens da lista
/like | Da um joinha
/limpar_chat Limpa toda as mensagems do chat""")

@bot.message_handler(commands=['adicionar'])
def adicionar(mensagem):
    pass

@bot.message_handler(commands=['remover'])
def remover(mensagem):
    pass

@bot.message_handler(commands=['listar'])
def listar(mensagem):
    pass
@bot.message_handler(commands=['like'])
def like(mensagem):
    bot.send_message(mensagem.chat.id, "👍")

@bot.message_handler(commands=['limpar_chat'])
def limpar_chat(mensagem):
    chat_id = mensagem.chat.id
    mensagem = bot.get

    for msg in mensagem:
        bot.delete_message(chat_id, msg.message_id)

    bot.send_message(chat_id, "Mensagens deletadas com sucesso!")


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def respostainicial(mensagem):
    bot.reply_to(mensagem, "Oi, Digite /ajuda para ver as opcoes")



bot.polling()

