import folium
import pandas as pd
import urllib.request
import datetime
import time
import json
import webbrowser


# [CODE 1]
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



# [CODE 2]

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


    jsonAddress = json.loads(retData)

    item = jsonAddress['addresses'][0]

    latitude = item['y']
    longitude = item['x']

    '''
    if 'result' in jsonAddress.keys():
        latitude = jsonAddress['result']['items'][0]['point']['y']
        longitude = jsonAddress['result']['items'][0]['point']['x']
    else:
        return None
    '''

    return [latitude, longitude]


def main():
    # [CODE 3]
    max = 20
    map = folium.Map(location=[37.5103, 126.982], zoom_start=12)

    filename = 's.csv'
    df = pd.DataFrame.from_csv(filename, encoding='EUC-KR', index_col=0, header=0)
    geoData = []

    df = df.iloc[0:max] # first five rows of dataframe
    # [CODE 4]

    for index, row in df.iterrows():
        geoData = getGeoData(row['주소'])
        print(geoData)
        if geoData != None:
            folium.Marker(geoData, popup=row['학교명'], icon=folium.Icon(color='red')).add_to(map)

        if index == max:
            break

    svFilename = 'elementary_school.html'
    map.save(svFilename)
    #webbrowser.open(svFilename)


if __name__ == "__main__":
    main()