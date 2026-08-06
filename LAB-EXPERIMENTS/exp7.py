import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
text = "The quick brown fox jumps over the lazy dog."

words = word_tokenize(text)
pos_tags = nltk.pos_tag(words)

print("Word\t\tPOS Tag")

print("-" * 25)

for word, tag in pos_tags:
    print(f"{word:15}{tag}")