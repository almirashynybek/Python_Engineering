price = int(input('Price: '))
tax_type = input('Tax type is ')

if tax_type == 'НДС':   
    print(price + (price * float(18/100)))

elif tax_type == 'Упрощенный налог':   
    print(price + (price * float(6/100)))

elif tax_type == 'Специальный налог':   
    print(price + (price * float(13/100)))