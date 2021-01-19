from pprint import pprint

sentence = "This is a common interview question"
char_freq = {}
for char in sentence:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

pprint(sorted(char_freq.items(), key=lambda kv: kv[1], reverse=True))
