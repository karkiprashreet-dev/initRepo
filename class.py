#count the words of a total sentence
sentence = input("Enter a sentence: ")

count = sentence.split()
i=0
numeral = 0
#Replacing words with
# result = ""
# for n in count:
#     count[i] = len(n)
#     i += 1

# for n in count:
#     result += str(n)

# print(result)

#Counting the vowel in a sentence
# for n in count:
#     if n[0] in 'aeiouAEIOU':
#         numeral += 1

# print(numeral)

intake = input("What word would u like the delete: ")
count.remove(intake)

result = " ".join(count)
print(result)