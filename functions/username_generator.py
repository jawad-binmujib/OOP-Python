def username_generator(name1,name2,name3,identity):
    first_name = name1[:3].upper()
    middle_name = name2
    last_name  = name3[len(name3)-3::].lower()
    id = str(identity)
    student_id = id[len(id)-4::]
    return print(f'{first_name}{middle_name}{last_name}_{student_id}')
    if middle_name == None:
       pass
    else:
        middle_name = name2
name1 = input(f'First Name:')
name2 = input(f'Middle Name:')
name3  = input(f'Last Name:')
identity = int(input(f'Student ID:'))

username_generator(name1, name2, name3, identity)