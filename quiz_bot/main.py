import telebot
import key
from telebot import types
import random

bot = telebot.TeleBot(key.keyword)

teachers_id = [676103951]

questions = ["С помощью какой команды осуществляется считывание с клавиатуры?",
                     "Как получить последнюю цифру целого числа n?",
                     "Как запустить цикл от большего числа к меньшему (от a до b, a > b)?",
                     "С помощью какой констуркции можно рассмотреть более двух исходов в ветвлении?",
                     "Какие виды циклов бывают в питоне?",
                     "Что вернёт данное выражение: 4 and \"w\"?",
                     "В чём особенность функции range?",
                     "Операция сложения двух строк называется ...",
                     "Дана строка a = \"Hello, world!\", какой из предложенных срезов вернёт \"world\"?",
                     "def f(x):\n    if x == 0:\n        return 0\n    return f(x - 1)\n\nТакая функция называется..."]

ans = [["print", "if", "input", "import"],
               ["n % 10", "n / 10", "n // 10", "n & 10"],
               ["range(a, b, -1)", "Так сделать нельзя", "range(b, a, -1)", "range(a, b - 1, -1)"],
               ["if if", "elif", "case", "Нет такой возможности"],
               ["for, for each, while", "for", "for, while, do while", "for, while"],
               ["True", "False", "4", "w"],
               ["Нет особенностей", "Правая граница не включается", "Обе границы не включаются",
                "Нельзя использовать без for"],
               ["Конкатенация", "Сложение", "Дизъюнкция", "Экранирование"],
               ["a[7:12]", "a[7:11]", "a[::-1]", "a[6:12]"],
               ["Рекуррентная", "Целочисленная", "Рекурсия", "Нет отдельного названия"]]
right_ans = [2, 0, 3, 1, 0, 3, 1, 0, 0, 2]
current_question = 0
score = 0
nums = set()

def get_question():
    global current_question
    current_num = random.randrange(0, 10)
    flag = False
    while not(flag):
        if current_num not in nums:
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            ans0 = types.InlineKeyboardButton(text=ans[current_num][0],
                                              callback_data=f'ans_0_{current_num}')
            keyboard.add(ans0)
            ans1 = types.InlineKeyboardButton(text=ans[current_num][1],
                                              callback_data=f'ans_1_{current_num}')
            keyboard.add(ans1)
            ans2 = types.InlineKeyboardButton(text=ans[current_num][2],
                                              callback_data=f'ans_2_{current_num}')
            keyboard.add(ans2)
            ans3 = types.InlineKeyboardButton(text=ans[current_num][3],
                                              callback_data=f'ans_3_{current_num}')
            keyboard.add(ans3)
            stop = types.InlineKeyboardButton(text="Остановить викторину ❌",
                                              callback_data='stop')
            keyboard.add(stop)
            nums.add(current_num)
            flag = True
            current_question += 1
        else:
            current_num = random.randrange(0, 10)
    return [current_num, keyboard]

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Приветствую! Чтобы получить список "
                                               "возможностей напишите /start")
    elif message.text == "/start":
        msg_text = "Здравствуйте! Это обучающий бот по Python. Для навигации пропишите /menu"
        bot.send_message(message.from_user.id, msg_text)
    elif message.text == "/menu":
        keyboard2 = types.InlineKeyboardMarkup(row_width=1)
        key_menu_python = types.InlineKeyboardButton(text='Изучение Python 🐍', callback_data='python')
        key_menu_oge = types.InlineKeyboardButton(text="ОГЭ 💯", callback_data='oge')
        key_menu_ege = types.InlineKeyboardButton(text="ЕГЭ 🖥️", callback_data='ege')
        key_sam_rab = types.InlineKeyboardButton(text="Самостоятельные работы ❓", callback_data='sam_rab')
        keyboard2.add(key_menu_python)
        keyboard2.add(key_menu_oge)
        keyboard2.add(key_menu_ege)
        keyboard2.add(key_sam_rab)
        bot.send_message(message.from_user.id, text="Навигация. Выберите нужный раздел", reply_markup=keyboard2)
    else:
        bot.send_message(message.from_user.id, "Я вас не понимаю! Чтобы получить информацию,"
                                               " напишите /start или /menu!")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        # эта часть относится к callback_data = 'quiz'
        global current_question, score, nums
        print(call.from_user.id)
        if call.data == "menu":
            # добавить текст с возможностями
            keyboard2 = types.InlineKeyboardMarkup(row_width=1)
            key_menu_python = types.InlineKeyboardButton(text='Изучение Python 🐍', callback_data='python')
            key_menu_oge = types.InlineKeyboardButton(text="ОГЭ 💯", callback_data='oge')
            key_menu_ege = types.InlineKeyboardButton(text="ЕГЭ 🖥️", callback_data='ege')
            key_sam_rab = types.InlineKeyboardButton(text="Самостоятельные работы ❓", callback_data='sam_rab')
            keyboard2.add(key_menu_python)
            keyboard2.add(key_menu_oge)
            keyboard2.add(key_menu_ege)
            keyboard2.add(key_sam_rab)
            bot.send_message(call.from_user.id, text="Навигация. Выберите нужный раздел", reply_markup=keyboard2)

        if call.data == "stop":
            keyboard2 = types.InlineKeyboardMarkup(row_width=1)
            key_menu_python = types.InlineKeyboardButton(text='Изучение Python 🐍', callback_data='python')
            key_menu_oge = types.InlineKeyboardButton(text="ОГЭ 💯", callback_data='oge')
            key_menu_ege = types.InlineKeyboardButton(text="ЕГЭ 🖥️", callback_data='ege')
            key_sam_rab = types.InlineKeyboardButton(text="Самостоятельные работы ❓", callback_data='sam_rab')
            keyboard2.add(key_menu_python)
            keyboard2.add(key_menu_oge)
            keyboard2.add(key_menu_ege)
            keyboard2.add(key_sam_rab)
            bot.send_message(call.from_user.id, text=f"Викторина остановлена. Ваш счёт: {score}. Выберите нужный раздел",
                             reply_markup=keyboard2)

        if call.data == "quiz_start":
            keyboard1 = types.InlineKeyboardMarkup(row_width=1)
            key_quiz = types.InlineKeyboardButton(text='Квиз по Python', callback_data='quiz')
            key_quiz_back = types.InlineKeyboardButton("Назад 🔙", callback_data='python')
            keyboard1.add(key_quiz)
            keyboard1.add(key_quiz_back)
            # добавить описание квиза
            question = "Вы хотите сыграть в викторину по Python?"
            bot.send_message(call.from_user.id, text=question, reply_markup=keyboard1)

        # меню для тичеров пока не написано
        if call.data == 'sam_rab':
            keyboard1 = types.InlineKeyboardMarkup(row_width=1)
            if call.from_user.id in teachers_id:
                teach_key = types.InlineKeyboardButton("Пул работ", callback_data='teacher')
                keyboard1.add(teach_key)
            work1_key = types.InlineKeyboardButton("Самостоятельная работа 1", callback_data='work 1')
            key_works_back = types.InlineKeyboardButton("Назад 🔙", callback_data='menu')
            keyboard1.add(work1_key, key_works_back)
            bot.send_message(call.from_user.id, 'Выберите нужный пункт', reply_markup=keyboard1)

        if call.data.split()[0] == 'work':
            def student_answer(message):
                acept = bot.send_message(message.from_user.id, "Вы уверены и хотите отправить работу на проверку?"
                                                               " (да/нет)\n\n"
                                                               "Ваш ответ:\n" + message.text)
                bot.register_next_step_handler(acept, acept_f, message.text)
            def acept_f(message, last_msg):
                if message.text.lower() == 'да':
                    f = open('work_1_logs.txt', 'r')
                    logs_1 = []
                    for i in f:
                        logs_1.append(i)
                    if str(message.from_user.id) + "\n" not in logs_1:
                        f = open('work_1_logs.txt', 'a')
                        f.write(str(message.from_user.id) + '\n')
                        bot.send_message(message.chat.id, 'Записано')
                        for i in teachers_id:
                            bot.send_message(i, f'Новый ответ от {message.from_user.first_name} '
                                            f'{message.from_user.last_name}, работа {call.data.split()[1]}\n\n'
                                                f'Текст ответа:\n{last_msg}')
                    else:
                        bot.send_message(message.from_user.id, 'Ошибка! Вы уже отправляли данную работу')
                    f.close()
                else:
                    repeat = bot.send_message(message.from_user.id, 'Повторите ввод')
                    bot.register_next_step_handler(repeat, student_answer)
            if call.data.split()[1] == '1':
                cap = ("Это тестовая работа, в следующем сообщении пришлите ваш ответ в формате:\n\n"
                       "Имя и Фамилия, класс\n\nОтветы:\n1.\n2.\n3.\n...")
                ''''
                doc = bot.send_document(call.from_user.id, open('work_1.pdf', 'rb'),
                                  caption=cap)
                '''
                doc = bot.send_message(call.from_user.id, cap)
                bot.register_next_step_handler(doc, student_answer)


        if call.data == "python":
            keyboard_python = types.InlineKeyboardMarkup(row_width=1)
            key_python = types.InlineKeyboardButton("Квиз ❓", callback_data='quiz_start')
            key_polz = types.InlineKeyboardButton("Полезные ссылки", callback_data='links')
            key_theory = types.InlineKeyboardButton("Теория", callback_data='theory')
            key_python_back = types.InlineKeyboardButton("Назад 🔙", callback_data='menu')
            keyboard_python.add(key_python, key_polz, key_theory, key_python_back)
            bot.send_message(call.from_user.id, text = 'Выберите нужный раздел', reply_markup=keyboard_python)

        if call.data == 'links':
            keyboard_links = types.InlineKeyboardMarkup(row_width=1)
            key_python_back = types.InlineKeyboardButton("Назад 🔙", callback_data='python')
            key_of = types.InlineKeyboardButton("Официальный сайт питона",
                                                url = 'https://www.python.org/')
            key_doc = types.InlineKeyboardButton("Документация по языку",
                                                 url = 'https://docs.python.org/3/')
            key_course1 = types.InlineKeyboardButton("Курс по языку для начинающих",
                                                     url = 'https://stepik.org/course/58852/syllabus?search=4295780044')
            key_course2 = types.InlineKeyboardButton('Курс по языку для продвинутых',
                                                     url = 'https://stepik.org/course/68343/promo?search=4295780045')
            keyboard_links.add(key_of,
                               key_doc,
                               key_course1,
                               key_course2,
                               key_python_back)
            bot.send_message(call.from_user.id, text = 'Полезные ссылки',
                             reply_markup=keyboard_links)

        if call.data == 'theory':
            gl = ['Глава 1. Введение в Python',
                  'Глава 2. Основы Python',
                  'Глава 3. Объектно-ориентированное программирование',
                  'Глава 4. Обработка ошибок и исключений',
                  'Глава 5. Списки, кортежи и словари',
                  'Глава 6. Модули',
                  'Глава 7. Строки',
                  'Глава 8. Pattern matching',
                  'Глава 9. Работа с файлами',
                  'Глава 10. Работа с датами и временем']

            url = ['https://metanit.com/python/tutorial/1.1.php',
                   'https://metanit.com/python/tutorial/2.1.php',
                   'https://metanit.com/python/tutorial/7.1.php',
                   'https://metanit.com/python/tutorial/2.11.php',
                   'https://metanit.com/python/tutorial/3.1.php',
                   'https://metanit.com/python/tutorial/2.10.php',
                   'https://metanit.com/python/tutorial/5.1.php',
                   'https://metanit.com/python/tutorial/2.13.php',
                   'https://metanit.com/python/tutorial/4.1.php',
                   'https://metanit.com/python/tutorial/8.1.php']

            theory_keyboard = types.InlineKeyboardMarkup(row_width=1)
            for i in range(10):
                key_th = types.InlineKeyboardButton(text=gl[i],
                                                    url=url[i])
                theory_keyboard.add(key_th)
            key_python_back = types.InlineKeyboardButton("Назад 🔙", callback_data='python')
            theory_keyboard.add(key_python_back)
            bot.send_message(call.from_user.id, text="Ссылки на теоретический материал. Выберите нужную главу:",
                             reply_markup=theory_keyboard)

        if call.data == "oge":
            oge_keyboard = types.InlineKeyboardMarkup(row_width=1)
            demo_key = types.InlineKeyboardButton("Демо-версия и симуляторы", callback_data='demo_oge')
            tasks_key = types.InlineKeyboardButton("Список заданий", callback_data='tasks_oge')
            key_back = types.InlineKeyboardButton("Назад 🔙", callback_data='menu')
            oge_keyboard.add(demo_key, tasks_key, key_back)
            bot.send_message(call.from_user.id, text="Выберите интересующий вас раздел", reply_markup=oge_keyboard)

        if call.data == 'demo_oge':
            keyboard_links_oge = types.InlineKeyboardMarkup(row_width=1)
            key_oge_back = types.InlineKeyboardButton("Назад 🔙", callback_data='oge')
            key_bank = types.InlineKeyboardButton("Открытый банк заданий",
                                                    url='https://oge.fipi.ru/bank/index.php?proj=74676951F093A0754D74F2D6E7955F06')
            key_demo = types.InlineKeyboardButton("Демо-версия",
                                                     url='https://fipi.ru/oge/demoversii-specifikacii-kodifikatory#!/tab/173801626-5')
            key_generat = types.InlineKeyboardButton("Генератор тренировочных вариантов",
                                                         url='https://kpolyakov.spb.ru/school/oge/generate.htm')
            key_navig_oge = types.InlineKeyboardButton(text='Навигатор подготовки к ОГЭ по информатике',
                                                       url = 'https://fipi.ru/navigator-podgotovki/navigator-oge#inf')
            key_balls = types.InlineKeyboardButton(text='Шкала перевода баллов',
                                                   url='https://4ege.ru/gia-in-9/55351-shkala-perevoda-ballov-oge.html')
            keyboard_links_oge.add(key_bank,
                                   key_demo,
                                   key_generat,
                                   key_navig_oge,
                                   key_balls,
                                   key_oge_back)
            bot.send_message(call.from_user.id, text='Полезные ссылки',
                                 reply_markup=keyboard_links_oge)

        if call.data == 'tasks_oge':
            tasks_keyb = types.InlineKeyboardMarkup(row_width=1)
            themes_oge = ['1. Оценка информационного объёма текста',
                          '2. Декодирование кодовой последовательности',
                          '3. Определение истинности высказывания',
                          '4. Анализ моделей объектов',
                          '5. Анализ алгоритмов для исполнителя',
                          '6. Анализ программ с ветвлениями',
                          '7. Адресация в сети Интернет',
                          '8. Поисковые запросы в сети Интернет',
                          '9. Анализ схем (графов)',
                          '10. Запись чисел в разных системах счисления',
                          '11. Поиск информации в файлах и каталогах',
                          '12. Определение количества и объёма файлов',
                          '13.1. Создание презентаций',
                          '13.2. Набор и оформление текстового документа',
                          '14. Обработка данных в электронной таблице',
                          '15.1. Составление программы для исполнителя',
                          '15.2. Составление программы на языке программирования'
                          ]
            for i in range(1, 18):
                key = types.InlineKeyboardButton(f"{themes_oge[i - 1]}", callback_data=f'task_oge {i}')
                tasks_keyb.add(key)
            key_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data='menu')
            tasks_keyb.add(key_back)
            bot.send_message(call.from_user.id, text = 'Выберите интересующее задание:', reply_markup=tasks_keyb)

        if call.data.split()[0] == 'task_oge':
            number = int(call.data.split()[1])
            url_web_oge = ['https://www.youtube.com/watch?v=9H9xAK3Y25o&ab_channel=%D0%98%D0%B2%D0%B0%D0%BD%D0%92%D0%B8%D0%BA%D1%82%D0%BE%D1%80%D0%BE%D0%B2%D0%B8%D1%87',
                           'https://www.youtube.com/watch?v=CEtG5MUmvWM&ab_channel=%D0%98%D0%B2%D0%B0%D0%BD%D0%92%D0%B8%D0%BA%D1%82%D0%BE%D1%80%D0%BE%D0%B2%D0%B8%D1%87',
                           'https://www.youtube.com/watch?v=Ekrt54b_8as&ab_channel=%D0%98%D0%B2%D0%B0%D0%BD%D0%92%D0%B8%D0%BA%D1%82%D0%BE%D1%80%D0%BE%D0%B2%D0%B8%D1%87',
                           'https://www.youtube.com/watch?v=8lv-35Y1yQY&ab_channel=%D0%98%D0%B2%D0%B0%D0%BD%D0%92%D0%B8%D0%BA%D1%82%D0%BE%D1%80%D0%BE%D0%B2%D0%B8%D1%87',
                           'https://www.youtube.com/watch?v=ybwyb-CdNTg&ab_channel=%D0%98%D0%B2%D0%B0%D0%BD%D0%92%D0%B8%D0%BA%D1%82%D0%BE%D1%80%D0%BE%D0%B2%D0%B8%D1%87',
                           'https://www.youtube.com/watch?v=R2upK0ujKaQ&ab_channel=%D0%98%D0%B2%D0%B0%D0%BD%D0%92%D0%B8%D0%BA%D1%82%D0%BE%D1%80%D0%BE%D0%B2%D0%B8%D1%87',
                           'https://www.youtube.com/watch?v=1qHXzmYnO7A&ab_channel=%D0%98%D0%B2%D0%B0%D0%BD%D0%92%D0%B8%D0%BA%D1%82%D0%BE%D1%80%D0%BE%D0%B2%D0%B8%D1%87',
                           'https://www.youtube.com/watch?v=xxxI27oFs1E&t=560s&ab_channel=%D0%98%D0%B2%D0%B0%D0%BD%D0%92%D0%B8%D0%BA%D1%82%D0%BE%D1%80%D0%BE%D0%B2%D0%B8%D1%87',
                           'https://www.youtube.com/watch?v=Xrjl7lv3sVM&ab_channel=%D0%98%D0%B2%D0%B0%D0%BD%D0%92%D0%B8%D0%BA%D1%82%D0%BE%D1%80%D0%BE%D0%B2%D0%B8%D1%87',
                           'https://www.youtube.com/watch?v=HNXq5tJS8Fg&ab_channel=%D0%98%D0%B2%D0%B0%D0%BD%D0%92%D0%B8%D0%BA%D1%82%D0%BE%D1%80%D0%BE%D0%B2%D0%B8%D1%87',
                           'https://www.youtube.com/watch?v=lbgNJVePReA&ab_channel=%D0%98%D0%B2%D0%B0%D0%BD%D0%92%D0%B8%D0%BA%D1%82%D0%BE%D1%80%D0%BE%D0%B2%D0%B8%D1%87',
                           'https://www.youtube.com/watch?v=CDIZ8jIfnWU&ab_channel=%D0%98%D0%B2%D0%B0%D0%BD%D0%92%D0%B8%D0%BA%D1%82%D0%BE%D1%80%D0%BE%D0%B2%D0%B8%D1%87',
                           'https://www.youtube.com/watch?v=NecFCDQnEJ8&ab_channel=%D0%98%D0%B2%D0%B0%D0%BD%D0%92%D0%B8%D0%BA%D1%82%D0%BE%D1%80%D0%BE%D0%B2%D0%B8%D1%87',
                           'https://www.youtube.com/watch?v=JPbaATVHMIE&ab_channel=%D0%98%D0%B2%D0%B0%D0%BD%D0%92%D0%B8%D0%BA%D1%82%D0%BE%D1%80%D0%BE%D0%B2%D0%B8%D1%87',
                           'https://www.youtube.com/watch?v=1JkOdpQ2LAQ&ab_channel=%D0%98%D0%B2%D0%B0%D0%BD%D0%92%D0%B8%D0%BA%D1%82%D0%BE%D1%80%D0%BE%D0%B2%D0%B8%D1%87',
                           'https://www.youtube.com/watch?v=EvsG6OImEMs&ab_channel=%D0%98%D0%B2%D0%B0%D0%BD%D0%92%D0%B8%D0%BA%D1%82%D0%BE%D1%80%D0%BE%D0%B2%D0%B8%D1%87',
                           'https://www.youtube.com/watch?v=CpK_k2H3v0s&ab_channel=%D0%98%D0%B2%D0%B0%D0%BD%D0%92%D0%B8%D0%BA%D1%82%D0%BE%D1%80%D0%BE%D0%B2%D0%B8%D1%87']
            url_polyakov_oge = ['https://kpolyakov.spb.ru/school/oge/gen.php?action=viewAllEgeNo&egeId=201&cat124=on',
                           'https://kpolyakov.spb.ru/school/oge/gen.php?action=viewAllEgeNo&egeId=202&cat125=on',
                           'https://kpolyakov.spb.ru/school/oge/gen.php?action=viewAllEgeNo&egeId=203&cat126=on&cat143=on',
                           'https://kpolyakov.spb.ru/school/oge/gen.php?action=viewAllEgeNo&egeId=204&cat127=on',
                           'https://kpolyakov.spb.ru/school/oge/gen.php?action=viewAllEgeNo&egeId=205&cat128=on',
                           'https://kpolyakov.spb.ru/school/oge/gen.php?action=viewAllEgeNo&egeId=206&cat129=on&cat178=on',
                           'https://kpolyakov.spb.ru/school/oge/gen.php?action=viewAllEgeNo&egeId=207&cat135=on',
                           'https://kpolyakov.spb.ru/school/oge/gen.php?action=viewAllEgeNo&egeId=208&cat134=on',
                           'https://kpolyakov.spb.ru/school/oge/gen.php?action=viewAllEgeNo&egeId=209&cat130=on',
                           'https://kpolyakov.spb.ru/school/oge/gen.php?action=viewAllEgeNo&egeId=210&cat131=on&cat132=on&cat133=on',
                           'https://kpolyakov.spb.ru/school/oge/gen.php?action=viewAllEgeNo&egeId=211&cat136=on',
                           'https://kpolyakov.spb.ru/school/oge/gen.php?action=viewAllEgeNo&egeId=212&cat137=on&cat138=on',
                           'https://kpolyakov.spb.ru/school/oge/gen.php?action=viewAllEgeNo&egeId=213&cat141=on',
                           'https://kpolyakov.spb.ru/school/oge/gen.php?action=viewAllEgeNo&egeId=214&cat142=on',
                           'https://kpolyakov.spb.ru/school/oge/gen.php?action=viewAllEgeNo&egeId=215&cat139=on',
                           'https://kpolyakov.spb.ru/school/oge/gen.php?action=viewAllEgeNo&egeId=216&cat140=on&cat115=on',
                           'https://kpolyakov.spb.ru/school/oge/gen.php?action=viewAllEgeNo&egeId=217&cat116=on']
            keyb = types.InlineKeyboardMarkup(row_width=1)
            key_tasks = types.InlineKeyboardButton(text='Задачи по теме', url=url_polyakov_oge[number - 1])
            key_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data='tasks_oge')
            key_web = types.InlineKeyboardButton(text='Вебинар', url=url_web_oge[number - 1])
            keyb.add(key_web, key_tasks, key_back)
            if number == 13:
                number = "13.1"
            if number == 14:
                number = "13.2"
            if number == 16:
                number = "15.1"
            if number == 17:
                number = "15.2"
            bot.send_message(call.from_user.id, text=f'Материалы для изучения задания номер {number}:',
                             reply_markup=keyb)

        if call.data == "ege":
            ege_keyboard = types.InlineKeyboardMarkup(row_width=1)
            demo_key = types.InlineKeyboardButton("Демо-версия и симуляторы", callback_data='demo_ege')
            tasks_key = types.InlineKeyboardButton("Список заданий", callback_data='tasks')
            key_back = types.InlineKeyboardButton("Назад 🔙", callback_data='menu')
            ege_keyboard.add(demo_key, tasks_key, key_back)
            bot.send_message(call.from_user.id, text="Выберите интересующий вас раздел", reply_markup=ege_keyboard)

        if call.data == 'demo_ege':
            keyboard_links_ege = types.InlineKeyboardMarkup(row_width=1)
            key_ege_back = types.InlineKeyboardButton("Назад 🔙", callback_data='ege')
            key_bank = types.InlineKeyboardButton("Демонстрационная версия станции КЕГЭ",
                                                    url='https://kompege.ru/')
            key_demo = types.InlineKeyboardButton("Демо-версия",
                                                     url='https://fipi.ru/ege/demoversii-specifikacii-kodifikatory#!/tab/151883967-5')
            key_generat = types.InlineKeyboardButton("Генератор тренировочных вариантов",
                                                         url='https://kpolyakov.spb.ru/school/ege/generate.htm')
            key_navig_ege = types.InlineKeyboardButton(text='Навигатор подготовки к ЕГЭ по информатике',
                                                       url = 'https://fipi.ru/navigator-podgotovki/navigator-ege#inf')
            key_balls = types.InlineKeyboardButton(text='Шкала перевода баллов',
                                                   url='https://4ege.ru/novosti-ege/4023-shkala-perevoda-ballov-ege.html')
            keyboard_links_ege.add(key_bank,
                                   key_demo,
                                   key_generat,
                                   key_navig_ege,
                                   key_balls,
                                   key_ege_back)
            bot.send_message(call.from_user.id, text='Полезные ссылки',
                                 reply_markup=keyboard_links_ege)

        if call.data == 'tasks':
            tasks_keyboard = types.InlineKeyboardMarkup(row_width=1)
            themes = ["Анализ информационных моделей",
                      "Таблицы истинности логических выражений",
                      "Поиск и сортировка в базах данных",
                      "Кодирование и декодирование данных. Условие Фано",
                      "Анализ алгоритмов для исполнителей",
                      "Анализ программ с циклами",
                      "Кодирование графической и звуковой информации",
                      "Комбинаторика",
                      "Обработка числовой информации в электронных таблицах",
                      "Поиск слова в текстовом документе",
                      "Вычисление количества информации",
                      "Алгоритмы для исполнителей с циклами и ветвлениями",
                      "IP-адреса и маски",
                      "Позиционные системы счисления",
                      "Истинность логического выражения",
                      "Вычисление значения рекурсивной функции",
                      "Обработка целочисленных данных. Проверка делимости",
                      "Динамическое программирование в электронных таблицах",
                      "Теория игр",
                      "",
                      "",
                      "Анализ программ с циклами и ветвлениями",
                      "Динамическое программирование (количество программ)",
                      "Обработка символьных строк",
                      "Обработка целочисленных данных. Поиск делителей",
                      "Обработка данных с помощью сортировки",
                      "Обработка потока данных",
                      ]
            for i in range(1, 28):
                if i == 20 or i == 21:
                    continue
                elif i == 19:
                    key = types.InlineKeyboardButton(f"Задания 19-21: {themes[18]}", callback_data=f'task {i}')
                    tasks_keyboard.add(key)
                else:
                    key = types.InlineKeyboardButton(f"Задание {i}: {themes[i - 1]}", callback_data=f'task {i}')
                    tasks_keyboard.add(key)
            key_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data='menu')
            tasks_keyboard.add(key_back)
            bot.send_message(call.from_user.id, text = 'Выберите интересующее задание:', reply_markup=tasks_keyboard)

        if call.data.split()[0] == 'task':
            number = int(call.data.split()[1])
            if number == 20 or number == 21:
                number = 19
            url_polyakov = ['https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=1&cat12=on&cat13=on',
                            'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=2&cat8=on',
                            'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=2&cat8=on',
                            'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=4&cat21=on&cat22=on&cat23=on&cat25=on&cat166=on',
                            'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=4&cat21=on&cat22=on&cat23=on&cat25=on&cat166=on',
                            'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=6&cat175=on&cat179=on&cat180=on',
                            'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=7&cat38=on&cat39=on',
                            'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=8&cat42=on&cat43=on&cat145=on',
                            'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=9&cat146=on&cat147=on',
                            'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=10&cat148=on',
                            'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=11&cat52=on&cat53=on&cat54=on&cat149=on',
                            'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=12&cat55=on&cat56=on&cat57=on&cat58=on',
                            'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=13&cat48=on&cat49=on&cat50=on&cat51=on&cat177=on',
                            'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=14&cat60=on&cat61=on&cat62=on&cat174=on',
                            'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=15&cat67=on&cat68=on&cat69=on&cat70=on&cat123=on&cat167=on',
                            'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=16&cat44=on&cat45=on&cat46=on&cat181=on',
                            'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=17&cat168=on&cat170=on',
                            'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=18&cat152=on&cat153=on&cat165=on',
                            'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=19&cat154=on&cat163=on&cat171=on',
                            '',
                            '',
                            'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=22&cat176=on',
                            'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=23&cat78=on&cat79=on&cat80=on&cat162=on',
                            'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=23&cat78=on&cat79=on&cat80=on&cat162=on',
                            'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=25&cat157=on&cat158=on&cat159=on&cat172=on',
                            'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=26&cat160=on',
                            'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=27&cat161=on']
            url_web = ['https://www.youtube.com/watch?v=ozdqnEJ5C0U&ab_channel=%D0%98%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0%D0%95%D0%93%D0%AD%D0%A3%D0%BC%D1%81%D0%BA%D1%83%D0%BB',
                       'https://www.youtube.com/watch?v=Af_U6uXnBAU&ab_channel=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%D0%9A%D0%B0%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2',
                       'https://www.youtube.com/watch?v=1-Uyk7R0Als&ab_channel=%D0%98%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%91%D0%A3',
                       'https://www.youtube.com/watch?v=dvh5Dqtak84&ab_channel=%D0%98%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0%D0%95%D0%93%D0%AD%D0%A3%D0%BC%D1%81%D0%BA%D1%83%D0%BB',
                       'https://www.youtube.com/watch?v=e6LREsEYSgs&ab_channel=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%D0%9A%D0%B0%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2',
                       'https://www.youtube.com/watch?v=NgQDtUT-Cfg&ab_channel=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%D0%9A%D0%B0%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2',
                       'https://www.youtube.com/watch?v=mXfkEe1sHjQ&ab_channel=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%D0%9A%D0%B0%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2',
                       ['https://www.youtube.com/watch?v=2rGWq2BtnPo&ab_channel=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%D0%9A%D0%B0%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2',
                        'https://www.youtube.com/watch?v=3Rs1O5LrqVg&t=22s&ab_channel=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%D0%9A%D0%B0%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2'],
                       ['https://www.youtube.com/watch?v=qHnU8bL6W-E&ab_channel=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%D0%9A%D0%B0%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2',
                        'https://www.youtube.com/watch?v=qSOfcDi18f0&ab_channel=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%D0%9A%D0%B0%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2'],
                       'https://www.youtube.com/watch?v=ZEsZ9ykEfjM&ab_channel=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%D0%9A%D0%B0%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2',
                       'https://www.youtube.com/watch?v=bnczfcOM_Hw&ab_channel=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%D0%9A%D0%B0%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2',
                       'https://www.youtube.com/watch?v=kLAEaxh5yXY&ab_channel=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%D0%9A%D0%B0%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2',
                       'https://www.youtube.com/watch?v=KpnBfUWbO5c&ab_channel=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%D0%9A%D0%B0%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2',
                       'https://www.youtube.com/watch?v=FZUClCb-ous&ab_channel=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%D0%9A%D0%B0%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2',
                       'https://www.youtube.com/watch?v=R4_lZkSFAew&t=3540s&ab_channel=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%D0%9A%D0%B0%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2',
                       'https://www.youtube.com/watch?v=-0J6DR8CyhY&ab_channel=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%D0%9A%D0%B0%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2',
                       'https://www.youtube.com/watch?v=91-2WWjZG5s&ab_channel=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%D0%9A%D0%B0%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2',
                       'https://www.youtube.com/watch?v=yRyI0bRR1ME&ab_channel=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%D0%9A%D0%B0%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2',
                       'https://www.youtube.com/watch?v=saqqoCS6wjk&ab_channel=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%D0%9A%D0%B0%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2',
                       '',
                       '',
                       'https://www.youtube.com/watch?v=V-5BmDuaGLQ&ab_channel=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%D0%9A%D0%B0%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2',
                       'https://www.youtube.com/watch?v=7WPN3t6vCSs&ab_channel=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%D0%9A%D0%B0%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2',
                       ['https://www.youtube.com/watch?v=3brn26Ad-ek&ab_channel=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%D0%9A%D0%B0%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2',
                        'https://www.youtube.com/watch?v=lx7FFGuoCjc&ab_channel=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%D0%9A%D0%B0%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2',
                        'https://www.youtube.com/watch?v=sRxnrC9b5Ww&ab_channel=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%D0%9A%D0%B0%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2'],
                       'https://www.youtube.com/watch?v=74JxEWKWdco&ab_channel=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%D0%9A%D0%B0%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2',
                       'https://www.youtube.com/watch?v=T71dkr15eXs&ab_channel=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%D0%9A%D0%B0%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2',
                       'https://www.youtube.com/watch?v=K98d5gi24Rc&list=PLuvJDOAX0cZEYnutYGo2Ny7qiaqtC1iZx&ab_channel=%D0%98%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0%D0%95%D0%93%D0%AD-%D0%A8%D0%BA%D0%BE%D0%BB%D0%BA%D0%BE%D0%B2%D0%BE'
                       ]
            keyb = types.InlineKeyboardMarkup(row_width=1)
            key_tasks = types.InlineKeyboardButton(text='Задачи по теме', url=url_polyakov[number - 1])
            key_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data='tasks')
            if number == 8 or number == 9:
                key_web1 = types.InlineKeyboardButton(text='Вебинар 1', url=url_web[number - 1][0])
                key_web2 = types.InlineKeyboardButton(text='Вебинар 2', url=url_web[number - 1][1])
                key_tasks = types.InlineKeyboardButton(text='Задачи по теме', url=url_polyakov[number - 1])
                keyb.add(key_web1, key_web2, key_tasks)
            elif number == 24:
                key_web1 = types.InlineKeyboardButton(text='Вебинар 1', url=url_web[number - 1][0])
                key_web2 = types.InlineKeyboardButton(text='Вебинар 2', url=url_web[number - 1][1])
                key_web3 = types.InlineKeyboardButton(text='Вебинар 3', url=url_web[number - 1][2])
                key_tasks = types.InlineKeyboardButton(text='Задачи по теме', url=url_polyakov[number - 1])
                keyb.add(key_web1, key_web2, key_web3, key_tasks)
            else:
                key_web = types.InlineKeyboardButton(text='Вебинар', url=url_web[number - 1])
                keyb.add(key_web, key_tasks)
            keyb.add(key_back)
            bot.send_message(call.from_user.id, text=f'Материалы для изучения задания номер {number}:',
                             reply_markup=keyb)

        print(current_question)
        if call.data == "quiz":
            start_message = ("Отлично, тогда начнём игру! Всего будет 10 вопросов, к каждому "
                             "вопросу предлагается 4 варианта ответа, из которых только один верный")
            bot.send_message(call.from_user.id, text=start_message)
            q = get_question()
            bot.send_message(call.from_user.id, text=questions[q[0]], reply_markup=q[1])
        if call.data.startswith("ans"):
            data = call.data.split("_")
            if not (current_question == 10):
                if right_ans[int(data[2])] == int(data[1]):
                    bot.send_message(call.from_user.id, text="Верно! Идём дальше")
                    score += 1
                else:
                    bot.send_message(call.from_user.id, text="Неверно(")
                q = get_question()
                bot.send_message(call.from_user.id, text=questions[q[0]], reply_markup=q[1])
            else:
                if right_ans[int(data[2])] == int(data[1]):
                    bot.send_message(call.from_user.id, text="Верно!")
                    score += 1
                else:
                    bot.send_message(call.from_user.id, text="Неверно(")
                bot.send_message(call.from_user.id, text=f"Игра окончена!\nВаш счёт: {score}")
                current_question = 0
                nums.clear()
                return 0


bot.polling(none_stop=True, interval=0)
