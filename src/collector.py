import requests
import pandas as pd
from src.config import API_URL, PARAMS, HEADERS, RAW_DATA_PATH




def run_collector():
    vacancies = []

    response = requests.get(API_URL, params=PARAMS, headers=HEADERS)

    if response.status_code != 200:
        print(f"Ошибка: {response.status_code}")
        return
    
    data = response.json()
    pages_count = data['pages']

    
    for page in range(pages_count):
        PARAMS["page"] = page
        response = requests.get(API_URL, params=PARAMS, headers=HEADERS)
        items = response.json()['items']
        vacancies.extend(items)

    df = pd.DataFrame(vacancies)
    df.to_csv(RAW_DATA_PATH, index=False)