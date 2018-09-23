from random import randint

first= ["Однажды, ","Сегодня ", "Вчера ",  "Прямо сейчас "]
name = ["шард ", "hxshard ", "пидорас ", "еблан "]
glagol = ["упал ","пошел ", "высрал ", "обосрался ", "пососал ", "отсосал "]
kyda = ["в онал мыша ", "в озеро ", "в канаву ", "в свою мамку ", "в пизду ",  "в член ", "в xui ", "на хуй "]
glagol2 = ["и сказал", "и выблевал", "и высрал", "и крикнул"]
bots = ["Connorbot ", "TriviaSearch ", "HQSearch ", "Trivia24 ", "QQuack ", "Apihot ", "53corp ", "Я "]
chto = ["говно!", "высер!", "срань!", "лучший бот!", "збс!"]
joke = first[randint(0, 3)]+name[randint(0, 3)]+glagol[randint(0, 5)]+kyda[randint(0, 7)]+glagol2[randint(0, 3)]+": '"+bots[randint(0, 7)]+chto[randint(0, 4)]+"'"
print(joke)
