import re

passage = (
    "Artificial Intelligence (AI) is transforming industries across the world. "
    "AI is used in healthcare to assist doctors in diagnosis, in banking to detect fraud, "
    "and in education to provide personalized learning experiences. Many companies "
    "invest heavily in AI research because AI improves efficiency and enables intelligent "
    "decision-making. As AI continues to evolve, professionals with AI skills are in high demand."
) 

print("--- Section 3: Text Tokenization & Segmentation ---")

sentence_pattern = r'[.?!]\s*'
sentences = re.split(sentence_pattern, passage.strip())
sentences = [s for s in sentences if s]

print(f"Total number of sentences: {len(sentences)}")
word_pattern = r'\s+'
words = re.split(word_pattern, passage.strip())

print(f"Total number of words: {len(words)}\n")

print("Extracted Sentences:")
for idx, sentence in enumerate(sentences, 1):
    print(f"  {idx}. {sentence}")

print("\nExtracted Words (First 15 displayed for brevity):")
print(words[:15])
