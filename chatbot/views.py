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
        dust = findDustGrade('동작구')
    if return_str == '안성':
        dust = findDustGrade('봉산동')

    return JsonResponse({
        'message': {
            'text': return_str + "의 미세먼지 단계는!" + str(dust)
        }
    })

def findDustGrade(station):
    url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName='
    stationName = station
    params = '&dataTerm=month&pageNo=1&numOfRows=10&ServiceKey=ay6El74FK5OaJ2Go2htYV%2BmXjF5Qc%2FT2IsuWcIhJiAPd7lkq27HBAG%2BwMDYvQxO9%2ByjoLmm7PvUh52dsCA18VA%3D%3D&ver=1.3'

    r = requests.get(url + stationName + params)
    soup = BeautifulSoup(r.text, "lxml")
    try:
        pmGrade = soup.find('pm25grade')
        result = pmGrade.get_text()
        return result
    except AttributeError:
        print(1)
