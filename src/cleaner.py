import pandas as pd
import ast
import pandas as pd
from src.config import RAW_DATA_PATH, PROCESSED_DATA_PATH



def run_clear():
    """Запускает очистку данных"""
    df = pd.read_csv(RAW_DATA_PATH)

    columns_to_keep = [
        'name', 'salary', 'area', 'employer', 'snippet', 
        'experience', 'schedule', 'alternate_url', 'published_at'
    ]
 
    df = df[columns_to_keep]

    def safe_eval(val):
        """Превращает строку-словарь в настоящий словарь, если это возможно"""
        if pd.isna(val):
            return None
        try:
            return ast.literal_eval(val)
        except:
            return None



    # Превращаем строки в словари обратно
    df['salary'] = df['salary'].apply(safe_eval)
    df['area'] = df['area'].apply(safe_eval)
    df['employer'] = df['employer'].apply(safe_eval)
    df['snippet'] = df['snippet'].apply(safe_eval)
    df['experience'] = df['experience'].apply(safe_eval)

    # Зарплата
    df['salary_from'] = df['salary'].apply(lambda x: x['from'] if x else None)
    df['salary_to'] = df['salary'].apply(lambda x: x['to'] if x else None)
    df['salary_currency'] = df['salary'].apply(lambda x: x['currency'] if x else None)

    # Город и Компания
    df['city'] = df['area'].apply(lambda x: x['name'] if x else None)
    df['company'] = df['employer'].apply(lambda x: x['name'] if x else None)

    # Опыт
    df['exp_level'] = df['experience'].apply(lambda x: x['name'] if x else None)

    # Навыки 
    df['requirement'] = df['snippet'].apply(lambda x: x.get('requirement', '') if x else "")
    df['responsibility'] = df['snippet'].apply(lambda x: x.get('responsibility', '') if x else "")

    # Теперь удаляем старые колонки, они больше не нужны
    df = df.drop(columns=['salary', 'area', 'employer', 'snippet', 'experience'])

    # Сохраняем чистый результат
    df.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f"Данные очищены и сохранены в {PROCESSED_DATA_PATH}")