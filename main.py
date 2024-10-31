import re
import requests
from bs4 import BeautifulSoup
import unittest

def is_valid_email(email: str) -> bool:
   
    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.(ru|com|ua|su)$'
    return re.match(pattern, email) is not None

def check_emails_from_file(file_path: str):
 
    try:
        with open(file_path, 'r') as file:
            emails = file.readlines()

            correct_emails = set()  
            incorrect_emails = set()

            for email in emails:
                email = email.strip()
                if not email:
                    continue  # Пропустить пустые строки

                if is_valid_email(email):
                    correct_emails.add(email)
                    status = "Корректный"
                else:
                    incorrect_emails.add(email)
                    status = "Некорректный"

                print(f"{email} - {status}")
                
                choice = input("1) Продолжить 2) Закрыть: ")
                if choice == '2':
                    print("Завершение проверки.")
                    break

            print("\nПроверка завершена.")
            print(f"Всего корректных e-mail: {len(correct_emails)}")
            print(f"Всего некорректных e-mail: {len(incorrect_emails)}")
            print("\nСписок корректных e-mail:")
            for email in correct_emails:
                print(email)
            print("\nСписок некорректных e-mail:")
            for email in incorrect_emails:
                print(email)

    except FileNotFoundError:
        print("Файл не найден. Проверьте путь к файлу.")
    except Exception as e:
        print(f"Ошибка: {e}")

def main():
   
    print("Выберите способ ввода e-mail:")
    print("1) Ввести e-mail вручную")
    print("2) Загрузить e-mail из файла")
    
    choice = input("Введите номер варианта (1 или 2): ")
    
    if choice == '1':
        while True:
            email = input("Введите e-mail для проверки (или 'exit' для выхода): ")
            if email.lower() == 'exit':
                break
            status = "Корректный" if is_valid_email(email) else "Некорректный"
            print(f"{email} - {status}")

    elif choice == '2':
        file_path = input("Введите путь к файлу: ")
        check_emails_from_file(file_path)
    
    else:
        print("Неверный выбор. Пожалуйста, выберите 1 или 2.")


class TestEmailValidation(unittest.TestCase):
    def test_valid_emails(self):
        self.assertTrue(is_valid_email("example@example.com"))
        self.assertTrue(is_valid_email("user.name@example.ru"))
        self.assertTrue(is_valid_email("username123@subdomain.ua"))
        self.assertTrue(is_valid_email("test-email@domain.su"))
    
    def test_invalid_emails(self):
        self.assertFalse(is_valid_email("example@com"))
        self.assertFalse(is_valid_email("user@domain.xy"))
        self.assertFalse(is_valid_email("user!name@domain.ru"))
        self.assertFalse(is_valid_email("@domain.com"))
        self.assertFalse(is_valid_email("user@.com"))

if __name__ == "__main__":
    main()
    unittest.main()
