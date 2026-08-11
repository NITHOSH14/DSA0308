import re

student_data = (
    "Name: John Doe ,Email: john.doe123@gmail.com ,Mobile: +91-9876543210 ,"
    "Password: P@ssw0rd123 ,Date of Birth: 15/08/2004 ,Register Number: 23AIML1056 ,"
    "Department: Artificial Intelligence and Machine Learning"
)

patterns = {
    "Email ID": r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    "Mobile Number": r'\+\d{2}-\d{10}',
    "Strong Password": r'(?<=Password:\s)\S+',
    "Date of Birth": r'\b\d{2}/\d{2}/\d{4}\b',
    "Register Number": r'\b\d{2}[A-Z]{4}\d{4}\b'
}

print("--- Section 1: Extracted Student Details ---")
for key, pattern in patterns.items():
    match = re.search(pattern, student_data)
    if match:
        print(f"{key}: {match.group()}")
    else:
        print(f"{key}: Not Found")
