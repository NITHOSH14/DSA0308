import re
text = "Contact us at support@example.com or sales-info@company.co.in. Phone: +91-9876543210 or 044-12345678."

print("Original Text:\n", text)

print("-" * 50)

emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

print("Extracted Email Addresses:")

for email in emails:
    print("-", email)

print("-" * 50)

phones = re.findall(r'\+?\d{2,4}-\d{8,10}', text)

print("Extracted Phone Numbers:")

for phone in phones:
    print("-", phone)

print("-" * 50)

match = re.search(r'support', text)

if match:
    print(f"Found 'support' at index {match.start()} to {match.end()}")