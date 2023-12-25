import telebot
import key
from telebot import types
import random

bot = telebot.TeleBot(key.keyword)

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
               ["Нет особенностей", "Правая граница не включается", "Обе границы не включаются", "Нельзя использовать без for"],
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
            keyboard = types.InlineKeyboardMarkup()
            ans0 = types.InlineKeyboardButton(text=ans[current_num][0], callback_data=f'ans_0_{current_num}')
            keyboard.add(ans0)
            ans1 = types.InlineKeyboardButton(text=ans[current_num][1], callback_data=f'ans_1_{current_num}')
            keyboard.add(ans1)
            ans2 = types.InlineKeyboardButton(text=ans[current_num][2], callback_data=f'ans_2_{current_num}')
            keyboard.add(ans2)
            ans3 = types.InlineKeyboardButton(text=ans[current_num][3], callback_data=f'ans_3_{current_num}')
            keyboard.add(ans3)
            nums.add(current_num)
            flag = True
            current_question += 1
        else:
            current_num = random.randrange(0, 10)
    return [current_num, keyboard]

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Приветствую! Чтобы получить список возможностей напишите /start")
    elif message.text == "/start":
        keyboard = types.InlineKeyboardMarkup()
        key_quiz = types.InlineKeyboardButton(text='Квиз по Python', callback_data='quiz')
        keyboard.add(key_quiz)
        question = "Вы хотите сыграть в викторину по Python?"
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, "Я вас не понимаю! Чтобы сыграть в викторину напишите /start!")

@bot.callback_query_handler(func=lambda call: True)
def quiz_call(call):
    global current_question, score, nums
    print(current_question)
    if call.data == "quiz":
        start_message = "Отлично, тогда начнём игру! Всего будет 10 вопросов, к каждому вопросу предлагается 4 варианта ответа, из которых только один верный"
        bot.send_message(call.from_user.id, text=start_message)
        q = get_question()
        bot.send_message(call.from_user.id, text = questions[q[0]], reply_markup=q[1])
    if call.data.startswith("ans"):
        data = call.data.split("_")
        if not(current_question == 10):
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