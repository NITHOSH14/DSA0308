import random
from collections import defaultdict
corpus = """
Natural language processing is a subfield of linguistics, computer science, and artificial intelligence. 
Natural language processing is concerned with the interactions between computers and human language. 
In particular, how to program computers to process and analyze large amounts of natural language data.
"""

words = corpus.lower().split()
bigrams = defaultdict(list)

for i in range(len(words) - 1):
    w1, w2 = words[i], words[i+1]
    bigrams[w1].append(w2)

def generate_text(start_word, num_words=15):
    current_word = start_word.lower()
    result = [current_word]
    for _ in range(num_words - 1):
        next_candidates = bigrams.get(current_word)
        if not next_candidates:
            break
        current_word = random.choice(next_candidates)
        result.append(current_word)
    return ' '.join(result)

start_word = "natural"
generated = generate_text(start_word, 10)

print(f"Generated text starting with '{start_word}':")

print(generated)