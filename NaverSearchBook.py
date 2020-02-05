import requests
from urllib.parse import quote
import json


# [CODE 1]
client_id = "EPUgDWSFhMVrEkAxRnXw"
client_secret = "EIURHTmyuc"


def make_naver_search_api_url(node, search_text, start_num, disp_num):
    base_url = 'https://openapi.naver.com/v1/search/' + node + '.json'
    param_query = "?query=" + quote(search_text)
    param_start = "&start=" + str(start_num)
    param_disp = "&display=" + str(disp_num)

    return base_url + param_query + param_start + param_disp

# 네이버 api call
def call(keyword, start):
    encText = quote(keyword)
    url = "https://openapi.naver.com/v1/search/blog?query = " + encText + "& display = 100" + "&start =" + str(start)
    result = requests.get(url=url,
                          headers={"X - Naver - Client - Id": client_id,
                                   "X - Naver - Client - Secret": client_secret}
    )
    print(result)  # Response [200]
    return result.json()


# 1000개의 검색 결과 받아오기
def get1000results(keyword):
    list = []
    for num in range(0, 10):
        list = list + call(keyword, num * 100 + 1)['items']  # list 안에 키값이 ’item’인 애들만 넣기
        return list

import urllib.request

url = "https://openapi.naver.com/v1/search/book.json"
option = "&display=3&sort=count"
query = "?query=" + urllib.parse.quote(input("질의:"))
url_query = url + query + option

# Open API 검색 요청 개체 설정
request = urllib.request.Request(url_query)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

# 검색 요청 및 처리
response = urllib.request.urlopen(request)
rescode = response.getcode()
if (rescode == 200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error code:" + rescode)


'''
list = []
result = get1000results("강남역 맛집")
result_2 = get1000results("강남역 찻집")
list = list + result + result_2

file = open("gangnam.json", "w+")  # gangnam.json 파일을 쓰기 가능한 상태로 열기 (만들기)
file.write(json.dumps(list))  # 쓰기
'''