class SimpleBrillTagger:

    def __init__(self):
        self.default_tag = "NN"

    def tag(self, words):
        tagged_words = []
        for w in words:
            if w.lower() in ["the", "a", "an"]:
                tagged_words.append((w, "DT"))
            elif w.lower() in ["is", "are", "was", "were", "be"]:
                tagged_words.append((w, "VB"))
            else:
                tagged_words.append((w, self.default_tag))
        for i in range(len(tagged_words)):
            word, tag = tagged_words[i]
            if word.lower() in ["can", "will", "would"]:
                tagged_words[i] = (word, "MD")
        for i in range(1, len(tagged_words)):
            prev_word, prev_tag = tagged_words[i-1]
            curr_word, curr_tag = tagged_words[i]
            if prev_tag == "MD" and curr_tag == "NN":
                tagged_words[i] = (curr_word, "VB")
        return tagged_words
sentence = "The student can write a program"

words = sentence.split()

tagger = SimpleBrillTagger()
tagged_result = tagger.tag(words)

print("Word\t\tTag")

print("-" * 20)

for w, t in tagged_result:
    print(f"{w:10}\t{t}")