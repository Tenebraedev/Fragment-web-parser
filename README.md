# Парсер fragment.com

Этот Python-скрипт предназначен для парсинга данных по цене premium с сайта fragment.com.

## Зависимости

Для запуска скрипта вам потребуется установить следующие библиотеки:

- `requests`
- `beautifulsoup4`
- `schedule`

Вы можете установить их с помощью `pip`:

```bash
pip install requirements.txt
```
## Использование
Запустите скрипт fragmentparser.py:
```python
python fragmentparser.py
```
Скрипт начнет парсить данные с сайта fragment.com и выводить результаты в командной строке.

Вы можете настроить параметры внутри скрипта, такие как интервал обновления данных и параметры запроса.

```python
def start_schedule(months, cookies, headers):
    schedule.every(0.15).minutes.do(scrape_website, months, cookies, headers)
```
0.15 = 15 секунд интервал между запросами

Параметры запроса
</br>Вам нужно зарегистрироваться на сайте fragment.com используя ваш кошелек TON
<img width="406" alt="image" src="https://github.com/Tenebraedev/Fragment-web-parser/assets/80919466/ad4c944e-1bd0-4db6-b0ce-038107490a79"></br>
Сканируете qr-code либо нажимаете кнопку авторизоваться через tonkeeper</br>
![image](https://github.com/Tenebraedev/Fragment-web-parser/assets/80919466/0c06d6a3-73ce-4f3d-b959-6b9281b549e0)</br>
Получаете вот такое окно</br>
![image](https://github.com/Tenebraedev/Fragment-web-parser/assets/80919466/2a79676c-803a-45b5-a2eb-0969d12821fd)</br>
Нажимаете исследовать элемент</br>
![image](https://github.com/Tenebraedev/Fragment-web-parser/assets/80919466/22d34aa9-a9e4-4f1c-8cba-ba0a52c39ce0)</br>
Затем переходим во вкладку Network(сеть) и перезагружаем страницу</br>
Самый первый элемент копируем как curl(bash)</br>
![image](https://github.com/Tenebraedev/Fragment-web-parser/assets/80919466/d5db87ae-f764-440b-8e8e-d7032e663888)</br>
И переходим на curlconverter.com</br>
Из полученного результата нас интересует headers и cookies</br>
![image](https://github.com/Tenebraedev/Fragment-web-parser/assets/80919466/3d7a836f-cd39-41f1-bb9d-444c10f6f1ea)</br>
и вставляем его в коде
