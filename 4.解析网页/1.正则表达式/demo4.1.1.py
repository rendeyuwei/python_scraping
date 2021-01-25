import re

lines = "Fat cats are smarter than dogs, is it right?"
m = re.match(r'(.*) are (.*?) dogs', lines)
print("匹配的整句话", m.group(0))
print("匹配的第一句话", m.group(1))
print("匹配的第二句话", m.group(2))
print("匹配的结果列表", m.groups())

m1 = re.match(r'.* are .*? dogs', lines)
print(m1.group())
print(m1.group(0))

m2 = re.match(r'(.*) are (.*?) dogs', lines)
print(m2.group())
print(m2.group(0))
print(m2.group(1))
print(m2.group(2))
print(m2.groups())
