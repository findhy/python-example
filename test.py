import re

text = 'fasga@fas#2*^10.90.1.2tfgws5151'

pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
pattern_re = re.compile(pattern)
ip_address = pattern_re.findall(text)
ip = str(ip_address[0])
print ip