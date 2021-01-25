import re

match = re.match(r'[0-9]+', '12345 is first, 67890 is second')
search = re.search(r'[0-9]+', '12345 is first, 67890 is second')
find_all = re.findall(r'[0-9]+', '12345 is first, 67890 is second')
print(match.group())
print(search.group())
print(find_all)
