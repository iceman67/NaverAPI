import os
import sys
import urllib.request
import datetime
import time
import json
from config import *
import pandas as pd

client_id = "l0cwbt4cr5"
client_secret = "Nu0GZfLlsCs8jWwFqZf9v5wLhmUVjseDgHDG3mLI"
def get_request_url(url):

    req = urllib.request.Request(url)
    req.add_header("X-NCP-APIGW-API-KEY-ID", client_id)
    req.add_header("X-NCP-APIGW-API-KEY", client_secret)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print ("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


def getGeoData(address):

    base = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
    node = ""
    parameters = "?query=%s" % urllib.parse.quote(address)
    url = base + node + parameters

    retData = get_request_url(url)
    print(retData)

    if (retData == None):
        print("결과 없음")
        return None
    else:
        return json.loads(retData)


for x in range(1):
    req_addr = '서울특별시 종로구 세종로 81-3'
    print('\n\n')
    jsonResult = getGeoData(req_addr)

    if 'addresses' in jsonResult.keys():
        print('총 검색 결과: ', jsonResult['meta']['totalCount'])
        print('요청 주소: ', req_addr)

        item =  jsonResult['addresses'][x]
        print('---------------------------------------------------')
        print('주소: ', item['roadAddress'])
        print('위도: ', str(item['y']))
        print('경도: ', str(item['x']))

    now = datetime.datetime.now()
    now_time = now.strftime('%Y-%m-%d %H:%M:%S')
    times = []



    # 저장
    # success_df.to_csv("final_list.csv", mode='w', index=False, encoding='euc-kr')