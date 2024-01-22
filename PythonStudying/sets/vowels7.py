vowels = {'a', 'e', 'e', 'i', 'o', 'u', 'u'}
vowels2 = set('aeeiouu')
print(vowels)
print(vowels2)
word = input("Provide a word to search for vowels \n")

found = vowels.intersection(set(word))

for vowel in found: 
    print(vowel)
