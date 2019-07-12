import re


str1='email ID: call.del@airindia.in'
email=re.search(r'[a-z]+\.[a-z]+\@[a-z]+\.[a-z]{1,3}',str1)
#print(email)
print(email.group(0))


str2='Landline Number:011-24667473'

lno=re.search(r'[0-9]{1,3}-[0-9]{1,8}',str2)
#print(lno)
print(lno.group(0))

str3='(Monday to Saturday, 0930 hrs. - 1730 hrs. IST)'

whrs=re.search(r'[0-9]+\s[a-z]+\.\s-\s[0-9]+\s[a-z]+\.\s[A-Z]{1,3}',str3)
#print(whrs)
print(whrs.group(0))


print()


text = "Python for beginner is a very cool website"
pattern = re.sub("cool", "good", text)
print(pattern)


