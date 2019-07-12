import re

str1='Hello World'
match=re.match('Hello',str1)
print(match)

'''
str1='Hello World'
match=re.match('World',str1)
print(match)
'''


str1='Hello World'
search=re.search('World',str1)
print(match)



print(match.span())
print(search.string)#prints input string
print(match.group(0))
print(search.group(0))#prints pattern


str2="How are you"
findo=re.findall('o',str2)
print(findo)


split=re.split(' ',str2)
print(split)



substitute=re.sub('o','%',str2)
print(substitute)

#words
str2="How are you"
findo=re.search(r'\w',str2)
print(findo)
str2="How are you"
findo=re.search(r'\W',str2)
print(findo)

#digits
str3="Hello 1"
digit=re.search(r'\d',str3)
print(digit)

str3="Hello 1"
Digit=re.search(r'\D',str3)
print(Digit)

#spaces
str4="Hello\nWorld"
space=re.search(r'\s',str4)
print(space)
notspace=re.search(r'\S',str4)
print(notspace)
#'.' any character other than new line

str4="%Hello world"
dot=re.search(r'.',str4)
print(dot)




ip='192.168.1.1'
ip1=re.search(r'\d\d\d\.\d\d\d\.\d\.\d',ip)
print(ip1)
print(ip1.group(0))#returns the entire value

ip='192.168.1.1'
ip1=re.search(r'(\d\d\d)\.(\d\d\d)\.(\d)\.(\d)',ip)
print(ip1)
print(ip1.group(1))
print(ip1.group(2))
print(ip1.group(3))
print(ip1.group(4))



ip='192.168.100.1'

ip2=re.search(r'\d+\.\d+\.\d+\.\d+',ip)#'+' denotes one or more occurrences
print(ip2)


ip='192.168.10.10'
ip3=re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ip)
print(ip3)



ip='192.168.10.10'
ip3=re.search(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',ip)
print(ip3)



ipv6='fe80::80c9:b500:2312%24'
ip4=re.search(r'[a-zA-Z0-9]{0,4}:[a-zA-Z0-9]{0,4}:[a-zA-Z0-9]{0,4}:[a-zA-Z0-9]{0,4}:[a-zA-Z0-9]{0,4}%[a-zA-Z0-9]{0,4}',ipv6)
print(ip4)

