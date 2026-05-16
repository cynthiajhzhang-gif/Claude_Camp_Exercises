# 词频统计器

text = input("请输入一段文字：")

text = text.lower()

import re
text = re.sub(r'[^\w\s]', '', text)

words = text.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

print("\n词频统计结果：")
for word, count in sorted_words:
    print(f"{word}: {count}次")
