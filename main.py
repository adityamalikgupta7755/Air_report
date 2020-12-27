import requests
from tabulate import tabulate
url='https://api.waqi.info/feed/lucknow/?token=2f715311d805afcb108432479fc49ea44613d202'

data = requests.get(url).json()

data1 = data['data']

print("""\
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                                 Air Quality forecast                                                                                         
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
""")


data_time = data['data']['time']['s'] #Measurement time infomration
data_time_tz = data['data']['time']['tz']  
print("Time Zone :-",data_time_tz)
print("     ")
print("Date :-",data_time)
print("-----------------------------------Detail-------------------------------------------------")
#EPA Attribution for the station
data_attributionsNCPCB = data['data']['attributions'][0]['name']
data_attributionsNCPCB_url = data['data']['attributions'][0]['url']
print("     ")
print("Name of Central Pollution Control Board :-",data_attributionsNCPCB)
print("     ")
print("Link :-",data_attributionsNCPCB_url)
print("     ")

data_city = data['data']['city']  #	Information about the monitoring station.
data_city_geo_lat = data['data']['city']['geo'][0]
data_city_geo_log= data['data']['city']['geo'][1]
data_city_name = data['data']['city']['name']
data_city_url = data['data']['city']['url']
print("coordinate Latitude:-",data_city_geo_lat,"Londitude :-",data_city_geo_log)
print("     ")
print("City name :-",data_city_name)
print("     ")
print("Link :-",data_city_url)
print("     ")
print("******************************************************************************************")
data_aqi ="Today Air Quality :- "+str( data['data']['aqi'])  #Real-time air quality infomrmation
y= data_aqi.center(90, " ")
print(y)
print("******************************************************************************************")


data_iaqi_co = data['data']['iaqi']['co']['v'] 
data_iaqi_dew = data['data']['iaqi']['dew']['v']
data_iaqi_no2 = data['data']['iaqi']['no2']['v']
data_iaqi_o3 = data['data']['iaqi']['o3']['v']
data_iaqi_so2 = data['data']['iaqi']['so2']['v']
data_iaqi_pm10 = data['data']['iaqi']['pm10']['v']
data_iaqi_pm25 = data['data']['iaqi']['pm25']['v'] #Measurement time infomration.
print(" co :-",data_iaqi_co,'\n\n',"No2 :-",data_iaqi_no2,'\n\n',
"Ozone :-",data_iaqi_o3,'\n\n',"So2 :-",data_iaqi_so2,'\n\n',
"PM10",data_iaqi_pm10,'\n\n',"PM2.5",data_iaqi_pm25,'\n\n',
"Amount of moisture",data_iaqi_dew)



data_forecast = data['data']['forecast']  #Forecast data
data_forecast_daily = data['data']['forecast']['daily'] #Daily forecast data
data_forecast_daily_o3 = data['data']['forecast']['daily']['o3'] #Ozone forecast
print("""\
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                                 Ozone forecast                                                     
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
""")
for o3 in data_forecast_daily_o3:
    data_o3_day = o3['day']
    data_o3_avg = o3['avg']
    data_o3_max = o3['max']
    data_o3_min = o3['min']
    print("| Date:- ",data_o3_day,"|| Average :-",data_o3_max,
    "|| Maximum :-",data_o3_max,"|| Minimum :-",data_o3_min," |") 

data_forecast_daily_pm10 = data['data']['forecast']['daily']['pm10'] #PM10 forecast
print("""\
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                                 PM10 forecast                                                     
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
""")
for pm10 in data_forecast_daily_pm10:
    data_pm10_day = pm10['day']
    data_pm10_avg = pm10['avg']
    data_pm10_max = pm10['max']
    data_pm10_min = pm10['min']
    print("| Date:- ",data_pm10_day,"|| Average :-",data_pm10_max,
    "|| Maximum :-",data_pm10_max,"|| Minimum :-",data_pm10_min," |")

data_forecast_daily_pm25 = data['data']['forecast']['daily']['pm25'] #PM2.5 forecast
print("""\
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                                 PM2.5 forecast                                                     
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
""")
for pm25 in data_forecast_daily_pm25:
    data_pm25_day = pm25['day']
    data_pm25_avg = pm25['avg']
    data_pm25_max = pm25['max']
    data_pm25_min = pm25['min']
    print("| Date:- ",data_pm25_day,"|| Average :-",data_pm25_max,
    "|| Maximum :-",data_pm25_max,"|| Minimum :-",data_pm25_min," |")

data_forecast_daily_uvi = data['data']['forecast']['daily']['uvi'] #Ultra Violet Index forecast
print("""\
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                                 Ultra Violet Index forecast                                                     
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
""")
for uvi in data_forecast_daily_uvi:
    data_uvi_day = uvi['day']
    data_uvi_avg = uvi['avg']
    data_uvi_max = uvi['max']
    data_uvi_min = uvi['min']
    print("| Date:- ",data_uvi_day,"|| Average :-",data_uvi_max,
    "|| Maximum :-",data_uvi_max,"|| Minimum :-",data_uvi_min," |")
print("------------------------------------------------------------------------------------------")






