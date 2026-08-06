import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
lemmatizer = WordNetLemmatizer()

text = "The boys are running, the girls are writing letters, and the children played games."

words = word_tokenize(text)
pos_tags = nltk.pos_tag(words)

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

print("Word\t\tPOS\tLemma")

print("-" * 35)

for word, tag in pos_tags:
    lemma = lemmatizer.lemmatize(word, get_wordnet_pos(tag))
    print(f"{word:12}{tag:8}{lemma}")