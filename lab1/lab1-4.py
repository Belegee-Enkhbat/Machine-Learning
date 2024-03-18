data = 'hello sjkaxyz bataa xyz xyzbataa bxyza'
words = data.split()
for word in words:
    if word.startswith('xyz') or word.endswith('xyz'):
        print(word)