def key_generator(*employee_name):

    l1 = []
    for i in employee_name:
        first_character = chr(ord(i[0]) + 32)
        last_character = chr(ord(i[len(i)-1])- 32)
        middle_characters = i[-2:0:-1]
        str1 = ""
        for j in middle_characters:
            str1+= str(ord(j))
        str2 = first_character + str1 + last_character
        l1.append(str2)
    return l1
key_generator("Alex", "Bob", "Trudy")