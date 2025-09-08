import os

def create_initial_file(fileName, num_words): # создает файл с английскими словами
    english_words = [
        "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
        "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry",
        "strawberry", "tangerine", "ugli", "vanilla", "watermelon", "xigua", "yam", "zucchini",
        "cat", "dog", "elephant", "fox", "giraffe", "horse", "iguana", "jaguar", "koala",
        "lion", "monkey", "newt", "owl", "penguin", "quetzal", "rabbit", "snake", "tiger",
        "umbrella", "violin", "whale", "xylophone", "yak", "zebra", "house", "table",
        "chair", "book", "pen", "computer", "keyboard", "mouse", "screen", "phone",
        "car", "bike", "train", "bus", "road", "city", "country", "mountain", "river",
        "ocean", "sky", "sun", "moon", "star", "cloud", "rain", "snow", "wind", "fire",
        "water", "earth", "air", "tree", "flower", "grass", "garden", "park", "school",
        "doctor", "nurse", "teacher", "student", "parent", "child", "friend", "family",
        "love", "hate", "happy", "sad", "big", "small", "tall", "short", "fast", "slow"
    ]
    
    
    if len(english_words) < num_words: # дополняем список до нужного количества слов
        english_words.extend(english_words[:num_words - len(english_words)])
    elif len(english_words) > num_words:
        english_words = english_words[:num_words]

    with open(fileName, "w", encoding = "utf-8") as f:
        for word in english_words:
            f.write(word + "\n")
    print(f"Файл '{fileName}' успешно создан и заполнен {num_words} словами")

def process_words(input_fileName, output_fileName): # читает файл, фильтрует слова и записывает в новый файл
    consonant_words = []
    consonants = "bcdfghjklmnpqrstvwxyz"

    with open(input_fileName, "r", encoding="utf-8") as infile:
        for line in infile:
            word = line.strip()
            if word and word[0].lower() in consonants:
                consonant_words.append(word)

    with open(output_fileName, "w", encoding = "utf-8") as outfile:
        for word in consonant_words:
            outfile.write(word + "\n")
    print(f"Файл '{output_fileName}' успешно создан. Найдены слова, начинающиеся c согласной")

def display_output_file(fileName): # выводит содержимое файла в консоль
    print("\nСодержимое файла new_words.txt:")
    if not os.path.exists(fileName):
        print("Файл не существует")
    
    with open(fileName, "r", encoding = "utf-8") as f:
        for line in f:
            print(line.strip())

if __name__ == "__main__":
    create_initial_file("homework_6/Diana_hw_05.09.25-main/Diana_hw_05.09.25-main/words.txt", 100)
    process_words("homework_6/Diana_hw_05.09.25-main/Diana_hw_05.09.25-main/words.txt", 
                  "homework_6/Diana_hw_05.09.25-main/Diana_hw_05.09.25-main/new_words.txt")
    display_output_file("homework_6/Diana_hw_05.09.25-main/Diana_hw_05.09.25-main/new_words.txt")