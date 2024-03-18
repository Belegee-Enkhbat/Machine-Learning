
# new_thing = {}

# def redefinedSet(word, left, right): 
#     if len(new_thing) < 1:
#         new_thing[word] = 1
#         return

#     mid = (left + right) // 2
#     if left > right:
#         new_thing[word] = 1    
#     elif word == list(new_thing.keys())[mid]:
#         new_thing[word] += 1
#     elif word > list(new_thing.keys())[mid]:
#         return redefinedSet(word, mid + 1, right)
#     elif word < list(new_thing.keys())[mid]:
#         return redefinedSet(word, left, mid - 1)
    
# sentence = "The cat sat on the mat and the dog barked at the cat dog"
# words = sentence.split()
# for word in words:
#     if len(new_thing) == 0:
#         new_thing[word] = 1
#     else:
#         redefinedSet(word, 0, len(list(new_thing.keys())) - 1)

# print(new_thing)


sentence = "The cat sat on the mat and the dog barked at the cat dog"
words = sentence.split()
words.sort()  
word_counts = {}
current_word = None
for word in words:
    if word != current_word:
        word_counts[word] = 1
        current_word = word
    else:
        word_counts[word] += 1

for word, count in word_counts.items():
    print(word,  count)


# for word, count in word_counts.items():
#     print(f"'{word}' {count}")
