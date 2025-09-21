def section_creator(*students, section='ABCDE'):
    ln = len(section)
    dict1 = {}
    for sec in section:
        dict1[sec] = []
    l1 = []
    for s in students:
        if s not in l1:
            l1.append(s)
    for i in l1:
        sum = 0
        for j in i:
            sum+=ord(j)
        section_select_method = sum % ln
        assigned_section = section[section_select_method]
        dict1[assigned_section].append(i)

    return dict1

section_creator( 'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace')