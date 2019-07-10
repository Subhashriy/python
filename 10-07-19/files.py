fid=open(r'C:\Users\trainee\Desktop\python\10-07-19\file1.txt','r+')
print(fid.tell())
fid.write("Hello World")
print(fid.tell())
print(fid.seek(3))
print(fid.read())
fid.close()






fid=open(r'C:\Users\trainee\Desktop\python\10-07-19\file1.txt','a')
print(fid.tell())
fid.write("How are you")
print(fid.tell())
fid.close()



with open(r'C:\Users\trainee\Desktop\python\10-07-19\file1.txt','r+') as fid:
    print(fid.read())
    print(fid.closed)

print(fid.closed)
