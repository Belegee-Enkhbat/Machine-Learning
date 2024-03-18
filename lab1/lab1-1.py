# 1. Өгөгдсөн хүснэгтээс нийт ялгаатай утгатай элемэнтүүдийн тоог ол.
def removeDuplicateLetters(s):
        
		last_occ = {}
		stack = []
		visited = set()

		for i in range(len(s)):
			last_occ[s[i]] = i		
		for i in range(len(s)):
			if s[i] not in visited:
				while (stack and stack[-1] > s[i] and last_occ[stack[-1]] > i):
					visited.remove(stack.pop())
				stack.append(s[i])
				visited.add(s[i])
		return ''.join(stack)

print(len(removeDuplicateLetters("abcdamsanfjkksadjsa")))

# 2. Өгөгдсөн өгүүлбэрийн үг бүр нь хэдэн удаа давтагдсанг ол.
sentence = "The cat sat on the mat and the dog barked at the cat"
words = sentence.split()
unique_words = set(words)
word_counts = {}
for word in unique_words:
    count = words.count(word)
    word_counts[word] = count
print(sentence)
print("Counted:", word_counts)


# 3. Өгөгдсөн хүснэгтээс 'xyz' тэмдэгт мөрийг агуулсан тэмдэгт мөрүүдийг хэвлэ.
data = 'hello sjkaxyz bataa xyz'
words = data.split()
for word in words:
    if 'xyz' in word:
        print(word)


# 4. Өгөгдсөн хүснэгтээс 'xyz' тэмдэгт мөрөөр эхэлсэн эсвэл төгссөн тэмдэгт мөрүүдийг хэвлэ.

data = 'hello sjkaxyz bataa xyz xyzbataa bxyza'
words = data.split()
for word in words:
    if word.startswith('xyz') or word.endswith('xyz'):
        print(word)


# 5. Хамгийн эхний анхны 50 тоог олох функц бич.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int((n+1)/2)):
        if n % i == 0:
            return False
    return True

def get_primes(n):
    primes = []
    i = 2
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes

print(get_primes(50))



