from collections import Counter
import string
import docx
import pandas as pd

# Путь к файлу .docx
file_path = 'lion.docx'

# Извлечение текста из файла .docx
doc = docx.Document(file_path)
full_text = []
for para in doc.paragraphs:
    full_text.append(para.text)
text = ' '.join(full_text)

# Удаление знаков препинания и перевод текста в нижний регистр
translator = str.maketrans('', '', string.punctuation)
text = text.translate(translator).lower()

# Подсчет встречаемости русских слов
words = text.split()
word_count = Counter(words)

# Подсчет общей суммы всех слов
total_words = sum(word_count.values())

# Подсчет частоты встречаемости слов в процентах
word_frequency = {word: (count / total_words) * 100 for word, count in word_count.items()}

# Сохранение статистики по словам в файл Excel
word_list = [(word, count, word_frequency[word]) for word, count in word_count.items()]
df = pd.DataFrame(word_list, columns=['Слово', 'Количество', 'Частота (%)'])
df.to_excel('word_frequency_statistics.xlsx', index=False)

# Подсчет встречаемости русских букв
letters = [char for char in text if char.isalpha() and char in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя']
letter_count = Counter(letters)

# Вывод статистики по русским буквам
print("Статистика по русским буквам:")
for letter, count in letter_count.items():
    print(f"{letter}: {count}")



