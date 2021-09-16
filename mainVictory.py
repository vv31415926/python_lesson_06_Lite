import victory  as v
import random

def startGame():

    nYes = 0
    nNo = 0

    dicItGM = list( v.getGreatMan().items() )
    dicManGame = random.choices( dicItGM, k=5 )  # люди для игры

    for name, bDay in dicManGame:
        dateIn = input('Введите дату рождения (дд.мм.гггг) для {}: '.format(name))
        if bDay != dateIn:
            nNo += 1
            print('Правильная дата рождения: ', v.bDayOut(bDay))
        else:
            nYes += 1
            print('Правильно!')
    print('\nПравильных ответов - {} ({}%)\nОшибок - {}\n'.format(nYes, int(nYes / len(dicManGame) * 100), nNo))

    print("Конец игре.")

endGame = False
while endGame == False:
    startGame()

    n = input( 'Желаете повторить игру? (1-Да, 0-Нет): ' )
    if n == '0':
        print('До свидания!' )
        endGame = True