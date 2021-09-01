#!/usr/bin/env python3

import time
import requests
import telegram_send

# config:
URL = 'https://sci-intern.hm.edu/fk/enroll.php?sem_nr=42&studiengruppe=BOB4'
USER = 'Griffin Peter'
PWRD = 'hehehehehehehe'
SUBSTRING = '0/0'
SLEEP_SECONDS = 10800


def count_given_string(text, string):
    x = str(text).count(str(string))
    return x


def get_website_text(url, user, pwrd):
    r = requests.get(url, auth=(user, pwrd))
    text = r.text
    return text


def nothing_happened():
    # send_telegram_message('nothing happened')
    pass


def something_happened():
    send_telegram_message('something happened! Link:')
    send_telegram_message(URL)


def send_telegram_message(message_text):
    message = [str(message_text)]
    telegram_send.send(messages=message)


def main():
    # -------------------------
    # Where the Magic happens:
    # -------------------------

    # initial website status:
    compare_1 = get_website_text(URL, USER, PWRD)
    print('running...')
    send_telegram_message('running...\n'
                          '"{0}" was found {1}x'.format(SUBSTRING, count_given_string(compare_1, SUBSTRING)))
    time.sleep(SLEEP_SECONDS)

    while True:
        try:
            # website status to compare with
            compare_2 = get_website_text(URL, USER, PWRD)

            # count how often substring occurs, compare and raise reaction fuction
            if count_given_string(compare_1, SUBSTRING) == count_given_string(compare_2, SUBSTRING):
                nothing_happened()
            else:
                something_happened()
                # set new website version as status quo
                compare_1 = compare_2
            # wait for next request
            time.sleep(SLEEP_SECONDS)
            continue
        except Exception:
            print('{0}: An exeption occured'.format(time.strftime('%d %b %Y %H:%M', )))
            send_telegram_message('An exeption occured')


if __name__ == '__main__':
    main()
