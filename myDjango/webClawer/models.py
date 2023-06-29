from django.db import models

# Create your models here.
class AirData(models.Model):
    publishTime = models.CharField(max_length=20,verbose_name='紀錄時間')
    country = models.CharField(max_length=10,verbose_name='縣市')
    site_name = models.CharField(max_length=10,verbose_name='測站')
    pm = models.CharField(max_length=10,verbose_name='PM2.5濃度')
    aqi = models.CharField(max_length=10,verbose_name='AQI指數')
    airQuility =models.CharField(max_length=10,verbose_name='空氣品質')
    
    # 自定義資料名稱
    class Meta:
        db_table = 'AirData'