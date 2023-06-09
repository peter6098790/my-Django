from abc import ABC, abstractmethod
import requests

#空氣品質網站抽象類別
class Website(ABC):

    def __init__(self, city_name):
        self.city_name = city_name 

    @abstractmethod
    def scrape(self): #抓網頁資料的抽象方法
        pass

# 行政院環境保護署API
class EPA(Website):
    def scrape(self):
        
        result = []
        url = 'https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON'

        #if self.city_name:
        data = requests.get(url) 
        data_json = data.json()

        for log in data_json['records']:
            country = log['county'] # 城市名稱

            if country[:2] ==  self.city_name:

                publishTime = log['publishtime'] #上傳時間
                siteName = log['sitename'] #測站名稱
                pm = log['pm2.5'] #pm2.5濃度
                aqi = log['aqi'] #AQI 指數
                airQuility = log['status'] #空氣品質

                result.append(
                    dict(publishTime = publishTime, country = country, siteName = siteName, pm = pm, aqi = aqi, airQuility = airQuility)
                )
        #print(result)
        return result