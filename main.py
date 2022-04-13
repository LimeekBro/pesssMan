import random
import time
def pas():
    print('lol')

options = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
q1 = random.choice(options)
q2 = random.choice(options)
q3 = random.choice(options)
q4 = random.choice(options)
q5 = random.choice(options)
q6 = random.choice(options)
q7 = random.choice(options)
q8 = random.choice(options)
q9 = random.choice(options)
q10 = random.choice(options)
q11 = random.choice(options)
q12 = random.choice(options)
q13 = random.choice(options)
q14 = random.choice(options)
q15 = random.choice(options)
q16 = random.choice(options)
q17 = random.choice(options)
q18 = random.choice(options)
q19 = random.choice(options)
q20 = random.choice(options)
cv1 = random.randint(0,9)
cv2 = random.randint(0,9)
cv3 = random.randint(0,9)
cv4 = random.randint(0,9)
cv5 = random.randint(0,9)



#Стартовые переменные
a = 0
m = 0
fg = 0
def reset():
    col1 = input('capcha: Введите любое числовое значение для того что-бы убедится что вы не бот\n')
    check = col1.isdigit()
    time.sleep(0.5)
    if check == True:
        a = 0
        m = 1
        while int(a) != int(col1):
            a = a + 1

            while fg != int(col1):
                time.sleep(0.1)
                print('Loading.')
                time.sleep(0.1)
                print('Loading..')
                time.sleep(0.1)
                print('Loading...')
                time.sleep(0.1)
                print('Loading.')
                time.sleep(0.1)
                print('Loading..')
                time.sleep(0.1)
                print('Loading..')
                time.sleep(0.1)
                print('Loading...')
                time.sleep(0.1)
                print('Loading.')

                print(str(q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8 + q9 + q10 + q11 + q12 + q13 + q14 + q15 + q16 + q17 + q18 + q19 + q20))
                print('Буквеный пароль готов, хотите добавить цифр и сделать пароль надёжнее?(Пропишите s1)\nЕсли хотите убрать половину чисел пропишите s2')
                sdf = input('///')
                if sdf == 's2':
                    print(str(q1 + q4 + q5 + q6 + q7 + q8 + q9 + q10 + q11 + q12))
                    time.sleep(2)
                elif sdf == 's1':
                    print(q1 + q2 + str(cv1) + str(cv3) + q5 + q6 + q7 + q8 + str(cv2) + q10 + q11 + q12 + q13 + str(cv4) + q15 + q16 + str(cv5) + q18 + q19 + q20)
            m = 1
    else:
        print('Это не цифра!')
        reset()


asd = reset()
if m >= 0:
    asd = print('')


asd
pas()