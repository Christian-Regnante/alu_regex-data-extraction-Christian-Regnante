import re

# pattern = re.compile(r'\d{4}[ -]\d{4}[ -]\d{4}[ -]\d{4}')
# pattern = re.compile(r'\(?\d{3}\)?[ -.]\d{3}[-.]\d{4}')
# pattern = re.compile(r'[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+\.[a-zA-Z0-9.]+')
# pattern = re.compile(r'https?://(www\.)?[a-z._-]+\.[a-z_-]{2,}')
pattern = re.compile(r'\$\d{1,3}(,?\d{3})*(.?\d{2})?')

file = open('search.txt', 'r')

text_pattern = file.read()

matches = pattern.finditer(text_pattern)

for match in matches:
    print(match)
    print(match.group())