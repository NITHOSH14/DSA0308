import re
def validate_email(email):
    pattern = r'^[a-zA-Z0-9][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.(com|org|edu|in)$' 
    return bool(re.match(pattern, email))

def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&!*])[^\s]{8,}$' 
    return bool(re.match(pattern, password))

test_emails = [
    "john.doe123@gmail.com",  
    ".johndoe@org.in",        
    "student@university.edu",  
    "admin@domain.net"      
]

test_passwords = [
    "P@ssw0rd123",            
    "password123",            
    "PASS#123",             
    "P@ss word1"            
]

print("--- Section 4: Email & Password Validation ---")
print("Email Validation Results:")
for email in test_emails:
    status = "VALID" if validate_email(email) else "INVALID"
    print(f"  '{email}': {status}")

print("\nPassword Validation Results:")
for pwd in test_passwords:
    status = "VALID" if validate_password(pwd) else "INVALID"
    print(f"  '{pwd}': {status}")
