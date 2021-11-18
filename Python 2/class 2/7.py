# 2) Rewrite the following small program using a list comprehension (instead of the looping structure
# found on the given code).
# ##This program creates a list that includes the word’s length from all the words in a
# sentence, excluding the word “the”. If you enter a dot at the end of the sentence, make sure
# to remove it (you can use strip()) 
#  Dept. Conted
# Group Concept E
# version 5
# Note: First try running the “original” program. (Just type it in your editor!)
#  See what the intended output is. The rewrite it by using a List Comprehension.

# sentence = input("Enter a sentence: ")
# words = sentence.strip(".").split()
# word_lengths = []
# for word in words:
#     if word.upper() != "THE":
#         word_lengths.append(len(word))
# print("Lengths of words found (Other than 'The'):", word_lengths)


list1 = [len(y) for y in input("Enter a sentence: ").strip(".").split() if y.upper() !="THE"];
print("Lengths of words found (Other than 'The'):", list1)