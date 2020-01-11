# Создайте словарь textDict для содержимого файла text1.txt, который приведен далее, по следующему принципу: ключи
# словаря – слова текста, значения словаря – частота появления слова в отрывке. Запишите словарь textDict в файл с
# именем textDict.txt.

text1 = open("text1.txt", 'r')
words = []
for line in text1:
    words.append(line.split(" "))
text1.close()
for i in range(len(words[0])):
    for j in range(words[0][i].count(".")):
        words[0][i] = words[0][i].replace(".", "")
    for j in range(words[0][i].count("-")):
        words[0][i] = words[0][i].replace("-", "")
    for j in range(words[0][i].count(",")):
        words[0][i] = words[0][i].replace(",", "")
setWords = set(words[0])
dictWords = {}
for i in setWords:
    dictWords.update({i: words[0].count(i)})
output = open("textDict.txt", 'w')
output.write(str(dictWords))
output.close()






