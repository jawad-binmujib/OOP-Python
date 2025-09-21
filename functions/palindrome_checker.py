def palindrome_checker(var):
    str2 = ""
    for i in var:
        if i != "":
            str2 += i
    if str2[::] == str2[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")
str1 = input()
palindrome_checker(str1)