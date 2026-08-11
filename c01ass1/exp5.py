import re
import time

email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
base_emails = [
    "user.name@company.com",
    "invalid-email-at-domain",
    "support+tech@service.org",
    "no_extension@domain.",
    "hr.dept@enterprise.co.in"
]
email_batch = base_emails * 200 

print("--- Section 5: Pattern Reusability & Performance Optimization ---")
print(f"Total emails to validate: {len(email_batch)}") 

valid_count = 0
invalid_count = 0
start_time = time.time()

for email in email_batch:
    if email_pattern.match(email):
        valid_count += 1
    else:
        invalid_count += 1

end_time = time.time()
execution_time = (end_time - start_time) * 1000 

print(f"Validation Complete!")
print(f"  Valid Emails Found  : {valid_count}")
print(f"  Invalid Emails Found: {invalid_count}")
print(f"  Batch Processing Time: {execution_time:.4f} ms")
