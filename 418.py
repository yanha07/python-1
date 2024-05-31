'''Created by Yanha Loharwad.'''

def count_words(input_str):
    word_frequency = {}
    words = input_str.split()
    for word in words:
        word = word.strip(".,'’")
        word = word.lower()
        word_frequency[word] = word_frequency.get(word, 0) + 1
    return word_frequency

Str1 = 'they don’t know that we know they know we know'
result_dict = count_words(Str1)
for word, frequency in result_dict.items():
    print(word + ': ' + str(frequency))
