# 4) Bonus Exercise (Small challenge). Write a program that reads a text file (you can create the text
# file beforehand in Notepad) and loads all the words found in the text file into in a dictionary.
# Keep count of the number of occurrences of each word in your dictionary. Assume words are
# delimited by spaces. Print all the words in your dictionary with the number of times they occur.
# To do this exercise (4), you need to do the same technique you saw in the dictionaries lecture
# where we were counting the occurrence of letters in a string. The difference is that this time you
# will be counting words. You will need to read lines from a text file and you will need to use the
# .split() method to separate the words into lists and add them to the dictionary.
# If you do this exercise (completely optional), sent it to your instructor via MIO for review and
# feedback. 
dict = {};
f = open('test.txt');

for x in f.read().split():
    word = x.replace('.', '');
    dict[word] = dict.get(word, 0) + 1;

for x, i in dict.items():
    print(x, i)

f.close()