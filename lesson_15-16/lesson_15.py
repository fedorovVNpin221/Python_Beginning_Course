import requests
from bs4 import BeautifulSoup
# Задача №1 
# Написать программу, которая парсит информацию о списке всех кафедр с сайта Политеха.
# Необходимо получить информацию о названии кафедры и ссылку на её сайт. 
# Полученные данные оформить в текстовом файле

def parse(url, file_name):
    page = requests.get(url)
    print(page.status_code)
    soup = BeautifulSoup(page.text, "lxml")

    main_headline = soup.find("h1", class_="main__title")
    headlines = soup.find("div", id="pagecontent").find_all("a")

    writeToFile(main_headline, headlines, file_name)


def writeToFile(main_headline, headlines, file_name):
    with open(file_name, "w+", encoding='utf-8') as file:
        file.write(main_headline.text.strip())
        file.write("\n")

        for headline in headlines:
            faculty_name = headline.text
            faculty_url = headline.get("href")
            print(f"{faculty_name} : \n{faculty_url}\n", file=file)


def main():
    url = 'https://www.omgtu.ru/general_information/the-structure/the-department-of-university.php'
    file_name = 'lesson_15-16/OmSTU_Faculty_List.txt'
    parse(url, file_name)

if __name__ == "__main__":
    main()