"""
created by Nagaj at 17/06/2021
"""
import re

five_digit_zip = '98101'
nine_digit_zip = '98101-0003, 54646-45 09912'
phone_number = '234-567-8901'

digits = [five_digit_zip, nine_digit_zip, phone_number]
for digit in digits:
    number = re.findall(r"\d{5}", digit)  # 5 how many times of occurrences
    if number:
        print(digit)

print(re.search(r"\d{5}", nine_digit_zip))  # <re.Match object; span=(0, 5), match='98101'>
print(re.search(r"\d{5}", phone_number))  # None ==> because no match
