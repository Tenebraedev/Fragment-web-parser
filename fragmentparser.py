import requests
from bs4 import BeautifulSoup
import schedule
import time
import threading

def scrape_website(months, cookies, headers):
    params = {'months': months}
    response = requests.get('https://fragment.com/premium', params=params, cookies=cookies, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        radio_input = soup.find('input', {'type': 'radio', 'class': 'radio', 'name': 'months', 'value': months})

        if radio_input:
            div_tm_value = radio_input.find_next_sibling('div', {'class': 'tm-form-radio-label'}).find('div', {'class': 'tm-value icon-before icon-ton'})

            if div_tm_value:
                value = div_tm_value.text.strip()
                print(f'Значение подписки ({months} месяцев): {value}')
            else:
                print(f'Элемент <div class="tm-value icon-before icon-ton"> не найден для {months} месяцев.')
        else:
            print(f'Элемент <input> не найден для {months} месяцев.')
    else:
        print(f'Ошибка при получении страницы для {months} месяцев: {response.status_code}')

def start_schedule(months, cookies, headers):
    schedule.every(0.15).minutes.do(scrape_website, months, cookies, headers)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    cookies = {
 }

headers = {
  }

    thread12 = threading.Thread(target=start_schedule, args=('12', cookies, headers))
    thread6 = threading.Thread(target=start_schedule, args=('6', cookies, headers))
    thread3 = threading.Thread(target=start_schedule, args=('3', cookies, headers))

    thread12.start()
    thread6.start()
    thread3.start()

    thread12.join()
    thread6.join()
    thread3.join()
