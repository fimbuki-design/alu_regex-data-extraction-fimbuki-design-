import re

text = """
Contact: user@example.com, firstname.lastname@company.co.uk
Bad emails: user@, @example.com
Call (123) 456-7890, 123-456-7890 or 123.456.7890
Card: 1234 5678 9012 3456 and 1234-5678-9012-3456
Meet at 14:30 or 2:30 PM (not 25:00)
Prices: $19.99 and $1,234.56
"""

# 1. Email addresses

email_pattern = r"[\w.+-]+@[\w-]+(?:\.[\w-]+)*\.[a-zA-Z]{2,}"
emails = re.findall(email_pattern, text)

# 2. Phone numbers: (123) 456-7890, 123-456-7890, 123.456.7890
phone_pattern = r"\(\d{3}\) \d{3}-\d{4}|\d{3}[-.]\d{3}[-.]\d{4}"
phones = re.findall(phone_pattern, text)

# 3. Credit card numbers: 1234 5678 9012 3456 or 1234-5678-9012-3456
card_pattern = r"\d{4}[ -]\d{4}[ -]\d{4}[ -]\d{4}"
cards = re.findall(card_pattern, text)

# 4. Time: 14:30 (24-hour format) 2:30 PM (12-hour format)
time_pattern = r"\b(?:(?:0?[1-9]|1[0-2]):[0-5]\d ?[AaPp][Mm]|(?:[01]?\d|2[0-3]):[0-5]\d)\b"
times = re.findall(time_pattern, text)

# 5. Currency: $19.99 or $1,234.56
currency_pattern = r"\$\d{1,3}(?:,\d{3})*\.\d{2}"
money = re.findall(currency_pattern, text)

# Show the results
print("Emails:", emails)
print("Phone numbers:", phones)
print("Credit cards:", cards)
print("Times:", times)
print("Currency:", money)