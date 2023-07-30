import os
from dotenv import load_dotenv # Анализирует файл .env и загружает все найденные переменные в качестве переменных
# окружения pip install python-dotenv
load_dotenv() # Вызываем этот метод из библиотеки dotenv


valid_email = os.getenv('valid_email') # getenv возвращает переменную окружения
valid_password = os.getenv('valid_password')
valid_phone = os.getenv('valid_phone')
