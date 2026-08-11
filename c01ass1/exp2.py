import re

passage = (
    "Artificial Intelligence (AI) is transforming industries across the world. "
    "AI is used in healthcare to assist doctors in diagnosis, in banking to detect fraud, "
    "and in education to provide personalized learning experiences. Many companies "
    "invest heavily in AI research because AI improves efficiency and enables intelligent "
    "decision-making. As AI continues to evolve, professionals with AI skills are in high demand."
) 

pattern = r'\bAI\b'

print("--- Section 2: Keyword Search Analysis ---")

first_match = re.search(pattern, passage)

if first_match:
    print(f"First occurrence found: '{first_match.group()}'")
    print(f"Starting position: {first_match.start()}")
    print(f"Ending position: {first_match.end()}")
else:
    print("The word 'AI' was not found in the passage.")

all_matches = re.findall(pattern, passage)
print(f"Total occurrences of 'AI': {len(all_matches)}")
