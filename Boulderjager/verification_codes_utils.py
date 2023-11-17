import csv
import os
import django
import random
import string


from jagd.models import VerificationCode

# TODO
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
django.setup()

num_of_codes = 300

for _ in range(num_of_codes):
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    VerificationCode.objects.create(code=code, is_valid=True)

print(f"{num_of_codes} Codes created and saved in the database.")

with open('verification_codes.csv', 'w', newline='') as csvfile:
    fieldnames = ['Code']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    codes = VerificationCode.objects.filter(is_valid=True)
    for code in codes:
        writer.writerow({'Code': code.code})

print("Codes saved in verification_codes.csv")
