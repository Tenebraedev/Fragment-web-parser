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
    'stel_ssid': '24201b00834bda24ce_15184294661743886494',
    'stel_dt': '-180',
    'stel_ton_token': '8zn92pIrIb0T1QIxyoIWhEF8z7uMIeq_WiJzL-3ApceNmWFrS-aRwcLM8a2edZT_qZrLLSiRoS21wcZrIenbq76rDqQmP8HzsrVNBd1qe9Iql-7DV7ogtTp_VxUlpxUXnzMebPEl5_1YyugXtooseR-KMvR_cLQKD0ZyNQL9O4904MjUQMs',
}

headers = {
    'authority': 'fragment.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'stel_ssid=24201b00834bda24ce_15184294661743886494; stel_dt=-180; stel_ton_token=8zn92pIrIb0T1QIxyoIWhEF8z7uMIeq_WiJzL-3ApceNmWFrS-aRwcLM8a2edZT_qZrLLSiRoS21wcZrIenbq76rDqQmP8HzsrVNBd1qe9Iql-7DV7ogtTp_VxUlpxUXnzMebPEl5_1YyugXtooseR-KMvR_cLQKD0ZyNQL9O4904MjUQMs',
    'referer': 'https://fragment.com/premium?months=3',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "YaBrowser";v="23"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
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
