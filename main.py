# # 5232363147:AAGGyuWRNpPym7otVbr75fAIrSxVQJs0NEM

import telebot
from telebot import types
import config
<<<<<<< HEAD
const tt  = "5232363147:AAGGyuWRNpPym7otVbr75fAIrSxVQJs0NEM"
bot = telebot.TeleBot(tt)
=======

bot = telebot.TeleBot(config.TOKEN)
>>>>>>> 5d5518f (first commit)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    first_name = str(message.chat.first_name)
    if message.text.lower() == 'грамматика' or message.text == '1' or message.text == '1)' or message.text == 'Назад🔙' or message.text=='/start':
        bot.send_message(message.from_user.id,
                         f"Привет {first_name}👋,я Грамматика БОТ,я помогу тебе изучить главные правила Русского языка!")
        keyboard = types.InlineKeyboardMarkup()
        key_alpha = types.InlineKeyboardButton(text='🔠Алфавит', callback_data='alpha')
        keyboard.add(key_alpha)
        key_voice = types.InlineKeyboardButton(text='🟠Звуки речи', callback_data='voice')
        keyboard.add(key_voice)
        key_letter = types.InlineKeyboardButton(text="🔷Гласные и согласные", callback_data='letter')
        keyboard.add(key_letter)
        key_parts = types.InlineKeyboardButton(text='💬Части слова', callback_data='parts')
        keyboard.add(key_parts)
        key_parts_of_speech = types.InlineKeyboardButton(text="🆎Части речи", callback_data="parts_of_speech")
        keyboard.add(key_parts_of_speech)
        key_parts_of_sentence = types.InlineKeyboardButton(text ="⚪Члены предложения",callback_data='parts_of_sentence')
        keyboard.add(key_parts_of_sentence)
        key_types_of_sentences = types.InlineKeyboardButton(text="Типы предложений(простое и сложное)✅",callback_data="types_of_sentence")
        keyboard.add(key_types_of_sentences)
        key_categories = types.InlineKeyboardButton(text = "Грамматические и синтаксические категории:",callback_data = 'categories')
        keyboard.add(key_categories)
        key_signs = types.InlineKeyboardButton(text = '⁉️Знаки препинания',callback_data='signs')
        keyboard.add(key_signs)

        key_stop = types.InlineKeyboardButton(text = "Стоп❗",callback_data='stop')
        keyboard.add(key_stop)



        bot.send_message(message.from_user.id, text='Выберите что вы хотите изучить?', reply_markup=keyboard)
    elif message.text in config.categories.keys():
        bot.send_message(message.from_user.id,config.categories[message.text])
    elif message.text in config.signs.keys():
        bot.send_message(message.from_user.id , config.signs[message.text])
    elif message.text.lower() == "привет":
        bot.send_message(message.from_user.id,
                         f"👋👋👋Привет,{first_name} я помогу тебе изучить русский язык!Доступные команды:\n1)Грамматика\n2)/help")
    elif message.text == "/help":

        bot.send_message(message.from_user.id, "Напиши-Грамматика")
    elif message.text == '/nurbek bratan tiger':
        bot.send_video(message.from_user.id , "https://www.youtube.com/shorts/NK4T-JAkQO8")
    elif message.text == '/info':
        bot.send_message(message.from_user.id , "Bot was made by Aitbai Alisher,follow on my insta: @aytbayev_ )))")
    # elif message.text == '/start':
    #     bot.send_message(message.from_user.id,
    #                      "Привет, я помогу тебе изучить русский язык!\nДоступные команды:\n1)Грамматика\n2)/help")
    elif message.text == 'Имя существительное':
        bot.send_message(message.from_user.id, config.noun)
        bot.send_photo(message.from_user.id, 'https://fs00.infourok.ru/images/doc/130/152171/img0.jpg')
    elif message.text == 'Имя прилагательное':
        bot.send_message(message.from_user.id, config.adjective)
        bot.send_photo(message.from_user.id,
                       'https://sites.google.com/site/kursrusskogoazyka4klass/_/rsrc/1468759269469/morfologia/ima-prilagatelnoe/russkij-prilagatelnye.jpg')
    elif message.text == 'Имя числительное📅':
        bot.send_message(message.from_user.id, config.numbers)
        bot.send_photo(message.from_user.id,
                       'https://uchitel.pro/wp-content/uploads/2018/01/%D0%BF%D1%80%D0%B8%D0%B7%D0%BD%D0%B0%D0%BA%D0%B8-%D1%87%D0%B8%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D1%85.jpg')

    elif message.text == 'Местоимение':
        bot.send_message(message.from_user.id, config.pronouns)

    elif message.text == 'Глагол':
        bot.send_message(message.from_user.id, config.verb)
        bot.send_photo(message.from_user.id,'data:image/jpeg;base64,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')

    elif message.text == 'Инфинитив':
        bot.send_message(message.from_user.id, config.infinitive)
    elif message.text == 'Причастие':
        bot.send_message(message.from_user.id, config.prich)
        bot.send_photo(message.from_user.id,'https://russkiiyazyk.ru/wp-content/uploads/2019/09/prichastie-eto-1.jpg')
    elif message.text == 'Деепричастие':
        bot.send_message(message.from_user.id, config.deeprich)
    elif message.text == 'Наречие':
        bot.send_message(message.from_user.id, config.narechie)
    elif message.text == 'Предлог':
        bot.send_message(message.from_user.id, config.predlog)
    elif message.text == 'Союзы':
        bot.send_message(message.from_user.id, config.souyz)
    elif message.text == 'Связка':
        bot.send_message(message.from_user.id, config.connection)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    try:
        if call.data == "alpha":
            msg = " В русском языке для обозначения звуков на письме используются специальные знаки, которые называются буквами.\nСовокупность букв, расположенных в установленном порядке, называется алфавитом, или азбукой.\nПредставляем буквы русского языка."
            bot.send_message(call.message.chat.id, msg)
            bot.send_photo(call.message.chat.id,
                           'https://дд7ростов.рф/800/600/https/schoolfiles.ru/wp-content/uploads/2020/07/03-alfavit-strochnye-i-propisnye-bukvy-2048x1448.jpg')

        elif call.data == "voice":
            bot.send_message(call.message.chat.id,
                             "Звуки речи – это звуки, из которых состоят слова. Звук есть самая мелкая единица языка.. Звуки речи, как и все другие звуки природы (звуки шагов человека, гудки машины, пение птиц и т.д.), порождаются колебаниями воздуха, то есть звуки речи [а], [б], [в], [о] относятся к акустическим явлениям, они воспринимаются органами слуха как разные звучания.Колебания воздуха возникают при прохождении воздушной струи через речевой аппарат.")
            bot.send_photo(call.message.chat.id,
                           'https://grammatika-rus.ru/wp-content/uploads/2018/06/zvuki-rechi-1.jpg')

        elif call.data == 'letter':
            bot.send_message(call.message.chat.id,
                             "Гласные звуки («глас» — это старославянское «голос») — это звуки [а], [и], [о], [у], [ы], [э], при создании которых участвуют голосовые связки, а на пути выдыхаемого воздуха не воздвигается преграда. Эти звуки поются: [ааааааа], [иииииии]…\nСогласные звуки — это звуки, при создании которых на пути выдыхаемого воздуха воздвигается преграда. Звонкие согласные произносятся с участием голоса, а глухие согласные без него. Разницу легко услышать в парных согласных, например, [п] — [б], при проговаривании которых губы и язык находятся в одинаковом положении.Мягкие согласные произносятся с участием средней части языка и в транскрипции обозначаются апострофом ', что происходит, когда согласные ")
            bot.send_photo(call.message.chat.id, 'https://pp.userapi.com/c837623/v837623438/51082/o0N54npPYe4.jpg')

        elif call.data == 'parts':
            word = 'Из каких частей состоит слово?\nКорень – это общая часть однокоренных слов , в которой передаётся их основное значение.Корень в однокоренных словах пишется одинаково: холод,холодный,холодить,холодильник;\nОкончание – это изменяемая часть слова, которая служит для связи слов в предложении:берёза,под берёзой,на берёзе;\nПриставка – это значимая часть слова, которая стоит перед корнем и служит для образования новых слов:ходить,переходить,уходить;\nСуффикс – это значимая часть слова, которая стоит после корня и служит для образования новых слов:дети-детский,детство;'

            bot.send_message(call.message.chat.id, word)
            bot.send_photo(call.message.chat.id,
                           'https://class.rambler.ru/qa-service/production/uploads/images/image/000/058/247/c5831aa5fc.jpeg')
        elif call.data == 'parts_of_speech':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.InlineKeyboardButton("Имя существительное")
            item2 = types.InlineKeyboardButton("Имя прилагательное")
            item3 = types.InlineKeyboardButton("Имя числительное📅")
            item4 = types.InlineKeyboardButton("Местоимение")
            item5 = types.InlineKeyboardButton("Глагол")
            item6 = types.InlineKeyboardButton("Инфинитив")
            item7 = types.InlineKeyboardButton("Причастие")
            item8 = types.InlineKeyboardButton("Деепричастие")
            item9 = types.InlineKeyboardButton("Наречие")
            item10 = types.InlineKeyboardButton("Предлог")
            item11 = types.InlineKeyboardButton("Союзы")
            item12 = types.InlineKeyboardButton("Связка")
            back = types.InlineKeyboardButton("Назад🔙")
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12,back)
            bot.send_message(call.message.chat.id, "Части речи:", reply_markup=markup)

        elif call.data == "parts_of_sentence":
            bot.send_message(call.message.chat.id,config.parts_of_sentence)
            bot.send_photo(call.message.chat.id,'https://uchitel.pro/wp-content/uploads/2018/02/%D1%86%D0%BE%D1%80_179.jpg')

        elif call.data == 'types_of_sentence':
            bot.send_message(call.message.chat.id ,config.types_of_sentence)
            bot.send_photo(call.message.chat.id ,'https://uchitel.pro/wp-content/uploads/2018/02/%D1%82%D0%B8%D0%BF%D1%8B-%D0%BF%D1%80%D0%B5%D0%B4%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9.jpg')

        elif call.data == 'signs':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.InlineKeyboardButton("🔘Точка")
            item2 = types.InlineKeyboardButton("❓Вопросительный знак")
            item3 = types.InlineKeyboardButton("❗Восклицательный знак")
            item4 = types.InlineKeyboardButton("Многоточие")
            item5 = types.InlineKeyboardButton("Двоеточие")
            item6 = types.InlineKeyboardButton("Точка с запятой")
            item7 = types.InlineKeyboardButton("Запятая")
            item8 = types.InlineKeyboardButton("Тире")
            item9 = types.InlineKeyboardButton("Скобки")
            item10 = types.InlineKeyboardButton("Кавычки")
            item11 = types.InlineKeyboardButton("Абзац")
            back = types.InlineKeyboardButton("Назад🔙")
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11,back)
            bot.send_message(call.message.chat.id, "Знаки препинания:", reply_markup=markup)

        elif call.data == 'categories':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.InlineKeyboardButton("Спряжение")
            item2 = types.InlineKeyboardButton("Наклонение")
            item3 = types.InlineKeyboardButton("Вид")
            item4 = types.InlineKeyboardButton("Время")
            item5 = types.InlineKeyboardButton("Залог")
            item6 = types.InlineKeyboardButton("Лицо")
            item7 = types.InlineKeyboardButton("Падеж")
            item8 = types.InlineKeyboardButton("Склонение")
            item9 = types.InlineKeyboardButton("Число")
            item10 = types.InlineKeyboardButton("Род")
            item11 = types.InlineKeyboardButton("Одушевленность/неодушевленность")
            back = types.InlineKeyboardButton("Назад🔙")
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11,back)
            bot.send_message(call.message.chat.id, "Грамматические и синтаксические категории:", reply_markup=markup)

        elif call.data=='stop':
            bot.send_message(call.message.chat.id , f"Спасибо за использование нашего бота😊.Для того чтобы перезапустить бота нажмите на кнопку➡️: /start")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Нажми на️➡️: /start ,для того чтобы еще раз получить информацию!😊",
                              reply_markup=None)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                  text=f"Отправь 1,для того чтобы еще раз получить информацию!😊  ")


    except Exception as e:
        print(repr(e))
bot.polling(none_stop=True, interval=0)
