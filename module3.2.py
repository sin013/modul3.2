a = True


def send_email(message, recipient, *, sender='university.help@gmail.com'):
    global a
    if recipient.endswith('.ru' or '.com' or '.net'):
        a = True
    else:
        print(f'Невозможно отправить письмо с адреса{sender} на адрес{recipient}')
    for i in recipient:
        if recipient.find('@'):
            a = True
        else:
            print(f'Невозможно отправить письмо с адреса{sender} на адрес{recipient}')

    if sender.endswith('.ru' or '.com' or '.net'):
        a = True
    else:
        print(f'Невозможно отправить письмо с адреса{sender}на адрес{recipient}')
    for i in sender:
        if sender.find('@'):
            a = True
        else:
            print(f'Невозможно отправить письмо с адреса{sender} на адрес{recipient}')
    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    else:
        a = True
    if a == True and sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    if a == True and sender != 'university.help@gmail.com':
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
