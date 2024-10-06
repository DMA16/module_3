import re

INCORRECT_EMAIL = "INCORRECT_EMAIL"
EMAILS_MATCH = "EMAILS_MATCH"
default_email = 'university.help@gmail.com'

def email_validation_check(email_sender: str, email_recipient: str):
    #Проверка корректности email
    for email in [email_sender, email_recipient]:
        if "@" not in email:
            print_exception(INCORRECT_EMAIL, email_sender, email_recipient)
            return False

        email_in_parts = re.split(r'[.]', email)

        if email_in_parts[-1] not in ['com', 'ru', 'net']:
            print_exception(INCORRECT_EMAIL, email_sender, email_recipient)
            return False

    # Проверка на отправку сообщений себе
    if email_sender == email_recipient:
        print_exception(EMAILS_MATCH, email_sender, email_recipient)
        return False

    return True


def print_exception(exception: str, email_sender: str, email_recipient: str):
    if exception == INCORRECT_EMAIL:
        print(f'Невозможно отправить письмо с адреса {email_sender} на адрес {email_recipient}.\n')

    if exception == EMAILS_MATCH:
        print('Нельзя отправить письмо самому себе!\n')


def send_email(message, recipient,*, sender = default_email):
    if email_validation_check(email_sender=sender, email_recipient=recipient):
        if sender == default_email:
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.\n")
        else:
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!\nПисьмо отправлено с адреса {sender} на адрес {recipient}.\n")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
