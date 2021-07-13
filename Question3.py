def isPalindrome(s):
    return s == s[::-1]


# Driver code
s = input('inter your string: ')
result = isPalindrome(s)

if result:
    print("Yes")
else:
    print("No")
