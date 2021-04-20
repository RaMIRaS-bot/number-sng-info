# osint-san
import os
from grab import Grab
# Color
WHSL = C = "\033[32;1m"
ENDL = W = "\033[0m"
REDL = R = "\033[0;31m"
GNSL = G = "\033[1;34m"
WHITEL = B = "\033[39m"


page_8 = f''' {GNSL}

  {WHSL}Модификация поиска по номеру телефона
   
  {WHSL}Версия {GNSL}0.7{REDL} beta
  ⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀                                     
  ⠀⠀⠀⡏⢢⡁⠂⠤⣀⣀⣀⣀⣀ ⠤⠐⢈⡔⢹                          
  ⠀⠀⠀⢿⡀⠙⠆⠀⠉⠀⠀⠀⠀⠉⠀⠰⠋⢀⡿                          
⠀ ⠀⠀⠀⠈⢷⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡾⠁                          
⠀ ⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹                 
  ⣰⠊⠉⠉⠉⡇⠀⠢⣤⣄⠀⠀ ⣠⣤⠔⠀⢸
  ⠙⠓⠒⢦⠀⠱⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠎                
  ⠀⠀⠀⠀⡇⠀⠀⠏⠑⠒⠀⠉⠀⠒⠊⠹                 
  ⡎⠉⢹⠀⠙⡶⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⠀⠀⡏⠉⢱
  ⢧⡈⠛⠉⠉⠀⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⠉⠉⠋⢁⡼      
  ⠀⢉⣿⠖⠚⠛⢋⢀⠀⠀⠀⠀⠀⠀⠀⡀⡙⠛⠓⠲⣿⣄        
  ⠀⢸⡇⠀⠀⠀⡞⠁⠈⡃⠀⠀⠀⠀⢘⠁⠈⢳⠀⠀⠀⢸⡇
  ⠀⠈⢷⣄⠀⠀⠙⠦⠌⠑⠢⠤⠔⠊⠁⢠⠎⠀⠀⣠⡾⠁
⠀  ⠀⠀⠈⠛⠲⠤⣤⣀⣀⣀⣀⣠⣤⣚⣡⠤⠖⠛⠁

 {WHSL}Больше инструментов в OSINT-SAN
  
 {GNSL}https://github.com/Bafomet666/OSINT-SAN
 {GNSL}https://t.me/osint_san_framework
   
 {REDL}_______________________________________'''

os.system("printf '\033]2; OSINT SAN mod \a'")


def number():
    os.system('clear')
    print(page_8)
    g = Grab()
    print(f'\n {WHSL}Введите номер телефона, без кода страны')
    print(f'\n {WHSL}Пример: {GNSL}9262063265\n')
    number = input(
        f" {REDL}[ {GNSL}+ {REDL}] {WHSL}Ожидаем ввод номера:{GNSL} ")
    g.go('http://phoneradar.ru/phone/' + number)
    try:
        operator = g.doc.select('//*[@class="table"]/tbody/tr[1]/td[2]').text()
        region = g.doc.select('//*[@class="table"]/tbody/tr[2]/td[2]').text()
        sity = g.doc.select('//*[@class="table"]/tbody/tr[3]/td[2]/a').text()
        search_number = g.doc.select('//*[@class="table"]/tbody/tr[4]/td[2]').text()
        views_number = g.doc.select('//*[@class="table"]/tbody/tr[5]/td[2]').text()
        positive_reviews = g.doc.select('//*[@class="table"]/tbody/tr[6]/td[2]').text()
        negative_reviews = g.doc.select('//*[@class="table"]/tbody/tr[7]/td[2]').text()
        neutral_reviews = g.doc.select('//*[@class="table"]/tbody/tr[8]/td[2]').text()

        print(f"\n{REDL} Базовые данные о номере:\n")
        print(f" {WHSL}Оператор            :{GNSL} {operator}")
        print(f" {WHSL}Регион              :{GNSL} {region}")
        print(f" {WHSL}Город               :{GNSL} {sity}")
        print(f" {WHSL}Поисков номера      :{GNSL} {search_number}")
        print(f" {WHSL}Просмотров номера   :{GNSL} {views_number}")
        print(f" {WHSL}Положительные отзывы:{GNSL} {positive_reviews}")
        print(f" {WHSL}Отрицательные отзывы:{GNSL} {negative_reviews}")
        print(f" {WHSL}Нейтральные отзывы  :{GNSL} {neutral_reviews}")
        print(f" \n{WHSL} Обязательно оставляйте отзывы о номере")
        print(f' {WHSL}Нам важен каждый отзыв )')
        print(f" \n{REDL} Комментарии к номеру\n")
        print(f'\n{WHSL} Первый уровень комментариев:')
        print(f' {REDL}+++++++++++++++++++++++++++++++++++++++')
        try:
            for elem in g.doc.select('//*[@class="card-body"]/div[3]/div'):
                review = elem.select('div[2]').text()
                print(f'\n {REDL}[{WHSL}{review}{REDL}]')
                print(f' {REDL}=======================================')

        except:
            print(f" {WHSL}Отзывов не найдено")
    except:
        print(f' {WHSL}Информация не найдена')

    print(f'\n{WHSL} Второй уровень комментариев:')
    print(f' {REDL}+++++++++++++++++++++++++++++++++++++++')
    g.go(f'https://po-nomeru.ru/phone/{number}/')
    try:
        for elem in g.doc.select('//*[@class="row"]/blockquote'):
            avtor_review = elem.select('h3').text()
            review = elem.select('p').text()
            print(f' \n {REDL}[{GNSL}{avtor_review}:{WHSL} {review}{REDL}]\n')
            print(f' {REDL}=======================================')
        if not avtor_review:
            print(f" {WHSL}Отзывов не найдено\n")
    except:
        print(f"Нет отзывов!\n")
    print(f' \n Вы желаете оставить отзыв о номере ?\n')
    print(
        f' {REDL}[ {GNSL}1 {REDL}] - {WHSL}Да       {REDL}[ {GNSL}2 {REDL}] -{WHSL} Нет\n')
    zapros = input(f' {WHSL}\n Введите опцию: {GNSL}')
    print('')
    if zapros == '1':
        os.system('clear')
        print(f' {REDL}____________________________________________')
        print(f' {WHSL}Используйте любое имя, отзыв будет оставлен анонимно')
        print(f' {WHSL}Но я бы на вашем месте не отказался от proxy/vpn')
        name = input(f'\n {WHSL}Введите ваше имя: {GNSL}')
        message = input(f'\n {WHSL}Введите ваш отзыв о владельце номера:{GNSL} ')
        rating = input(f'\n {GNSL}Выберите рейтинг человека:\n'

                       f'{REDL} [ {GNSL}1 {REDL}] -{WHSL} Положительный, можно звонить и отвечать на звонок.\n'
                       f'{REDL} [ {GNSL}2 {REDL}] -{WHSL} Отрицательный, не отвечать на звонок с этого номера.\n'
                       f'{REDL} [ {GNSL}3 {REDL}] -{WHSL} Нейтральный.\n Введите рейтинг: ')
        g.setup(headers={'X-Requested-With': 'XMLHttpRequest',
                         'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                         'Origin': 'https://po-nomeru.ru'})
        g.setup(post={'name': name,
                      'message': message,
                      'rating': rating,
                      'number': number,
                      'action': 'addReview'})
        g.go('https://po-nomeru.ru/comments/')
        print(f' \n{REDL} Поздравляю !!! Ваш отзыв добавлен. ')
    else:
        pass
        os.system('clear')


number()
