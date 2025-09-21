def hospital_fee(**amount):
    max_payer = ""
    max_amount = 0
    for i,j in amount.items():
        if j>max_amount:
            max_amount = j
            max_payer = i
    print(f'Highest fee was {max_amount} tk which was paid by {max_payer}')
hospital_fee(Mashrafe = 400, Bumrah = 900, Steyn = 1200, Cummins = 900, Wood = 400, Marsh = 700)
