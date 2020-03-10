import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone

def get_html(url):
    r = requests.get(url)
    return r.text

def get_today_temp(string):
    if string == 'погода':
        html = get_html(day_link(sinoptik_link, string))
        day = 'bd1'
    elif string == 'погода завтра':
        html = get_html(day_link(sinoptik_link, string))
        day = 'bd2'
    soup = BeautifulSoup(html, 'lxml')
    temp = soup.find('div', id=day).find('div', {'class': 'temperature'})
    return temp.text

def day_description(string):
    if string == 'погода':
        html = get_html(day_link(sinoptik_link, string))
    elif string == 'погода завтра':
        html = get_html(day_link(sinoptik_link, string))
    soup = BeautifulSoup(html, 'lxml')
    desc = soup.find('div', {'class': 'wDescription clearfix'}).find('div', {'class': 'rSide'})
    return desc.text


def day_link(url, string):
    time_now = datetime.now(timezone.utc).astimezone()
    time_now = time_now.strftime('%Y:%m:%d')
    time_now = time_now.replace(':', '-')

    url = url

    if string == 'погода':
        return url + time_now
    elif string == 'погода завтра':
        new_time = time_now[:-2] + str(int(time_now[-2::]) + 1)
        return url + new_time



sinoptik_link = 'https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BE%D0%B4%D0%B5%D1%81%D1%81%D0%B0/'

