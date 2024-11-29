from collections import Counter
import string
import docx
import pandas as pd
import matplotlib.pyplot as plt


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

df_letters = pd.DataFrame(letter_count.items(), columns=['Буква', 'Частота'])
plt.figure(figsize=(10, 6))
plt.bar(df_letters['Буква'], df_letters['Частота'], color='orange')
plt.title('Частота встречаемости букв')
plt.xlabel('Буквы')
plt.ylabel('Частота')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Вывод статистики по русским буквам
print("Статистика по русским буквам:")
for letter, count in letter_count.items():
    print(f"{letter}: {count}")



