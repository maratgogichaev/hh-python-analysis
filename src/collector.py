import requests
import pandas as pd


my_params = {
    "text": "Python",
    "experience": "noExperience", 
    "area": 1,                
    "per_page": 100,           
    "page": 0
}

my_headers = {
    "User-Agent": "PythonHhAnalysis/0.1"
}


r = requests.get("https://api.hh.ru/vacancies", params=my_params, headers=my_headers)

data = r.json()
pages_count = data['pages']

all_vacancies = []

for page in range(pages_count):
    my_params["page"] = page
    r = requests.get("https://api.hh.ru/vacancies", params=my_params, headers=my_headers)
    items = r.json()['items']
    all_vacancies.extend(items)

df = pd.DataFrame(all_vacancies)
df.to_csv('data/raw/raw_data.csv', index=False)