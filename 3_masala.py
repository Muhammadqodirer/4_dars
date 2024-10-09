
from telebot import TeleBot
from telebot.types import Message
from buttons import main_button,boks_buttons,kursh_buttons,shahmat_buttons

Boks ={
    "Hasanboy Do‘stmatov":{
        "Tug‘ilgan yili":"1993-yil 24-iyun",
        "Vazn toifasi":"Yengil vazn (49 kg)",
        
    },
    "Bektimir Meliqo‘ziyev":{
        "Tug‘ilgan yili":"1996-yil 8-mart",
        "Vazn toifasi":"Yengil og‘ir vazn (81 kg)",
      
    },
    "Shahobiddin Zoirov":{
        "Tug‘ilgan yili":"1993-yil 3-sentabr",
        "Vazn toifasi":"Super yengil vazn (52 kg)",
        
    },
    "Rustam Saidov":{
        "Tug‘ilgan yili":"1978-yil 6-fevral",
        "Vazn toifasi":"Super og‘ir vazn (+91 kg)",
       
}

Kurash = { "O‘ktamjon Karomatov": { "Tug‘ilgan yili": "1991-yil 15-mart", "Vazn toifasi": "90 kg", "Erishgan yutuqlari": "2018-yilgi Osiyo o‘yinlari oltin medali sohibi.\n2017-yilgi Osiyo chempioni." },
           "Jasurbek Qurbonov": { "Tug‘ilgan yili": "1995-yil 11-aprel", "Vazn toifasi": "81 kg", "Erishgan yutuqlari": "2021-yilgi Jahon chempioni.\n2019-yilgi Osiyo o‘yinlari kumush medali sovrindori." },
           "Sherzod Tohirov": { "Tug‘ilgan yili": "1990-yil 19-may", "Vazn toifasi": "66 kg", "Erishgan yutuqlari": "2019-yilgi Osiyo o‘yinlari oltin medali sohibi.\n2018-yilgi Jahon chempionatida bronza medalni qo‘lga kiritgan." }
           }

Shaxmat = {"Shamsiddin Vohidov": { "Tug‘ilgan yili": "2002-yil 4-iyul", "Unvoni": "Grossmeyster", "Erishgan yutuqlari": "2018-yilgi Osiyo chempioni.\n2020-yilgi Jahon yoshlar chempionatida bronza medal sohibi." },
            "Dinara Saduakasova": { "Tug‘ilgan yili": "1996-yil 31-oktabr", "Unvoni": "Xalqaro grossmeyster", "Erishgan yutuqlari": "2019-yilda Markaziy Osiyo chempioni.\n2016-yilgi Jahon yoshlar chempionatida kumush medal sovrindori." },
            "Javohir Sindorov": { "Tug‘ilgan yili": "2005-yil 8-dekabr", "Unvoni": "Grossmeyster", "Erishgan yutuqlari": "2019-yilgi Yoshlar o‘rtasidagi Jahon chempionatida oltin medal.\n2018-yilgi Osiyo chempionatida bronza medal sohibi." }
            }

Token = "7786685841:AAFT9x0VhLmRQrk9WgGACmKTxezEpwz55iw"
bot = TeleBot(Token,parse_mode="html")

@bot.message_handler(commands=["start"])
def reaction_start(message:Message):
    chat_id = message.chat.id
    bot.send_message(chat_id,"Sport yangiliklariga hushkelibsiz",reply_markup=main_button())

@bot.message_handler(regexp="Boks")
def reaction_to_text(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Boks chilar", reply_markup=boks_buttons(message.text))

@bot.message_handler(regexp="Kursh")
def reaction_to_text(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Kurash chilar", reply_markup=kursh_buttons(message.text))

@bot.message_handler(regexp="Shahmat")
def reaction_to_text(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Shahmat chilar", reply_markup=shahmat_buttons(message.text))

@bot.message_handler(func=lambda message: message.text == "Ortga")
def reaction_to_back(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Sport yangiliklari", reply_markup=main_button())

def worker_1(message: Message):
    chat_id = message.chat.id
    Tugilgan_yili = Boks[message.text]['Tug‘ilgan yili']
    Vazn_toifasi = Boks[message.text]['Vazn toifasi']
    Erishgan_yutuqlari = Boks[message.text]['Erishgan yutuqlari']
    bot.send_message(chat_id,f"<b>Oti:</b> <b>{message.text}</b>\n<i>Tug‘ilgan yili</i>: {Tugilgan_yili} <i>Vazn toifasi</i>: {Vazn_toifasi}\n<i>Erishgan yutuqlari</i>: {Erishgan_yutuqlari}")


@bot.message_handler(func=lambda message: message.text == "Hasanboy Do‘stmatov")
def reaction_bok1(message: Message):
    worker_1(message)


@bot.message_handler(func=lambda message: message.text == "Bektimir Meliqo‘ziyev")
def reaction_bok2(message: Message):
    worker_1(message)


@bot.message_handler(func=lambda message: message.text == "Shahobiddin Zoirov")
def reaction_bok3(message: Message):
    worker_1(message)

@bot.message_handler(func=lambda message: message.text == "Rustam Saidov")
def reaction_bok4(message: Message):
    worker_1(message)


def worker_2(message: Message):
    chat_id = message.chat.id
    Tugilgan_yili = Kurash[message.text]['Tug‘ilgan yili']
    Vazn_toifasi = Kurash[message.text]['Vazn toifasi']
    Erishgan_yutuqlari = Kurash[message.text]['Erishgan yutuqlari']
    bot.send_message(chat_id,f"<b>Oti:</b> <b>{message.text}</b>\n<i>Tug‘ilgan yili</i>: {Tugilgan_yili} <i>Vazn toifasi</i>: {Vazn_toifasi}\n<i>Erishgan yutuqlari</i>: {Erishgan_yutuqlari}")


@bot.message_handler(func=lambda message: message.text == "O‘ktamjon Karomatov")
def reaction_bok1(message: Message):
    worker_2(message)


@bot.message_handler(func=lambda message: message.text == "Jasurbek Qurbonov")
def reaction_bok2(message: Message):
    worker_2(message)


@bot.message_handler(func=lambda message: message.text == "Komiljon Tog‘ayev")
def reaction_bok3(message: Message):
    worker_2(message)

@bot.message_handler(func=lambda message: message.text == "Sherzod Tohirov")
def reaction_bok4(message: Message):
    worker_2(message)


def worker_4(message: Message):
    chat_id = message.chat.id
    Tugilgan_yili = Shaxmat[message.text]['Tug‘ilgan yili']
    Unvoni = Shaxmat[message.text]['Unvoni']
    Erishgan_yutuqlari = Shaxmat[message.text]['Erishgan yutuqlari']
    bot.send_message(chat_id,f"<b>Oti:</b> <b>{message.text}</b>\n<i>Tug‘ilgan yili</i>: {Tugilgan_yili} <i>Unvoni</i>: {Unvoni}\n<i>Erishgan yutuqlari</i>: {Erishgan_yutuqlari}")


@bot.message_handler(func=lambda message: message.text == "Nodirbek Abdusattorov")
def reaction_bok1(message: Message):
    worker_4(message)


@bot.message_handler(func=lambda message: message.text == "Shamsiddin Vohidov")
def reaction_bok2(message: Message):
    worker_4(message)


@bot.message_handler(func=lambda message: message.text == "Dinara Saduakasova")
def reaction_bok3(message: Message):
    worker_4(message)

@bot.message_handler(func=lambda message: message.text == "Javohir Sindorov")
def reaction_bok4(message: Message):
    worker_4(message)

bot.polling()