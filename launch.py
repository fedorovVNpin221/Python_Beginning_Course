# Программа для запуска python-файлов
import os
import importlib.util
import sys

def run_python_file(filepath):
    try:
        abs_path = os.path.abspath(filepath)
        
        module_name = os.path.splitext(os.path.basename(filepath))[0]
        
        spec = importlib.util.spec_from_file_location(module_name, abs_path)
        if spec is None:
            print(f"Ошибка: не удалось загрузить {filepath}")
            return
            
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        
        if hasattr(module, 'main'):
            print(f"\n--- Запуск {filepath} ---")
            module.main()
            print(f"--- Завершено {filepath} ---")
        else:
            print(f"Файл {filepath} не содержит функцию main()")
            
    except Exception as e:
        print(f"Ошибка в {filepath}: {str(e)}")

def main():
    file_groups = {
        'ДЗ': {
            '3': os.path.join("homework_3", "tasks_1-5.py"),
            '4': os.path.join("homework_4", "tasks_1-7.py"),
            '5': os.path.join("homework_5", "tasks_1-3.py"),
            '6': os.path.join("homework_6", "tasks_1-3.py"),
            '7': os.path.join("homework_7", "tasks_1-3.py"),
        },
        'Уроки': {
            '2': os.path.join("lesson_1-2", "lesson_2.py"),
            '3': os.path.join("lesson_3-4", "lesson_3.py"),
            '4': os.path.join("lesson_3-4", "lesson_4.py"),
            '5': os.path.join("lesson_5-6", "lesson_5.py"),
            '6': os.path.join("lesson_5-6", "lesson_6.py"),
            '7': os.path.join("lesson_7-8", "lesson_7.py"),
            '8': os.path.join("lesson_7-8", "lesson_8.py"),
            '9': os.path.join("lesson_9-10", "lesson_9.py"),
            '10': os.path.join("lesson_9-10", "lesson_10.py"),
            '11': os.path.join("lesson_11-12", "lesson_11.py"),
        }
    }

    while True:
        print("\n" + "="*40)
        print("Меню запуска программ".center(40))
        print("="*40)
        print("1. Запустить ДЗ")
        print("2. Запустить уроки")
        print("0. Выход")
        
        choice = input("Выберите вариант (0-2): ").strip()
        
        if choice == '0':
            print("Завершение работы...")
            break
            
        elif choice == '1':
            print("\nДоступные домашние задания:")
            for num in file_groups['ДЗ']:
                print(f"{num}. {file_groups['ДЗ'][num]}")
                
            hw_num = input("Введите номер ДЗ: ").strip()
            if hw_num in file_groups['ДЗ']:
                run_python_file(file_groups['ДЗ'][hw_num])
            else:
                print("Неверный номер ДЗ!")
                
        elif choice == '2':
            print("\nДоступные уроки:")
            for num in file_groups['Уроки']:
                print(f"{num}. {file_groups['Уроки'][num]}")
                
            lesson_num = input("Введите номер урока: ").strip()
            if lesson_num in file_groups['Уроки']:
                run_python_file(file_groups['Уроки'][lesson_num])
            else:
                print("Неверный номер урока!")
                
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()