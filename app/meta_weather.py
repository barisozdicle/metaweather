import datetime

import requests

from app.urls import MAIN_URL


class MetaWeather:

    def __init__(self, city):
        self.city = city
        self.tomorrow = datetime.date.today() + datetime.timedelta(days=1)

    def tomorrow_format(self):
        return str(self.tomorrow.strftime("%Y/%m/%d"))

    def find_location_woeid_id(self):
        try:
            url = MAIN_URL + "search/?query=" + self.city
            req = requests.get(url)
            return str(req.json()[0]["woeid"])
        except:
            return "Woeid Id Not Valid"

    def forecast(self):
        url = MAIN_URL + self.find_location_woeid_id() + "/" + self.tomorrow_format()
        req = requests.get(url)
        data = req.json()[0]
        self.weather_state_name = data['weather_state_name']
        self.temp = "%.1f" % data['the_temp'] + " °C"
        self.wind = "%.1f" % data['wind_speed'] + " mph"
        self.humidity = str(data['humidity']) + " %"

        print("Tomorrow {0} in {1}:\n{2}\nTemp: {3}\nWind: {4}\nHumidity: {5}".format(self.tomorrow_format(),
                                                                                      self.city.capitalize(),
                                                                                      self.weather_state_name,
                                                                                      self.temp,
                                                                                      self.wind,
                                                                                      self.humidity
                                                                                      )
              )

        return self.tomorrow_format(), self.city.capitalize(), self.weather_state_name, self.temp, self.wind, self.humidity
