import requests
import json
import pandas as pd


# go to https://openweathermap.org/ and create your API key for free. Past it as a string and it's all done!

API_key = ""
CITY = "Messina"

base_url = f"https://api.openweathermap.org/data/2.5/weather?"
url = base_url + "appid=" + API_key + "&q=" + CITY + "&units=metric"

response = requests.get(url).json()
print(response.keys())

weather = response['weather'][0]
main = response['main']
sys_id = response['sys']
name = response['name']


df = pd.DataFrame.from_dict(weather, orient='index')

df2 = pd.DataFrame.from_dict(main, orient='index')

df3 = pd.concat([df, df2], ignore_index=False, join='outer')

df3.loc['Name'] = [name]


sorted_df = df3.reindex(['Name', 'id', 'main', 'description', 'icon', 'temp', 'feels_like', 'temp_min',
       'temp_max', 'pressure', 'humidity'])
print(sorted_df)
