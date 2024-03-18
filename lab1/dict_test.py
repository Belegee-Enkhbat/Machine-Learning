new_thing = {}

def redefinedSet(word):
    if word in new_thing:
        new_thing[word] += 1
    else:
        new_thing[word] = 1

sentence = "The cat sat on the mat and the dog barked at the cat"
words = sentence.split()
for word in words:
    redefinedSet(word)

print(new_thing)