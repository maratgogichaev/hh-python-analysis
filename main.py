from src.collector import run_collector
from src.cleaner import run_clear

def main():
    print("Сбор данных")
    run_collector()
    
    print("\nОчистка данных")
    run_clear()
    
    print("\nВсе данные собраны и очищены. Можно приступать к анализу!")

if __name__ == "__main__":
    main()