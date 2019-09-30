import requests
from bs4 import BeautifulSoup
from datetime import datetime

def run():
    str_url = "http://school.cbe.go.kr/gukwon-h/M010301/list?s_idx="
    
    now_datetime = datetime.now()

    lst_result = []
    is_break = False

    for i in range(1, 10):
        response = requests.get(str_url + str(i))
        soup = BeautifulSoup(response.text, 'html.parser')

        lst_post = soup.select('table.usm-brd-lst tbody tr')
        
        for k in lst_post:
            lst_datetime = k.select_one('td.tch-dte').text.split('.')
            lst_element = []

            diff_days = (now_datetime - datetime(int('20' + lst_datetime[0]), int(lst_datetime[1]), int(lst_datetime[2]))).days

            if diff_days <= 30:
                last_tag = k.select_one('td.tch-tit a')
                lst_element.append(last_tag.text)
                lst_element.append(last_tag['href'])

                lst_result.append(lst_element)
            else:
                is_break = True
                break

        if is_break:
            break

    with open("data/Notice.dat", 'w', encoding='utf-8') as fp:
        fp.write(str(len(lst_result)) + '\n')
        
        for i in lst_result:
            fp.write(i[0] + '\n')
            fp.write('http://school.cbe.go.kr' + i[1] + '\n')