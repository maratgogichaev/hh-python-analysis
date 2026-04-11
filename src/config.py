import os


API_URL = "https://api.hh.ru/vacancies"

HEADERS = {
    "User-Agent": "PythonHhAnalysis/0.1"
}

PARAMS = {
    "text": "Python",
    "experience": "noExperience", 
    "area": 1,                
    "per_page": 100,           
    "page": 0
}

CURRENT_DIR = os.path.dirname(__file__)

BASE_DIR = os.path.dirname(CURRENT_DIR)

RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "raw_data.csv")
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "cleaned", "clean_data.csv")
