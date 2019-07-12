str1=input("Enter the string: ")
l=(len(str1))

def palindrome(str2):
    f=0
    for i in range(int(l/2)):
        if(str2[i]!=str2[l-i-1]):
            print("{} is not a plindrome".format(str1))
            f=1
            return False
    
    if(f==0):
       print("{} is a plaindrome".format(str1))


palindrome(str1)
    
