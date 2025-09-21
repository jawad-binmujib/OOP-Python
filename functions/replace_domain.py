def replace_domain(email, new, old ='kaaj.com'):
    address, domain= email.split("@")
    if new == domain:
        print(f'unchanged:{email}')
    else:
        print(f'changed:{address}@{new}')
replace_domain('alice@kaaj.com','sheba.xyz','kaaj.com')

