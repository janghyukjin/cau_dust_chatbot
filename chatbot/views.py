from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
import json
import requests


def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons': ['흑석', '안성']
    })


@csrf_exempt
def message(request):
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content']
    dust =3
    if return_str == '흑석':
        dustgrade = findDustGrade('동작구')
        dustvalue = findDustValue('동작구')
    if return_str == '안성':
        dustgrade = findDustGrade('봉산동')
        dustvalue = findDustValue('봉산동')

    image_url = ""
    if dustgrade == '좋음':
        image_url = 'https://raw.githubusercontent.com/janghyukjin/cau_dust_chatbot/master/src/laughing.png'
    elif dustgrade == '보통':
        image_url = 'https://raw.githubusercontent.com/janghyukjin/cau_dust_chatbot/master/src/muted.png'
    elif dustgrade == '나쁨':
        image_url = 'https://raw.githubusercontent.com/janghyukjin/cau_dust_chatbot/master/src/tongue.png'
    else :
        image_url = 'https://raw.githubusercontent.com/janghyukjin/cau_dust_chatbot/master/src/angel.png'
    return JsonResponse({
        'photo': {'url': image_url,
                  'width': 128,
                  'height': 128
                  },
        'message': {
            'text': return_str + "의 미세먼지 농도는 " + str(dustvalue) + "이고, " + return_str + "의 미세먼지 단계는 " + str(dustgrade) + "입니당"
        },
        'keyboard': {
            'type': 'buttons',
            'buttons': ['흑석','안성']
        }
    })

def findDustGrade(station):
    url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName='
    stationName = station
    params = '&dataTerm=month&pageNo=1&numOfRows=10&ServiceKey=ay6El74FK5OaJ2Go2htYV%2BmXjF5Qc%2FT2IsuWcIhJiAPd7lkq27HBAG%2BwMDYvQxO9%2ByjoLmm7PvUh52dsCA18VA%3D%3D&ver=1.3'

    r = requests.get(url + stationName + params)
    soup = BeautifulSoup(r.text, "lxml")
    try:
        pmGrade = soup.find('pm10grade')
        result = pmGrade.get_text()
        status = ''
        if result == '1':
            status = '좋음'
        if result == '2':
            status = '보통'
        if result == '3':
            status = '나쁨'
        if result == '4':
            status = '매우나쁨'
        return status
    except AttributeError:
        print(1)

def findDustValue(station):
    url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName='
    stationName = station
    params = '&dataTerm=month&pageNo=1&numOfRows=10&ServiceKey=ay6El74FK5OaJ2Go2htYV%2BmXjF5Qc%2FT2IsuWcIhJiAPd7lkq27HBAG%2BwMDYvQxO9%2ByjoLmm7PvUh52dsCA18VA%3D%3D&ver=1.3'

    r = requests.get(url + stationName + params)
    soup = BeautifulSoup(r.text, "lxml")
    try:
        pmValue = soup.find('pm10value')
        result = pmValue.get_text()
        return result
    except AttributeError:
        print(1)
