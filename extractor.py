import re

text = """
From: support@my-shop.com
Reply-To: john_doe+orders@mail.example.org
 
Hi team, please email sales@company.co.uk or admin@site.io before Friday.
Broken emails: user@, @example.com, hello@world, just some plain text
 
Phone numbers:
  Office (555) 123-4567, mobile 555-987-6543, fax 555.222.3333.
  Not phones: 5551234567, 55-123-4567, 12-3456
 
Payment info:
  Visa 4111 1111 1111 1111, Mastercard 5500-0000-0000-0004.
  Too short: 1234 5678 9012, wrong separator: 1234/5678/9012/3456
 
Schedule:
  Standup at 9:15 AM, lunch at 12:30 pm, meeting ends 17:45.
  Midnight is 00:00 and the last minute of the day is 23:59.
  Invalid times: 25:00, 12:75, 13:99
 
Invoice: Subtotal $1,250.00, tax $100.50, total $1,350.50.
A discount of $5.00 was applied. Plain 19.99 has no dollar sign.
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
