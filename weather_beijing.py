import urllib.request
import json
from datetime import datetime

def get_beijing_weather():
    url = "https://wttr.in/Beijing?format=j1"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode())
        current = data['current_condition'][0]
        temp_C = current['temp_C']
        weatherDesc = current['weatherDesc'][0]['value']
        winddir = current['winddir16Point']
        windspeed = current['windspeedKmph']
        humidity = current['humidity']
        feelsLike = current['FeelsLikeC']
        uvIndex = current['uvIndex']

        tomorrow = data['weather'][1]
        tomorrow_max = tomorrow['maxtempC']
        tomorrow_min = tomorrow['mintempC']
        tomorrow_desc = tomorrow['hourly'][4]['weatherDesc'][0]['value']

        print("=" * 50)
        print(f"北京天气预报 - {datetime.now().strftime('%Y年%m月%d日 %H:%M')}")
        print("=" * 50)
        print(f"\n【今日天气】")
        print(f"  天气状况：{weatherDesc}")
        print(f"  气温：{temp_C}°C（体感 {feelsLike}°C）")
        print(f"  风向风力：{winddir} {windspeed}km/h")
        print(f"  相对湿度：{humidity}%")
        print(f"  紫外线指数：{uvIndex}")
        print(f"\n【明日天气】")
        print(f"  天气状况：{tomorrow_desc}")
        print(f"  气温：{tomorrow_min}°C ~ {tomorrow_max}°C")
        print("=" * 50)
    except Exception as e:
        print(f"获取天气信息失败：{e}")

if __name__ == "__main__":
    get_beijing_weather()
